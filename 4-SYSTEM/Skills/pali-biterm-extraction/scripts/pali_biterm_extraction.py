#!/usr/bin/env python3
"""
pali_biterm_extraction.py — two-pass bilingual term extractor (no Pāli stemming)
=================================================================================
Produces a compact YAML bilingual glossary from a block-aligned Pāli source file
and an English translation file:

    āsavā: taints-23, cankers-12
    phasso: contact-45
    vedanā: feeling-38, sensation-12

Pass 1  TF-IDF on the English blocks selects domain keywords — terms that recur
        in this translation but are rare in general English, using the Google-10k
        Zipf-law IDF table in en_freq.py (or wordfreq if installed).

Pass 2  Each aligned block is split on Ka/Kha/Ga markers before alignment so
        triad entries map line-by-line, not block-by-block.  For each English
        keyword, weighted Pāli co-occurrence is accumulated (weight = 1 / |unique
        Pāli tokens in that sub-block|, so short mātikā lines outweigh long prose
        paragraphs).

No Pāli stemming is applied.  Exact token forms are used throughout.  Common Pāli
function words (particles, pronouns, question-word formulae) are listed in
PALI_STOP and filtered out.  Pāli tokens appearing in more than MAX_PI_DF of all
aligned pairs are suppressed as high-frequency function words not caught by the
stop list.

Usage
-----
    python3 pali_biterm_extraction.py <pali_file> <en_file> <output.yaml> [options]

Options
-------
    --top N          English keywords to consider (default 600)
    --min-co N       Minimum raw co-occurrence count (default 2)
    --min-score F    Minimum weighted alignment score (default 0.25)
    --max-pi-df F    Maximum Pāli doc-freq fraction (default 0.50)
    --max-pi-per-kw  Maximum Pāli tokens linked to one English keyword (default 2)
"""

import argparse
import math
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

# ── local frequency module ───────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
import en_freq

# ── Pāli function-word stop list (exact token forms, no stemming) ────────────
PALI_STOP = {
    # particles / conjunctions
    "ca", "kho", "pana", "ceva", "vā", "na", "no", "nu", "hi", "tu",
    "pi", "api", "atha", "ti", "iti", "eva", "yeva", "vā",
    # relative / demonstrative pronouns
    "yo", "yā", "yaṃ", "yad", "ye", "yāni",
    "yasmiṃ", "yasmin", "yassā", "yassa",   # relative locatives / genitives
    "so", "sā", "taṃ", "tad", "te", "tāni",
    "ayaṃ", "ayam", "idaṃ", "idam", "ime", "imā", "imāni",
    "eso", "esā", "etaṃ", "etad", "ete", "etāni",
    "tam", "tesam", "tad",
    # formula phrase "whatever other" (aññepi ... paṭiccasamuppannā arūpino dhammā)
    "aññepi", "añño", "aññā", "aññaṃ", "aññe",
    # locatives / adverbs
    "tattha", "tatra", "yattha", "idha", "ettha",
    "tathā", "yathā", "seyyathā",
    "atha", "puna", "tena", "evam", "evaṃ",
    # "on that occasion" formula — tasmiṃ samaye — extremely high frequency
    "tasmiṃ", "tasmin", "tasmim", "tasmā", "tasma",
    "samaye", "samayam", "samayan",
    # question-formula words (defining sections)
    "katame", "katamā", "katamo", "katamaṃ", "katamā",
    # high-frequency prose-formula verbs
    "hoti", "honti", "ahosi", "atthi", "santi",
    "vuccati", "vuccanti",
    # common copular / existential
    "neva", "nāva",
    # number words that appear as section markers
    "ka", "kha", "ga",
}

# ── English formula-word stop list (words used in definition syntax, ──────────
# ── not as translation choices) ──────────────────────────────────────────────
EN_FORMULA_STOP = {
    # question / relative pronouns used in definition formulae
    "which", "what", "whatever", "whichever", "that", "this", "these",
    "those", "who", "whom", "whose",
    # common auxiliary / copular verbs that slip past IDF
    "are", "were", "been", "being", "have", "has", "had",
    "will", "would", "could", "should", "may", "might", "shall",
    # spatial / temporal formula words
    "there", "here", "then", "when", "while", "thus", "hence",
    "therein", "herein", "wherein", "thereby",
    # discourse connectors that appear in every analytical block
    "having", "being", "yet", "still", "also", "both", "neither",
    "nor", "either", "whether", "however", "moreover",
}

