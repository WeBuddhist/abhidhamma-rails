#!/usr/bin/env python3
"""
pali_keyword_md.py
------------------
Loads pali_keyword/output/pi-1.keyword.json, looks up meaning_1 for each
lemma from the DPD database, and writes a Markdown table to output/.

Output format:
| Common Surface Forms | Lemma | Meaning |
| -------------------- | ----- | ------- |
| dhammā, dhammaṃ, ... | dhamma | teaching; doctrine |
|                      |        | thing; phenomenon  |
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

KEYWORD_PATH = OUTPUT_DIR / "pi-1.keyword.json"
MD_OUTPUT_PATH = OUTPUT_DIR / "pi-1.keyword.md"


def load_keywords(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("pali_keyword", [])


def build_table(keywords: list[dict], lookup) -> list[str]:
    lines = [
        "| Common Surface Forms | Lemma | Meaning |",
        "| -------------------- | ----- | ------- |",
    ]

    for entry in keywords:
        lemma = entry["lemma"]
        variants = entry.get("variants", [])
        surface_forms = ", ".join(variants)

        entries = lookup.get_translations(lemma)
        meanings = [e.meaning_1 for e in entries if e.meaning_1]

        if not meanings:
            lines.append(f"| {surface_forms} | {lemma} |  |")
            continue

        # First row: surface forms + lemma + first meaning
        lines.append(f"| {surface_forms} | {lemma} | {meanings[0]} |")

        # Subsequent rows: empty surface forms + lemma, next meanings
        for meaning in meanings[1:]:
            lines.append(f"|  |  | {meaning} |")

    return lines


def main() -> None:
    sys.path.insert(0, str(SCRIPT_DIR.parent))
    from db_query.connect_db import DBConnection
    from db_query.lookup import PaliLookup

    if not KEYWORD_PATH.exists():
        raise FileNotFoundError(f"Not found: {KEYWORD_PATH}\nRun pali_keyword_generate.py first.")

    print(f"Loading {KEYWORD_PATH.name} ...")
    keywords = load_keywords(KEYWORD_PATH)
    print(f"  {len(keywords):,} pali keywords")

    lookup = PaliLookup()
    try:
        lines = build_table(keywords, lookup)
        MD_OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Written -> {MD_OUTPUT_PATH}  ({len(lines) - 2:,} rows)")
    finally:
        DBConnection.close()


if __name__ == "__main__":
    main()
