#!/usr/bin/env python3
"""Identify Pāli tokens in a root text using a block-aligned English translation.

Pairs ``1-SOURCES/Text/pi-1.md`` (or any root) with
``1-SOURCES/Translations/en-1-rhys_davids.md`` (or any translation) via shared
Obsidian block IDs (``^1-0a-1``, etc.), tokenises each Pāli block, and maps
tokens to English renderings using:

1. **gloss** (best) — an interlinear gloss file (``\\gla`` / ``\\glb`` pairs).
2. **heuristic** — (Ka)/(Kha)/(Ga) clause split aligned to English ``;`` clauses.
3. **tokens-only** — Pāli tokens listed with no English match (long blocks).

Usage:

    # Full token mapping table (CSV)
    python3 identify_pali_from_translation.py \\
        1-SOURCES/Text/pi-1.md \\
        1-SOURCES/Translations/en-1-rhys_davids.md \\
        0-INBOX/temp/pi-en-rd-token-map.csv

    # Same + Markdown table
    python3 identify_pali_from_translation.py \\
        1-SOURCES/Text/pi-1.md \\
        1-SOURCES/Translations/en-1-rhys_davids.md \\
        0-INBOX/temp/pi-en-rd-token-map.csv \\
        --markdown 0-INBOX/temp/pi-en-rd-token-map.md

    # Use existing interlinear gloss for accurate pairs
    python3 identify_pali_from_translation.py \\
        1-SOURCES/Text/pi-1.md \\
        1-SOURCES/Translations/en-1-rhys_davids.md \\
        0-INBOX/temp/pi-en-rd-token-map.csv \\
        --gloss 2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md

    # Inspect one block
    python3 identify_pali_from_translation.py \\
        1-SOURCES/Text/pi-1.md \\
        1-SOURCES/Translations/en-1-rhys_davids.md \\
        /dev/stdout \\
        --block-id 1-0a-1

    # Look up Pāli lemma across all blocks (from last generated map or gloss)
    python3 identify_pali_from_translation.py \\
        1-SOURCES/Text/pi-1.md \\
        1-SOURCES/Translations/en-1-rhys_davids.md \\
        0-INBOX/temp/pi-en-rd-token-map.csv \\
        --lookup-pali kusala
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Reuse block parsing from align_blocks (same directory).
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from align_blocks import parse_blocks, _sort_key  # noqa: E402

BLOCK_HEADING_RE = re.compile(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", re.MULTILINE)
GLOSS_BLOCK_RE = re.compile(r"```gloss\s*\n(.*?)```", re.DOTALL)
KA_KHA_GA_RE = re.compile(r"\((Ka|Kha|Ga)\)\s*")

TRAILING_PUNCT = ".,;:!?"
LEADING_PUNCT = "([{"

# English boilerplate stripped before clause splitting (mātikā-style lists).
EN_PREFIXES = (
    r"States that are ",
    r"States, the ",
    r"States ",
    r"Which are the states that are ",
    r"Which on that occasion is ",
    r"What on that occasion is ",
)


def tokenise_pali(text: str) -> list[str]:
    """Split Pāli block text into tokens; strip editorial brackets and numbers."""
    cleaned = re.sub(r"\[[^\]]*\]", "", text)
    cleaned = re.sub(r"\([^)]*\)", "", cleaned)
    cleaned = re.sub(r"^\s*\d+\.\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"…pe…", " ", cleaned)
    tokens: list[str] = []
    for raw in cleaned.split():
        token = raw.strip(TRAILING_PUNCT + LEADING_PUNCT + "—–\"'")
        if not token or re.fullmatch(r"\d+", token):
            continue
        tokens.append(token)
    return tokens


def normalise_english(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_pali_clauses(text: str) -> list[str]:
    """Split (Ka)/(Kha)/(Ga) matrix lines into clause bodies."""
    text = re.sub(r"^\s*\d+\.\s*", "", text.strip())
    if not KA_KHA_GA_RE.search(text):
        return [text] if text else []

    clauses: list[str] = []
    parts = KA_KHA_GA_RE.split(text)
    i = 1
    while i < len(parts):
        body = parts[i + 1] if i + 1 < len(parts) else ""
        body = body.strip().rstrip(".")
        if body:
            clauses.append(body)
        i += 2
    return clauses


def split_english_clauses(text: str) -> list[str]:
    """Split Rhys Davids list translations on ';' after removing common prefixes."""
    text = normalise_english(text)
    for prefix in EN_PREFIXES:
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix) :].rstrip(".")
            break
    if ";" in text:
        return [c.strip().rstrip(".") for c in text.split(";") if c.strip()]
    return [text] if text else []


def tokenise_english_clause(clause: str) -> list[str]:
    """Rough content-word tokens from an English clause (for positional align)."""
    clause = clause.lower()
    clause = re.sub(r"[^\w\s\-]", " ", clause)
    stop = {
        "that", "are", "is", "the", "a", "an", "of", "to", "by", "and", "or",
        "not", "so", "as", "their", "have", "has", "been", "which", "on", "in",
        "for", "with", "from", "at", "one", "who", "be", "do", "does", "both",
        "neither", "nor", "but", "other", "whatever", "there", "then", "when",
    }
    out: list[str] = []
    for w in clause.split():
        w = w.strip("-_")
        if not w or w in stop:
            continue
        out.append(w.replace("-", "_"))
    return out


def load_gloss_pairs(gloss_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Return {block_id: [(pali_token, english_gloss), ...]}."""
    text = gloss_path.read_text(encoding="utf-8")
    out: dict[str, list[tuple[str, str]]] = {}
    parts = re.split(BLOCK_HEADING_RE, text)
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        m = GLOSS_BLOCK_RE.search(section)
        if not m:
            continue
        body = m.group(1)
        gla = _gloss_line(body, "gla")
        glb = _gloss_line(body, "glb")
        pairs: list[tuple[str, str]] = []
        for j, src in enumerate(gla):
            rend = glb[j] if j < len(glb) else "--"
            if rend and rend != "--":
                pairs.append((src, rend))
        if pairs:
            out[block_id] = pairs
    return out


