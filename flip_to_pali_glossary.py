#!/usr/bin/env python3
"""
flip_to_pali_glossary.py
========================
Phase 1: flip the en→pi co-occurrence map produced by
`map_keywords_to_pali.py` into a Pāli-keyed draft glossary in the
style of `3-TRANSFORMATIONS/.../bb-glossary.md`:

    pali-lemma: (1) english-rendering-1; (2) english-rendering-2; ...

How it works
------------
1. Reads `keyword-pi-en-map.md` rows of the form
       | english | en_blocks | **pali** (dice · pi_blocks · co_occ); ... |
2. Applies a rule-based Pāli case-ending stripper to collapse inflected
   forms to a stem (`vedanākkhandho`, `vedanākkhandhaṃ`,
   `vedanākkhandhā` → `vedanākkhandha`).
3. Filters Pāli particles by document frequency (default: drop any
   candidate that occurs in more than 20% of aligned blocks — this
   removes `taṃ`, `idaṃ`, `katamaṃ`, `rūpaṃ`-style pervasive items).
4. Filters English noise (translation artifacts, citations, fragments
   like `etc`, `iii`, `pali`, `davids`).
5. Aggregates: for each (lemma, english) pair, keeps the max Dice
   across inflected forms; sums co-occurrences.
6. Writes a markdown file with two sections:
   - **Compact form** (bb-glossary style: one line per lemma)
   - **Detailed entries** (per-lemma table with stats and forms seen)

Phase 1 caveats (improve in later phases):
- The case-ending stripper is rule-based, not a real lemmatizer.
- "Senses" here are just the top-N English renderings ranked by Dice.
  Genuine sense-splitting (Phase 3) requires block-level co-occurrence
  clustering.
- The Pāli vocabulary is still anchored on the 500 English keywords.
  Phase 2 will replace this with a Pāli-first keyword extractor.

Usage
-----
    python3 flip_to_pali_glossary.py \\
        --input keyword-pi-en-map.md \\
        --aligned-blocks 1780 \\
        --max-pi-df 0.20 \\
        --min-dice 0.10 \\
        --top-senses 5 \\
        --out pi-en-glossary
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Parsing the existing keyword-pi-en-map.md
# ---------------------------------------------------------------------------

# Matches a candidate token of the form: **pali** (0.37 · 135 · 48)
# Accepts both U+00B7 MIDDLE DOT and ASCII period as separator.
PI_CAND_RE = re.compile(
    r"\*\*([^*]+)\*\*\s*\(([\d.]+)\s*[·.]\s*(\d+)\s*[·.]\s*(\d+)\)"
)


# ---------------------------------------------------------------------------
# Rule-based Pāli case-ending stripper
# ---------------------------------------------------------------------------
# Order matters: longest endings first so that `-asmiṃ` is tried before `-aṃ`.
CASE_ENDINGS = [
    "asmiṃ", "amhi", "ānaṃ", "āya", "ehi", "esu", "āni",
    "assa", "ena",
    "aṃ", "ā", "o", "e",
]
# 3 chars is enough — words like `rūpaṃ` need to collapse to `rūpa`.
# Shorter stems (`taṃ`, `yaṃ`, `idaṃ`) fail the check naturally because
# their stem after stripping is 1–2 chars.
MIN_STEM = 3


# Explicit overrides: surface form (lowercased) -> canonical lemma.
# Covers words whose rule-based stripping produces the wrong result.
LEMMA_OVERRIDES = {
    # nibbāna: `nibbānaṃ` strips `ānaṃ` → `nibb` + `a` = `nibba` (wrong)
    "nibbānaṃ": "nibbāna",
    "nibbānassa": "nibbāna",
    "nibbānāya": "nibbāna",
    "nibbāne": "nibbāna",
    # sati: `satiṃ` has no matching ending in the table → passes through as `satiṃ`
    "satiṃ": "sati",
    "satiyā": "sati",
    "satiyaṃ": "sati",
    # paññā: `paññāya` strips `āya` → `pañña` (correct), but `paññā` strips `ā` → `pañña` (correct)
    # viññāṇa: `viññāṇaṃ` strips `aṃ` → `viññāṇ` (wrong, ends in consonant → `viññāṇa` — actually OK)
    # phassa: pure ASCII, may survive tokenizer; normalize explicitly
    "phassa": "phassa",
    "phassena": "phassa",
    "phassassa": "phassa",
    "phasse": "phassa",
    # kamma
    "kamma": "kamma",
    "kammassa": "kamma",
    "kammaṃ": "kamma",
    "kammena": "kamma",
    "kammāni": "kamma",
    # nāma
    "nāmassa": "nāma",
    "nāmaṃ": "nāma",
    # paññā
    "paññā": "paññā",
    "paññāya": "paññā",
    "paññāṃ": "paññā",
    "paññāssa": "paññā",
    # mettā
    "mettā": "mettā",
    "mettāya": "mettā",
    # karuṇā
    "karuṇā": "karuṇā",
    "karuṇāya": "karuṇā",
    # saddhā
    "saddhā": "saddhā",
    "saddhāya": "saddhā",
}


def normalize_pali(word: str) -> str:
    """Collapse inflected Pāli forms to a canonical lemma.

    Checks an explicit override table first, then falls back to a
    rule-based case-ending stripper.
    """
    w = word.lower().strip()
    if w in LEMMA_OVERRIDES:
        return LEMMA_OVERRIDES[w]
    for end in CASE_ENDINGS:
        if w.endswith(end) and len(w) - len(end) >= MIN_STEM:
            stem = w[: -len(end)]
            if stem and stem[-1] not in "aāiīuūeēoō":
                return stem + "a"
            return stem
    return w


# ---------------------------------------------------------------------------
# English noise filter (Phase 1 hand-list; later phases can replace with a
# real authority list)
# ---------------------------------------------------------------------------
NOISE_EN = {
    # citation / front-matter / footer artifacts from Rhys Davids edition
    "etc", "pali", "davids", "rhys", "rys", "litt", "iii", "vii", "viii",
    "samm", "http", "https", "noncommercial", "licence", "commons",
    "reprinted", "caroline", "compendium", "manual", "psychological",
    "buddhist", "ethics", "passim", "viz", "wit",
    # Pāli-fragment tokens that snuck into the English keyword list
    "ata", "appa", "atti", "bala", "ihita", "ipad", "passa", "adh",
    "yatana", "dhammasa", "sava", "savas", "sati", "citta", "indriya",
    "yojana", "gocchaka", "suddhika", "sapid", "sapids", "nas",
}


# ---------------------------------------------------------------------------
# Map parser
# ---------------------------------------------------------------------------

def parse_map(path: Path):
    """Yield (english, en_blocks, [(pali, dice, pi_blocks, co_occ), ...])."""
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            if not line.startswith("|") or "---" in line:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 3:
                continue
            try:
                en_blocks = int(cells[1])
            except ValueError:
                continue                                  # header row
            cands = [
                (m.group(1), float(m.group(2)),
                 int(m.group(3)), int(m.group(4)))
                for m in PI_CAND_RE.finditer(cells[2])
            ]
            rows.append((cells[0], en_blocks, cands))
    return rows


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="keyword-pi-en-map.md",
                    help="Output of map_keywords_to_pali.py")
    ap.add_argument("--out", default="pi-en-glossary",
                    help="Output basename (default 'pi-en-glossary')")
    ap.add_argument("--aligned-blocks", type=int, default=1780,
                    help="Total aligned blocks (header of input file)")
    ap.add_argument("--max-pi-df", type=float, default=0.20,
                    help="Drop Pāli candidates whose pi_blocks / aligned > this")
    ap.add_argument("--min-dice", type=float, default=0.10,
                    help="Drop English renderings below this Dice score")
    ap.add_argument("--top-senses", type=int, default=5,
                    help="Keep top N English renderings per Pāli lemma")
    args = ap.parse_args()

    rows = parse_map(Path(args.input))
    print(f"Read {len(rows)} en→pi rows", file=sys.stderr)

    df_cap = args.aligned_blocks * args.max_pi_df

    # lemma -> english -> [max_dice, sum_co_occ, max_pi_blocks]
    glossary = defaultdict(lambda: defaultdict(lambda: [0.0, 0, 0]))
    # lemma -> set of inflected forms seen in source
    forms = defaultdict(set)

    for en, _en_blocks, cands in rows:
        if en.lower() in NOISE_EN or len(en) < 3:
            continue
        for pi, dice, pi_blocks, co in cands:
            if pi_blocks > df_cap or dice < args.min_dice:
                continue
            lemma = normalize_pali(pi)
            forms[lemma].add(pi)
            entry = glossary[lemma][en]
            entry[0] = max(entry[0], dice)
            entry[1] += co
            entry[2] = max(entry[2], pi_blocks)

    sorted_lemmas = sorted(glossary.keys())

    out_path = Path(f"{args.out}.md")
    with out_path.open("w", encoding="utf-8") as f:
        f.write("# Pāli → English draft glossary\n\n")
        f.write(f"- Source: `{args.input}` (en→pi map, flipped)\n")
        f.write(f"- Normalization: rule-based case-ending stripping\n")
        f.write(f"- Aligned blocks: {args.aligned_blocks}\n")
        f.write(f"- Filters: Pāli DF ≤ {args.max_pi_df:.2f}, "
                f"Dice ≥ {args.min_dice}, top {args.top_senses} senses per lemma\n")
        f.write(f"- Total Pāli lemmas: {len(sorted_lemmas)}\n\n")
        f.write("> Status: draft. Every entry is statistically derived from "
                "block-level co-occurrence, not yet citation-backed. "
                "Sense numbering reflects Dice-rank, not real polysemy splits "
                "(see Phase 3).\n\n")
        f.write("---\n\n")

        # Section A: compact bb-glossary style
        f.write("## Compact form (bb-glossary style)\n\n")
        for lemma in sorted_lemmas:
            cands = sorted(glossary[lemma].items(),
                           key=lambda x: -x[1][0])[:args.top_senses]
            if not cands:
                continue
            senses = "; ".join(f"({i+1}) {en}"
                               for i, (en, _) in enumerate(cands))
            f.write(f"- **{lemma}**: {senses}\n")
        f.write("\n---\n\n")

        # Section B: detailed per-lemma tables
        f.write("## Detailed entries\n\n")
        for lemma in sorted_lemmas:
            cands = sorted(glossary[lemma].items(),
                           key=lambda x: -x[1][0])[:args.top_senses]
            if not cands:
                continue
            f.write(f"### {lemma}\n\n")
            seen = ", ".join(sorted(forms[lemma]))
            f.write(f"_Inflected forms seen: {seen}_\n\n")
            f.write("| # | english | dice | co-occ | pi blocks |\n")
            f.write("| ---: | --- | ---: | ---: | ---: |\n")
            for i, (en, stats) in enumerate(cands, 1):
                dice, co, blocks = stats
                f.write(f"| {i} | {en} | {dice:.2f} | {co} | {blocks} |\n")
            f.write("\n")

    print(f"Wrote: {out_path} ({len(sorted_lemmas)} Pāli lemmas)",
          file=sys.stderr)


if __name__ == "__main__":
    main()
