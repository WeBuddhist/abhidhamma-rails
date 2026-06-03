#!/usr/bin/env python3
"""
gather_examples.py
==================
Build a single markdown file containing each Pāli keyword paired with
example block(s) drawn ONLY from the Pāli source.

The Cursor agent reads the produced context file and generates the
glossary entries directly in chat — no external API and no English
reference translation are consulted.

Usage:
    python3 gather_examples.py \\
        --keywords pi-keywords.txt \\
        --pali 1-SOURCES/Text/pi-1.md \\
        --examples 2 --max-chars 320 \\
        --out pi-keywords-context
"""

import argparse
import sys
from pathlib import Path

from zero_shot_glossary import build_index, get_examples
from map_keywords_to_pali import parse_keywords


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keywords", default="pi-keywords.txt")
    ap.add_argument("--pali",     default="1-SOURCES/Text/pi-1.md")
    ap.add_argument("--examples", type=int, default=2)
    ap.add_argument("--max-chars", type=int, default=320)
    ap.add_argument("--out", default="pi-keywords-context")
    args = ap.parse_args()

    pi_text = Path(args.pali).read_text(encoding="utf-8")
    # build_index needs an English text to align block IDs; we pass the
    # Pāli text in twice so we still get a working block→lemma index but
    # never read or emit any English content.
    pi_blocks, _en_blocks, lemma_to_bids = build_index(pi_text, pi_text)

    keywords = parse_keywords(Path(args.keywords))
    out_path = Path(f"{args.out}.md")

    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"# Pāli keyword examples — {len(keywords)} lemmas\n\n")
        f.write(f"_Pāli only. {args.examples} example block(s) per lemma, "
                f"truncated to {args.max_chars} chars._\n\n---\n\n")
        for i, lemma in enumerate(keywords, 1):
            f.write(f"## {i}. {lemma}\n\n")
            examples = get_examples(
                lemma, pi_blocks, pi_blocks, lemma_to_bids, args.examples
            )
            if not examples:
                f.write("_(no examples found)_\n\n")
                continue
            for j, (pi, _en) in enumerate(examples, 1):
                pi_s = " ".join(pi.split())[: args.max_chars]
                f.write(f"**pi#{j}:** {pi_s}\n\n")

    print(f"Wrote: {out_path} ({len(keywords)} keywords)", file=sys.stderr)


if __name__ == "__main__":
    main()
