#!/usr/bin/env python3
"""
translation_variants.py — two-pass translation-variant extractor
================================================================
Pass 1  TF-IDF on the English blocks to identify domain keywords —
        terms that recur in this translation but are rare in general
        English (corpus reference: en_freq.py / wordfreq).

Pass 2  For each English keyword, scan aligned Pali-English SUB-BLOCKS
        (split within each block on Ka/Kha/Ga markers so that triads
        are aligned line-by-line rather than block-by-block).

This sub-block alignment means "Wholesome" maps to kusalā, not to all
three terms in a triad block.

Output  YAML: pali_stem -> {en_rendering: raw_block_count}

Usage
-----
    python3 translation_variants.py <source_file> <target_file> <output_yaml>
"""

import math, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import en_freq

# ── stopwords ────────────────────────────────────────────────────────────────

PALI_STOP = {
    "ca", "kho", "pana", "ceva", "va", "na", "no", "nu", "hi", "tu",
    "pi", "api", "atha", "ti", "iti", "eva", "yeva",
    "seyyatha", "yatha", "tatha", "tattha", "idha", "tam", "tesam",
    "ime", "ima", "imani", "ye", "ya", "yani", "tad",
    "dhamma", "dhamme", "dhammanan",
    "ka", "kha", "ga", "neva", "puna", "tena",
    # prose-formula words that swamp term-alignment
    "katame", "katama", "katam", "katami",
    "samaya", "samay", "tasmin", "tasmim", "tasma",
    "yassa", "yasm", "tasm", "evam", "ettha",
    "tatiya", "dutiya", "patham",
}

EN_STOP = {
    "the","a","an","and","or","but","that","which","who","is","are","were",
    "was","be","been","being","have","has","had","do","does","did","will",
    "would","could","should","may","might","must","can","of","in","to",
    "for","on","at","by","with","from","into","through","both","also",
    "not","nor","neither","no","only","than","as","if","whether","when",
    "while","yet","thus","then","here","there","now","just","still",
    "all","any","each","every","some","this","these","those","its","it",
    "they","them","their","ka","kha","ga",
    "phenomena","states","state","dhammas","associated","dissociated",
    "disjoined","conjoined","accompanied","pertaining","conducive",
    "excluding","included","including","called","said","known","named",
    "what","whatever","whichever","remaining","other","same","such",
    "whether","either",
}

# ── regexes ──────────────────────────────────────────────────────────────────

BLOCK_ID_RE      = re.compile(r"\^[\w\-]+")
# Section markers — used to SPLIT sub-blocks (not just strip)
SUB_SPLIT_RE     = re.compile(r"(?=\([KkGgAaBb][a-z]*\))")
SECTION_STRIP_RE = re.compile(r"^\([KkGgAaBb][a-z]*\)\s*")
BRACKET_RE       = re.compile(r"\[.*?\]")
HEADING_RE       = re.compile(r"^#{1,6}\s+")
FRONTMATTER_RE   = re.compile(r"^---\s*$")
NUMBER_PFX_RE    = re.compile(r"^\d+\.\s*")
HASH_RE          = re.compile(r"^#+$")
_PUNCT = str.maketrans("", "", ".,;:!?()" + "[]{}\"'`''""—–-_/\\")


