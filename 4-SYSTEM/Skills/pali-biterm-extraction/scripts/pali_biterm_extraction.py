#!/usr/bin/env python3
"""
pali_biterm_extraction.py — two-pass bilingual term extractor (no Pali stemming)
=================================================================================
Produces bilingual frequency tables from a block-aligned Pali source file and an
English translation file.  Two output modes:

  YAML mode (default):
    asava: taints-23, cankers-12
    phasso: contact-45
    sammaditthi: right view-62, wisdom-58

  Markdown mode (--format md --focus TERM):
    Produces two flat draft Markdown files focused on TERM's morphological family:
      {output}-pali-to-en.md   — one section per Pali form, pali:/translations: blocks
      {output}-en-to-pali.md   — one section per Pali form, bare rendering: count lines
    Claude then applies semantic grouping (merging variants, adding sense labels).

Pass 1  TF-IDF on the English blocks selects domain keywords — terms that recur
        in this translation but are rare in general English, using the Google-10k
        Zipf-law IDF table in en_freq.py (or wordfreq if installed).

        Before scoring, multi-word compound terms ("right view", "initial
        application", "right concentration") are detected via an n-gram scan
        (2..max_n words) and treated as single tokens so the Pali alignment
        maps to the full phrase rather than its components.  A candidate phrase
        qualifies when: (a) all component words have IDF >= idf_threshold,
        (b) the phrase appears in >= min_phrase_df blocks, and (c) the phrase
        appears in this word order at least order_ratio times more often than
        the reverse (which filters accidental list co-occurrences like
        "states wholesome" vs. "wholesome states").

Pass 2  Each aligned block is split on Ka/Kha/Ga markers before alignment so
        triad entries map line-by-line.  For each English keyword (unigram or
        phrase), weighted Pali co-occurrence is accumulated
        (weight = 1 / |unique Pali tokens in that sub-block|).
        Pali tokens appearing in > max_pi_df of all pairs are suppressed.

No Pali stemming — exact token forms are used throughout.

Usage
-----
    python3 pali_biterm_extraction.py <pali_file> <en_file> <output> [options]

    YAML mode (default):
        python3 pali_biterm_extraction.py pi.md en.md output.yaml

    Markdown mode (focused on a root term):
        python3 pali_biterm_extraction.py pi.md en.md 0-INBOX/asava \\
            --focus asava --format md

Options
-------
    --top N           English keywords to consider (default 600)
    --min-co N        Minimum raw co-occurrence count (default 2)
    --min-score F     Minimum weighted alignment score (default 0.25)
    --max-pi-df F     Maximum Pali doc-freq fraction (default 0.30; auto 0.99 in md mode)
    --max-pi-per-kw N Maximum Pali tokens linked to one English keyword (default 2; auto 20 in md mode)
    --max-phrase N    Maximum phrase length in words (default 4)
    --focus TERM      Root term to focus on; filters output to its morphological family
    --format {yaml,md} Output format (default: yaml)
"""

import argparse
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import en_freq

# ---------------------------------------------------------------------------
# Pali function-word stop list (exact token forms, no stemming)
# ---------------------------------------------------------------------------
PALI_STOP = {
    "ca", "kho", "pana", "ceva", "va", "na", "no", "nu", "hi", "tu",
    "pi", "api", "atha", "ti", "iti", "eva", "yeva",
    "yo", "ya", "yam", "yad", "ye", "yani",
    "yasmin", "yassa",
    "so", "sa", "tam", "tad", "te", "tani",
    "ayam", "idam", "ime", "ima", "imani",
    "eso", "esa", "etam", "etad", "ete", "etani",
    "tesam",
    "aññepi", "añño", "añña", "aññam", "aññe",
    "tattha", "tatra", "yattha", "idha", "ettha",
    "tatha", "yatha", "seyyatha",
    "puna", "tena", "evam",
    "tasmin", "tasmim", "tasma",
    "samaye", "samayam",
    "katame", "katamo", "katamam",
    "hoti", "honti", "ahosi", "atthi", "santi",
    "vuccati", "vuccanti",
    "neva", "nava",
    "ka", "kha", "ga",
}
# diacritic variants added at runtime (plain form in PALI_STOP catches them via _plain())

