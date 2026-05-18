#!/usr/bin/env python3
"""Extract token-pair rows from an interlinear gloss file.

Walks every ``gloss`` code block in the input file, pairs each ``\\gla``
token with the ``\\glb`` cell at the same column, and emits a CSV row per
token pair. The CSV is the working table that ``glossary-extract-raw``
reads to tally keyword renderings.

Usage:

    python3 extract_pairs.py <gloss-file>.md <output>.csv

CSV columns: ``source_token, source_lemma, target_rendering, block_id``.

Rows where the rendering is ``--`` (placeholder) are skipped.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

BLOCK_HEADING_RE = re.compile(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", re.MULTILINE)
GLOSS_BLOCK_RE = re.compile(r"```gloss\s*\n(.*?)```", re.DOTALL)


def parse_gloss_file(path: Path):
    """Yield (block_id, gla_tokens, glb_tokens) per heading."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(BLOCK_HEADING_RE, text)
    # parts: [preamble, id1, section1, id2, section2, ...]
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        m = GLOSS_BLOCK_RE.search(section)
        if not m:
            continue
        body = m.group(1)
        gla = _line(body, "gla")
        glb = _line(body, "glb")
        yield block_id, gla, glb


def _line(body: str, marker: str) -> list[str]:
    match = re.search(rf"^\\{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not match:
        # Fallback for old format without backslash
        match = re.search(rf"^{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not match:
        return []
    return match.group(1).split()


def extract(gloss_path: Path, output_path: Path) -> tuple[int, int, int]:
    """Write the CSV. Return (rows_written, blocks_seen, rows_skipped_placeholder)."""
    rows_written = 0
    blocks_seen = 0
    rows_skipped = 0
    with output_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["source_token", "source_lemma", "target_rendering", "block_id"])
        for block_id, gla, glb in parse_gloss_file(gloss_path):
            blocks_seen += 1
            if not gla:
                continue
            for i, src in enumerate(gla):
                rendering = glb[i] if i < len(glb) else "--"
                if rendering == "--" or not rendering:
                    rows_skipped += 1
                    continue
                # Without a separate morphology line, lemma falls back to the source token.
                lemma = src
                writer.writerow([src, lemma, rendering, block_id])
                rows_written += 1
    return rows_written, blocks_seen, rows_skipped


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    gloss_path = Path(argv[1])
    output_path = Path(argv[2])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows, blocks, skipped = extract(gloss_path, output_path)
    print(
        f"Wrote {output_path}: rows={rows} blocks={blocks} skipped_placeholders={skipped}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
