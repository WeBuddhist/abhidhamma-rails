#!/usr/bin/env python3
"""
extract_keywords.py
===================
Extract and rank English keywords from a SuttaCentral-style markdown
translation (e.g. en-1-rhys_davids.md, the Dhammasangani).

Two modes:

  default  TF-IDF using the NLTK Brown Corpus (500 documents of general
           American English across 15 genres) as the background corpus,
           with the user's file added as the 501st document. Each term's
           score is TF (in the user's file) * IDF (across all 501 docs),
           which promotes terms that are *frequent in the user's file but
           rare in general English* -- exactly the distinctive vocabulary
           of the source text (skandha, abides, sensuous, alobho, ...).

  --raw    Plain surface-form frequency count in the user's file. No
           lemmatization, no stopword removal, no IDF weighting.

Both modes share the same structural cleanup of the markdown source:
  - YAML front-matter, markdown headers, verse anchors (^1-21), section
    references (§ 7), bracket/paren marks are stripped.
  - Pali tokens (anything containing non-ASCII letters like a, m, n) are
    dropped, since the question is about English keywords.

Outputs:
  <out>.md    ranked keyword table (markdown)
  <out>.txt   plain keyword list, one per line

Usage:
  python3 extract_keywords.py INPUT.md --top 500 --out keywords
  python3 extract_keywords.py INPUT.md --top 500 --out keywords --raw
"""

import argparse
import re
import ssl
import sys
from collections import Counter
from pathlib import Path

import nltk
from nltk.corpus import brown
from sklearn.feature_extraction.text import TfidfVectorizer

WORD_RE = re.compile(r"[A-Za-z]+")
NLTK_DATA_DIR = Path(__file__).resolve().parent / ".venv" / "nltk_data"


def _ensure_nltk_ssl():
    """Use certifi CA bundle when the system store is missing (common on macOS)."""
    try:
        import certifi
    except ImportError:
        return
    ssl._create_default_https_context = lambda: ssl.create_default_context(
        cafile=certifi.where()
    )


def ensure_nltk_data(*packages):
    """Download NLTK corpora into the project venv; exit if download fails."""
    NLTK_DATA_DIR.mkdir(parents=True, exist_ok=True)
    nltk.data.path.insert(0, str(NLTK_DATA_DIR))
    _ensure_nltk_ssl()
    missing = []
    for pkg in packages:
        try:
            nltk.data.find(f"corpora/{pkg}" if pkg == "brown" else f"tokenizers/{pkg}")
        except LookupError:
            missing.append(pkg)
    if not missing:
        return
    print(f"Downloading NLTK data: {', '.join(missing)}...", file=sys.stderr)
    for pkg in missing:
        ok = nltk.download(pkg, download_dir=str(NLTK_DATA_DIR), quiet=False)
        if not ok:
            print(
                f"\nError: could not download NLTK package '{pkg}'.\n"
                "Fix SSL certificates (macOS Python): run\n"
                "  /Applications/Python 3.*/Install Certificates.command\n"
                "Or install certifi and retry:\n"
                "  pip install certifi\n"
                "For TF-IDF mode you need 'brown'. Use --raw to skip it.\n",
                file=sys.stderr,
            )
            sys.exit(1)


# --------------------------------------------------------------------------
# Markdown cleanup
# --------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
HEADER_LINE_RE = re.compile(r"^#{1,6}\s.*$", re.MULTILINE)   # Pali section titles
ANCHOR_RE      = re.compile(r"\^[\w][\w-]*")                  # ^1-21, ^abhidhamma-0
SECTION_REF_RE = re.compile(r"§\s*\d*")                       # § 7 , §
BRACKETS_RE    = re.compile(r"[\[\]\(\)]")                    # keep inner text, drop marks


def clean_markdown(text: str) -> str:
    """Strip non-English-prose markup; leave readable English sentences."""
    text = FRONTMATTER_RE.sub("", text)
    text = (text.replace("\u201c", '"').replace("\u201d", '"')
                .replace("\u2018", "'").replace("\u2019", "'")
                .replace("\u2014", " ").replace("\u2013", " "))
    text = HEADER_LINE_RE.sub("", text)
    text = ANCHOR_RE.sub(" ", text)
    text = SECTION_REF_RE.sub(" ", text)
    text = BRACKETS_RE.sub(" ", text)
    return text


def english_words_only(text: str) -> str:
    """Drop tokens with non-ASCII letters (Pali) and non-alphabetic tokens.
    Returns a space-joined string of surviving lowercase tokens, ready to
    feed into TfidfVectorizer or a Counter."""
    kept = []
    for tok in WORD_RE.findall(text):
        try:
            tok.encode("ascii")
        except UnicodeEncodeError:
            continue                                # Pali / diacritic token
        kept.append(tok.lower())
    return " ".join(kept)