# ---------------------------------------------------------------------------
# English formula-word stop list
# ---------------------------------------------------------------------------
EN_FORMULA_STOP = {
    "which", "what", "whatever", "whichever", "that", "this", "these",
    "those", "who", "whom", "whose",
    "are", "were", "been", "being", "have", "has", "had",
    "will", "would", "could", "should", "may", "might", "shall",
    "there", "here", "then", "when", "while", "thus", "hence",
    "therein", "herein", "wherein", "thereby",
    "having", "being", "yet", "still", "also", "both", "neither",
    "nor", "either", "whether", "however", "moreover",
}

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------
BLOCK_ID_RE      = re.compile(r"\^[\w\-]+")
FRONTMATTER_RE   = re.compile(r"^---\s*$")
HEADING_RE       = re.compile(r"^#{1,6}\s+")
BRACKET_RE       = re.compile(r"\[.*?\]")
SUB_SPLIT_RE     = re.compile(r"(?=\([KkGgAaBb][a-z]*\))")
SECTION_STRIP_RE = re.compile(r"^\([KkGgAaBb][a-z]*\)\s*")
_PUNCT = str.maketrans("", "", r""".,;:!?()"'`‘’“”—–-_/\\[]{}""")
_PALI_RE = re.compile(r"[\wĀ-žḀ-ỿ]+")

# Module-level phrase set — populated by build_phrases() before Pass 1
_PHRASES: set = set()


