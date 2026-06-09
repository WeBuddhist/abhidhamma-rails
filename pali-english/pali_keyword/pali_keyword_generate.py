import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
EN_KEYWORD_DIR = SCRIPT_DIR.parent / "english_keyword"

RHYS_DAVIDS_RAW_PATH = EN_KEYWORD_DIR / "en-1-rhys_davids-raw.json"
RHYS_DAVIDS_NORMALIZED_PATH = EN_KEYWORD_DIR / "en-1-rhys_davids-normalized.json"
UKYAW_KHINE_RAW_PATH = EN_KEYWORD_DIR / "en-1-ukyaw_khine-raw.json"
UKYAW_KHINE_NORMALIZED_PATH = EN_KEYWORD_DIR / "en-1-ukyaw_khine-normalized.json"
PALI_WORDS_PATH = SCRIPT_DIR / "pi-1.words.json"
KEYWORD_OUTPUT_PATH = SCRIPT_DIR / PALI_WORDS_PATH.name.replace(".words.json", ".keyword.json")


def load_map(path: Path) -> dict[str, float]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_words(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["words"]


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


def meaning_in_keywords(meaning: str, english_keyword_dicts: tuple[dict[str, float], ...]) -> bool:
    for d in english_keyword_dicts:
        if meaning in d:
            return True
    return False


def is_technical_term(meanings: list[str], english_keyword_dicts: tuple[dict[str, float], ...]) -> bool:
    return any(meaning_in_keywords(meaning, english_keyword_dicts) for meaning in meanings)


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

    rhys_davids_raw = load_map(RHYS_DAVIDS_RAW_PATH)
    rhys_davids_normalized = load_map(RHYS_DAVIDS_NORMALIZED_PATH)
    ukyaw_khine_raw = load_map(UKYAW_KHINE_RAW_PATH)
    ukyaw_khine_normalized = load_map(UKYAW_KHINE_NORMALIZED_PATH)

    english_keyword_dicts = (
        rhys_davids_raw,
        rhys_davids_normalized,
        ukyaw_khine_raw,
        ukyaw_khine_normalized,
    )

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
                    "is_technical": is_technical_term(meanings, english_keyword_dicts),
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
