---
name: glossary-extract-raw
description: Extract every source-language keyword and the rendering(s) it receives from one existing translation or reference text into a raw per-source glossary at 2-RAILS/Glossaries/Raw/<source-name>.md. Uses block-ID alignment between root text and translation to pair source/target snippets, then catalogues attested renderings keyword by keyword.
---

# glossary-extract-raw

This skill turns one translation file in `1-SOURCES/Translations/` (or any other reference text in the target language) into a **raw glossary** — a per-source record of every keyword in the original language and every distinct rendering that translation uses for it. The raw glossaries are the input for `glossary-combine`.

The skill has two halves:

1. **Mechanical alignment** (helper script) — pair every translation block with the corresponding root-text block by block ID. Output a working table.
2. **Keyword extraction** (LLM) — walk through the paired blocks, identify source-language keywords, and record every rendering each one receives.

---

## Inputs

- **Translation file** — one file in `1-SOURCES/Translations/<source-name>.md` (or a reference text in the same target language).
- **Root text** — the source-language file the translation is aligned against, declared in the translation file's `root_text` frontmatter field.
- **Keyword list (optional)** — if a controlled keyword list exists for this text (extracted from the mātikā, or pulled from existing Local-Wiki articles), pass it in to constrain extraction. If none is supplied, extract every recurring substantive in the source.

## Output

One file at:

```
2-RAILS/Glossaries/Raw/<source-name>.md
```

`<source-name>` matches the translation filename without the `.md` extension (e.g. `en-dhammasangani-rd`). Always include the `lang_tag` from the translation file's frontmatter in the source name so the language pair is obvious from the filename.

---

## Output file format

```markdown
---
source_file: 1-SOURCES/Translations/<translation-name>.md
source_language: <pi | sa | bo | zh>
target_language: <en | bn | sin | ...>
language_pair: <pi-en | pi-bn | ...>
root_text: 1-SOURCES/Text/<root-text>.md
translator: <name from translation frontmatter, if present>
total_keywords: <count>
status: draft
---

# Raw glossary — <translator / translation short name>

## <source-lang keyword> → renderings

**Renderings attested in this source:**

| Rendering | Frequency | First seen | Notes |
|-----------|-----------|------------|-------|
| <target-language rendering> | <n> | ^<block-id> | <inflection / context note> |
| <alternative rendering> | <n> | ^<block-id> | <when this rendering is used> |

**Sample pairings:**

> **^1-0a-1** — *<source snippet containing the keyword>*
> → "<corresponding target snippet>"

> **^1-0a-5** — *<source snippet>*
> → "<target snippet>"

---

## <next keyword> → renderings

...
```

One `##` heading per keyword. Keywords are sorted alphabetically (by source-language form). Diacritics are preserved.

---

## Rules

1. **One file per translation source.** Never merge two translations into one raw file — that's what `glossary-combine` is for.
2. **Pair by block ID, not by sentence proximity.** Translation files in this vault are block-aligned with the root text. Every snippet pairing uses the shared block ID.
3. **Record every distinct rendering.** If the translator renders *dhammā* as "states" in one passage and "phenomena" in another, both appear in the rendering table with their frequencies.
4. **Frequencies are counts of distinct blocks, not raw token counts.** A block in which *dhammā* appears three times all rendered as "states" counts once for "states".
5. **Sample pairings show context.** Two to four blocks per keyword is enough. Pick blocks that show different renderings or different inflectional contexts.
6. **No interpretive notes.** This file is descriptive: what the translation actually does. Judgments about whether a rendering is good belong in `glossary-select`, not here.
7. **Use the translator's exact wording.** Preserve capitalisation, punctuation, and any glosses inline.

---

## Procedure

1. **Verify alignment.** Confirm that the translation file and the root text both use the same block-ID scheme. Run the alignment helper (below) to produce the working table.
2. **Identify keywords.** Run a frequency pass over the source-language file (or use the supplied keyword list). Substantives that recur at least three times across the text are candidates. Discard function words and inflectional particles unless they carry interpretive weight (e.g. *iti*).
3. **For each keyword:** walk through every aligned block in which the keyword appears in the source snippet. Read the target snippet. Identify the word or phrase in the target that renders the keyword. Record it.
4. **Tally renderings.** Build the rendering table — one row per distinct rendering, frequency = number of distinct blocks in which the rendering occurs.
5. **Pick sample pairings.** Two to four blocks per keyword, chosen to cover the range of renderings and inflectional contexts.
6. **Write the file** to `2-RAILS/Glossaries/Raw/<source-name>.md` with the frontmatter populated.
7. **Set `status: draft`.** A domain specialist marks the file `complete` after spot-checking.

---

## Alignment helper

A small Python script under `scripts/` does the mechanical alignment. It reads both files, pulls out every block in each (block IDs of the form `^<id>` at end of paragraph), and emits a CSV of paired blocks.

```bash
python3 4-SYSTEM/Skills/glossary-extract-raw/scripts/align_blocks.py \
    1-SOURCES/Text/pi-dhammasangani.md \
    1-SOURCES/Translations/en-dhammasangani-rd.md \
    0-INBOX/temp/align-en-rd.csv
```

The CSV has four columns: `block_id, source_text, target_text, notes`. Open it; this is the working table the keyword pass reads from.

Blocks that exist in only one file are flagged in the `notes` column (`source-only` or `target-only`) so untranslated passages don't generate false renderings.

---

## Completion check

- [ ] Every keyword appears as its own `##` heading
- [ ] Every keyword has at least one rendering row and one sample pairing
- [ ] Sample pairings show the block ID and quote both source and target verbatim
- [ ] Frequencies count distinct blocks, not raw tokens
- [ ] `total_keywords` in frontmatter matches the number of `##` headings
- [ ] Source-only blocks (untranslated) have not generated empty rendering rows
- [ ] File is sorted alphabetically by source-language keyword
