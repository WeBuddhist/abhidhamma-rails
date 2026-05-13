#!/usr/bin/env python3
"""
tipitaka_org_book.py — converter for tipitaka.org Mūla book exports.

Schema (observed):
  Top level:  id, title_pali, title_breadcrumb, collection, pitaka, layer,
              layer_type, fts_prefix, source_filename, total_segments,
              total_characters, full_text, segments
  Each segment: id, chapter, paragraph, span_start, span_end, content,
                css_class, original_path

  css_class values and their structural roles:
    centered    — homage line ("Namo tassa…")             → preface
    nikaya      — pitaka label ("Abhidhammapiṭake")       → preface
    book        — book title  ("Dhammasaṅgaṇīpāḷi")       → preface
    chapter     — chapter heading (one per source chapter)  → ##  ^N-0
    title       — major sub-section (e.g. "Dukamātikā")     → ###  ^N-M-0
    subhead     — minor sub-section. CONTEXT-DEPENDENT:
                    • if seen before any `title` in this chapter,
                      it's a sibling of `title`   → ### ^N-M-0
                    • if seen after a `title`, it's a child of that title
                      and emits as            → #### ^N-M-K-0
    bodytext    — verse / prose body                      → verse ^N-V
    unindented  — verse body (continuation)               → verse ^N-V

Output strategy:
  - Opening run of `centered`/`nikaya`/`book` segments → synthetic
    `## 0. Introduction ^0-0` with verses `^0-1`, `^0-2`, …
  - Source chapter N → `## (N+1). {chapter_title} ^(N+1)-0`
  - Per chapter, maintain a section counter (incremented for each `title`
    or for each `subhead` seen BEFORE the first title) and a subsection
    counter (incremented for each `subhead` AFTER a title, reset whenever
    a new title is seen).
  - Verses get `^chapter-V` with V restarting at 1 per chapter, regardless
    of any nesting under titles or subheads (per source-formatting.md:
    "sub-sections do not affect verse IDs").
  - Leading "N. " in source titles is stripped (our own numbering replaces it).

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
    format_subsubsection_heading,
    format_verse,
    clean_text,
)


_leading_num_re = re.compile(r"^\s*\d+\.\s*")


def strip_leading_number(title: str) -> str:
    """Strip leading 'N. ' from source titles to avoid double-numbering
    (the source's '1. Cittuppādakaṇḍaṃ' becomes our '## 2. Cittuppādakaṇḍaṃ')."""
    return _leading_num_re.sub("", title).strip()


# Roles
ROLE_CHAPTER = "chapter"
ROLE_TITLE = "title"
ROLE_SUBHEAD = "subhead"
ROLE_VERSE = "verse"
ROLE_PREFACE = "preface"

CATEGORY_TO_ROLE = {
    "centered":   ROLE_PREFACE,
    "nikaya":     ROLE_PREFACE,
    "book":       ROLE_PREFACE,
    "chapter":    ROLE_CHAPTER,
    "title":      ROLE_TITLE,
    "subhead":    ROLE_SUBHEAD,
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
        "verse_id_format": "hierarchical-path",
        "pitaka": pitaka,
        "layer": layer,
        "source_description": description,
        "source_filename": source_filename,
        "source_url": f"https://tipitaka.org/romn/cscd/{source_id}.mul.xml" if source_id else None,
        "other_ids": [f"tipitaka.org: {source_id}"] if source_id else None,
    }


def convert_json_to_source_text(json_path, output_path) -> None:
    """Convert one tipitaka.org JSON file to a source-text Markdown.

    - Source chapter numbers are preserved (no shift). The source's chapter 0
      (Mātikā) becomes our chapter 0 — i.e. the Introduction / TOC chapter
      of the book. Verses from the opening homage/title preface are folded
      into chapter 0 as its first verses.
    - Verse IDs carry the full heading path: ^0-1 for verses directly under
      `## 0`, ^0-1-V for verses under `### 0.1`, ^0-2-1-V for verses under
      `#### 0.2.1`. Verse counters restart at 1 every time a new heading
      changes the path.
    """
    json_path = Path(json_path)
    output_path = Path(output_path)

    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    meta = extract_metadata(data, json_path)
    segments = data.get("segments", [])

    # Phase 1: bucket segments by source chapter; pull opening preface separately.
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

    # Phase 2: emit Markdown.
    output: list[str] = [format_frontmatter(meta), "\n"]

    for src_ch in sorted(chapters.keys()):
        out_ch = src_ch  # preserve source chapter numbering — Mātikā stays as chapter 0
        items = chapters[src_ch]

        chapter_title_raw = next(
            (c for r, c in items if r == ROLE_CHAPTER),
            f"Chapter {out_ch}",
        )
        chapter_title = strip_leading_number(chapter_title_raw)
        output.append(format_chapter_heading(out_ch, chapter_title))
        output.append("\n")

        # Heading-path state for this chapter
        current_path = str(out_ch)
        verse_counter = 0
        section_counter = 0
        subsection_counter = 0
        seen_title = False
        consumed_chapter_title = False

        # For chapter 0, the book's opening preface (homage, pitaka label, book
        # title) is emitted as the first verses of the chapter, directly under
        # ## 0, before any sub-section heading.
        if src_ch == 0 and preface:
            for content in preface:
                verse_counter += 1
                output.append(format_verse(content, current_path, verse_counter))

        for role, content in items:
            if role == ROLE_CHAPTER and not consumed_chapter_title:
                consumed_chapter_title = True
                continue
            if role == ROLE_CHAPTER:
                # Extra chapter-class element inside a source chapter — treat as ###
                section_counter += 1
                subsection_counter = 0
                seen_title = False
                current_path = f"{out_ch}-{section_counter}"
                verse_counter = 0
                output.append(format_subsection_heading(
                    out_ch, section_counter, strip_leading_number(content)))
                output.append("\n")
                continue
            if role == ROLE_TITLE:
                section_counter += 1
                subsection_counter = 0
                seen_title = True
                current_path = f"{out_ch}-{section_counter}"
                verse_counter = 0
                output.append(format_subsection_heading(
                    out_ch, section_counter, strip_leading_number(content)))
                output.append("\n")
                continue
            if role == ROLE_SUBHEAD:
                if seen_title:
                    subsection_counter += 1
                    current_path = f"{out_ch}-{section_counter}-{subsection_counter}"
                    verse_counter = 0
                    output.append(format_subsubsection_heading(
                        out_ch, section_counter, subsection_counter,
                        strip_leading_number(content)))
                else:
                    section_counter += 1
                    current_path = f"{out_ch}-{section_counter}"
                    verse_counter = 0
                    output.append(format_subsection_heading(
                        out_ch, section_counter, strip_leading_number(content)))
                output.append("\n")
                continue
            # ROLE_VERSE
            verse_counter += 1
            output.append(format_verse(content, current_path, verse_counter))

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
