#!/usr/bin/env python3
"""
translation_variants.py
=======================
Extract term-translation frequency pairs from a pair of block-aligned
source (Pāli) and target (English) markdown files.

Usage
-----
    python3 translation_variants.py <source_file> <target_file> <output_yaml>

Example
-------
    python3 translation_variants.py \
        1-SOURCES/Text/pi-1.md \
        3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md \
        0-INBOX/translation-variants-pi-en.yaml

Output format
-------------
    āsava:
      taints: 23
      cankers: 12
    ogha:
      floods: 18
      torrent: 1
"""

import re
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# 1. Pāli stopwords — grammatical particles and ubiquitous content words
# ---------------------------------------------------------------------------
PALI_STOP = {
    "ca", "kho", "pana", "ceva", "va", "na", "no", "nu", "hi", "tu",
    "pi", "api", "atha", "ti", "iti", "eva", "yeva", "vā", "nāma",
    "seyyathā", "yathā", "tathā", "tattha", "idha", "taṃ", "tesaṃ",
    "ime", "imā", "imāni", "ye", "yā", "yāni", "tam", "tad",
    # ubiquitous content words
    "dhamma", "dhammā", "dhamme", "dhammānaṃ",
    "ka", "kha", "ga",          # Ka / Kha / Ga section labels
    "neva", "puna", "tena",
}

# ---------------------------------------------------------------------------
# 2. English stopwords — function words + structural translation words
# ---------------------------------------------------------------------------
EN_STOP = {
    # function words
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
    # section markers that leak through
    "ka", "kha", "ga",
    # structural words ubiquitous in Abhidhamma translation prose
    "phenomena", "states", "state", "dhammas",
    "associated", "dissociated", "disjoined", "conjoined",
    "accompanied", "pertaining",
    "excluding", "included", "including",
    "called", "said", "known", "named",
    "what", "whatever", "whichever",
    "two", "three", "four", "five",
    "remaining", "other", "same",
    "whether", "either", "lead",
}

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------
BLOCK_ID_RE = re.compile(r"\^[\w\-]+")
SECTION_LABEL_RE = re.compile(r"\([KkGgAaBb][a-z]?\)\s*", re.UNICODE)
BRACKET_CONTENT_RE = re.compile(r"\[.*?\]")   # [syā.] variants
HEADING_RE = re.compile(r"^#{1,6}\s+")
FRONTMATTER_RE = re.compile(r"^---\s*$")
NUMBER_PREFIX_RE = re.compile(r"^\d+\.\s*")
HASH_TOKEN_RE = re.compile(r"^#+$")


