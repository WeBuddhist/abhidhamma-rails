#!/usr/bin/env python3
"""
translation_variants.py
=======================
Extract term-translation frequency pairs from a pair of block-aligned
source (Pali) and target (English) markdown files.

Algorithm
---------
1. Parse both files into parallel blocks keyed by Obsidian block ID.
2. For each aligned block pair:
   - Tokenise Pali text into normalised stems (inflectional suffixes stripped,
     diacritics kept in output but stripped for matching).
   - Tokenise English text into content words.
   - Accumulate WEIGHTED co-occurrence: each block contributes 1/|pi_tokens|
     so short mAtikA entries (1-2 Pali terms) outweigh long prose paragraphs.
3. Filter pairs by:
   - exclusivity  = w_cooc / src_wdf  >= 0.45  (English word appears in
                                                 >=45% of Pali stem's weight)
   - precision    = w_cooc / tgt_wdf  >= 0.45  (Pali stem present in >=45%
                                                 of English word's weight)
   - w_cooc                           >= 1.0   (minimum total weighted count)
   - src_wdf                          >= 1.5   (stem in at least ~2 blocks)

Usage
-----
    python3 translation_variants.py <source_file> <target_file> <output_yaml>

Output format
-------------
    asava:
      taints: 23
      cankers: 12
    ogha:
      floods: 18
"""

import re
import sys
import unicodedata
from collections import defaultdict

# ---------------------------------------------------------------------------
# 1. Pali stopwords (normalised, no diacritics)
# ---------------------------------------------------------------------------
PALI_STOP = {
    "ca", "kho", "pana", "ceva", "va", "na", "no", "nu", "hi", "tu",
    "pi", "api", "atha", "ti", "iti", "eva", "yeva", "namma",
    "seyyatha", "yatha", "tatha", "tattha", "idha", "tam", "tesam",
    "ime", "ima", "imani", "ye", "ya", "yani", "tad",
    "dhamma", "dhamme", "dhammanan",
    "ka", "kha", "ga",
    "neva", "puna", "tena", "vatha", "yattha", "tattha",
}

# ---------------------------------------------------------------------------
# 2. English stopwords
# ---------------------------------------------------------------------------
EN_STOP = {
    "the", "a", "an", "and", "or", "but", "that", "which", "who", "whom",
    "is", "are", "were", "was", "be", "been", "being", "have", "has",
    "had", "do", "does", "did", "will", "would", "could", "should",
    "may", "might", "must", "can", "shall",
    "of", "in", "to", "for", "on", "at", "by", "with", "from",
    "into", "through", "both", "also", "not", "nor", "neither",
    "no", "only", "than", "as", "if", "whether", "when", "while",
    "indeed", "even", "further", "however", "yet", "thus", "then",
    "here", "there", "now", "just", "still", "again", "already",
    "all", "any", "each", "every", "some", "this", "these", "those",
    "its", "it", "they", "them", "their", "his", "her", "our", "your",
    # section markers that leak through after stripping punctuation
    "ka", "kha", "ga",
    # structural words in Abhidhamma translation prose
    "phenomena", "states", "state", "dhammas", "things", "thing",
    "associated", "dissociated", "disjoined", "conjoined",
    "accompanied", "pertaining", "conducive",
    "excluding", "included", "including",
    "called", "said", "known", "named",
    "what", "whatever", "whichever",
    "two", "three", "four", "five", "six", "seven", "eight",
    "remaining", "other", "same", "such",
    "whether", "either", "lead", "leads",
    "has", "had", "have", "been",
}

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------
BLOCK_ID_RE     = re.compile(r"\^[\w\-]+")
SECTION_LABEL_RE = re.compile(r"\([KkGgAaBb][a-z]?\)\s*")
BRACKET_RE      = re.compile(r"\[.*?\]")
HEADING_RE      = re.compile(r"^#{1,6}\s+")
FRONTMATTER_RE  = re.compile(r"^---\s*$")
NUMBER_PFX_RE   = re.compile(r"^\d+\.\s*")
HASH_RE         = re.compile(r"^#+$")

_PUNCT = str.maketrans("", "", ".,;:!?()" + "[]{}\"'`‘’“”—–-_/\\")


