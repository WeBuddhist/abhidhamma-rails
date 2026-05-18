#!/usr/bin/env python3
"""Scaffold an interlinear gloss file for one (root-text, translation) pair.

Reads two markdown files that share an Obsidian block-ID scheme and writes a
gloss file under ``2-RAILS/Bilingual-Glossaries/Raw/`` with one ``gloss`` code
block per paired block. The format is vertical: the translation appears above
the block, and the block contains ``token gloss`` pairs.

If the output file already exists, existing gloss lines are preserved when
their Pāli token matches.

Usage:

    python3 scaffold_gloss.py <root-text>.md <translation>.md <output>.md

    python3 scaffold_gloss.py --validate <gloss-file>.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s")
FM_FIELD_RE = lambda name: re.compile(rf"^{name}:\s*(.+?)\s*$", re.MULTILINE)

# Tokens we strip from the end of a source token before placing it on gla.
TRAILING_PUNCT = ".,;:!?"
# Tokens we strip from the beginning.
LEADING_PUNCT = "([{"


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end():]
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields, body


def parse_blocks(path):
    """Return {block_id: paragraph_text} for ``path``. Skip headings and frontmatter."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    blocks = {}
    order = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph or HEADING_RE.match(paragraph):
            continue
        match = BLOCK_ID_RE.search(paragraph)
        if not match:
            continue
        block_id = match.group(1)
        body = paragraph[: match.start()].rstrip()
        if block_id not in blocks:
            order.append(block_id)
        blocks[block_id] = body
    return blocks, order


def tokenise_source(text):
    """Split source text into gloss tokens, stripping editorial markup."""
    cleaned = re.sub(r"\[[^\]]*\]", "", text)
    cleaned = re.sub(r"\([^)]*\)", "", cleaned)
    cleaned = re.sub(r"^\s*\d+\.\s*", "", cleaned)
    tokens = []
    for raw in cleaned.split():
        token = raw.strip(TRAILING_PUNCT + LEADING_PUNCT + "—–\"\'")
        if not token:
            continue
        if re.fullmatch(r"\d+", token):
            continue
        tokens.append(token)
    return tokens


def normalise_free_translation(text):
    """Collapse internal whitespace and newlines; preserve sentence punctuation."""
    return re.sub(r"\s+", " ", text).strip()


def parse_existing_gloss(text):
    """Return {block_id: {token: gloss}}.

    Used when refreshing an existing gloss file to preserve filled lines.
    Supports both legacy horizontal and new vertical formats.
    """
    out = {}
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        
        # Check for vertical format inside ```gloss block
        gloss_match = re.search(r"```gloss\s*\n(.*?)\n```", section, re.DOTALL)
        if gloss_match:
            lines = gloss_match.group(1).strip().splitlines()
            block_data = {}
            for line in lines:
                if line.startswith("\\gla") or line.startswith("\\glb") or line.startswith("\\ex"):
                    # Legacy horizontal format - we'll handle this separately if needed
                    continue
                parts_line = line.split(maxsplit=1)
                if len(parts_line) == 2:
                    block_data[parts_line[0]] = parts_line[1]
                elif len(parts_line) == 1:
                    block_data[parts_line[0]] = "--"
            if block_data:
                out[block_id] = block_data
                continue

        # Legacy horizontal format fallback
        gla = _find_horizontal_line(section, "gla").split()
        glb = _find_horizontal_line(section, "glb").split()
        if gla and glb and len(gla) == len(glb):
            out[block_id] = dict(zip(gla, glb))
            
    return out


def _find_horizontal_line(section, marker):
    match = re.search(rf"^\\{marker}\s+(.*)$", section, flags=re.MULTILINE)
    if not match:
        match = re.search(rf"^{marker}\s+(.*)$", section, flags=re.MULTILINE)
    return match.group(1).rstrip() if match else ""


def build_gloss_block(block_id, gla_tokens, free_translation, existing_blocks):
    """Render the translation and a vertical ```gloss``` block."""
    existing = existing_blocks.get(block_id, {})
    lines = [free_translation, "", "```gloss"]
    
    # Calculate padding for alignment
    max_len = max(len(t) for t in gla_tokens) if gla_tokens else 0
    
    for token in gla_tokens:
        gloss = existing.get(token, "--")
        lines.append(f"{token.ljust(max_len + 2)}{gloss}")
    
    lines.append("```")
    return "\n".join(lines)


