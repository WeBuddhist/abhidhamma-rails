#!/usr/bin/env python3
"""
extract_pali_keywords.py
========================
Extract and rank Pāli lemmas from a SuttaCentral-style markdown root
text (e.g. `1-SOURCES/Text/pi-1.md`).

Mirror of `extract_keyword.py` for Pāli, with three differences:

1. **Frequency, not TF-IDF.** There is no Pāli reference corpus, so we
   rank lemmas by document frequency (DF) over aligned anchored
   blocks: how many blocks contain the lemma at least once.
2. **Lemmatization.** Tokens are normalized with the rule-based
   case-ending stripper from `flip_to_pali_glossary.py`. Inflected
   forms (`vedanākkhandho`, `vedanākkhandhaṃ`, `vedanākkhandhassa`)
   collapse to one lemma (`vedanākkhandha`).
3. **Stopword filter.** Particles that pervade the corpus (`taṃ`,
   `idaṃ`, `katamaṃ`, `dhammā`, `hoti`, …) are filtered by a DF cap.

Outputs:
  <out>.md    ranked keyword table (rank, lemma, DF, total TF, example forms)
  <out>.txt   plain lemma list, one per line — feeds map_pali_to_english.py

Usage:
  python3 extract_pali_keywords.py 1-SOURCES/Text/pi-1.md \\
      --top 500 \\
      --max-df 0.60 \\
      --out pi-keywords
"""

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Reuse parsing/tokenization from the existing English-side scripts.
from map_keywords_to_pali import parse_blocks, tokenize_pali
from flip_to_pali_glossary import normalize_pali


# Closed-class Pāli particles, pronouns, demonstratives, and formulaic
# auxiliaries that survive the DF cap but aren't useful glossary
# headwords. After lemmatization, every variant collapses to one of
# these stems.
PALI_STOPWORDS = {
    # demonstrative / personal pronouns and their case forms
    "ta", "sa", "ya", "ka", "ima", "esa", "eta",
    "taṃ", "idaṃ", "ayaṃ", "yaṃ", "etaṃ", "imaṃ", "naṃ",
    "tasmiṃ", "asmiṃ", "yasmiṃ", "imasmiṃ", "etasmiṃ", "tamhi",
    "tassa", "yassa", "imassa", "etassa",
    "tena", "yena", "kena", "imena", "etena",
    "te", "ye", "ke", "ime", "ete", "ne",
    "so", "yo", "ko", "ayo",
    # discourse particles
    "ca", "vā", "hi", "pi", "kho", "eva", "nu", "no", "atho",
    "atha", "iti", "yathā", "tathā", "evaṃ", "tena",
    # question / quantity markers
    "katama", "kati", "kim",
    # formulaic / generic auxiliaries (NOT content terms like dhamma/rūpa)
    "samaye", "samayo", "hoti", "atthi",
    "bhavati", "viharati", "katha",
    # negative / emphatic that aren't headword material
    "ma", "na", "vi",
}


def extract(text: str, max_df: float, lemmatize: bool):
    blocks = parse_blocks(text)
    n_blocks = len(blocks)

    df = Counter()                              # lemma -> # blocks containing it
    tf = Counter()                              # lemma -> total token count
    forms = defaultdict(Counter)                # lemma -> Counter of inflected forms

    for _bid, block_text in blocks.items():
        seen_in_block = set()
        for tok in tokenize_pali(block_text):
            lemma = normalize_pali(tok) if lemmatize else tok
            tf[lemma] += 1
            forms[lemma][tok] += 1
            seen_in_block.add(lemma)
        for lemma in seen_in_block:
            df[lemma] += 1

    df_cap = max_df * n_blocks
    keepers = [
        lemma for lemma, c in df.items()
        if c <= df_cap and lemma not in PALI_STOPWORDS
    ]
    keepers.sort(key=lambda l: (-df[l], -tf[l], l))
    return n_blocks, keepers, df, tf, forms


def main():
    ap = argparse.ArgumentParser(description="Rank Pāli lemmas from a markdown source.")
    ap.add_argument("input", help="Path to the .md Pāli root text file")
    ap.add_argument("--top", type=int, default=500,
                    help="Number of lemmas to keep (default 500)")
    ap.add_argument("--out", default="pi-keywords",
                    help="Output basename (default 'pi-keywords')")
    ap.add_argument("--max-df", type=float, default=0.80,
                    help="Drop lemmas appearing in more than this fraction of blocks (default 0.80)")
    ap.add_argument("--no-lemmatize", action="store_true",
                    help="Disable rule-based lemmatization; keep surface forms.")
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    n_blocks, keepers, df, tf, forms = extract(
        text, args.max_df, lemmatize=not args.no_lemmatize
    )

    top = keepers[: args.top]

    md_path = Path(f"{args.out}.md")
    with md_path.open("w", encoding="utf-8") as f:
        f.write(f"# Pāli keywords — {args.input}\n\n")
        f.write("Mode: document-frequency over anchored blocks  \n")
        f.write(f"Aligned blocks: {n_blocks}  \n")
        f.write(
            "Lemmatization: "
            f"{'rule-based case-ending stripping' if not args.no_lemmatize else 'off'}  \n"
        )
        f.write(
            f"Filters: DF ≤ {args.max_df:.2f} · top {args.top} of "
            f"{len(keepers)} surviving lemmas (of {len(df)} total)\n\n"
        )
        f.write("| rank | lemma | block-DF | total-TF | example inflected forms |\n")
        f.write("| ---: | --- | ---: | ---: | --- |\n")
        for i, lemma in enumerate(top, 1):
            ex = ", ".join(f"{w}({c})" for w, c in forms[lemma].most_common(3))
            f.write(f"| {i} | {lemma} | {df[lemma]} | {tf[lemma]} | {ex} |\n")

    txt_path = Path(f"{args.out}.txt")
    with txt_path.open("w", encoding="utf-8") as f:
        for lemma in top:
            f.write(lemma + "\n")

    print(
        f"Total lemmas: {len(df)} | after DF filter: {len(keepers)} | "
        f"written: {len(top)}",
        file=sys.stderr,
    )
    print(f"Wrote: {md_path}", file=sys.stderr)
    print(f"Wrote: {txt_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
