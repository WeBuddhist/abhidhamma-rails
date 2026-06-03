#!/usr/bin/env python3
"""
map_pali_to_english.py
======================
Mirror of `map_keywords_to_pali.py`, but inverted: for each Pāli lemma,
find the most likely English renderings via block-aligned Dice
co-occurrence.

Pipeline
--------
    extract_pali_keywords.py  →  pi-keywords.md / pi-keywords.txt
    map_pali_to_english.py    →  pi-en-direct-map.md      (this script)

Scoring
-------
For a Pāli lemma L (over its inflected forms) and an English word w:

    blocks(L) = union of block IDs containing any inflected form of L
    blocks(w) = block IDs containing w
    Dice(L, w) = 2 · |blocks(L) ∩ blocks(w)| / (|blocks(L)| + |blocks(w)|)

Output
------
A single markdown file with two sections:

  1. **Compact form** (bb-glossary style):
        - **kusala**: (1) good; (2) moral; (3) wholesome ...
  2. **Detailed entries**: per-lemma table with stats and inflected
     forms.

Usage
-----
    python3 map_pali_to_english.py \\
        --pali     1-SOURCES/Text/pi-1.md \\
        --english  1-SOURCES/Translations/en-1-rhys_davids.md \\
        --keywords pi-keywords.md \\
        --top 5 \\
        --out pi-en-direct-map
"""

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from map_keywords_to_pali import (
    parse_blocks,
    tokenize_english,
    tokenize_pali,
    parse_keywords,
)
from flip_to_pali_glossary import normalize_pali, NOISE_EN


# Closed-class English function words that flood high-frequency Pāli
# blocks and drown out real translation candidates. We don't want any
# of these as a "sense" of a Pāli lemma.
ENGLISH_STOPWORDS = {
    # articles, pronouns, possessives
    "the", "this", "that", "these", "those", "all", "any", "some",
    "each", "every", "both", "either", "neither", "such", "same",
    "other", "another", "one", "two", "three", "four", "five",
    "few", "many", "more", "most", "much", "less", "least", "very",
    "she", "her", "his", "him", "they", "them", "their", "theirs",
    "you", "your", "yours", "our", "ours", "its", "itself", "themselves",
    "he", "we", "us", "i",
    # auxiliaries, copulas, common verbs
    "are", "was", "were", "been", "being", "have", "has", "had",
    "having", "does", "did", "doing", "done", "will", "would",
    "shall", "should", "can", "could", "may", "might", "must",
    "let", "make", "made", "becomes", "become", "becoming",
    # prepositions, conjunctions
    "with", "without", "into", "onto", "from", "upon", "over",
    "under", "between", "among", "through", "during", "before",
    "after", "above", "below", "until", "while", "since", "than",
    "out", "off", "down", "back", "forth", "round", "across",
    "against", "along", "around", "behind", "beside", "beyond",
    "for", "and", "but", "nor", "yet", "still", "also",
    # adverbs / fillers
    "now", "then", "there", "here", "where", "when", "what",
    "which", "whose", "who", "whom", "how", "why", "while",
    "ever", "never", "again", "thus", "hence", "therefore",
    "however", "moreover", "furthermore",
    "just", "even", "only", "too", "rather",
    # negators / qualifiers
    "not", "nor", "neither", "without",
    # generic content-light verbs / words
    "be", "do", "go", "come", "came", "go", "got", "get",
    "say", "said", "see", "seen", "saw",
}


