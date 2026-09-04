# Parser — Commentary

Takes a linted commentary file and produces API-ready JSON payloads for the edition, TOC, and root-text alignment.

Forked from `parser-root-text`. Content segments default to **`paragraph`** (not verse). Always emits `alignment.json` from Obsidian transclusions to the root text.

## What it does

Runs these functions from the commentary `.md` and its lint JSON:

1. **extract_text_input** — strips null/empty fields from the lint JSON and writes a clean `text.json` (includes `commentary_of` when present)
2. **build_edition** — extracts content, builds a segmented edition with character-level spans (`type: paragraph` for body), writes `edition.json`
3. **build_toc** — builds a nested table of contents from title segments, writes `toc.json`
4. **build_alignment** — extracts segment-to-segment alignment from Obsidian transclusion links (`![[...#^ref]]`), writes `alignment.json`

## Output

```
output/
  <stem>.text.json        # clean text_input payload (with commentary_of)
  <stem>.edition.json     # edition content + segmentation (paragraph default)
  <stem>.toc.json         # nested TOC with character spans
  <stem>.alignment.json   # commentary↔root-text segment alignments
```

## Alignment / transclusion

Transclusion links in the commentary (`![[1-SOURCES/Text/pi-1.md#^1-585]]`) define which root-text segment each commentary segment corresponds to.

- `source_segment_reference` — segment in the commentary
- `target_segment_reference` — segment in the root text

A transclusion or consecutive group of transclusions opens an alignment scope.
Every following commentary paragraph aligns to that root-text block or group
until the scope ends. A scope ends at either:

- the next transclusion group, or
- any heading — commentary after a heading must carry its own transclusion to
  be aligned

Headings themselves are never aligned. Alignment may be many-to-one (several
commentary paragraphs gloss one root verse) or many-to-many (several
paragraphs discuss a transcluded verse group).

## Requirements

```
pip install PyYAML pyewts
```

Requires Python 3.8+.

## How to run

Run from the project root (`abhidhamma-rails/`):

```bash
python3 4-SYSTEM\scripts\parser-commentary\parser.py "1-SOURCES\Commentaries\pi-dhammasangani-atthakatha.md" "4-SYSTEM\scripts\linter-commentary\output\pi-dhammasangani-atthakatha.lint.json"
```

## Notes

- Run the linter first — the parser reads `commentary_of` and other resolved fields from the lint JSON
- Author contributions without a resolvable id are dropped with a warning; missing contributions are allowed
- Missing `alt_titles` is allowed (warning only)
- Blocks without a reference marker (`^ref`) are skipped with a warning
- Header refs may have any depth; content refs max `^n-n-n` (3 parts)
- Pure transclusion blocks (`![[...]]` only) are silently skipped from edition content — they feed alignment only
- Tibetan TOC titles in Wylie are auto-converted to Unicode