def _gloss_line(body: str, marker: str) -> list[str]:
    m = re.search(rf"^\\{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not m:
        m = re.search(rf"^{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not m:
        return []
    return m.group(1).split()


def heuristic_pairs(
    pali_text: str, english_text: str
) -> list[tuple[str, str, int, str]]:
    """Return [(pali, english, clause_index, method)]."""
    pali_clauses = split_pali_clauses(pali_text)
    en_clauses = split_english_clauses(english_text)

    rows: list[tuple[str, str, int, str]] = []
    if len(pali_clauses) == len(en_clauses) and len(pali_clauses) > 1:
        for ci, (pc, ec) in enumerate(zip(pali_clauses, en_clauses)):
            ptoks = tokenise_pali(pc)
            etoks = tokenise_english_clause(ec)
            rows.extend(_zip_align(ptoks, etoks, ci, "heuristic_clause"))
        return rows

    # Whole-block positional align when clause counts differ.
    ptoks = tokenise_pali(pali_text)
    etoks = tokenise_english_clause(normalise_english(english_text))
    if ptoks and etoks:
        rows.extend(_zip_align(ptoks, etoks, 0, "heuristic_block"))
    elif ptoks:
        for t in ptoks:
            rows.append((t, "", 0, "pali_only"))
    return rows


def _zip_align(
    ptoks: list[str], etoks: list[str], clause_index: int, method: str
) -> list[tuple[str, str, int, str]]:
    rows: list[tuple[str, str, int, str]] = []
    n = max(len(ptoks), len(etoks))
    for i in range(n):
        p = ptoks[i] if i < len(ptoks) else ""
        e = etoks[i] if i < len(etoks) else ""
        if not p:
            continue
        m = method if e else "pali_only"
        rows.append((p, e, clause_index, m))
    return rows


def build_mappings(
    source_path: Path,
    target_path: Path,
    gloss_path: Path | None,
) -> list[dict[str, str]]:
    source_blocks = parse_blocks(source_path)
    target_blocks = parse_blocks(target_path)
    gloss = load_gloss_pairs(gloss_path) if gloss_path and gloss_path.exists() else {}

    all_ids = sorted(set(source_blocks) & set(target_blocks), key=_sort_key)
    rows: list[dict[str, str]] = []

    for block_id in all_ids:
        pali_text = source_blocks[block_id]
        english_text = target_blocks[block_id]

        if block_id in gloss:
            for pali, english in gloss[block_id]:
                rows.append({
                    "block_id": block_id,
                    "pali_token": pali,
                    "english_rendering": english,
                    "clause_index": "0",
                    "method": "gloss",
                    "source_snippet": _snippet(pali_text),
                    "english_snippet": _snippet(english_text),
                })
            continue

        for pali, english, ci, method in heuristic_pairs(pali_text, english_text):
            rows.append({
                "block_id": block_id,
                "pali_token": pali,
                "english_rendering": english,
                "clause_index": str(ci),
                "method": method,
                "source_snippet": _snippet(pali_text),
                "english_snippet": _snippet(english_text),
            })

    return rows


def _snippet(text: str, max_len: int = 120) -> str:
    s = normalise_english(text.replace("\n", " "))
    return s if len(s) <= max_len else s[: max_len - 3] + "..."


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "block_id",
        "pali_token",
        "english_rendering",
        "clause_index",
        "method",
        "source_snippet",
        "english_snippet",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write("# Pāli token map (from translation alignment)\n\n")
        fh.write(f"Total rows: {len(rows)}\n\n")
        fh.write(
            "| block_id | pali_token | english_rendering | method | clause |\n"
        )
        fh.write("|----------|------------|-------------------|--------|--------|\n")
        for r in rows:
            fh.write(
                f"| ^{r['block_id']} | {r['pali_token']} | "
                f"{r['english_rendering']} | {r['method']} | {r['clause_index']} |\n"
            )


def print_block(rows: list[dict[str, str]], block_id: str) -> None:
    block_rows = [r for r in rows if r["block_id"] == block_id]
    if not block_rows:
        print(f"No mapping for block ^{block_id}", file=sys.stderr)
        return
    print(f"## ^{block_id}\n")
    print(f"English: {block_rows[0]['english_snippet']}\n")
    print(f"Pāli:    {block_rows[0]['source_snippet']}\n")
    print("| pali_token | english_rendering | method |")
    print("|------------|-------------------|--------|")
    for r in block_rows:
        print(
            f"| {r['pali_token']} | {r['english_rendering']} | {r['method']} |"
        )


def lookup_pali(rows: list[dict[str, str]], query: str) -> None:
    q = query.lower()
    hits = [
        r for r in rows
        if q in r["pali_token"].lower() or q == r["pali_token"].lower()
    ]
    if not hits:
        print(f"No hits for Pāli query: {query}")
        return
    print(f"Hits for '{query}': {len(hits)}\n")
    seen: set[tuple[str, str, str]] = set()
    for r in hits:
        key = (r["pali_token"], r["english_rendering"], r["method"])
        if key in seen:
            continue
        seen.add(key)
        print(
            f"  ^{r['block_id']}: {r['pali_token']} → {r['english_rendering'] or '—'} "
            f"({r['method']})"
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source", type=Path, help="Root text markdown (e.g. pi-1.md)")
    parser.add_argument(
        "translation",
        type=Path,
        help="Translation markdown (e.g. en-1-rhys_davids.md)",
    )
    parser.add_argument("output", type=Path, help="Output CSV path (use /dev/stdout)")
    parser.add_argument(
        "--gloss",
        type=Path,
        default=None,
        help="Interlinear gloss file for accurate \\gla/\\glb pairs",
    )
    parser.add_argument(
        "--markdown",
        type=Path,
        default=None,
        help="Also write a Markdown table to this path",
    )
    parser.add_argument(
        "--block-id",
        type=str,
        default=None,
        help="Print mapping for one block only (e.g. 1-0a-1)",
    )
    parser.add_argument(
        "--lookup-pali",
        type=str,
        default=None,
        help="Search accumulated map for a Pāli substring/lemma",
    )
    args = parser.parse_args()

    if not args.source.exists():
        print(f"Source not found: {args.source}", file=sys.stderr)
        return 1
    if not args.translation.exists():
        print(f"Translation not found: {args.translation}", file=sys.stderr)
        return 1

    rows = build_mappings(args.source, args.translation, args.gloss)

    if args.block_id:
        print_block(rows, args.block_id)
        return 0

    if args.lookup_pali:
        lookup_pali(rows, args.lookup_pali)
        return 0

    write_csv(rows, args.output)
    if args.markdown:
        write_markdown(rows, args.markdown)

    methods = {}
    for r in rows:
        methods[r["method"]] = methods.get(r["method"], 0) + 1

    print(f"Wrote {args.output}: rows={len(rows)}")
    for m, n in sorted(methods.items()):
        print(f"  {m}: {n}")
    if args.markdown:
        print(f"Wrote {args.markdown}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
