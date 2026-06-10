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
      "variants": ["dhammā", "dhammānaṃ", ...],
      "meaning": ["meaning 1", "meaning 2", ...]
    },
    ...
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


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add English meanings to pali_keyword lemmas from a pi-*.keyword.json file."
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help=f"Path to pi-*.keyword.json (default: {_DEFAULT_INPUT})",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to output JSON (default: <input_stem>.meaning.json in output/)",
    )
    return parser.parse_args()


MAX_MEANINGS = 7


def load_meanings(lookup, lemma: str) -> list[str]:
    """
    Fetch the meaning_1 string for each sense of a Pali lemma
    (e.g. "dhamma 1.01", "dhamma 1.02", ...) in the DPD database,
    keeping each sense's meaning together (semicolon-separated),
    deduped, and capped at MAX_MEANINGS.
    """
    entries = lookup.get_translations(lemma)

    meanings: list[str] = []
    for entry in entries:
        meaning = entry.meaning_1.strip()
        if meaning and meaning not in meanings:
            meanings.append(meaning)
        if len(meanings) >= MAX_MEANINGS:
            break
    return meanings


def main() -> None:
    args = _parse_args()

    src = Path(args.input).resolve() if args.input else _DEFAULT_INPUT
    if not src.exists():
        raise FileNotFoundError(f"Input not found:\n  {src}")

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
    dest.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(results)} pali_keyword entries with meanings -> {dest}")


if __name__ == "__main__":
    main()