# ---------------------------------------------------------------------------
# 3. Parse a markdown file into {block_id: text_content}
# ---------------------------------------------------------------------------
def parse_blocks(path: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    current_lines: list[str] = []
    in_frontmatter = False
    fm_count = 0

    with open(path, encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.rstrip("\n")

            if FRONTMATTER_RE.match(line):
                fm_count += 1
                if fm_count == 1:
                    in_frontmatter = True
                elif fm_count == 2:
                    in_frontmatter = False
                continue
            if in_frontmatter:
                continue

            m = BLOCK_ID_RE.search(line)
            if m:
                block_id = m.group()[1:]
                text_part = line[: m.start()].strip()
                current_lines.append(text_part)
                clean_lines = [HEADING_RE.sub("", l) for l in current_lines]
                blocks[block_id] = " ".join(clean_lines)
                current_lines = []
            else:
                current_lines.append(line)

    return blocks


# ---------------------------------------------------------------------------
# 4. Tokenise Pāli → list of normalised stems
# ---------------------------------------------------------------------------
_PALI_SUFFIXES = [
    "sampayuttānaṃ", "sampayuttā", "sampayutto", "sampayuttam",
    "vippayuttānaṃ", "vippayuttā", "vippayutto",
    "niyānaṃ", "niyā", "niyo", "niyaṃ",
    "ārammaṇānaṃ", "ārammaṇā", "ārammaṇo",
    "ādhipatino", "ādhipati",
    "hetukānaṃ", "hetukā", "hetuko",
    "gāminīnaṃ", "gāmino", "gāminī",
    "ānaṃ", "āni", "āsu",
]
_SHORT_SUFFIXES = ["ā", "o", "aṃ", "e"]

_PALI_PUNCT = str.maketrans("", "", ".,;:!?()[]{}\"'`''""—–-_/\\")


def _stem_pali(word: str) -> str:
    for suf in _PALI_SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[: -len(suf)]
    for suf in _SHORT_SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 4:
            return word[: -len(suf)]
    return word


def tokenise_pali(text: str) -> list[str]:
    text = BRACKET_CONTENT_RE.sub("", text)
    text = SECTION_LABEL_RE.sub("", text)
    text = NUMBER_PREFIX_RE.sub("", text)
    text = text.translate(_PALI_PUNCT).lower()

    tokens = []
    for raw in text.split():
        tok = raw.strip()
        if not tok or tok.isdigit() or HASH_TOKEN_RE.match(tok):
            continue
        if tok.isascii() and len(tok) <= 3:
            continue
        stem = _stem_pali(tok)
        if stem in PALI_STOP or len(stem) < 3:
            continue
        tokens.append(stem)
    return tokens


# ---------------------------------------------------------------------------
# 5. Tokenise English → list of lowercase tokens
# ---------------------------------------------------------------------------
_EN_PUNCT = str.maketrans("", "", ".,;:!?()[]{}\"'`''""—–-_/\\")


def tokenise_english(text: str) -> list[str]:
    text = SECTION_LABEL_RE.sub("", text)
    text = NUMBER_PREFIX_RE.sub("", text)
    text = HEADING_RE.sub("", text)
    text = text.translate(_EN_PUNCT).lower()

    tokens = []
    for raw in text.split():
        tok = raw.strip()
        if not tok or tok.isdigit() or HASH_TOKEN_RE.match(tok):
            continue
        if tok in EN_STOP or len(tok) < 3:
            continue
        tokens.append(tok)
    return tokens


# ---------------------------------------------------------------------------
# 6. Build co-occurrence counts (at block level)
# ---------------------------------------------------------------------------
def build_cooccurrence(
    src_blocks: dict[str, str],
    tgt_blocks: dict[str, str],
) -> tuple[dict[str, dict[str, int]], dict[str, int], dict[str, int]]:
    """
    Returns:
      cooc[pi_stem][en_tok] = blocks where both appear
      src_df[pi_stem]       = blocks where pi_stem appears
      tgt_df[en_tok]        = blocks where en_tok appears (for IDF filter)
    """
    cooc: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    src_df: dict[str, int] = defaultdict(int)
    tgt_df: dict[str, int] = defaultdict(int)

    common_ids = set(src_blocks) & set(tgt_blocks)
    for bid in sorted(common_ids):
        pi_tokens = set(tokenise_pali(src_blocks[bid]))
        en_tokens = set(tokenise_english(tgt_blocks[bid]))

        for pt in pi_tokens:
            src_df[pt] += 1
            for et in en_tokens:
                cooc[pt][et] += 1

        for et in en_tokens:
            tgt_df[et] += 1

    return cooc, src_df, tgt_df


# ---------------------------------------------------------------------------
# 7. Score and filter pairs
# ---------------------------------------------------------------------------
def compute_variants(
    cooc: dict[str, dict[str, int]],
    src_df: dict[str, int],
    tgt_df: dict[str, int],
    total_blocks: int,
    min_src_freq: int = 2,
    min_cooc: int = 2,
    min_exclusivity: float = 0.35,
    max_en_prevalence: float = 0.30,
) -> dict[str, dict[str, int]]:
    """
    For each Pāli stem (≥ min_src_freq blocks), return English tokens where:
      - cooc ≥ min_cooc
      - exclusivity = cooc / src_df ≥ min_exclusivity
        (English word appears in ≥35% of blocks containing this Pāli stem)
      - en prevalence = tgt_df / total_blocks < max_en_prevalence
        (English word is not so ubiquitous it appears everywhere — IDF cutoff)
    """
    results: dict[str, dict[str, int]] = {}

    for pi_stem, en_counts in cooc.items():
        if src_df[pi_stem] < min_src_freq:
            continue

        renderings: dict[str, int] = {}
        for en_tok, cnt in en_counts.items():
            if cnt < min_cooc:
                continue
            exclusivity = cnt / src_df[pi_stem]
            if exclusivity < min_exclusivity:
                continue
            en_prevalence = tgt_df[en_tok] / total_blocks
            if en_prevalence >= max_en_prevalence:
                continue
            renderings[en_tok] = cnt

        if renderings:
            results[pi_stem] = dict(
                sorted(renderings.items(), key=lambda x: x[1], reverse=True)
            )

    return results


# ---------------------------------------------------------------------------
# 8. Write YAML output
# ---------------------------------------------------------------------------
def write_yaml(variants: dict[str, dict[str, int]], out_path: str) -> None:
    lines = [
        "# Translation variant frequencies",
        "# pali_stem:",
        "#   en_rendering: frequency",
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
def main() -> None:
    if len(sys.argv) != 4:
        print(
            "Usage: translation_variants.py <source_file> <target_file> <output_yaml>",
            file=sys.stderr,
        )
        sys.exit(1)

    src_path, tgt_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

    src_blocks = parse_blocks(src_path)
    tgt_blocks = parse_blocks(tgt_path)
    common = set(src_blocks) & set(tgt_blocks)

    cooc, src_df, tgt_df = build_cooccurrence(src_blocks, tgt_blocks)
    variants = compute_variants(
        cooc, src_df, tgt_df,
        total_blocks=len(common),
        min_src_freq=2,
        min_cooc=2,
        min_exclusivity=0.35,
        max_en_prevalence=0.30,
    )

    write_yaml(variants, out_path)

    # Summary to stdout
    print(f"source : {src_path} ({len(src_blocks)} blocks)")
    print(f"target : {tgt_path} ({len(tgt_blocks)} blocks)")
    print(f"aligned: {len(common)} block pairs")
    print(f"terms  : {len(variants)} Pāli stems with attested renderings")
    print(f"output : {out_path}")


if __name__ == "__main__":
    main()
