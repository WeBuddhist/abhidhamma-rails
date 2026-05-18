---
name: glossary-extract-raw
description: Extract every source-language keyword and the rendering(s) it receives from one (root-text, translation) pair into a raw per-source bilingual glossary at 2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>.md. Reads the interlinear gloss file produced by interlinear-gloss (token-level \gla ↔ \glb alignment already done) and catalogues attested renderings keyword by keyword.
---

# glossary-extract-raw

This skill turns one **interlinear gloss file** in `2-RAILS/Bilingual-Glossaries/Raw/` into a **raw bilingual glossary** — a per-source record of every keyword in the original language and every distinct rendering it receives in this translation. The raw bilingual glossaries are the input for `glossary-combine`.

The gloss file is the primary input. It must exist before this skill runs. Run `interlinear-gloss` first to produce it.

The skill has two passes:

1. **Token-pair extraction** (helper script) — walk every ```` ```gloss ```` block in the gloss file, pair each `\gla` token with the `\glb` token at the same column position, and tally distinct (source-token, target-rendering) pairs across verses.
2. **Sense disambiguation and curation** (LLM) — group the raw tallies by source lemma, merge inflectional variants, separate clearly distinct senses, pick sample pairings, and write the final raw bilingual glossary.

---

## Inputs

- **Interlinear gloss file** — `2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md`. Produced by the `interlinear-gloss` skill. Must validate clean (run `scaffold_gloss.py --validate` first).
- **Keyword list (optional)** — if a controlled keyword list exists (extracted from the mātikā, or pulled from existing Local-Wiki articles), pass it in to constrain extraction. If omitted, extract every source token that recurs at least three times across the gloss file.

## Output

One file at:

```
2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>.md
```

The filename mirrors the gloss file but without the `-gloss` suffix. For example, `pi-en-rd-gloss.md` → `pi-en-rd.md`. Both files live side by side under `Bilingual-Glossaries/Raw/`.

---

## Output file format

```markdown
---
gloss_file: 2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md
source_file: 1-SOURCES/Text/<root-text>.md
target_file: 1-SOURCES/Translations/<translation>.md
source_language: <pi | sa | bo | zh>
target_language: <en | bn | sin | ...>
language_pair: <pi-en | pi-bn | ...>
target_lang_tag: <en-rd | en | bn | sin | ...>
translator: <name from translation frontmatter, if present>
total_keywords: <count>
status: draft
---

# Raw bilingual glossary — <translator / translation short name>

## <source-lang keyword>

**Renderings attested in this source:**

| Rendering | Frequency | First seen | Notes |
|-----------|-----------|------------|-------|
| <target-language rendering> | <n> | ^<block-id> | <inflection / context note> |
| <alternative rendering> | <n> | ^<block-id> | <when this rendering is used> |

**Sample pairings:**

> **^<block-id>** — *<source snippet containing the keyword>*
> → "<corresponding target rendering>"

---

## <next keyword>

...
```

One `##` heading per keyword. Keywords are sorted alphabetically (by source-language form). Diacritics are preserved.

The output schema is **unchanged** from earlier versions of this skill — what changed is the input: the source/target alignment is no longer extracted from the block level (whole-paragraph pairs) but from the token level (one `\gla` token paired with one `\glb` cell), giving cleaner and finer-grained rendering data.

---

## Rules

1. **One raw bilingual glossary per gloss file.** A `pi-en-rd-gloss.md` becomes `pi-en-rd.md`. Never merge two translations into one raw file — that's what `glossary-combine` is for.
2. **Tokens come from `\gla`; renderings come from `\glb`.** The free translation on `\ex` is not used for rendering extraction (it's full-sentence English; `\glb` is the per-token gloss).
3. **Inflectional variants are merged.** *dhammā*, *dhammānaṃ*, *dhammehi* all map to lemma *dhamma*. Normalise manually during the curation pass.
4. **Distinct renderings stay distinct.** `states` and `mental-states` are two renderings of the same keyword, not one. They each get a row with their own frequency.
5. **Sample pairings show context.** Two to four pairings per keyword, chosen to cover the range of renderings and inflectional contexts. Quote the source token in context (a few words on each side) and the rendering verbatim.
6. **No interpretive judgments.** This file is descriptive: what the translation actually does. Whether a rendering is good belongs in `glossary-select`, not here.

---

## Procedure

1. **Validate the gloss file.** Run:

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       --validate 2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

   The gloss file must validate clean — every `\glb` line has the same token count as its `\gla` line.

2. **Run the token-pair extractor:**

   ```bash
   python3 4-SYSTEM/Skills/glossary-extract-raw/scripts/extract_pairs.py \
       2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md \
       0-INBOX/temp/pi-en-rd-pairs.csv
   ```

   The script reads every `gloss` block, pairs `\gla[i]` with `\glb[i]` for each column `i`, and emits a CSV with columns: `source_token, source_lemma, target_rendering, block_id, frequency_within_block`.

3. **Tally by lemma.** Open the CSV and group rows by `source_lemma`. For each lemma, count how many distinct blocks contain each `target_rendering`. Discard rows where the rendering is `--` (unfilled placeholder).

4. **Filter to keywords.** Keep lemmas that recur at least three times. Discard function words and inflectional particles unless they carry interpretive weight (e.g. *iti*). If a controlled keyword list was supplied, intersect with it.

5. **Pick sample pairings.** For each retained lemma, pick two to four blocks that illustrate the range of renderings. The CSV contains the block IDs; cross-reference the gloss file to extract the surrounding tokens for the snippet.

6. **Write the raw bilingual glossary file** to `2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>.md` with the frontmatter populated. Sort `##` headings alphabetically.

7. **Set `status: draft`.** A domain specialist marks the file `complete` after spot-checking.

---

## Helper scripts

- **`scripts/extract_pairs.py`** — walks one gloss file and emits a CSV of `(source_token, source_lemma, target_rendering, block_id)` rows.
- **`scripts/align_blocks.py`** — legacy fallback for cases where no gloss file exists (e.g. for sources where token-level glossing was skipped). Pairs root-text and translation by block ID into a CSV. Use this only if the gloss workflow is not yet available for the language pair in question; the gloss-based extraction is otherwise the canonical input.

---

## Completion check

- [ ] Every keyword appears as its own `##` heading
- [ ] Every keyword has at least one rendering row and one sample pairing
- [ ] Sample pairings show the block ID and quote both source token (in context) and target rendering
- [ ] Frequencies count distinct blocks, not raw token-pair occurrences
- [ ] `total_keywords` in frontmatter matches the number of `##` headings
- [ ] `--` placeholder renderings have not generated rows
- [ ] File is sorted alphabetically by source-language keyword
- [ ] `gloss_file` frontmatter field points at the gloss file that was the input
