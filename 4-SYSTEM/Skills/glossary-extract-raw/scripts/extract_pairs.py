#!/usr/bin/env python3
"""Extract token-pair rows from an interlinear gloss file.

Walks every ``gloss`` code block in the input file, pairs each source
token with its target gloss, and emits a CSV row per pair.
Supports both legacy horizontal (\gla/\glb) and new vertical formats.

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
    """Yield (block_id, pairs) per heading. pairs is list of (src, gloss)."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(BLOCK_HEADING_RE, text)
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        m = GLOSS_BLOCK_RE.search(section)
        if not m:
            continue
        body = m.group(1).strip()
        
        # Check for legacy horizontal format
        if "\\gla" in body or "\\glb" in body:
            gla = _line(body, "gla")
            glb = _line(body, "glb")
            pairs = []
            for j, src in enumerate(gla):
                rendering = glb[j] if j < len(glb) else "--"
                pairs.append((src, rendering))
            yield block_id, pairs
        else:
            # New vertical format: each line is "token gloss"
            pairs = []
            for line in body.splitlines():
                if not line.strip(): continue
                parts_line = line.split(maxsplit=1)
                if len(parts_line) == 2:
                    pairs.append((parts_line[0], parts_line[1]))
                elif len(parts_line) == 1:
                    pairs.append((parts_line[0], "--"))
            yield block_id, pairs


def _line(body: str, marker: str) -> list[str]:
    match = re.search(rf"^\\{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not match:
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
        for block_id, pairs in parse_gloss_file(gloss_path):
            blocks_seen += 1
            for src, rendering in pairs:
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