def _plain(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


# ── block parser ─────────────────────────────────────────────────────────────

def parse_blocks(path):
    blocks = {}
    current = []
    in_fm, fm_count = False, 0
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if FRONTMATTER_RE.match(line):
                fm_count += 1
                in_fm = (fm_count == 1)
                if fm_count == 2: in_fm = False
                continue
            if in_fm: continue
            m = BLOCK_ID_RE.search(line)
            if m:
                bid = m.group()[1:]
                current.append(line[:m.start()].strip())
                blocks[bid] = " ".join(HEADING_RE.sub("", l) for l in current)
                current = []
            else:
                current.append(line)
    return blocks


def split_subblocks(text):
    """
    Split a block text at Ka/Kha/Ga markers into labelled sub-strings.
    Returns [(label, text), ...].  If no markers, returns [('', text)].
    """
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
            label = ""
            body  = part
        if body:
            result.append((label, body))
    return result if result else [("", text)]


# ── tokenisers ───────────────────────────────────────────────────────────────

def _en_tokens(text):
    text = BRACKET_RE.sub("", text)
    text = HEADING_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    out = []
    for tok in text.split():
        tok = tok.strip()
        if not tok or tok.isdigit() or HASH_RE.match(tok): continue
        if tok in EN_STOP or len(tok) < 3: continue
        out.append(tok)
    return out


_PALI_SFXS = [
    "sampayuttanam","sampayutta","sampayutto",
    "vippayuttanam","vippayutta","vippayutto",
    "niyaham","niya","niyo","arammanam","arammana","arammano",
    "adhipatino","hetukam","hetuka","hetuko","gamino","gamini",
    "anam","ani","asu",
]
_SHORT_SFXS = ["a","o","e"]


def _stem(word):
    p = _plain(word)
    for suf in _PALI_SFXS:
        if p.endswith(suf) and len(p)-len(suf) >= 3:
            return word[:len(word)-len(suf)]
    for suf in _SHORT_SFXS:
        if p.endswith(suf) and len(p)-len(suf) >= 4:
            return word[:len(word)-len(suf)]
    return word


def _pali_tokens(text):
    text = BRACKET_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    out = []
    for tok in text.split():
        tok = tok.strip()
        if not tok or tok.isdigit() or HASH_RE.match(tok): continue
        if tok.isascii() and len(tok) <= 3: continue
        p = _plain(tok)
        if p in PALI_STOP or len(p) < 3: continue
        stem = _stem(tok)
        ps = _plain(stem)
        if ps in PALI_STOP or len(ps) < 3 or len(ps) > 12: continue
        out.append(stem)
    return out


# ── build sub-block pairs ────────────────────────────────────────────────────

def build_subblock_pairs(src_blocks, tgt_blocks):
    """
    For each aligned block, split into (Ka/Kha/Ga) sub-blocks and pair
    them by matching label.  Returns list of (pali_text, en_text) strings.
    """
    pairs = []
    for bid in sorted(set(src_blocks) & set(tgt_blocks)):
        src_subs = {lbl: body for lbl, body in split_subblocks(src_blocks[bid])}
        tgt_subs = {lbl: body for lbl, body in split_subblocks(tgt_blocks[bid])}
        # Match by label; fall back to full block if only '' label
        if len(src_subs) == 1 and "" in src_subs:
            pairs.append((src_subs[""], tgt_subs.get("", list(tgt_subs.values())[0] if tgt_subs else "")))
        else:
            for lbl in src_subs:
                if lbl in tgt_subs:
                    pairs.append((src_subs[lbl], tgt_subs[lbl]))
    return pairs


# ── Pass 1: TF-IDF English keyword extraction ────────────────────────────────

def extract_en_keywords(tgt_blocks, top_n=600, min_df=2):
    """
    Return [(en_token, tfidf_score, block_df), ...] sorted by score desc.
    TF  = block document frequency (blocks where token appears)
    IDF = log(1 + 1/corpus_freq) from en_freq
    """
    df = defaultdict(int)
    for text in tgt_blocks.values():
        seen = set()
        for tok in _en_tokens(text):
            if tok not in seen:
                df[tok] += 1
                seen.add(tok)

    N = len(tgt_blocks)
    scores = []
    for tok, doc_freq in df.items():
        if doc_freq < min_df: continue
        if en_freq.is_common(tok): continue
        corpus_f = en_freq.get_frequency(tok)
        idf = min(math.log(1.0 + 1.0 / (corpus_f + 1e-8)), math.log(1e6))
        scores.append((tok, (doc_freq / N) * idf, doc_freq))

    scores.sort(key=lambda x: -x[1])
    return scores[:top_n]


# ── Pass 2: align each English keyword to its Pali counterpart ───────────────

def align_keywords(keywords, pairs, min_pali_score=0.3):
    """
    For each English keyword, iterate over sub-block pairs and accumulate
    weighted Pali stem co-occurrences (weight = 1/|unique_pali_stems|).

    Returns {en_kw: {pali_stem: weighted_score}}.
    """
    kw_set = {kw for kw, _, _ in keywords}

    # Pre-tokenise all pairs once
    tok_pairs = [(set(_pali_tokens(s)), set(_en_tokens(e))) for s, e in pairs]

    en_to_pali = {kw: defaultdict(float) for kw in kw_set}

    for pi_set, en_set in tok_pairs:
        hit_kws = en_set & kw_set
        if not hit_kws or not pi_set:
            continue
        w = 1.0 / len(pi_set)
        for kw in hit_kws:
            for pt in pi_set:
                en_to_pali[kw][pt] += w

    return {kw: dict(sorted(d.items(), key=lambda x: -x[1]))
            for kw, d in en_to_pali.items() if d}


# ── Build final glossary: pali_stem → {en_kw: raw_count} ────────────────────

def build_glossary(keywords, en_to_pali, pairs,
                   max_pali_per_kw=1, min_pali_score=0.3, min_raw=2):
    """
    Flip the alignment: pali_stem → list of en keywords it is the top
    counterpart for, with raw co-occurrence counts.
    """
    # Raw (unweighted) counts
    raw = defaultdict(lambda: defaultdict(int))
    for pi_set, en_set in [(set(_pali_tokens(s)), set(_en_tokens(e))) for s, e in pairs]:
        for pt in pi_set:
            for et in en_set:
                raw[pt][et] += 1

    glossary = defaultdict(dict)
    for kw, _, _ in keywords:
        pali_ranks = list((en_to_pali.get(kw) or {}).items())
        if not pali_ranks: continue
        for pali_stem, score in pali_ranks[:max_pali_per_kw]:
            if score < min_pali_score: continue
            count = raw[pali_stem].get(kw, 0)
            if count >= min_raw:
                glossary[pali_stem][kw] = count

    return {stem: dict(sorted(v.items(), key=lambda x: -x[1]))
            for stem, v in sorted(glossary.items())}


# ── YAML writer ───────────────────────────────────────────────────────────────

def write_yaml(glossary, out_path):
    lines = [
        "# Translation variant frequencies",
        "# Method: English TF-IDF keyword extraction + sub-block Pali alignment",
        "# pali_stem:",
        "#   en_rendering: co_occurrence_count",
        "#",
        "# Generated by 4-SYSTEM/Skills/translation-variants/scripts/translation_variants.py",
        "",
    ]
    for stem in sorted(glossary):
        lines.append(f"{stem}:")
        for en_tok, freq in glossary[stem].items():
            lines.append(f"  {en_tok}: {freq}")
        lines.append("")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) != 4:
        print("Usage: translation_variants.py <source> <target> <output.yaml>", file=sys.stderr)
        sys.exit(1)
    src_path, tgt_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    src_blocks = parse_blocks(src_path)
    tgt_blocks = parse_blocks(tgt_path)

    print(f"source : {src_path} ({len(src_blocks)} blocks)")
    print(f"target : {tgt_path} ({len(tgt_blocks)} blocks)")

    print("Pass 1 : TF-IDF keyword extraction …")
    keywords = extract_en_keywords(tgt_blocks, top_n=600, min_df=2)
    print(f"         {len(keywords)} keywords")

    print("Building sub-block pairs …")
    pairs = build_subblock_pairs(src_blocks, tgt_blocks)
    print(f"         {len(pairs)} sub-block pairs")

    print("Pass 2 : aligning keywords to Pali stems …")
    en_to_pali = align_keywords(keywords, pairs)

    glossary = build_glossary(keywords, en_to_pali, pairs)
    write_yaml(glossary, out_path)
    print(f"terms  : {len(glossary)} Pali stems in output")
    print(f"output : {out_path}")


if __name__ == "__main__":
    main()
