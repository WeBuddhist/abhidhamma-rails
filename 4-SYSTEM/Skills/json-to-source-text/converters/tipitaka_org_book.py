#!/usr/bin/env python3
"""
tipitaka_org_book.py — converter for tipitaka.org Mūla book exports.

Outputs Markdown using a Bible-style addressing scheme: one file = one "book"
in the Bible sense (= one tipitaka.org-level book like Dhammasaṅgaṇī),
which corresponds to a single "chapter" in the larger pitaka. Verses run
continuously through the whole book.

Header hierarchy:
    Namo tassa…         — plain text, no ID
    # <pitaka>          — h1, anchor ^<pitaka-slug>-0
    ## <book>           — h2, anchor ^<book_id>-0 (book_id = 1 for Dhammasaṅgaṇī)
    ### <h3 title>      — h3, source-level "chapter" segments (Mātikā,
                          Cittuppādakaṇḍaṃ, Rūpakaṇḍaṃ, Nikkhepakaṇḍaṃ,
                          Aṭṭhakathākaṇḍaṃ). Anchor ^<book>-<h3>-0.
    #### <h4 title>     — h4, source-level "title" segments (or a standalone
                          "subhead" before the first title in this h3).
                          - Inside Mātikā (TOC), uses letter-suffix path:
                            ^<book>-0a-0, ^<book>-0b-0, …
                          - Elsewhere: ^<book>-<h3>-<h4>-0
    ##### <h5 title>    — h5, source-level "subhead" segments that appear
                          after a title.
                          - Inside Mātikā: ^<book>-0<letter>-<h5>-0
                          - Elsewhere:     ^<book>-<h3>-<h4>-<h5>-0

Verse IDs:
    Main book content (everything except Mātikā):
        ^<book>-V   where V is a SINGLE counter that runs continuously
                    through every h3/h4/h5 from the first non-TOC verse
                    to the last verse of the book.

    TOC (Mātikā) exception:
        ^<book>-0<letter>-V   verse V of TOC sub-section <letter>
        The letter (a, b, c, …) is assigned to each h4 inside Mātikā in order.
        V restarts at 1 for each h4 but does NOT restart at h5 boundaries
        (gocchakas under Dukamātikā continue Dukamātikā's verse count).

Verse grouping:
    Same as before: a bodytext segment starting with `<digit>+. ` opens a new
    verse. Subsequent bodytext segments without a leading number are merged
    into the current verse as continuation lines.

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

from json_to_source_text import format_frontmatter, clean_text  # noqa: E402


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

# Map this source's pitaka field to a stable slug for the # heading anchor.
PITAKA_SLUG = {
    "abhidhamma": "abhidhamma",
    "sutta":      "sutta",
    "vinaya":     "vinaya",
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
        "verse_id_format": "book-verse",
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

    # Phase 1: bucket segments.
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

    # Phase 2: emit.
    out: list[str] = [format_frontmatter(meta), "\n"]

    if homage:
        out.append(homage + "\n\n")

    pitaka_slug = PITAKA_SLUG.get(str(meta.get("pitaka", "")).lower(), "pitaka")
    if pitaka_heading:
        out.append(f"# {pitaka_heading} ^{pitaka_slug}-0\n\n")

    # book_id: position of this book within its pitaka. Dhammasaṅgaṇī is the
    # 1st of the 7 Abhidhamma books, so we hard-code 1 here. When other books
    # are added, derive this from the source ID (abh01m → 1, abh02m → 2, …).
    book_id = _derive_book_id(meta.get("source_filename"), data.get("id"))

    if book_heading:
        out.append(f"## {book_heading} ^{book_id}-0\n\n")

    # Single global counter for non-TOC ("main") verses of the book.
    main_verse_counter = [0]  # list to allow nested-function mutation w/o nonlocal

    for src_ch in sorted(chapters.keys()):
        h3_position = src_ch
        is_toc = (src_ch == 0)
        items = chapters[src_ch]

        h3_title_raw = next(
            (c for r, c in items if r == ROLE_CHAPTER),
            f"Section {h3_position}",
        )
        h3_title = strip_leading_number(h3_title_raw)
        out.append(f"### {h3_title} ^{book_id}-{h3_position}-0\n\n")

        # Per-h3 emission state.
        h4_counter = 0          # numeric counter for h4 in non-TOC h3
        toc_letter_index = -1   # -1 → no h4 yet; 0 → 'a', 1 → 'b', …
        toc_letter = None       # current TOC h4 letter
        h5_counter = 0          # h5 counter (resets per h4)
        seen_title = False
        consumed_chapter_title = False
        toc_verse_counter = [0]  # resets per TOC h4

        verse_buffer: list[str] = []

        def make_verse_id():
            if is_toc and toc_letter is not None:
                toc_verse_counter[0] += 1
                return f"^{book_id}-{h3_position}{toc_letter}-{toc_verse_counter[0]}"
            else:
                main_verse_counter[0] += 1
                return f"^{book_id}-{main_verse_counter[0]}"

        def flush_verse():
            if not verse_buffer:
                return
            id_str = make_verse_id()
            body = "\n".join(verse_buffer)
            out.append(f"{body} {id_str}\n\n")
            verse_buffer.clear()

        for role, content in items:
            if role == ROLE_CHAPTER:
                if not consumed_chapter_title:
                    consumed_chapter_title = True
                    continue
                # Stray chapter inside source chapter — promote to title
                role = ROLE_TITLE
            if role == ROLE_TITLE:
                seen_title = True
                flush_verse()
                if is_toc:
                    toc_letter_index += 1
                    toc_letter = chr(ord("a") + toc_letter_index)
                    toc_verse_counter[0] = 0
                    heading_id = f"^{book_id}-{h3_position}{toc_letter}-0"
                else:
                    h4_counter += 1
                    h5_counter = 0
                    heading_id = f"^{book_id}-{h3_position}-{h4_counter}-0"
                out.append(f"#### {strip_leading_number(content)} {heading_id}\n\n")
                continue
            if role == ROLE_SUBHEAD:
                flush_verse()
                if seen_title:
                    # H5: deeper sub-section under a title — preserves verse path
                    h5_counter += 1
                    if is_toc:
                        heading_id = f"^{book_id}-{h3_position}{toc_letter}-{h5_counter}-0"
                    else:
                        heading_id = f"^{book_id}-{h3_position}-{h4_counter}-{h5_counter}-0"
                    out.append(f"##### {strip_leading_number(content)} {heading_id}\n\n")
                else:
                    # Standalone subhead before any title — treat as H4
                    if is_toc:
                        toc_letter_index += 1
                        toc_letter = chr(ord("a") + toc_letter_index)
                        toc_verse_counter[0] = 0
                        heading_id = f"^{book_id}-{h3_position}{toc_letter}-0"
                    else:
                        h4_counter += 1
                        h5_counter = 0
                        heading_id = f"^{book_id}-{h3_position}-{h4_counter}-0"
                    out.append(f"#### {strip_leading_number(content)} {heading_id}\n\n")
                continue
            # ROLE_VERSE
            if _verse_opening_re.match(content):
                flush_verse()
            verse_buffer.append(content)

        flush_verse()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(out), encoding="utf-8")


_book_id_re = re.compile(r"abh(\d+)m")


def _derive_book_id(source_filename, source_id) -> int:
    """Derive the book's position within the Abhidhamma pitaka from the
    source ID/filename. tipitaka.org uses abh01m, abh02m, … for the seven
    Abhidhamma books."""
    for s in (source_filename, source_id):
        if not s:
            continue
        m = _book_id_re.search(str(s))
        if m:
            return int(m.group(1))
    return 1  # default


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("output_path", type=Path)
    args = ap.parse_args()
    convert_json_to_source_text(args.json_path, args.output_path)
    print(f"Wrote {args.output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
