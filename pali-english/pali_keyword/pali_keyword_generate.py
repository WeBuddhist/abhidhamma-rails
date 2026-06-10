import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
EN_KEYWORD_DIR = SCRIPT_DIR.parent / "english_keyword" / "output"
OUTPUT_DIR = SCRIPT_DIR / "output"

UKYAW_KHINE_RAW_PATH = EN_KEYWORD_DIR / "en-1-ukyaw_khine-raw.json"
UKYAW_KHINE_NORMALIZED_PATH = EN_KEYWORD_DIR / "en-1-ukyaw_khine-normalized.json"
TERMBASE_PATH = EN_KEYWORD_DIR / "en-1-rhys_davids_vs_en-1-ukyaw_khine_termbase.json"

PALI_WORDS_PATH = OUTPUT_DIR / "pi-1.words.json"
KEYWORD_OUTPUT_PATH = OUTPUT_DIR / PALI_WORDS_PATH.name.replace(".words.json", ".keyword.json")

# Only phrases with more than 2 words (i.e. 3+ word n-grams) are taken from the
# English keyword dicts. Single-word meanings are instead checked against the
# combined termbase word list.
MIN_PHRASE_NGRAM = 3


def load_words(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["words"]


def load_phrase_keywords(*paths: Path) -> set[str]:
    """
    Load multi-word (>2 token / 3+ n-gram) keys from one or more
    {phrase: score} JSON dictionaries, lower-cased for matching.
    """
    phrases: set[str] = set()
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for phrase in data:
            if len(phrase.split()) >= MIN_PHRASE_NGRAM:
                phrases.add(phrase.strip().lower())
    return phrases


def load_single_words(path: Path) -> set[str]:
    """Load single English words from the combined termbase JSON ({"word": [...]})."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return {w.strip().lower() for w in data.get("word", [])}


def fetch_meanings(lookup, word: str) -> tuple[str, list[str]] | None:
    entries = lookup.get_translations(word)
    if not entries:
        return None

    lemma = entries[0].lemma_clean
    meanings: list[str] = []
    for entry in entries:
        for part in entry.meaning_1.split(";"):
            part = part.strip()
            if part:
                meanings.append(part)
    return lemma, meanings


def meaning_in_keywords(
    meaning: str,
    phrase_keywords: set[str],
    single_words: set[str],
) -> bool:
    cleaned = meaning.strip().lower()
    n = len(cleaned.split())
    if n == 1:
        return cleaned in single_words
    if n >= MIN_PHRASE_NGRAM:
        return cleaned in phrase_keywords
    # 2-word (bigram) meanings are neither phrase keywords nor single words —
    # not considered a match.
    return False


def is_technical_term(
    meanings: list[str],
    phrase_keywords: set[str],
    single_words: set[str],
) -> bool:
    return any(
        meaning_in_keywords(meaning, phrase_keywords, single_words)
        for meaning in meanings
    )


def build_keyword_entries(
    groups: dict[str, dict],
    *,
    is_technical: bool,
) -> list[dict]:
    entries = []
    for lemma, group in groups.items():
        if group["is_technical"] != is_technical:
            continue
        variants = sorted(
            group["variants"],
            key=lambda form: (-group["variants"][form], form),
        )
        entries.append({"lemma": lemma, "variants": variants})

    entries.sort(
        key=lambda entry: (
            -sum(groups[entry["lemma"]]["variants"][form] for form in entry["variants"]),
            entry["lemma"],
        )
    )
    return entries


def main() -> None:
    sys.path.insert(0, str(SCRIPT_DIR.parent))
    from db_query.connect_db import DBConnection
    from db_query.lookup import PaliLookup

    phrase_keywords = load_phrase_keywords(
        UKYAW_KHINE_RAW_PATH,
        UKYAW_KHINE_NORMALIZED_PATH,
    )
    single_words = load_single_words(TERMBASE_PATH)

    pali_words = load_words(PALI_WORDS_PATH)
    lookup = PaliLookup()
    try:
        groups: dict[str, dict] = {}

        for item in pali_words:
            word = item["word"]
            frequency = item.get("frequency", 0)
            result = fetch_meanings(lookup, word)
            if result is None:
                continue

            lemma, meanings = result

            if lemma not in groups:
                groups[lemma] = {
                    "variants": {},
                    "is_technical": is_technical_term(meanings, phrase_keywords, single_words),
                }

            groups[lemma]["variants"][word] = frequency

        pali_keyword = build_keyword_entries(groups, is_technical=True)
        non_pali_keyword = build_keyword_entries(groups, is_technical=False)

        output = {
            "source": str(PALI_WORDS_PATH),
            "pali_keyword": pali_keyword,
            "non_pali_keyword": non_pali_keyword,
        }
        KEYWORD_OUTPUT_PATH.write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(
            f"Wrote {len(pali_keyword)} pali keywords and "
            f"{len(non_pali_keyword)} non-pali keywords to {KEYWORD_OUTPUT_PATH}"
        )
    finally:
        DBConnection.close()


if __name__ == "__main__":
    main()