# --------------------------------------------------------------------------
# Mode 1: TF-IDF against Brown corpus
# --------------------------------------------------------------------------

def extract_tfidf(user_text: str, top_n: int):
    """Rank keywords in user_text by TF-IDF where the IDF is computed over
    the Brown Corpus + the user's document."""
    user_doc = english_words_only(clean_markdown(user_text))

    # Build the background corpus: one string per Brown fileid.
    print(f"Loading Brown Corpus ({len(brown.fileids())} documents)...")
    background = [" ".join(w.lower() for w in brown.words(fid) if w.isalpha())
                  for fid in brown.fileids()]

    corpus = background + [user_doc]
    user_idx = len(corpus) - 1

    # Sublinear TF (1 + log tf) dampens the effect of very common words and
    # is the standard sklearn recommendation; smooth_idf avoids div-by-zero.
    print(f"Fitting TF-IDF over {len(corpus)} documents...")
    vec = TfidfVectorizer(
        token_pattern=r"(?u)\b[a-z]{3,}\b",   # alphabetic, length >= 3
        sublinear_tf=True,
        smooth_idf=True,
        norm="l2",
    )
    matrix = vec.fit_transform(corpus)
    vocab = vec.get_feature_names_out()

    user_row = matrix[user_idx].toarray().ravel()
    # Raw term frequencies in the user's document, for the output column.
    raw_counts = Counter(user_doc.split())

    # (term, tfidf, raw_tf), restricted to terms that actually appear in
    # the user's document (tfidf > 0).
    scored = [(vocab[i], float(user_row[i]), raw_counts.get(vocab[i], 0))
              for i in range(len(vocab)) if user_row[i] > 0]
    scored.sort(key=lambda x: -x[1])

    return scored[:top_n], len(scored)


# --------------------------------------------------------------------------
# Mode 2: raw surface-form frequency
# --------------------------------------------------------------------------

def extract_raw(user_text: str, top_n: int):
    cleaned = english_words_only(clean_markdown(user_text))
    counts = Counter(cleaned.split())
    most = counts.most_common(top_n)
    return most, len(counts)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Rank English keywords from a markdown translation.")
    ap.add_argument("input", help="Path to the .md translation file")
    ap.add_argument("--top", type=int, default=500, help="Number of keywords to keep (default 500)")
    ap.add_argument("--out", default="keywords", help="Output basename (default 'keywords')")
    ap.add_argument("--raw", action="store_true",
                    help="Use plain surface-form frequency instead of TF-IDF")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        raw_text = f.read()

    if not args.raw:
        ensure_nltk_data("brown")

    if args.raw:
        rows, total_unique = extract_raw(raw_text, args.top)
        mode = "raw frequency"
    else:
        rows, total_unique = extract_tfidf(raw_text, args.top)
        mode = "TF-IDF (Brown Corpus + user file)"

    # markdown table
    md_path = f"{args.out}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Keywords — {args.input}\n\n")
        f.write(f"Mode: {mode}  \n")
        f.write(f"Top {len(rows)} of {total_unique} unique terms\n\n")
        if args.raw:
            f.write("| rank | keyword | frequency |\n")
            f.write("| ---: | --- | ---: |\n")
            for i, (kw, freq) in enumerate(rows, 1):
                f.write(f"| {i} | {kw} | {freq} |\n")
        else:
            f.write("| rank | keyword | tfidf | frequency |\n")
            f.write("| ---: | --- | ---: | ---: |\n")
            for i, (kw, score, freq) in enumerate(rows, 1):
                f.write(f"| {i} | {kw} | {score:.4f} | {freq} |\n")

    # plain text
    txt_path = f"{args.out}.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(row[0] + "\n")

    # report
    print()
    print(f"Mode                          : {mode}")
    print(f"Unique terms in user document : {total_unique}")
    print(f"Keywords written (top {args.top})    : {len(rows)}")
    print()
    print(f"  {md_path}")
    print(f"  {txt_path}")
    print()
    print("Top 30:")
    if args.raw:
        print(f"  {'rank':>4}  {'keyword':<18}{'freq':>6}")
        for i, (kw, freq) in enumerate(rows[:30], 1):
            print(f"  {i:>4}  {kw:<18}{freq:>6}")
    else:
        print(f"  {'rank':>4}  {'keyword':<18}{'tfidf':>8}  {'freq':>6}")
        for i, (kw, score, freq) in enumerate(rows[:30], 1):
            print(f"  {i:>4}  {kw:<18}{score:>8.4f}  {freq:>6}")


if __name__ == "__main__":
    main()