#!/usr/bin/env python3
"""
map_keywords_to_pali.py
=======================
For each English keyword (output of extract_keyword.py), find the most
likely Pāli translation candidates by co-occurrence over block-aligned
source files.

How alignment works
-------------------
Both source files share Obsidian-style block anchors (^1-0a-1, ^1-1, …):

    1-SOURCES/Text/pi-1.md            # Pāli root
    1-SOURCES/Translations/en-1-rhys_davids.md  # block-aligned English

Each anchored block on one side is the translation of the same anchor
on the other. We use that as the unit of alignment.

Scoring
-------
For an English keyword e and a Pāli word p:

    blocks(e) = set of block IDs containing e
    blocks(p) = set of block IDs containing p
    Dice(e, p) = 2 * |blocks(e) ∩ blocks(p)|
                 / (|blocks(e)| + |blocks(p)|)

Dice rewards Pāli words that appear in *most* of the keyword's blocks
*and* are not too common globally — exactly what we want for a
translation candidate.

Output
------
A markdown table at <out>.md:

    | English keyword | en blocks | top Pāli candidates (dice · pi blocks · co-occ) |

Usage
-----
    python3 map_keywords_to_pali.py \\
        --pali    1-SOURCES/Text/pi-1.md \\
        --english 1-SOURCES/Translations/en-1-rhys_davids.md \\
        --keywords keywords.md \\
        --top 5 \\
        --out keyword-pi-en-map
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# Markdown / text cleanup
# --------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
HEADER_RE      = re.compile(r"^#{1,6}\s.*$", re.MULTILINE)
PARENS_RE      = re.compile(r"\([^)]*\)")
BRACKETS_RE    = re.compile(r"\[[^\]]*\]")
ANCHOR_RE      = re.compile(r"\^([\w][\w-]*)")

# English: ASCII alphabetic only, length >= 3.
EN_WORD_RE = re.compile(r"[A-Za-z]{3,}")

# Pāli: Roman letters + IAST diacritics, length >= 3.
# The character class covers ā ī ū ṃ ṅ ñ ṭ ḍ ṇ ḷ etc. (and uppercase forms).
PI_WORD_RE = re.compile(r"[A-Za-z\u00C0-\u024F\u1E00-\u1EFF]{3,}")


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text)


def parse_blocks(text: str) -> dict:
    """Return {block_id: text_of_block}.

    A block is everything between two anchors (or between start-of-file
    and the first anchor). Heading lines are removed first so that
    heading anchors do not capture content.
    """
    text = strip_frontmatter(text)
    text = HEADER_RE.sub("", text)

    blocks = {}
    last_end = 0
    for m in ANCHOR_RE.finditer(text):
        block_id = m.group(1)
        blocks[block_id] = text[last_end:m.start()]
        last_end = m.end()
    return blocks


def tokenize_english(text: str):
    text = PARENS_RE.sub(" ", text)
    text = BRACKETS_RE.sub(" ", text)
    return [t.lower() for t in EN_WORD_RE.findall(text) if t.isascii()]


def tokenize_pali(text: str):
    """Return lowercased Pāli tokens.

    Drop strategy:
    - Tokens with at least one IAST diacritic are definitely Pāli → keep.
    - Pure-ASCII tokens of length < 4 are list markers / particles → drop.
    - Pure-ASCII tokens of length >= 4 that contain double consonants
      typical of Pāli (ss, tt, kk, pp, mm, nn, gg, cc, bh, dh, gh, jh,
      kh, th, ph) are likely Pāli inflected forms (phassa, kamma, …) → keep.
    - All other pure-ASCII tokens are likely English strays → drop.
    """
    text = PARENS_RE.sub(" ", text)
    text = BRACKETS_RE.sub(" ", text)
    # Pāli double-consonant / digraph patterns (not common in English)
    PALI_ASCII_RE = re.compile(r"(ss|tt|kk|pp|mm|nn|gg|cc|bh|dh|gh|jh|kh|th|ph|bb|dd)")
    out = []
    for tok in PI_WORD_RE.findall(text):
        if not tok.isascii():
            pass                             # has diacritic → definitely Pāli
        elif len(tok) < 4:
            continue                         # short ASCII: particle / marker
        elif not PALI_ASCII_RE.search(tok.lower()):
            continue                         # plain ASCII, no Pāli pattern → English stray
        out.append(tok.lower())
    return out


# --------------------------------------------------------------------------
# Keyword list parsing
# --------------------------------------------------------------------------

def parse_keywords(path: Path):
    """Accept either keywords.md (markdown table from extract_keyword.py)
    or keywords.txt (one keyword per line)."""
    keywords = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("|") and "---" not in line:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 2 and cells[0].isdigit():
                    keywords.append(cells[1])
                continue
            if line.startswith("#") or line.startswith("|"):
                continue
            # Plain-text mode: a real keyword is a single token without
            # punctuation. Lines with whitespace or a colon are metadata
            # ("Mode: ...", "Aligned blocks: ...", "Top 500 of N").
            if " " in line or ":" in line:
                continue
            keywords.append(line)
    return keywords


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Map English keywords to Pāli candidates via block co-occurrence."
    )
    ap.add_argument("--pali",     required=True, help="Pāli source markdown")
    ap.add_argument("--english",  required=True, help="English translation markdown")
    ap.add_argument("--keywords", required=True, help="keywords.md or keywords.txt")
    ap.add_argument("--top",      type=int, default=5,
                    help="Top N Pāli candidates per keyword (default 5)")
    ap.add_argument("--min-pali-blocks", type=int, default=2,
                    help="Drop Pāli candidates appearing in fewer blocks (default 2)")
    ap.add_argument("--out",      default="keyword-pi-en-map",
                    help="Output basename (default 'keyword-pi-en-map')")
    args = ap.parse_args()

    pi_text = Path(args.pali).read_text(encoding="utf-8")
    en_text = Path(args.english).read_text(encoding="utf-8")

    pi_blocks = parse_blocks(pi_text)
    en_blocks = parse_blocks(en_text)
    common = set(pi_blocks) & set(en_blocks)
    print(f"Pāli blocks: {len(pi_blocks)}, English blocks: {len(en_blocks)}, "
          f"aligned: {len(common)}", file=sys.stderr)

    # Inverted indexes over the aligned blocks only.
    en_word_blocks = defaultdict(set)
    pi_word_blocks = defaultdict(set)
    for bid in common:
        for tok in set(tokenize_english(en_blocks[bid])):
            en_word_blocks[tok].add(bid)
        for tok in set(tokenize_pali(pi_blocks[bid])):
            pi_word_blocks[tok].add(bid)

    keywords = parse_keywords(Path(args.keywords))
    print(f"Mapping {len(keywords)} English keywords...", file=sys.stderr)

    out_path = Path(f"{args.out}.md")
    matched = 0
    with out_path.open("w", encoding="utf-8") as f:
        f.write("# English → Pāli keyword map\n\n")
        f.write(f"- Pāli source: `{args.pali}`\n")
        f.write(f"- English translation: `{args.english}`\n")
        f.write(f"- Keywords list: `{args.keywords}`\n")
        f.write(f"- Aligned blocks: {len(common)}\n")
        f.write(f"- Top {args.top} Pāli candidates per keyword, "
                f"min {args.min_pali_blocks} block(s) for a candidate\n\n")
        f.write("Each candidate is shown as **pali** (dice · pi-blocks · co-occurrences).\n\n")
        f.write("| English keyword | en blocks | top Pāli candidates |\n")
        f.write("| --- | ---: | --- |\n")

        for en in keywords:
            en_set = en_word_blocks.get(en.lower(), set())
            if not en_set:
                f.write(f"| {en} | 0 | — |\n")
                continue

            scored = []
            for pi, pi_set in pi_word_blocks.items():
                if len(pi_set) < args.min_pali_blocks:
                    continue
                co = len(en_set & pi_set)
                if co == 0:
                    continue
                dice = 2 * co / (len(en_set) + len(pi_set))
                scored.append((pi, dice, len(pi_set), co))

            if not scored:
                f.write(f"| {en} | {len(en_set)} | — |\n")
                continue

            matched += 1
            scored.sort(key=lambda x: -x[1])
            top = scored[:args.top]
            cands = "; ".join(
                f"**{p}** ({d:.2f} · {pb} · {co})" for p, d, pb, co in top
            )
            f.write(f"| {en} | {len(en_set)} | {cands} |\n")

    print(f"Mapped {matched}/{len(keywords)} keywords with Pāli candidates",
          file=sys.stderr)
    print(f"Wrote: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