def scaffold(source_path, target_path, output_path):
    source_fm, _ = parse_frontmatter(source_path.read_text(encoding="utf-8"))
    target_fm, _ = parse_frontmatter(target_path.read_text(encoding="utf-8"))
    source_blocks, order = parse_blocks(source_path)
    target_blocks, _ = parse_blocks(target_path)

    source_lang = source_fm.get("lang_tag", source_fm.get("language", "src"))
    target_lang_tag = target_fm.get("lang_tag", target_fm.get("language", "tgt"))
    target_language = target_fm.get("language", target_lang_tag)
    translator = target_fm.get("translator", "")

    existing = {}
    if output_path.exists():
        try:
            existing = parse_existing_gloss(output_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"warning: could not re-parse existing {output_path}: {exc}", file=sys.stderr)

    blocks_rendered = 0
    skipped_target_missing = 0
    skipped_source_missing = 0
    reset_lines = []

    out_lines = []
    out_lines.append("---")
    out_lines.append(f"source_file: 1-SOURCES/Text/{source_path.name}")
    out_lines.append(f"source_language: {source_lang}")
    out_lines.append(f"target_file: 1-SOURCES/Translations/{target_path.name}")
    out_lines.append(f"target_language: {target_language}")
    out_lines.append(f"target_lang_tag: {target_lang_tag}")
    if translator:
        out_lines.append(f"translator: {translator}")
    out_lines.append("total_verses: __PLACEHOLDER__")
    out_lines.append(f"generated: {dt.date.today().isoformat()}")
    out_lines.append("status: draft")
    out_lines.append("---")
    out_lines.append("")
    title = f"Interlinear gloss — {source_lang} → {target_lang_tag}"
    out_lines.append(f"# {title}")
    out_lines.append("")

    for block_id in order:
        source_text = source_blocks.get(block_id, "")
        target_text = target_blocks.get(block_id, "")
        if not source_text:
            skipped_source_missing += 1
            continue
        if not target_text.strip() or target_text.strip() == "-":
            skipped_target_missing += 1
            continue
        gla_tokens = tokenise_source(source_text)
        if not gla_tokens:
            continue
            
        free_t = normalise_free_translation(target_text)
        block = build_gloss_block(block_id, gla_tokens, free_t, existing)
        out_lines.append(f"## ^{block_id}")
        out_lines.append("")
        out_lines.append(block)
        out_lines.append("")
        blocks_rendered += 1

    rendered = "\n".join(out_lines).replace("__PLACEHOLDER__", str(blocks_rendered))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    return {
        "blocks_rendered": blocks_rendered,
        "skipped_target_missing": skipped_target_missing,
        "skipped_source_missing": skipped_source_missing,
        "reset_lines": reset_lines,
    }


def validate(gloss_path):
    text = gloss_path.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    errors = []
    checked = 0
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        gloss_match = re.search(r"```gloss\s*\n(.*?)\n```", section, re.DOTALL)
        if not gloss_match:
            errors.append(f"{block_id}: missing gloss block")
            continue
        checked += 1
        lines = gloss_match.group(1).strip().splitlines()
        for line_no, line in enumerate(lines, 1):
            if not line.strip(): continue
            parts_line = line.split()
            if len(parts_line) < 2:
                errors.append(f"{block_id} line {line_no}: missing gloss for token '{parts_line[0] if parts_line else '?'}'")
    return checked, errors


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", metavar="FILE", help="Validate an existing gloss file")
    parser.add_argument("source", nargs="?", type=Path, help="Root-text markdown file")
    parser.add_argument("target", nargs="?", type=Path, help="Translation markdown file")
    parser.add_argument("output", nargs="?", type=Path, help="Output gloss file")
    args = parser.parse_args(argv[1:])

    if args.validate:
        checked, errors = validate(Path(args.validate))
        if errors:
            for err in errors:
                print(f"  {err}", file=sys.stderr)
            print(f"FAIL — {len(errors)} errors across {checked} blocks", file=sys.stderr)
            return 1
        print(f"OK — {checked} blocks all valid")
        return 0

    if not (args.source and args.target and args.output):
        parser.print_help(sys.stderr)
        return 2

    stats = scaffold(args.source, args.target, args.output)
    print(
        f"Wrote {args.output}: blocks={stats['blocks_rendered']} "
        f"skipped_target_missing={stats['skipped_target_missing']} "
        f"skipped_source_missing={stats['skipped_source_missing']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
