#!/usr/bin/env python3
"""
json_to_source_text.py — generic JSON → source-text converter template.

This script does a "best effort" pass on any JSON file with a top-level array
of segment-like objects, mapping common category values to source-formatting.md
constructs. It is intended primarily as the base for source-specific converters
(see converters/<source_slug>.py), but can be run directly as a fallback.

CLI:
    python json_to_source_text.py path/to/source.json path/to/output.md

Programmatic:
    from json_to_source_text import convert_json_to_source_text
    convert_json_to_source_text(json_path, output_path)

The module also exports helper functions that source-specific converters use:

  format_frontmatter(meta: dict) -> str
  format_chapter_heading(num: int, title: str) -> str       # "## N. title ^N-0"
  format_subsection_heading(chapter: int, section: int, title: str) -> str
  format_verse(content: str, chapter: int, verse: int) -> str
  clean_text(s: str) -> str
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable


# ----- formatting helpers -----------------------------------------------------

def format_frontmatter(meta: dict) -> str:
    """Render a YAML frontmatter block. Strips None values; preserves field order."""
    lines = ["---"]
    for k, v in meta.items():
        if v is None or v == "":
            continue
        if isinstance(v, list):
            if not v:
                continue
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, (int, float, bool)):
            lines.append(f"{k}: {v}")
        else:
            s = str(v)
            # quote if the value contains characters that need it
            if any(c in s for c in ":#\"'\n") or s.strip() != s:
                s = '"' + s.replace('"', '\\"') + '"'
            lines.append(f"{k}: {s}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def format_chapter_heading(num: int, title: str) -> str:
    """## N. title ^N-0"""
    title = title.strip()
    return f"## {num}. {title} ^{num}-0\n"


def format_subsection_heading(chapter: int, section: int, title: str) -> str:
    """### N.M title ^N-M-0"""
    title = title.strip()
    return f"### {chapter}.{section} {title} ^{chapter}-{section}-0\n"


def format_verse(content: str, chapter: int, verse: int) -> str:
    """content ^chapter-verse"""
    content = content.rstrip()
    return f"{content} ^{chapter}-{verse}\n"


_ws_re = re.compile(r"[ \t]+")