def _plain(s):
    """Strip diacritics for matching; keep original for output."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


# ---------------------------------------------------------------------------
# 3. Parse blocks: {block_id -> raw_text}
# ---------------------------------------------------------------------------
def parse_blocks(path):
    blocks = {}
    current = []
    in_fm = False
    fm_count = 0
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if FRONTMATTER_RE.match(line):
                fm_count += 1
                in_fm = (fm_count == 1)
                if fm_count == 2:
                    in_fm = False
                continue
            if in_fm:
                continue
            m = BLOCK_ID_RE.search(line)
            if m:
                bid = m.group()[1:]
                current.append(line[: m.start()].strip())
                blocks[bid] = " ".join(HEADING_RE.sub("", l) for l in current)
                current = []
            else:
                current.append(line)
    return blocks


# ---------------------------------------------------------------------------
# 4. Pali stemmer (inflection normalisation)
# ---------------------------------------------------------------------------
# Ordered longest-first; matching on plain (diacritic-stripped) form.
_PALI_SFXS = [
    "sampayuttanam", "sampayutta", "sampayutto",
    "vippayuttanam", "vippayutta", "vippayutto",
    "niyaham", "niya", "niyo",
    "arammanam", "arammana", "arammano",
    "adhipatino",
    "hetukam", "hetuka", "hetuko",
    "gamino", "gamini",
    "anam", "ani", "asu",
]
_SHORT_SFXS = ["a", "o", "e"]  # strip only if >= 4 chars remain


def _stem(word):
    p = _plain(word)
    for suf in _PALI_SFXS:
        if p.endswith(suf) and len(p) - len(suf) >= 3:
            return word[: len(word) - len(suf)]
    for suf in _SHORT_SFXS:
        if p.endswith(suf) and len(p) - len(suf) >= 4:
            return word[: len(word) - len(suf)]
    return word


def tokenise_pali(text):
    text = BRACKET_RE.sub("", text)
    text = SECTION_LABEL_RE.sub("", text)
    text = NUMBER_PFX_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    tokens = []
    for tok in text.split():
        tok = tok.strip()
        if not tok or tok.isdigit() or HASH_RE.match(tok):
            continue
        if tok.isascii() and len(tok) <= 3:
            continue
        p = _plain(tok)
        if p in PALI_STOP or len(p) < 3:
            continue
        stem = _stem(tok)
        ps = _plain(stem)
        if ps in PALI_STOP or len(ps) < 3:
            continue
        # Drop very long compounds (>20 plain chars) — not useful dictionary lemmas
        if len(ps) > 20:
            continue
        tokens.append(stem)
    return tokens


# ---------------------------------------------------------------------------
# 5. English tokeniser
# ---------------------------------------------------------------------------
def tokenise_english(text):
    text = SECTION_LABEL_RE.sub("", text)
    text = NUMBER_PFX_RE.sub("", text)
    text = HEADING_RE.sub("", text)
    text = text.translate(_PUNCT).lower()
    tokens = []
    for tok in text.split():
        tok = tok.strip()
        if not tok or tok.isdigit() or HASH_RE.match(tok):
            continue
        if tok in EN_STOP or len(tok) < 3:
            continue
        tokens.append(tok)
    return tokens


# ---------------------------------------------------------------------------
# 6. Build WEIGHTED co-occurrence
#    Weight per block = 1 / |unique Pali tokens in that block|
#    This ensures short mAtikA blocks (1-2 Pali terms) dominate over
#    long prose paragraphs (50+ Pali terms).
# ---------------------------------------------------------------------------
def build_cooccurrence(src_blocks, tgt_blocks):
    cooc    = defaultdict(lambda: defaultdict(float))
    src_wdf = defaultdict(float)   # weighted document frequency for Pali stems
    tgt_wdf = defaultdict(float)   # weighted document frequency for English tokens

    common = set(src_blocks) & set(tgt_blocks)
    for bid in sorted(common):
        pi_set = set(tokenise_pali(src_blocks[bid]))
        en_set = set(tokenise_english(tgt_blocks[bid]))
        if not pi_set:
            continue
        w = 1.0 / len(pi_set)      # block weight
        for pt in pi_set:
            src_wdf[pt] += w
            for et in en_set:
                cooc[pt][et] += w
        for et in en_set:
            tgt_wdf[et] += w

    return cooc, src_wdf, tgt_wdf


# ---------------------------------------------------------------------------
# 7. Filter and rank
# ---------------------------------------------------------------------------
def compute_variants(cooc, src_wdf, tgt_wdf,
                     min_wcooc=1.0, min_src_wdf=1.5,
                     min_exclusivity=0.45, min_precision=0.45):
    """
    For each Pali stem with src_wdf >= min_src_wdf, keep English tokens where:
      w_cooc >= min_wcooc
      exclusivity = w_cooc / src_wdf >= min_exclusivity
      precision   = w_cooc / tgt_wdf >= min_precision
    """
    results = {}
    for pi_stem, en_counts in cooc.items():
        if src_wdf[pi_stem] < min_src_wdf:
            continue
        renderings = {}
        for en_tok, w in en_counts.items():
            if w < min_wcooc:
                continue
            if w / src_wdf[pi_stem] < min_exclusivity:
                continue
            if w / tgt_wdf[en_tok] < min_precision:
                continue
            # store the weighted count as a rounded integer for readability
            renderings[en_tok] = round(w)
        if renderings:
            results[pi_stem] = dict(sorted(renderings.items(), key=lambda x: -x[1]))
    return results


# ---------------------------------------------------------------------------
# 8. YAML output
# ---------------------------------------------------------------------------
def write_yaml(variants, out_path):
    lines = [
        "# Translation variant frequencies",
        "# pali_stem:",
        "#   en_rendering: weighted_frequency",
        "#",
        "# Generated by 4-SYSTEM/Skills/translation-variants/scripts/translation_variants.py",
        "",
    ]
    for stem in sorted(variants):
        lines.append(f"{stem}:")
        for en_tok, freq in variants[stem].items():
            lines.append(f"  {en_tok}: {freq}")
        lines.append("")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ---------------------------------------------------------------------------
# 9. Main
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) != 4:
        print("Usage: translation_variants.py <source> <target> <output.yaml>",
              file=sys.stderr)
        sys.exit(1)

    src_path, tgt_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    src_blocks = parse_blocks(src_path)
    tgt_blocks = parse_blocks(tgt_path)
    common = set(src_blocks) & set(tgt_blocks)
    cooc, src_wdf, tgt_wdf = build_cooccurrence(src_blocks, tgt_blocks)
    variants = compute_variants(cooc, src_wdf, tgt_wdf)
    write_yaml(variants, out_path)

    print(f"source : {src_path} ({len(src_blocks)} blocks)")
    print(f"target : {tgt_path} ({len(tgt_blocks)} blocks)")
    print(f"aligned: {len(common)} block pairs")
    print(f"terms  : {len(variants)} Pali stems with attested renderings")
    print(f"output : {out_path}")


if __name__ == "__main__":
    main()
