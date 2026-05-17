---
name: interlinear-gloss
description: For one root text + one translation, build an interlinear gloss file at 2-RAILS/Glossaries/Raw/<source>-<target>-gloss.md. Each verse becomes a ```gloss``` block in the Obsidian Interlinear Glossing plugin format (\gla / \glb / \glc / \t), pairing source tokens against their morphological analysis, token-by-token target glosses, and the translator's free translation. Run once per translation. The output is what glossary-extract-raw reads to catalogue keyword renderings.
---

# interlinear-gloss

This skill creates the **interlinear gloss file** that pairs one root text against one translation, verse by verse. Each verse is rendered as a four-line `gloss` block:

- `\gla` — source-language tokens (Pali, in PTS Roman diacritics).
- `\glb` — morphology / lemma analysis, one token per source token, hyphen-separated where the source has compounds.
- `\glc` — token-by-token gloss in the target language, one entry per source token, lined up by position.
- `\t` — the translator's free translation of the verse, verbatim from the translation file.

A gloss block is the **token-level alignment** that all downstream glossary work depends on. `glossary-extract-raw` reads these files to find keyword renderings; `local-wiki-article` cites them when documenting how a term is rendered across translations; `glossary-select` consults them when judging whether an attested rendering meets a track's requirements.

This skill is run **once per translation**. Four translations → four gloss files.

---

## Inputs

- **Root text** — `1-SOURCES/Text/<root-text>.md` (e.g. `pi-dhammasangani.md`).
- **Translation** — one file from `1-SOURCES/Translations/<translation>.md`. Must be block-aligned with the root text (same `^block-id` scheme).

## Output

One file at:

```
2-RAILS/Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md
```

`<source-lang>` is the root text's `lang_tag` (`pi` for Dhammasaṅgaṇī).
`<target-lang-tag>` is the translation's `lang_tag` exactly (e.g. `en-rd` for the Rhys Davids translation, `en` for the modern English, `bn`, `sin`).

Examples:

| Translation | Output file |
|---|---|
| `en-dhammasangani-rd.md` (lang_tag `en-rd`) | `2-RAILS/Glossaries/Raw/pi-en-rd-gloss.md` |
| `en-dhammasangani.md` (lang_tag `en`) | `2-RAILS/Glossaries/Raw/pi-en-gloss.md` |
| `bn-dhammasangani.md` (lang_tag `bn`) | `2-RAILS/Glossaries/Raw/pi-bn-gloss.md` |
| `sin-dhammasangani.md` (lang_tag `sin`) | `2-RAILS/Glossaries/Raw/pi-sin-gloss.md` |

If the file already exists, update in place: keep manually filled `\glb` and `\glc` lines, and only refresh `\gla` and `\t` from the underlying source files (so re-running this skill after the root text or translation is re-formatted does not lose token-gloss work).

---

## Output file format

```markdown
---
source_file: 1-SOURCES/Text/<root-text>.md
source_language: <pi>
target_file: 1-SOURCES/Translations/<translation>.md
target_language: <en | bn | sin | ...>
target_lang_tag: <en-rd | en | bn | sin | ...>
translator: <from the translation's frontmatter>
total_verses: <count of gloss blocks>
status: draft
---

# Interlinear gloss — <source-lang> → <target-lang> (<translator short name>)

## ^<block-id>

`​`​`​gloss
\gla    <source token 1>   <source token 2>   <source token 3>   ...
\glb    <lemma-1.morph>    <lemma-2.morph>    <lemma-3.morph>    ...
\glc    <target gloss 1>   <target gloss 2>   <target gloss 3>   ...
\t      <free translation, verbatim from the translation file>
`​`​`

## ^<next block-id>

`​`​`​gloss
...
`​`​`
```

One `##` heading per verse block, using the block ID with the caret. One `gloss` code block per `##` heading. Verse order matches root-text order.

---

## Format rules — Obsidian Interlinear Glossing plugin

