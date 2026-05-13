#!/usr/bin/env python3
"""
tipitaka_org_book.py — converter for tipitaka.org Mūla book exports.

Schema (observed):
  Top level:  id, title_pali, title_breadcrumb, collection, pitaka, layer,
              layer_type, fts_prefix, source_filename, total_segments,
              total_characters, full_text, segments
  Each segment: id, chapter, paragraph, span_start, span_end, content,
                css_class, original_path

  css_class values:
    centered    — homage line ("Namo tassa…")
    nikaya      — pitaka label ("Abhidhammapiṭake")
    book        — book title  ("Dhammasaṅgaṇīpāḷi")
    chapter     — chapter heading (one per chapter)
    title       — major sub-section heading
    subhead     — minor sub-section heading
    bodytext    — verse / prose body
    unindented  — verse body (continuation)

Output strategy:
  - All `centered` / `nikaya` / `book` segments BEFORE the first chapter
    css_class segment are pulled into a synthetic `## 0. Introduction ^0-0`
    block, numbered ^0-1, ^0-2, …
  - Each source chapter is emitted as `## N. {chapter title} ^N-0`, with
    source chapter numbers shifted by +1 to make room for chapter 0.
  - `title` and `subhead` become `### N.M {title} ^N-M-0` (section counter
    increments for either).
  - `bodytext` / `unindented` become verses with `^N-V` IDs, V restarting
    per chapter.
  - Leading "N. " in source titles is stripped (the source's own numbering
    is replaced by our chapter / section number).

CLI:
    python tipitaka_org_book.py source.json output.md
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

# Allow `python converters/tipitaka_org_book.py …` to import the template
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from json_to_source_text import (  # noqa: E402
    format_frontmatter,
    format_chapter_heading,
    format_subsection_heading,
    format_verse,
    clean_text,
)


_leading_num_re = re.compile(r"^\s*\d+\.\s*")


def strip_leading_number(title: str) -> str:
    """Source titles like '1. Cittuppādakaṇḍaṃ' carry their own numbering;
    we add our own chapter/section number, so strip the leading 'N. ' to
    avoid duplicates like '## 2. 1. Cittuppādakaṇḍaṃ'."""
    return _leading_num_re.sub("", title).strip()


# Roles
ROLE_CHAPTER = "chapter"
ROLE_SUBSECTION = "subsection"
ROLE_VERSE = "verse"
ROLE_PREFACE = "preface"

CATEGORY_TO_ROLE = {
    "centered":   ROLE_PREFACE,
    "nikaya":     ROLE_PREFACE,
    "book":       ROLE_PREFACE,
    "chapter":    ROLE_CHAPTER,
    "title":      ROLE_SUBSECTION,
    "subhead":    ROLE_SUBSECTION,
    "bodytext":   ROLE_VERSE,
    "unindented": ROLE_VERSE,
}


def extract_metadata(data: dict, source_path: Path) -> dict:
    title = data.get("title_pali") or data.get("title") or source_path.stem
    breadcrumb = data.get("title_breadcrumb")
    pitaka = data.get("pitaka")
    layer = data.get("layer")
    source_id = data.get("id")
    source_filename = data.get("source_filename")
    total_segments = data.get("total_segments")

    bits = []
    if breadcrumb:
        bits.append(breadcrumb)
    if total_segments:
        bits.append(f"{total_segments} segments in source")
    description = "Tipitaka.org Mūla edition export."
    if bits:
        description += " " + "; ".join(bits) + "."

    return {
        "title": title,
        "language": "Pali",
        "script": "Roman (PTS diacritics)",
        "file_type": "root-text",
        "lang_tag": "pi",
        "verse_id_format": "chapter-verse",
        "pitaka": pitaka,
        "layer": layer,
        "source_description": description,
        "source_filename": source_filename,
        "source_url": f"https://tipitaka.org/romn/cscd/{source_id}.mul.xml" if source_id else None,
        "other_ids": [f"tipitaka.org: {source_id}"] if source_id else None,
    }


def convert_json_to_source_text(json_path: str | Path, output_path: str | Path) -> None:
    json_path = Path(json_path)
    output_path = Path(output_path)

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    meta = extract_metadata(data, json_path)
    segments = data.get("segments", [])

    preface: list[str] = []
    chapters: dict[int, list[tuple[str, str]]] = {}

    saw_first_chapter = False
    for seg in segments:
        css = seg.get("css_class", "")
        role = CATEGORY_TO_ROLE.get(css, ROLE_VERSE)
        content = clean_text(seg.get("content", ""))
        if not content:
            continue
        src_ch = seg.get("chapter", 0)

        if role == ROLE_PREFACE and not saw_first_chapter:
            preface.append(content)
            continue
        if role == ROLE_CHAPTER:
            saw_first_chapter = True
        if role == ROLE_PREFACE:
            role = ROLE_VERSE
        chapters.setdefault(src_ch, []).append((role, content))

    output: list[str] = [format_frontmatter(meta), "\n"]

    if preface:
        output.append(format_chapter_heading(0, "Introduction"))
        output.append("\n")
        for i, content in enumerate(preface, start=1):
            output.append(format_verse(content, 0, i))
        output.append("\n")

    for src_ch in sorted(chapters.keys()):
        out_ch = src_ch + 1
        items = chapters[src_ch]

        chapter_title_raw = next((c for r, c in items if r == ROLE_CHAPTER), f"Chapter {out_ch}")
        chapter_title = strip_leading_number(chapter_title_raw)
        output.append(format_chapter_heading(out_ch, chapter_title))
        output.append("\n")

        section_counter = 0
        verse_counter = 0
        consumed_title = False

        for role, content in items:
            if role == ROLE_CHAPTER and not consumed_title:
                consumed_title = True
                continue
            if role == ROLE_CHAPTER:
                section_counter += 1
                output.append(format_subsection_heading(out_ch, section_counter, strip_leading_number(content)))
                output.append("\n")
                continue
            if role == ROLE_SUBSECTION:
                section_counter += 1
                output.append(format_subsection_heading(out_ch, section_counter, strip_leading_number(content)))
                output.append("\n")
                continue
            verse_counter += 1
            output.append(format_verse(content, out_ch, verse_counter))

        output.append("\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(output), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("output_path", type=Path)
    args = ap.parse_args()
    convert_json_to_source_text(args.json_path, args.output_path)
    print(f"Wrote {args.output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