# ── regex helpers ─────────────────────────────────────────────────────────────
BLOCK_ID_RE      = re.compile(r"\^[\w\-]+")
FRONTMATTER_RE   = re.compile(r"^---\s*$")
HEADING_RE       = re.compile(r"^#{1,6}\s+")
BRACKET_RE       = re.compile(r"\[.*?\]")
NUMBER_PFX_RE    = re.compile(r"^\d+\.\s*")
# Split on Ka/Kha/Ga section markers — used for sub-block alignment
SUB_SPLIT_RE     = re.compile(r"(?=\([KkGgAaBb][a-z]*\))")
SECTION_STRIP_RE = re.compile(r"^\([KkGgAaBb][a-z]*\)\s*")

_PUNCT = str.maketrans("", "", r""".,;:!?()"'`''""—–-_/\\[]{}""")

# Unicode-aware Pāli tokeniser pattern (covers all diacritical Latin)
_PALI_RE = re.compile(
    r"[\wĀ-žḀ-ỿ]+"
    r"(?:[Ā-žḀ-ỿ\w]*)"
)


def _plain(s: str) -> str:
    """Strip diacritics for stop-list comparison."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


# ── block parser ──────────────────────────────────────────────────────────────

def parse_blocks(path: str) -> dict:
    """
    Return {block_id: text} for every ^block-id in the markdown file.
    Frontmatter and heading markers are stripped; multi-line blocks are joined.
    """
    blocks: dict = {}
    pending: list = []
    in_fm, fm_count = False, 0

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if FRONTMATTER_RE.match(line):
                fm_count += 1
                in_fm = fm_count == 1
                if fm_count >= 2:
                    in_fm = False
                continue
            if in_fm:
                continue
            m = BLOCK_ID_RE.search(line)
            if m:
                bid = m.group()[1:]
                text_part = line[: m.start()].strip()
                pending.append(text_part)
                full = " ".join(pending).strip()
                full = HEADING_RE.sub("", full)
                blocks[bid] = full
                pending = []
            else:
                pending.append(line)

    return blocks


# ── sub-block splitter ────────────────────────────────────────────────────────

def split_subblocks(text: str) -> list:
    """
    Split block text on (Ka)/(Kha)/(Ga) markers.
    Returns [(label, body), ...].  Falls back to [("", text)] if no markers.
    """
    parts = SUB_SPLIT_RE.split(text.strip())
    result = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        m = SECTION_STRIP_RE.match(part)
        if m:
            label = part[m.start() : m.end()].strip("() ")
            body = part[m.end() :].strip()
        else:
            label = ""
            body = part
        if body:
            result.append((label, body))
    return result or [("", text)]


def build_subblock_pairs(src_blocks: dict, tgt_blocks: dict) -> list:
    """
    For each aligned block, split into Ka/Kha/Ga sub-blocks and match by label.
    Returns [(pali_text, en_text), ...].
    """
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


# ── tokenisers ────────────────────────────────────────────────────────────────

def en_tokens(text: str) -> list:
    text = BRACKET_RE.sub("", text)
    text = HEADING_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    return [
        t for t in text.split()
        if t and not t.isdigit() and len(t) >= 3
        and t not in EN_FORMULA_STOP
    ]


def pali_tokens(text: str) -> list:
    """
    Exact Pāli tokens — no stemming.  Filters short particles, digits, and
    stop-list entries (compared with diacritics stripped for safety).
    """
    text = BRACKET_RE.sub("", text)
    out = []
    for tok in _PALI_RE.findall(text):
        tok_lc = tok.lower()
        if tok_lc.isdigit() or len(tok_lc) < 2:
            continue
        plain = _plain(tok_lc)
        if plain in PALI_STOP or tok_lc in PALI_STOP:
            continue
        # skip pure ASCII tokens ≤ 3 chars (likely section labels: ka, kha, ga)
        if tok_lc.isascii() and len(tok_lc) <= 3:
            continue
        out.append(tok_lc)
    return out


# ── Pass 1: TF-IDF English keyword selection ─────────────────────────────────

def select_en_keywords(tgt_blocks: dict, top_n: int = 600, min_df: int = 2) -> list:
    """
    Score each English token by (block_df / N) × IDF_corpus.
    Return [(token, score), ...] sorted descending, capped at top_n.
    """
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
        if doc_freq < min_df:
            continue
        if tok in EN_FORMULA_STOP:
            continue
        idf = en_freq.get_idf(tok)
        # Suppress common English: require IDF > 3.5 (≈ words outside top-30)
        if idf < 3.5:
            continue
        scored.append((tok, (doc_freq / N) * idf))

    scored.sort(key=lambda x: -x[1])
    return scored[:top_n]


# ── Pass 2: weighted co-occurrence ────────────────────────────────────────────

def build_cooccurrence(
    pairs: list,
    keywords: list,
    max_pi_df: float = 0.50,
) -> tuple:
    """
    For every (pali_text, en_text) sub-block pair:
      - weight = 1 / |unique_pali_tokens|   (shorter blocks get higher weight)
      - weighted_co[pi][en] += weight
      - raw_co[pi][en] += 1

    Pāli tokens appearing in > max_pi_df fraction of all pairs are suppressed
    (ubiquitous function words not caught by the stop list).

    Returns (weighted_co, raw_co, pi_df) where pi_df is doc-freq per Pāli token.
    """
    kw_set = {kw for kw, _ in keywords}
    N = len(pairs)

    # Pre-compute Pāli doc-freq to identify high-frequency tokens
    pi_df_pre: dict = defaultdict(int)
    for pi_text, _ in pairs:
        for pt in set(pali_tokens(pi_text)):
            pi_df_pre[pt] += 1

    pi_freq_limit = max_pi_df * N

    weighted_co: dict = defaultdict(lambda: defaultdict(float))
    raw_co: dict = defaultdict(lambda: defaultdict(int))
    pi_df: dict = defaultdict(int)

    for pi_text, en_text in pairs:
        pi_toks = set(pali_tokens(pi_text))
        en_toks = set(en_tokens(en_text))
        en_hits = en_toks & kw_set
        if not en_hits or not pi_toks:
            continue

        # Filter out high-frequency Pāli function words
        pi_toks = {pt for pt in pi_toks if pi_df_pre[pt] <= pi_freq_limit}
        if not pi_toks:
            continue

        w = 1.0 / len(pi_toks)   # weight inversely proportional to sub-block size

        for pt in pi_toks:
            pi_df[pt] += 1
            for ek in en_hits:
                weighted_co[pt][ek] += w
                raw_co[pt][ek] += 1

    return weighted_co, raw_co, pi_df


# ── Glossary builder ──────────────────────────────────────────────────────────

def build_glossary(
    keywords: list,
    weighted_co: dict,
    raw_co: dict,
    min_co: int = 2,
    min_score: float = 0.25,
    max_pi_per_kw: int = 2,
) -> dict:
    """
    For each English keyword, pick the top-scoring Pāli token(s) and record
    the raw co-occurrence count.

    Returns {pali_token: {en_token: raw_count}}.
    """
    glossary: dict = defaultdict(dict)

    for kw, _ in keywords:
        # Rank Pāli tokens by weighted alignment score for this keyword
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

    # Sort each Pāli entry's translations by frequency descending
    return {
        pt: dict(sorted(en_dict.items(), key=lambda x: -x[1]))
        for pt, en_dict in sorted(glossary.items())
    }


# ── YAML writer ───────────────────────────────────────────────────────────────

def write_yaml(glossary: dict, out_path: str, src_path: str, tgt_path: str) -> None:
    """
    Write compact YAML:  pali_token: en1-N, en2-N, ...
    Entries sorted by total co-occurrence frequency (most frequent first).
    """
    sorted_entries = sorted(
        glossary.items(),
        key=lambda kv: sum(kv[1].values()),
        reverse=True,
    )
    lines = [
        "# Translation variant frequencies",
        "# Method: English TF-IDF (Google-10k Zipf IDF) + weighted sub-block co-occurrence",
        "# Pāli: exact token forms, no stemming",
        f"# source: {src_path}",
        f"# target: {tgt_path}",
        "# Generated by 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py",
        "",
    ]
    for pt, en_dict in sorted_entries:
        value = ", ".join(f"{ek}-{cnt}" for ek, cnt in en_dict.items())
        lines.append(f"{pt}: {value}")

    Path(out_path).write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description="Pāli-English bilingual term extraction")
    p.add_argument("pali",    help="Pāli source markdown file")
    p.add_argument("english", help="English translation markdown file")
    p.add_argument("output",  help="Output YAML file")
    p.add_argument("--top",          type=int,   default=600,  help="English keywords to consider")
    p.add_argument("--min-co",       type=int,   default=2,    help="Min raw co-occurrence count")
    p.add_argument("--min-score",    type=float, default=0.25, help="Min weighted alignment score")
    p.add_argument("--max-pi-df",    type=float, default=0.30, help="Max Pāli doc-freq fraction")
    p.add_argument("--max-pi-per-kw",type=int,   default=2,    help="Max Pāli tokens per English keyword")
    args = p.parse_args()

    print(f"source : {args.pali}", file=sys.stderr)
    print(f"target : {args.english}", file=sys.stderr)

    src_blocks = parse_blocks(args.pali)
    tgt_blocks = parse_blocks(args.english)
    print(f"blocks : {len(src_blocks)} src / {len(tgt_blocks)} tgt", file=sys.stderr)

    aligned_ids = set(src_blocks) & set(tgt_blocks)
    print(f"aligned: {len(aligned_ids)} block pairs", file=sys.stderr)
    if not aligned_ids:
        print("ERROR: no aligned block pairs — check that both files use matching ^block-ids", file=sys.stderr)
        sys.exit(1)

    print("Pass 1 : TF-IDF keyword extraction …", file=sys.stderr)
    keywords = select_en_keywords(tgt_blocks, top_n=args.top)
    print(f"         {len(keywords)} keywords selected", file=sys.stderr)
    if keywords:
        top10 = [kw for kw, _ in keywords[:10]]
        print(f"         top 10: {top10}", file=sys.stderr)

    print("Building sub-block pairs …", file=sys.stderr)
    pairs = build_subblock_pairs(src_blocks, tgt_blocks)
    print(f"         {len(pairs)} sub-block pairs", file=sys.stderr)

    print("Pass 2 : weighted co-occurrence …", file=sys.stderr)
    weighted_co, raw_co, pi_df = build_cooccurrence(
        pairs, keywords, max_pi_df=args.max_pi_df
    )

    glossary = build_glossary(
        keywords, weighted_co, raw_co,
        min_co=args.min_co,
        min_score=args.min_score,
        max_pi_per_kw=args.max_pi_per_kw,
    )
    print(f"terms  : {len(glossary)} Pāli tokens in output", file=sys.stderr)

    write_yaml(glossary, args.output, args.pali, args.english)
    print(f"output : {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
s.stderr)
    if not aligned_ids:
        print("ERROR: no aligned block pairs — check that both files use matching ^block-ids", file=sys.stderr)
        sys.exit(1)

    print("Pass 1 : TF-IDF keyword extraction …", file=sys.stderr)
    keywords = select_en_keywords(tgt_blocks, top_n=args.top)
    print(f"         {len(keywords)} keywords selected", file=sys.stderr)
    if keywords:
        top10 = [kw for kw, _ in keywords[:10]]
        print(f"         top 10: {top10}", file=sys.stderr)

    print("Building sub-block pairs …", file=sys.stderr)
    pairs = build_subblock_pairs(src_blocks, tgt_blocks)
    print(f"         {len(pairs)} sub-block pairs", file=sys.stderr)

    print("Pass 2 : weighted co-occurrence …", file=sys.stderr)
    weighted_co, raw_co, pi_df = build_cooccurrence(
        pairs, keywords, max_pi_df=args.max_pi_df
    )

    glossary = build_glossary(
        keywords, weighted_co, raw_co,
        min_co=args.min_co,
        min_score=args.min_score,
        max_pi_per_kw=args.max_pi_per_kw,
    )
    print(f"terms  : {len(glossary)} Pāli tokens in output", file=sys.stderr)

    write_yaml(glossary, args.output, args.pali, args.english)
    print(f"output : {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