The plugin (`Interlinear Glossing` by the Obsidian community) renders ```` ```gloss ```` blocks as aligned columns where every token on the `\gla` line lines up with the token at the same position on `\glb` and `\glc`. For the rendering to be correct:

1. **One token per column.** Splitting is by whitespace on the `\gla` line. The number of whitespace-separated tokens on `\glb` and `\glc` must match `\gla` exactly.
2. **Multi-word concepts are joined with hyphens, not spaces.** If "having paid homage" glosses a single Pali absolutive, write it as `having-paid-homage` on `\glc` so it occupies one column.
3. **Empty cells use `--`.** If a `\glb` or `\glc` entry is genuinely blank, write `--` so the column count stays consistent.
4. **Compound parts use `+` on `\glb`.** Sanskrit-style compound analysis: `sa+gaṇa` for *sagaṇa*. The `\glc` line glosses the whole compound, not its parts, unless the analysis on `\glb` splits it into separate columns.
5. **No trailing punctuation on `\gla`.** Period, comma, semicolon, question mark — strip from the token. They re-appear in the `\t` line via the translation.
6. **`\t` is verbatim from the translator.** Do not paraphrase, do not normalise punctuation, do not strip footnote markers. This line is what `glossary-extract-raw` reads as the canonical rendering of the verse.

---

## Procedure

The recommended path is the scaffold helper followed by an LLM pass for the `\glb` and `\glc` lines.

1. **Run the scaffold script:**

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       1-SOURCES/Text/pi-dhammasangani.md \
       1-SOURCES/Translations/en-dhammasangani-rd.md \
       2-RAILS/Glossaries/Raw/pi-en-rd-gloss.md
   ```

   The script aligns blocks by `^block-id`, emits one `##` heading per paired block, and scaffolds each `gloss` block with `\gla` populated from the source tokens and `\t` populated verbatim from the translation. The `\glb` and `\glc` lines are scaffolded with `--` placeholders at the right column count.

2. **Spot-check the scaffold.** Confirm: every block in the source has a matching `##` heading; `\gla` tokens look clean (no stray punctuation); the `\t` line matches the translation file's body. The frontmatter `total_verses` matches the heading count.

3. **Fill `\glb` and `\glc`, verse by verse or in batches.** This is the LLM-driven half. For each verse:
   - On `\glb`, write the lemma + morphology for each token, using compound markers `+` where compounds are present, and Leipzig-style POS/inflection markers where they help.
   - On `\glc`, write the token-by-token gloss in the target language. Each `\glc` cell aligns with the `\gla` token at the same position. Use hyphens to bind multi-word concepts.
   - Keep `--` only when a token genuinely has no analysis or no gloss (rare; usually one of the two lines has something).

4. **Verify column count.** Run the scaffold script with `--validate` to re-check that `\glb` and `\glc` have the same number of whitespace-separated tokens as `\gla` for every block:

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       --validate 2-RAILS/Glossaries/Raw/pi-en-rd-gloss.md
   ```

5. **Set `status: draft`.** A domain specialist marks the file `complete` after review.

---

## Re-running this skill

The scaffold script can be re-run safely:

- Existing `\glb` and `\glc` lines are preserved if their token count still matches `\gla` after the source text is re-read.
- If the source text was re-formatted (e.g. a verse was retokenised), the affected `\glb` and `\glc` lines are reset to `--` placeholders and the change is flagged in stderr so you can review.
- `\gla` and `\t` are always refreshed from the underlying source files.

---

## How downstream skills consume this file

- `glossary-extract-raw` walks every `gloss` block in this file, pairs `\gla` tokens against `\glc` cells, and records every distinct `(source-token, target-gloss)` rendering. Frequencies are counts of distinct verses where the rendering occurs.
- `glossary-combine` does not read this file directly — it works on the rendering tables that `glossary-extract-raw` produces.
- `local-wiki-article` may transclude individual gloss blocks (`![[pi-en-rd-gloss.md#^1-15]]`) when documenting how a term is rendered.
- `verse-context` may transclude a gloss block as part of the Commentary passages section for the verse, when token-level renderings clarify a reading.

---

## Completion check

- [ ] One `##` heading per source-text block, in source order
- [ ] One `gloss` code block per `##` heading
- [ ] `\gla`, `\glb`, `\glc`, `\t` all present in every block
- [ ] Token count matches across `\gla`, `\glb`, `\glc` for every block (use `--validate`)
- [ ] `\t` is verbatim from the translation file
- [ ] Frontmatter `total_verses` matches the heading count
- [ ] `--` placeholders remain only where a true gap exists, not as un-filled work
