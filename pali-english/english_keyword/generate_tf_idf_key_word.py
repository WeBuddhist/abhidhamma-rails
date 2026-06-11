#!/usr/bin/env python3
"""
generate_tf_idf_key_word.py
===========================
Reads two markdown translation files, computes TF-IDF against the Reuters-21578
general-English IDF corpus (idf_corpus.py), and writes:

  output/<stem1>-keywords.md    -- ranked termbase for source 1
  output/<stem2>-keywords.md    -- ranked termbase for source 2
  output/singular_keywords.json -- all keywords in singular form
  output/plural_keywords.json   -- noun keywords in plural form

Usage
-----
    python3 generate_tf_idf_key_word.py

Dependencies
------------
    pip install scikit-learn nltk spacy inflect
    python -m spacy download en_core_web_sm
"""

import json
import re
import sys
import argparse
import pathlib
from datetime import date

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "output"))
from idf_corpus import IDF_CORPUS

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = SCRIPT_DIR.parent.parent
_DEFAULT_INPUTS = [
    REPO_ROOT / "1-SOURCES" / "Translations" / "en-1-rhys_davids.md",
    REPO_ROOT / "1-SOURCES" / "Translations" / "en-1-ukyaw_khine.md",
]
_DEFAULT_OUTPUT = SCRIPT_DIR / "output"

# ---------------------------------------------------------------------------
# IDF table
# ---------------------------------------------------------------------------
IDF: dict[str, float] = IDF_CORPUS
IDF_UNKNOWN: float = 9.59

# ---------------------------------------------------------------------------
# Stop-words
# ---------------------------------------------------------------------------
STOPWORDS = {
    "the","a","an","and","or","of","in","on","to","at","by","for","with",
    "that","this","these","those","is","are","was","were","be","been","being",
    "have","has","had","do","does","did","will","would","shall","should",
    "may","might","can","could","not","no","nor","so","yet","but","both",
    "either","neither","as","if","then","there","here","when","where","which",
    "who","whom","whose","what","how","it","its","he","she","they","we","you",
    "i","me","him","her","them","us","my","your","his","our","their",
    "from","into","up","out","about","after","before","between","through",
    "now","also","only","just","even","than","more","very","each","all","any",
    "some","such","other","same","own","new","first","last","long","great",
    "little","good","well","back","over","still","though","however","thus",
    "upon","per","own","one","two","three","four","five","six","seven","eight",
}

# ---------------------------------------------------------------------------
# Singular / Plural via spaCy + inflect
# ---------------------------------------------------------------------------

def _load_nlp():
    try:
        import spacy
        return spacy.load("en_core_web_sm")
    except Exception:
        return None


def _load_inflect():
    try:
        import inflect
        return inflect.engine()
    except Exception:
        return None


def split_singular_plural(words: list[str]) -> tuple[list[str], list[str]]:
    """
    For each word:
    - Non-noun (adverb, adjective, etc.): singular only, unchanged.
    - Noun: derive singular (lemma) -> singular_keywords, plural -> plural_keywords.
    - Hyphenated compound: treat last part as head noun. If noun, singularize/pluralize
      the head and keep prefix with space. If not noun, singular only.
    Returns (singular_words, plural_words).
    """
    nlp    = _load_nlp()
    engine = _load_inflect()
    if nlp is None:
        print("WARNING: spaCy not available, cannot produce singular/plural JSON.", file=sys.stderr)
        return [], []
    if engine is None:
        print("WARNING: inflect not available, cannot produce plural JSON.", file=sys.stderr)
        return [], []

    singular_set: set[str] = set()
    plural_set:   set[str] = set()

    for word in words:
        if "-" in word:
            parts  = word.lower().split("-")
            head   = parts[-1]
            prefix = " ".join(parts[:-1])
            doc    = nlp(head)
            token  = doc[0] if doc else None
            pos    = token.pos_ if token else "X"
            if pos in ("NOUN", "PROPN"):
                singular_head = token.lemma_.lower()
                plural_head   = engine.plural_noun(singular_head)
                singular_set.add(f"{prefix} {singular_head}")
                if plural_head:
                    plural_set.add(f"{prefix} {plural_head}")
            else:
                singular_set.add(word.replace("-", " "))
        else:
            doc   = nlp(word)
            token = doc[0] if doc else None
            pos   = token.pos_ if token else "X"
            if pos in ("NOUN", "PROPN"):
                singular = token.lemma_.lower()
                plural   = engine.plural_noun(singular)
                singular_set.add(singular)
                if plural:
                    plural_set.add(plural.lower())
            else:
                singular_set.add(word.lower())

    return sorted(singular_set), sorted(plural_set)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def tokenize(text: str) -> list[str]:
    text = strip_frontmatter(text)
    text = re.sub(r"\^[\w\-]+", " ", text)
    text = re.sub(r"[#\[\]`*_>|]", " ", text)
    text = re.sub(r"\d+", " ", text)
    tokens = re.findall(r"[a-zA-Z]+(?:[-][a-zA-Z]+)*", text)
    return [t.lower() for t in tokens]


def count_tf(path: pathlib.Path) -> dict[str, int]:
    raw = tokenize(path.read_text(encoding="utf-8"))
    counts: dict[str, int] = {}
    for w in raw:
        if w not in STOPWORDS and len(w) > 2:
            counts[w] = counts.get(w, 0) + 1
    return counts


def tfidf(word: str, count: int, total: int) -> float:
    tf  = count / total
    idf = IDF.get(word, IDF_UNKNOWN)
    return round(tf * idf * 1_000_000, 4)


