---
name: glossary-extract-raw
description: Extract every source-language keyword and its rendering from an interlinear gloss file into a raw per-source bilingual glossary. Supports both horizontal (\gla/\glb) and vertical gloss formats.
---

# glossary-extract-raw

This skill walks through an **interlinear gloss file** and extracts every `(source-token, target-rendering)` pair into a tabular format. This is the first step in building the bilingual glossaries.

## Inputs

- **Interlinear gloss file** — `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target-lang-tag>-gloss.md`.

## Output

One file at:

```
2-RAILS/Bilingual-Glossaries/Raw/<source>-<target-lang-tag>.md
```

This file contains a table of renderings found in that specific translation, with frequencies and block-ID citations.

---

## Procedure

1. **Run the extraction script:**

   ```bash
   python3 4-SYSTEM/Skills/glossary-extract-raw/scripts/extract_pairs.py \
       2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md \
       0-INBOX/pi-en-rd-pairs.csv
   ```

2. **Tally and format:**
   The script produces a CSV of raw pairs. A secondary pass (often handled by the same helper or a spreadsheet) tallies these into the final markdown table format.

---

## Format support

The extraction script `extract_pairs.py` is format-agnostic:
- **Vertical Format:** Pairs are extracted line-by-line from the `gloss` block.
- **Horizontal Format:** Pairs are extracted by aligning columns in the `\gla` and `\glb` lines.

This ensures that the pipeline continues to work even as older gloss files are migrated to the new vertical standard.

---

## Completion check

- [ ] Every non-placeholder rendering in the gloss file appears in the output.
- [ ] Source tokens are correctly paired with their target glosses.
- [ ] Block ID citations are preserved for every rendering.