def main():
    ap = argparse.ArgumentParser(
        description="Map Pāli lemmas to English candidates via block co-occurrence."
    )
    ap.add_argument("--pali", required=True, help="Pāli root markdown")
    ap.add_argument("--english", required=True, help="English translation markdown")
    ap.add_argument(
        "--keywords",
        required=True,
        help="Pāli keyword list (markdown table from extract_pali_keywords.py, "
        "or one lemma per line)",
    )
    ap.add_argument("--top", type=int, default=5,
                    help="Top N English candidates per lemma (default 5)")
    ap.add_argument("--min-en-blocks", type=int, default=2,
                    help="Drop English candidates appearing in fewer blocks (default 2)")
    ap.add_argument("--max-en-df", type=float, default=0.30,
                    help="Drop English candidates whose blocks/aligned > this (default 0.30)")
    ap.add_argument("--min-dice", type=float, default=0.10,
                    help="Drop English candidates below this Dice score (default 0.10)")
    ap.add_argument("--out", default="pi-en-direct-map",
                    help="Output basename (default 'pi-en-direct-map')")
    args = ap.parse_args()

    pi_text = Path(args.pali).read_text(encoding="utf-8")
    en_text = Path(args.english).read_text(encoding="utf-8")
    pi_blocks = parse_blocks(pi_text)
    en_blocks = parse_blocks(en_text)
    common = sorted(set(pi_blocks) & set(en_blocks))
    print(
        f"Pāli blocks: {len(pi_blocks)} · English blocks: {len(en_blocks)} · "
        f"aligned: {len(common)}",
        file=sys.stderr,
    )

    # Build block-set indexes over the aligned subset.
    lemma_blocks = defaultdict(set)
    en_word_blocks = defaultdict(set)
    forms_per_lemma = defaultdict(set)

    for bid in common:
        for tok in set(tokenize_pali(pi_blocks[bid])):
            lemma = normalize_pali(tok)
            lemma_blocks[lemma].add(bid)
            forms_per_lemma[lemma].add(tok)
        for tok in set(tokenize_english(en_blocks[bid])):
            en_word_blocks[tok].add(bid)

    en_df_cap = args.max_en_df * len(common)
    keywords = parse_keywords(Path(args.keywords))
    print(f"Mapping {len(keywords)} Pāli lemmas...", file=sys.stderr)

    matched = 0
    rows = []
    for lemma in keywords:
        lemma_lc = lemma.lower()
        pi_set = lemma_blocks.get(lemma_lc, set())
        if not pi_set:
            rows.append((lemma_lc, set(), []))
            continue
        scored = []
        for en, en_set in en_word_blocks.items():
            if en in NOISE_EN or en in ENGLISH_STOPWORDS or len(en) < 3:
                continue
            if len(en_set) < args.min_en_blocks or len(en_set) > en_df_cap:
                continue
            co = len(pi_set & en_set)
            if co == 0:
                continue
            dice = 2 * co / (len(pi_set) + len(en_set))
            if dice < args.min_dice:
                continue
            scored.append((en, dice, len(en_set), co))
        if scored:
            matched += 1
        scored.sort(key=lambda x: -x[1])
        rows.append((lemma_lc, pi_set, scored[: args.top]))

    out_path = Path(f"{args.out}.md")
    with out_path.open("w", encoding="utf-8") as f:
        f.write("# Pāli → English direct map\n\n")
        f.write(f"- Pāli source: `{args.pali}`\n")
        f.write(f"- English translation: `{args.english}`\n")
        f.write(f"- Keyword list: `{args.keywords}`\n")
        f.write(f"- Aligned blocks: {len(common)}\n")
        f.write(
            f"- Filters: en blocks ≥ {args.min_en_blocks}, en DF ≤ "
            f"{args.max_en_df:.2f}, Dice ≥ {args.min_dice}, top {args.top} senses\n"
        )
        f.write(f"- Mapped {matched}/{len(rows)} lemmas with at least one candidate\n\n")
        f.write(
            "> Status: draft — every entry is statistically derived. "
            "Senses are top-Dice English co-occurrences, not real polysemy splits.\n\n"
        )
        f.write("---\n\n## Compact form (bb-glossary style)\n\n")
        for lemma, pi_set, scored in rows:
            if not scored:
                note = "no aligned blocks" if not pi_set else "no candidate above thresholds"
                f.write(f"- **{lemma}**: —  _({note})_\n")
                continue
            senses = "; ".join(f"({i+1}) {en}" for i, (en, *_) in enumerate(scored))
            f.write(f"- **{lemma}**: {senses}\n")

        f.write("\n---\n\n## Detailed entries\n\n")
        for lemma, pi_set, scored in rows:
            f.write(f"### {lemma}\n\n")
            forms = ", ".join(sorted(forms_per_lemma.get(lemma, ())))
            f.write(f"_pi blocks: {len(pi_set)}; inflected forms: {forms or '—'}_\n\n")
            if not scored:
                f.write("_No English candidates above thresholds._\n\n")
                continue
            f.write("| # | english | dice | en blocks | co-occ |\n")
            f.write("| ---: | --- | ---: | ---: | ---: |\n")
            for i, (en, dice, en_blocks_, co) in enumerate(scored, 1):
                f.write(f"| {i} | {en} | {dice:.2f} | {en_blocks_} | {co} |\n")
            f.write("\n")

    print(f"Wrote: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