def clean_text(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = _ws_re.sub(" ", s)
    return s.strip()


# ----- generic conversion -----------------------------------------------------

# Default category routing — override in source-specific converters
DEFAULT_CATEGORY_TO_ROLE = {
    # tipitaka.org / many HTML-derived schemas use these CSS class names
    "centered": "preface",
    "nikaya":   "preface",
    "book":     "preface",
    "chapter":  "chapter",
    "title":    "subsection",
    "subhead":  "subsection",
    "bodytext": "verse",
    "unindented": "verse",
    # generic role names
    "heading":     "chapter",
    "subheading":  "subsection",
    "paragraph":   "verse",
}

# Roles we know how to emit
ROLE_CHAPTER = "chapter"
ROLE_SUBSECTION = "subsection"
ROLE_VERSE = "verse"
ROLE_PREFACE = "preface"  # goes into ## 0. Introduction


def load_metadata(data: dict, source_path: Path) -> dict:
    """Build a minimal frontmatter dict from common top-level keys."""
    title = (
        data.get("title")
        or data.get("title_pali")
        or data.get("title_sanskrit")
        or data.get("title_tibetan")
        or source_path.stem
    )
    return {
        "title": title,
        "file_type": "root-text",
        "verse_id_format": "chapter-verse",
        "source_description": f"Converted from {source_path.name}",
        "source_filename": data.get("source_filename"),
        "source_url": data.get("source_url"),
    }


def find_segments(data) -> list[dict]:
    """Return the first top-level array of dicts."""
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        # pick the largest array of dicts
        best = []
        for v in data.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and len(v) > len(best):
                best = v
        return best
    return []


def _category_of(seg: dict) -> str | None:
    for k in ("css_class", "class", "type", "kind", "role"):
        v = seg.get(k)
        if isinstance(v, str):
            return v
    return None


def _content_of(seg: dict) -> str:
    for k in ("content", "text", "body"):
        v = seg.get(k)
        if isinstance(v, str):
            return v
    return ""


def _chapter_of(seg: dict, default: int = 0) -> int:
    for k in ("chapter", "ch", "section", "book"):
        v = seg.get(k)
        if isinstance(v, int):
            return v
        if isinstance(v, str) and v.isdigit():
            return int(v)
    return default


def iter_blocks(segments: list[dict], routing: dict[str, str]):
    """
    Yield (role, content, chapter, ...extras) tuples ready to be emitted.

    Default routing dispatches each segment by its category field.
    """
    for seg in segments:
        cat = _category_of(seg)
        role = routing.get(cat, ROLE_VERSE)
        yield role, clean_text(_content_of(seg)), _chapter_of(seg), seg


def convert_json_to_source_text(
    json_path: str | Path,
    output_path: str | Path,
    *,
    routing: dict[str, str] | None = None,
    extra_metadata: dict | None = None,
) -> None:
    """
    Generic conversion. Walks segments, dispatches each by category, emits Markdown.

    Source-specific converters typically call this with a customised `routing` table
    and `extra_metadata` overlay, or wrap their own logic on top.
    """
    json_path = Path(json_path)
    output_path = Path(output_path)
    routing = {**DEFAULT_CATEGORY_TO_ROLE, **(routing or {})}

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    meta = load_metadata(data if isinstance(data, dict) else {}, json_path)
    if extra_metadata:
        meta = {**meta, **extra_metadata}

    segments = find_segments(data)

    # Group by source chapter, with a synthetic chapter 0 for preface material
    output: list[str] = [format_frontmatter(meta)]
    chapter_state: dict[int, dict] = {}

    # First pass: collect any preface segments (encountered before the first chapter heading
    # OR carrying explicit "preface" role) into chapter 0
    preface_segments = []
    chapter_segments: dict[int, list] = {}
    seen_first_chapter = False
    for role, content, ch, seg in iter_blocks(segments, routing):
        if role == ROLE_PREFACE and not seen_first_chapter:
            preface_segments.append((content, seg))
            continue
        seen_first_chapter = True
        chapter_segments.setdefault(ch, []).append((role, content, seg))

    # Emit preface as Chapter 0
    if preface_segments:
        output.append("\n")
        output.append(format_chapter_heading(0, "Introduction"))
        output.append("\n")
        for i, (content, seg) in enumerate(preface_segments, start=1):
            if content:
                output.append(format_verse(content, 0, i))

    # Emit each subsequent chapter
    for ch in sorted(chapter_segments.keys()):
        items = chapter_segments[ch]
        # Find chapter title — first "chapter" role segment
        chapter_title = None
        section_counter = 0
        verse_counter = 0
        title_idx = None
        for i, (role, content, seg) in enumerate(items):
            if role == ROLE_CHAPTER:
                chapter_title = content
                title_idx = i
                break
        output.append("\n")
        output.append(format_chapter_heading(ch, chapter_title or f"Chapter {ch}"))
        output.append("\n")
        for i, (role, content, seg) in enumerate(items):
            if i == title_idx:
                continue
            if not content:
                continue
            if role == ROLE_CHAPTER:
                # Another "chapter" role inside the same chapter — promote to subsection
                section_counter += 1
                output.append(format_subsection_heading(ch, section_counter, content))
                output.append("\n")
            elif role == ROLE_SUBSECTION:
                section_counter += 1
                output.append(format_subsection_heading(ch, section_counter, content))
                output.append("\n")
            else:  # ROLE_VERSE / ROLE_PREFACE in chapter > 0
                verse_counter += 1
                output.append(format_verse(content, ch, verse_counter))

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