def _plain(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


# ---------------------------------------------------------------------------
# Block parser
# ---------------------------------------------------------------------------
def parse_blocks(path: str) -> dict:
    blocks: dict = {}
    pending: list = []
    in_fm, fm_count = False, 0
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if FRONTMATTER_RE.match(line):
                fm_count += 1
                in_fm = (fm_count == 1)
                if fm_count >= 2:
                    in_fm = False
                continue
            if in_fm:
                continue
            m = BLOCK_ID_RE.search(line)
            if m:
                bid = m.group()[1:]
                pending.append(line[:m.start()].strip())
                full = HEADING_RE.sub("", " ".join(pending).strip())
                blocks[bid] = full
                pending = []
            else:
                pending.append(line)
    return blocks


# ---------------------------------------------------------------------------
# Sub-block splitter
# ---------------------------------------------------------------------------
def split_subblocks(text: str) -> list:
    parts = SUB_SPLIT_RE.split(text.strip())
    result = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        m = SECTION_STRIP_RE.match(part)
        if m:
            label = part[m.start():m.end()].strip("() ")
            body  = part[m.end():].strip()
        else:
            label, body = "", part
        if body:
            result.append((label, body))
    return result or [("", text)]


def build_subblock_pairs(src_blocks: dict, tgt_blocks: dict) -> list:
    pairs = []
    for bid in sorted(set(src_blocks) & set(tgt_blocks)):
        src_subs = {lbl: body for lbl, body in split_subblocks(src_blocks[bid])}
        tgt_subs = {lbl: body for lbl, body in split_subblocks(tgt_blocks[bid])}
        if len(src_subs) == 1 and "" in src_subs:
            tgt_body = tgt_subs.get("") or (list(tgt_subs.values())[0] if tgt_subs else "")
            pairs.append((src_subs[""], tgt_body))
        else:
            for lbl, src_body in src_subs.items():
                if lbl in tgt_subs:
                    pairs.append((src_body, tgt_subs[lbl]))
    return pairs


# ---------------------------------------------------------------------------
# Tokenisers
# ---------------------------------------------------------------------------
def _raw_en_words(text: str) -> list:
    """Lowercased word list, formula-stop removed, no phrase merging."""
    text = BRACKET_RE.sub("", text)
    text = HEADING_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    return [t for t in text.split()
            if t and not t.isdigit() and len(t) >= 3
            and t not in EN_FORMULA_STOP]


def en_tokens(text: str) -> list:
    """
    English tokens with greedy longest-match phrase merging.
    At each position tries to consume the longest phrase in _PHRASES first.
    E.g. "right concentration faculty" beats "right concentration" if both qualify.
    """
    words = _raw_en_words(text)
    if not _PHRASES:
        return words
    result = []
    i = 0
    while i < len(words):
        matched = False
        # try longest possible phrase down to bigram
        for n in range(min(4, len(words) - i), 1, -1):
            phrase = " ".join(words[i:i + n])
            if phrase in _PHRASES:
                result.append(phrase)
                i += n
                matched = True
                break
        if not matched:
            result.append(words[i])
            i += 1
    return result


def pali_tokens(text: str) -> list:
    """Exact Pali tokens — no stemming."""
    text = BRACKET_RE.sub("", text)
    out = []
    for tok in _PALI_RE.findall(text):
        tok_lc = tok.lower()
        if tok_lc.isdigit() or len(tok_lc) < 2:
            continue
        plain = _plain(tok_lc)
        if plain in PALI_STOP or tok_lc in PALI_STOP:
            continue
        if tok_lc.isascii() and len(tok_lc) <= 3:
            continue
        out.append(tok_lc)
    return out


# ---------------------------------------------------------------------------
# N-gram phrase detection
# ---------------------------------------------------------------------------
def build_phrases(
    tgt_blocks: dict,
    max_n: int = 4,
    min_df: int = 3,
    idf_threshold: float = 3.5,
    order_ratio: float = 4.0,
    min_coverage: float = 0.30,
) -> set:
    """
    Detect multi-word compound terms of length 2..max_n.

    A candidate phrase (w1 w2 ... wk) qualifies when ALL of:
      1. All component words have IDF >= idf_threshold
      2. The phrase appears in >= min_df distinct blocks
      3. Order-consistency: each adjacent pair appears in this order at least
         order_ratio x more often than reversed — filters list co-occurrences
         like "states wholesome" vs "wholesome states".
      4. Component coverage: phrase_block_df / min(component_block_df) >=
         min_coverage — the phrase accounts for a meaningful fraction of the
         rarest component word's occurrences.  This filters synonym-list
         co-occurrences like "nondelusion investigation" where both words
         appear in many other contexts, while keeping "right view" where
         "view" almost exclusively occurs inside that phrase.
    """
    global _PHRASES

    # Step 1: count unigram block-level freqs (needed for coverage check)
    unigram_block_df: dict = defaultdict(int)
    for text in tgt_blocks.values():
        words = _raw_en_words(text)
        for w in set(words):
            if en_freq.get_idf(w) >= idf_threshold:
                unigram_block_df[w] += 1

    # Step 2: count raw (token-level) and block-level freq for all n-grams
    raw_count:   dict = defaultdict(int)
    block_count: dict = defaultdict(int)

    for text in tgt_blocks.values():
        words = _raw_en_words(text)
        seen_in_block: set = set()
        for n in range(2, max_n + 1):
            for i in range(len(words) - n + 1):
                chunk = words[i:i + n]
                if not all(en_freq.get_idf(w) >= idf_threshold for w in chunk):
                    continue
                phrase = " ".join(chunk)
                raw_count[phrase] += 1
                if phrase not in seen_in_block:
                    block_count[phrase] += 1
                    seen_in_block.add(phrase)

    # Step 3: qualify by frequency + order-consistency + component coverage
    qualified: set = set()
    for phrase, df in block_count.items():
        if df < min_df:
            continue
        words = phrase.split()
        # Order-consistency
        consistent = True
        for j in range(len(words) - 1):
            fwd = raw_count.get(f"{words[j]} {words[j+1]}", 0)
            rev = raw_count.get(f"{words[j+1]} {words[j]}", 0)
            if fwd < order_ratio * max(rev, 1):
                consistent = False
                break
        if not consistent:
            continue
        # Component coverage: phrase must represent >= min_coverage of the
        # rarest component word's occurrences
        min_comp_df = min(unigram_block_df.get(w, 1) for w in words)
        if df / min_comp_df < min_coverage:
            continue
        qualified.add(phrase)

    # Step 4: prune sub-phrases dominated by longer qualified phrases
    pruned: set = set()
    for phrase in qualified:
        dominated = any(
            phrase != longer and phrase in longer
            for longer in qualified
            if len(longer.split()) > len(phrase.split())
        )
        if not dominated:
            pruned.add(phrase)

    _PHRASES = pruned
    return _PHRASES


# ---------------------------------------------------------------------------
# Pass 1: TF-IDF English keyword selection
# ---------------------------------------------------------------------------
def select_en_keywords(
    tgt_blocks: dict,
    top_n: int = 600,
    min_df: int = 2,
    max_phrase: int = 4,
) -> list:
    """
    1. Build multi-word phrases (populates _PHRASES).
    2. Score every English token/phrase by (block_df / N) x IDF.
       For phrases, IDF = min(component IDFs) — weakest word is the bottleneck.
    Return [(token, score), ...] sorted descending, capped at top_n.
    """
    phrases = build_phrases(tgt_blocks, max_n=max_phrase)
    print(f"         {len(phrases)} compound phrases detected", file=sys.stderr)
    if phrases:
        sample = sorted(phrases, key=lambda p: -len(p.split()))[:10]
        print(f"         sample (longest first): {sample}", file=sys.stderr)

    df: dict = defaultdict(int)
    for text in tgt_blocks.values():
        seen: set = set()
        for tok in en_tokens(text):
            if tok not in seen:
                df[tok] += 1
                seen.add(tok)

    N = max(len(tgt_blocks), 1)
    scored = []
    for tok, doc_freq in df.items():
        if doc_freq < min_df or tok in EN_FORMULA_STOP:
            continue
        if " " in tok:
            idf = min(en_freq.get_idf(w) for w in tok.split())
        else:
            idf = en_freq.get_idf(tok)
        if idf < 3.5:
            continue
        scored.append((tok, (doc_freq / N) * idf))

    scored.sort(key=lambda x: -x[1])
    return scored[:top_n]


# ---------------------------------------------------------------------------
# Pass 2: weighted co-occurrence
# ---------------------------------------------------------------------------
def build_cooccurrence(
    pairs: list,
    keywords: list,
    max_pi_df: float = 0.30,
) -> tuple:
    kw_set = {kw for kw, _ in keywords}
    N = len(pairs)

    pi_df_pre: dict = defaultdict(int)
    for pi_text, _ in pairs:
        for pt in set(pali_tokens(pi_text)):
            pi_df_pre[pt] += 1

    pi_freq_limit = max_pi_df * N
    weighted_co: dict = defaultdict(lambda: defaultdict(float))
    raw_co:      dict = defaultdict(lambda: defaultdict(int))
    pi_df:       dict = defaultdict(int)

    for pi_text, en_text in pairs:
        pi_toks = set(pali_tokens(pi_text))
        en_toks = set(en_tokens(en_text))
        en_hits = en_toks & kw_set
        if not en_hits or not pi_toks:
            continue
        pi_toks = {pt for pt in pi_toks if pi_df_pre[pt] <= pi_freq_limit}
        if not pi_toks:
            continue
        w = 1.0 / len(pi_toks)
        for pt in pi_toks:
            pi_df[pt] += 1
            for ek in en_hits:
                weighted_co[pt][ek] += w
                raw_co[pt][ek] += 1

    return weighted_co, raw_co, pi_df


# ---------------------------------------------------------------------------
# Glossary builder
# ---------------------------------------------------------------------------
def build_glossary(
    keywords: list,
    weighted_co: dict,
    raw_co: dict,
    min_co: int = 2,
    min_score: float = 0.25,
    max_pi_per_kw: int = 2,
) -> dict:
    glossary: dict = defaultdict(dict)
    for kw, _ in keywords:
        pali_scores = sorted(
            ((pt, weighted_co[pt].get(kw, 0.0)) for pt in weighted_co),
            key=lambda x: -x[1],
        )
        kept = 0
        for pt, score in pali_scores:
            if score < min_score:
                break
            count = raw_co[pt].get(kw, 0)
            if count < min_co:
                continue
            glossary[pt][kw] = count
            kept += 1
            if kept >= max_pi_per_kw:
                break
    return {
        pt: dict(sorted(en_dict.items(), key=lambda x: -x[1]))
        for pt, en_dict in sorted(glossary.items())
    }


# ---------------------------------------------------------------------------
# YAML writer
# ---------------------------------------------------------------------------
def write_yaml(glossary: dict, out_path: str, src_path: str, tgt_path: str) -> None:
    sorted_entries = sorted(
        glossary.items(),
        key=lambda kv: sum(kv[1].values()),
        reverse=True,
    )
    lines = [
        "# Translation variant frequencies",
        "# Method: English TF-IDF (Google-10k Zipf IDF) + weighted sub-block co-occurrence",
        "# Pali: exact token forms, no stemming; compound phrases merged (n-gram)",
        f"# source: {src_path}",
        f"# target: {tgt_path}",
        "# Generated by 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py",
        "",
    ]
    for pt, en_dict in sorted_entries:
        value = ", ".join(f"{ek}-{cnt}" for ek, cnt in en_dict.items())
        lines.append(f"{pt}: {value}")
    Path(out_path).write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Markdown writer (flat draft — one section per Pali form)
# ---------------------------------------------------------------------------
def write_markdown_flat(
    glossary: dict,
    focus_term: str | None,
    out_base: str,
    src_path: str,
    tgt_path: str,
) -> tuple:
    """Write two flat Markdown files (one section per Pali form).

    When focus_term is given, only forms whose plain-ASCII form contains the
    plain-ASCII form of focus_term are included.  Output files:
        {out_base}-pali-to-en.md   — pali: [...] + translations: blocks
        {out_base}-en-to-pali.md   — bare rendering: count lines

    Returns (pali_to_en_path, en_to_pali_path).

    NOTE: This is a *flat draft*.  Claude merges forms into semantic clusters
    and adds sense labels in the semantic-grouping step described in SKILL.md.
    """
    if focus_term:
        focus_plain = _plain(focus_term.lower())
        entries = [
            (pt, en_dict) for pt, en_dict in glossary.items()
            if focus_plain in _plain(pt.lower())
        ]
    else:
        entries = list(glossary.items())

    # Sort by total raw co-occurrence count, descending
    entries.sort(key=lambda kv: sum(kv[1].values()), reverse=True)

    title = focus_term or Path(src_path).stem

    # --- pali-to-en ---
    p2e_path = f"{out_base}-pali-to-en.md"
    lines: list = [f"# {title} — translation variants by sense", ""]
    for i, (pt, en_dict) in enumerate(entries, 1):
        lines += [
            f"## {i}. {pt}",
            f"pali: [{pt}]",
            "translations:",
        ]
        for en, cnt in en_dict.items():
            lines.append(f"  {en}: {cnt}")
        lines.append("")
    Path(p2e_path).write_text("\n".join(lines), encoding="utf-8")

    # --- en-to-pali ---
    e2p_path = f"{out_base}-en-to-pali.md"
    lines = [f"# {title} — English variants grouped by sense", ""]
    for i, (pt, en_dict) in enumerate(entries, 1):
        lines.append(f"## {i}. {pt}")
        for en, cnt in en_dict.items():
            lines.append(f"{en}: {cnt}")
        lines.append("")
    Path(e2p_path).write_text("\n".join(lines), encoding="utf-8")

    return p2e_path, e2p_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    p = argparse.ArgumentParser(description="Pali-English bilingual term extraction")
    p.add_argument("pali",    help="Pali source markdown file")
    p.add_argument("english", help="English translation markdown file")
    p.add_argument("output",  help="Output path (YAML file, or base path for --format md)")
    p.add_argument("--top",           type=int,   default=600,  help="English keywords to consider")
    p.add_argument("--min-co",        type=int,   default=2,    help="Min raw co-occurrence count")
    p.add_argument("--min-score",     type=float, default=0.25, help="Min weighted alignment score")
    p.add_argument("--max-pi-df",     type=float, default=None, help="Max Pali doc-freq fraction (default 0.30; 0.99 in md mode)")
    p.add_argument("--max-pi-per-kw", type=int,   default=None, help="Max Pali tokens per English keyword (default 2; 20 in md mode)")
    p.add_argument("--max-phrase",    type=int,   default=4,    help="Max phrase length in words")
    p.add_argument("--focus",         default=None, help="Root term to focus on (filters output to morphological family)")
    p.add_argument("--format",        choices=["yaml", "md"], default="yaml", help="Output format")
    args = p.parse_args()

    # Apply mode-aware defaults
    md_mode = args.format == "md"
    max_pi_df     = args.max_pi_df     if args.max_pi_df     is not None else (0.99 if md_mode else 0.30)
    max_pi_per_kw = args.max_pi_per_kw if args.max_pi_per_kw is not None else (20   if md_mode else 2)

    print(f"source : {args.pali}", file=sys.stderr)
    print(f"target : {args.english}", file=sys.stderr)
    if args.focus:
        print(f"focus  : {args.focus}", file=sys.stderr)
    print(f"format : {args.format}", file=sys.stderr)

    src_blocks = parse_blocks(args.pali)
    tgt_blocks = parse_blocks(args.english)
    print(f"blocks : {len(src_blocks)} src / {len(tgt_blocks)} tgt", file=sys.stderr)

    aligned_ids = set(src_blocks) & set(tgt_blocks)
    print(f"aligned: {len(aligned_ids)} block pairs", file=sys.stderr)
    if not aligned_ids:
        print("ERROR: no aligned block pairs", file=sys.stderr)
        sys.exit(1)

    print("Pass 1 : TF-IDF keyword extraction ...", file=sys.stderr)
    keywords = select_en_keywords(tgt_blocks, top_n=args.top, max_phrase=args.max_phrase)
    print(f"         {len(keywords)} keywords selected", file=sys.stderr)
    if keywords:
        print(f"         top 10: {[kw for kw, _ in keywords[:10]]}", file=sys.stderr)

    print("Building sub-block pairs ...", file=sys.stderr)
    pairs = build_subblock_pairs(src_blocks, tgt_blocks)
    print(f"         {len(pairs)} sub-block pairs", file=sys.stderr)

    print("Pass 2 : weighted co-occurrence ...", file=sys.stderr)
    weighted_co, raw_co, pi_df = build_cooccurrence(
        pairs, keywords, max_pi_df=max_pi_df
    )

    glossary = build_glossary(
        keywords, weighted_co, raw_co,
        min_co=args.min_co,
        min_score=args.min_score,
        max_pi_per_kw=max_pi_per_kw,
    )
    print(f"terms  : {len(glossary)} Pali tokens in output", file=sys.stderr)

    if md_mode:
        p2e, e2p = write_markdown_flat(
            glossary, args.focus, args.output, args.pali, args.english
        )
        print(f"output : {p2e}", file=sys.stderr)
        print(f"         {e2p}", file=sys.stderr)
        if args.focus:
            found = [pt for pt in glossary if _plain(args.focus.lower()) in _plain(pt.lower())]
            print(f"focus  : {len(found)} forms matched — {found}", file=sys.stderr)
    else:
        write_yaml(glossary, args.output, args.pali, args.english)
        print(f"output : {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
