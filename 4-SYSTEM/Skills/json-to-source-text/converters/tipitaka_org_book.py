#!/usr/bin/env python3
"""
tipitaka_org_book.py — converter for tipitaka.org Mūla book exports.

Outputs Markdown matching the Abhidhamma-rails source-text conventions
(see 4-SYSTEM/Guidelines/source-formatting.md and the file-level header
hierarchy adopted for canonical Pāli texts).

Header hierarchy emitted:
    Namo tassa…             — plain text, no ID
    # <pitaka name>         — from css_class="nikaya"
    ## <book name>          — from css_class="book"
    ## N. <chapter name>    — one per source chapter; chapter 0 = Mātikā (TOC)
    ### N.M <title>         — major sub-section (css_class="title", or a
                              standalone css_class="subhead" before any title)
    #### N.M.K <subhead>    — minor sub-section (css_class="subhead" after a
                              title in the same chapter)

Block IDs:
    Headings:   ^N-0, ^N-M-0, ^N-M-K-0  (trailing 0 = heading marker)
    Verses:     ^N-V, ^N-M-V, ^N-M-K-V  (full path of enclosing heading +
                                          verse number from the source)

Verse grouping:
    A bodytext segment whose content starts with `<digit>+.` (e.g. "1.",
    "23.") opens a new verse. Subsequent bodytext segments are accumulated
    as continuation lines of that verse until the next numbered segment or
    a heading. Each verse emits as a multi-line block with the ID at the
    end of the last line, followed by a blank line.

CLI:
    python tipitaka_org_book.py source.json output.md
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from json_to_source_text import (  # noqa: E402
    format_frontmatter,
    format_chapter_heading,
    format_subsection_heading,
    format_subsubsection_heading,
    clean_text,
)


_leading_num_re = re.compile(r"^\s*\d+\.\s*")
_verse_opening_re = re.compile(r"^\s*\d+\.\s")


def strip_leading_number(title: str) -> str:
    return _leading_num_re.sub("", title).strip()


# Internal roles
ROLE_CHAPTER = "chapter"
ROLE_TITLE = "title"
ROLE_SUBHEAD = "subhead"
ROLE_VERSE = "verse"

CATEGORY_TO_ROLE = {
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
    json_path = Path(json_path)
    output_path = Path(output_path)

    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    meta = extract_metadata(data, json_path)
    segments = data.get("segments", [])

    # Phase 1 — bucket segments.
    homage = None
    pitaka_heading = None
    book_heading = None
    chapters: dict[int, list] = {}
    saw_first_chapter = False

    for seg in segments:
        css = seg.get("css_class", "")
        content = clean_text(seg.get("content", ""))
        if not content:
            continue
        src_ch = seg.get("chapter", 0)

        if not saw_first_chapter:
            if css == "centered":
                if homage is None:
                    homage = content
                continue
            if css == "nikaya":
                pitaka_heading = content
                continue
            if css == "book":
                book_heading = content
                continue

        role = CATEGORY_TO_ROLE.get(css, ROLE_VERSE)
        if role == ROLE_CHAPTER:
            saw_first_chapter = True
        chapters.setdefault(src_ch, []).append((role, content))

    # Phase 2 — emit.
    out: list[str] = [format_frontmatter(meta), "\n"]

    if homage:
        out.append(homage + "\n\n")
    if pitaka_heading:
        out.append(f"# {pitaka_heading}\n\n")
    if book_heading:
        out.append(f"## {book_heading}\n\n")

    for src_ch in sorted(chapters.keys()):
        out_ch = src_ch
        items = chapters[src_ch]
        chapter_title_raw = next(
            (c for r, c in items if r == ROLE_CHAPTER),
            f"Chapter {out_ch}",
        )
        chapter_title = strip_leading_number(chapter_title_raw)
        out.append(format_chapter_heading(out_ch, chapter_title))
        out.append("\n")

        current_path = str(out_ch)
        verse_counter = 0
        section_counter = 0
        subsection_counter = 0
        seen_title = False
        consumed_chapter_title = False
        verse_buffer: list[str] = []

        def flush_verse() -> None:
            nonlocal verse_counter
            if not verse_buffer:
                return
            verse_counter += 1
            body = "\n".join(verse_buffer)
            out.append(f"{body} ^{current_path}-{verse_counter}\n\n")
            verse_buffer.clear()

        def change_path(new_path: str) -> None:
            nonlocal current_path, verse_counter
            flush_verse()
            current_path = new_path
            verse_counter = 0

        for role, content in items:
            if role == ROLE_CHAPTER:
                if not consumed_chapter_title:
                    consumed_chapter_title = True
                    continue
                section_counter += 1
                subsection_counter = 0
                seen_title = False
                change_path(f"{out_ch}-{section_counter}")
                out.append(format_subsection_heading(
                    out_ch, section_counter, strip_leading_number(content)))
                out.append("\n")
                continue
            if role == ROLE_TITLE:
                section_counter += 1
                subsection_counter = 0
                seen_title = True
                change_path(f"{out_ch}-{section_counter}")
                out.append(format_subsection_heading(
                    out_ch, section_counter, strip_leading_number(content)))
                out.append("\n")
                continue
            if role == ROLE_SUBHEAD:
                if seen_title:
                    subsection_counter += 1
                    change_path(f"{out_ch}-{section_counter}-{subsection_counter}")
                    out.append(format_subsubsection_heading(
                        out_ch, section_counter, subsection_counter,
                        strip_leading_number(content)))
                else:
                    section_counter += 1
                    change_path(f"{out_ch}-{section_counter}")
                    out.append(format_subsection_heading(
                        out_ch, section_counter, strip_leading_number(content)))
                out.append("\n")
                continue
            # ROLE_VERSE — accumulate; a new "<n>." opens a new verse
            if _verse_opening_re.match(content):
                flush_verse()
            verse_buffer.append(content)

        flush_verse()
        out.append("\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(out), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("output_path", type=Path)
    args = ap.parse_args()
    convert_json_to_source_text(args.json_path, args.output_path)
    print(f"Wrote {args.output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
