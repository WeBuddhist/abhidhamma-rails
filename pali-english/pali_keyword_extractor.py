#!/usr/bin/env python3
"""
Extract case-insensitive distinct keywords and frequencies from Pali text.
Only merges words that differ by letter case (e.g. dhamma + Dhamma).
"""

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


WORD_PATTERN = re.compile(
    r"""
    (?<![\w\u0100-\u024F])
    [\w\u0100-\u024F]+
    (?![\w\u0100-\u024F])
    """,
    re.UNICODE | re.VERBOSE,
)

STRIP_CHARS = ".,;:!?\"'()[]{}«»—–-…।॥"

SCRIPT_DIR = Path(__file__).resolve().parent

# Set to a file path to run without a CLI argument; leave empty to pass input on the command line.
SOURCE = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Text\pi-1.md"


def normalize_token(token: str) -> str:
    return unicodedata.normalize("NFC", token.strip(STRIP_CHARS))


def merge_key(word: str) -> str:
    """Case-insensitive key only — diacritics are preserved."""
    return unicodedata.normalize("NFC", word).casefold()


def extract_keywords(text: str, *, min_length: int = 1) -> list[dict]:
    totals: dict[str, int] = defaultdict(int)
    forms: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for match in WORD_PATTERN.finditer(text):
        word = normalize_token(match.group(0))
        if len(word) < min_length:
            continue

        key = merge_key(word)
        totals[key] += 1
        forms[key][word] += 1

    results = []
    for key, frequency in totals.items():
        canonical = max(forms[key].items(), key=lambda x: (x[1], x[0]))[0]
        results.append({"word": canonical, "frequency": frequency})

    results.sort(key=lambda x: (-x["frequency"], merge_key(x["word"])))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Case-insensitive keyword frequencies from Pali text."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        help="Source text file (UTF-8); omitted when SOURCE is set in the script",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output JSON (default: <script-dir>/<input-stem>.keywords.json)",
    )
    parser.add_argument("--min-length", type=int, default=1)
    args = parser.parse_args()

    if SOURCE:
        input_path = Path(SOURCE)
    elif args.input:
        input_path = args.input
    else:
        parser.error("no input file: set SOURCE in the script or pass a path on the command line")

    text = input_path.read_text(encoding="utf-8")
    keywords = extract_keywords(text, min_length=args.min_length)

    out = args.output or (SCRIPT_DIR / f"{input_path.stem}.keywords.json")
    payload = {
        "source": str(input_path),
        "distinct_count": len(keywords),
        "total_tokens": sum(k["frequency"] for k in keywords),
        "keywords": keywords,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(keywords)} keywords to {out}")


if __name__ == "__main__":
    main()
