"""
generate_pali_meaning.py
-------------------------
Reads a pi-*.keyword.json file (output of pali_keyword_generate.py),
takes only the `pali_keyword` entries (ignores `non_pali_keyword`),
and looks up the English meaning(s) for each lemma from the DPD
database via PaliLookup.

Output JSON shape:

{
  "source": "...",
  "pali_keyword": [
    {
      "lemma": "dhamma",
      "variants": ["dhamma_variant_1", "dhamma_variant_2"],
      "meaning": ["meaning 1", "meaning 2"]
    }
  ]
}
"""

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"

_DEFAULT_INPUT = OUTPUT_DIR / "pi-1.keyword.json"

MAX_MEANINGS = 9

# DPD part-of-speech codes -> full, human-readable names.
POS_MAP = {
    "masc": "masculine noun",
    "fem": "feminine noun",
    "nt": "neuter noun",
    "masc fem": "masculine/feminine noun",
    "masc nt": "masculine/neuter noun",
    "adj": "adjective",
    "pron": "pronoun",
    "ind": "indeclinable",
    "prefix": "prefix",
    "suffix": "suffix",
    "card": "cardinal number",
    "ordin": "ordinal number",
    "perf": "perfect tense verb",
    "aor": "aorist verb",
    "pr": "present tense verb",
    "imperf": "imperfect tense verb",
    "ptp": "past participle",
    "pp": "past participle",
    "prp": "present participle",
    "fut p": "future participle",
    "abs": "absolutive",
    "inf": "infinitive",
    "cond": "conditional verb",
    "opt": "optative verb",
    "imp": "imperative verb",
    "fut": "future tense verb",
    "ger": "gerund",
    "cs": "causative verb",
    "denom": "denominative verb",
    "root": "verbal root",
    "idiom": "idiom",
    "sandhi": "sandhi",
    "abbrev": "abbreviation",
    "letter": "letter",
    "particle": "particle",
    "ve": "verb",
    "cmp": "compound",
    "comp": "compound",
}


def expand_pos(pos):
    """Map a DPD part-of-speech abbreviation to its full name (unchanged if unknown)."""
    key = pos.strip().lower()
    return POS_MAP.get(key, pos)


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Add English meanings to pali_keyword lemmas from a pi-*.keyword.json file."
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Path to pi-*.keyword.json (default: " + str(_DEFAULT_INPUT) + ")",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to output JSON (default: <input_stem>.meaning.json in output/)",
    )
    return parser.parse_args()


def load_meanings(lookup, lemma):
    """
    Fetch the meaning_1 string for each sense of a Pali lemma
    (e.g. "dhamma 1.01", "dhamma 1.02") in the DPD database,
    prefixed with the full part-of-speech name
    (e.g. "(masculine noun) nature; character"),
    keeping each sense's meaning together (semicolon-separated),
    deduped, and capped at MAX_MEANINGS.
    """
    entries = lookup.get_translations(lemma)

    meanings = []
    for entry in entries:
        meaning = entry.meaning_1.strip()
        if not meaning:
            continue

        pos = entry.pos.strip()
        if pos:
            formatted = "(" + expand_pos(pos) + ") " + meaning
        else:
            formatted = meaning

        if formatted not in meanings:
            meanings.append(formatted)
        if len(meanings) >= MAX_MEANINGS:
            break
    return meanings


def main():
    args = _parse_args()

    if args.input:
        src = Path(args.input).resolve()
    else:
        src = _DEFAULT_INPUT

    if not src.exists():
        raise FileNotFoundError("Input not found: " + str(src))

    if args.output:
        dest = Path(args.output).resolve()
    else:
        dest = OUTPUT_DIR / src.name.replace(".keyword.json", ".meaning.json")

    sys.path.insert(0, str(SCRIPT_DIR.parent))
    from db_query.connect_db import DBConnection
    from db_query.lookup import PaliLookup

    data = json.loads(src.read_text(encoding="utf-8"))
    pali_keyword = data.get("pali_keyword", [])

    lookup = PaliLookup()
    try:
        results = []
        for entry in pali_keyword:
            lemma = entry["lemma"]
            variants = entry.get("variants", [])
            meanings = load_meanings(lookup, lemma)
            results.append({
                "lemma": lemma,
                "variants": variants,
                "meaning": meanings,
            })
    finally:
        DBConnection.close()

    output = {
        "source": str(src),
        "pali_keyword": results,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    text = json.dumps(output, ensure_ascii=False, indent=2)
    dest.write_text(text + chr(10), encoding="utf-8")
    print("Wrote " + str(len(results)) + " pali_keyword entries with meanings -> " + str(dest))


if __name__ == "__main__":
    main()