def build_rows(tf: dict[str, int]) -> list[dict]:
    total = sum(tf.values())
    rows  = []
    for word, count in tf.items():
        score = tfidf(word, count, total)
        rows.append({"word": word, "count": count, "score": score,
                     "idf": IDF.get(word, IDF_UNKNOWN)})
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows


_BANDS = [
    (50_000, "extremely high -- text-exclusive"),
    (10_000, "very high -- domain-specific"),
    ( 3_000, "high -- specialist register"),
    (   500, "medium -- moderately distinctive"),
    (    50, "low -- common in general English"),
    (     0, "very low -- function / universal word"),
]

def band(score: float) -> str:
    for threshold, label in _BANDS:
        if score >= threshold:
            return label
    return "very low"


def render_md(rows: list[dict], source: pathlib.Path) -> str:
    today   = date.today().isoformat()
    total_w = sum(r["count"] for r in rows)
    n       = len(rows)
    stem    = source.stem

    band_counts: dict[str, int] = {}
    for r in rows:
        b = band(r["score"])
        band_counts[b] = band_counts.get(b, 0) + 1

    top    = rows[:50]
    bottom = rows[-50:]

    L: list[str] = []
    L += [
        "---",
        f"title: TF-IDF Vocabulary Analysis -- {stem}",
        f"source: {source}",
        "corpus: Reuters-21578 (10,788 newswire documents)",
        "method: TF x IDF x 10^6",
        f"generated: {today}",
        f"unique_terms: {n}",
        f"total_content_tokens: {total_w:,}",
        "status: draft",
        "---",
        "",
        f"# TF-IDF Vocabulary Analysis -- {stem}",
        "",
        f"Generated {today} | {n:,} unique content terms ranked.",
        "",
        "---",
        "",
        "## Distribution by Band",
        "",
        "| Band | Terms | % |",
        "|------|-------|---|",
    ]
    for threshold, label in _BANDS:
        c = band_counts.get(label, 0)
        pct = f"{100 * c / n:.1f}" if n else "0.0"
        L.append(f"| {label} | {c:,} | {pct}% |")
    L += ["", "---", ""]

    L += ["## Most Distinctive Words (top 50)", ""]
    for i, r in enumerate(top, 1):
        b = band(r["score"])
        line = "**" + str(i) + ". " + r["word"] + "**" + " -- count: " + str(r["count"]) + ", TF-IDF: " + f"{r['score']:,.0f}" + ", IDF: " + str(r["idf"]) + " [" + b + "]"
        L.append(line)
    L += ["", "---", ""]

    L += ["## Least Distinctive Words (bottom 50)", ""]
    for i, r in enumerate(reversed(bottom), 1):
        b = band(r["score"])
        line = "**" + str(i) + ". " + r["word"] + "**" + " -- count: " + str(r["count"]) + ", TF-IDF: " + f"{r['score']:,.2f}" + ", IDF: " + str(r["idf"]) + " [" + b + "]"
        L.append(line)
    L += ["", "---", ""]

    L += [
        "## Full Ranked Table",
        "",
        "All " + str(n) + " content terms, sorted by TF-IDF descending.",
        "",
        "| Rank | Word | Count | TF-IDF | IDF | Band |",
        "|------|------|-------|--------|-----|------|",
    ]
    for i, r in enumerate(rows, 1):
        b     = band(r["score"])
        score = f"{r['score']:,.2f}"
        L.append("| " + str(i) + " | **" + r["word"] + "** | " + str(r["count"]) + " | " + score + " | " + str(r["idf"]) + " | " + b + " |")

    L += ["", f"*Generated {today} by generate_tf_idf_key_word.py*"]
    return "\n".join(L)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Compute TF-IDF vocabulary analysis for two translation files.",
    )
    p.add_argument("--input", "-i", metavar="PATH", nargs="+", default=None,
                   help="Translation .md files (default: rhys_davids + ukyaw_khine).")
    p.add_argument("--output-dir", "-o", metavar="DIR", default=None,
                   help="Output directory (default: output/ next to this script).")
    return p.parse_args()


def main() -> None:
    args = _parse_args()

    sources = (
        [pathlib.Path(p).resolve() for p in args.input]
        if args.input else _DEFAULT_INPUTS
    )
    out_dir = pathlib.Path(args.output_dir).resolve() if args.output_dir else _DEFAULT_OUTPUT
    out_dir.mkdir(parents=True, exist_ok=True)

    all_keywords: set[str] = set()

    for en_source in sources:
        if not en_source.exists():
            raise FileNotFoundError(f"Translation not found:\n  {en_source}")

        output = out_dir / f"{en_source.stem}-keywords.md"
        print(f"Reading  {en_source.name} ...")
        tf = count_tf(en_source)
        print(f"  {len(tf):,} unique content tokens")

        rows = build_rows(tf)
        print(f"  {len(rows):,} terms scored")

        md = render_md(rows, en_source)
        output.write_text(md, encoding="utf-8")
        print(f"Written  -> {output}")

        # only include medium and above (score >= 500) in keyword JSONs
        all_keywords.update(r["word"] for r in rows if r["score"] >= 500)

    kw_list = sorted(all_keywords)
    singular, plural = split_singular_plural(kw_list)

    if singular:
        (out_dir / "singular_keywords.json").write_text(
            json.dumps({"words": singular}, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Written  -> singular_keywords.json  ({len(singular):,} words)")

    if plural:
        (out_dir / "plural_keywords.json").write_text(
            json.dumps({"words": plural}, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Written  -> plural_keywords.json  ({len(plural):,} words)")


if __name__ == "__main__":
    main()
