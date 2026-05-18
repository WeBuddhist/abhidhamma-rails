---
name: interlinear-gloss
description: For one root text + one translation, build an interlinear gloss file at 2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md. Each verse becomes a ```gloss``` block in the Obsidian Interlinear Glossing plugin format (\gla / \glc / \ex), pairing source tokens against token-by-token target glosses and the translator's free translation. Run once per translation. The output is what glossary-extract-raw reads to catalogue keyword renderings.
---

# interlinear-gloss

This skill creates the **interlinear gloss file** that pairs one root text against one translation, verse by verse. Each verse is rendered as a three-line `gloss` block:

- `\gla` — source-language tokens (Pali, in PTS Roman diacritics). Long compounds may be split into their component parts when that helps the alignment.
- `\glc` — token-by-token gloss in the target language, one entry per `\gla` token, lined up by position. **Every word used in `\glc` must come verbatim from the translator's `\ex` line — do not introduce new terminology or paraphrase.**
- `\ex` — the translator's free translation of the verse, verbatim from the translation file.

A gloss block is the **token-level alignment** that all downstream bilingual glossary work depends on. `glossary-extract-raw` reads these files to find keyword renderings; `local-wiki-article` cites them when documenting how a term is rendered across translations; `glossary-select` consults them when judging whether an attested rendering meets a track's requirements.

This skill is run **once per translation**. Four translations → four gloss files.

---

## Inputs

- **Root text** — `1-SOURCES/Text/<root-text>.md` (e.g. `pi-dhammasangani.md`).
- **Translation** — one file from `1-SOURCES/Translations/<translation>.md`. Must be block-aligned with the root text (same `^block-id` scheme).

## Output

One file at:

```
2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md
```

`<source-lang>` is the root text's `lang_tag` (`pi` for Dhammasaṅgaṇī).
`<target-lang-tag>` is the translation's `lang_tag` exactly (e.g. `en-rd` for the Rhys Davids translation, `en` for the modern English, `bn`, `sin`).

Examples:

| Translation | Output file |
|---|---|
| `en-dhammasangani-rd.md` (lang_tag `en-rd`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md` |
| `en-dhammasangani.md` (lang_tag `en`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-en-gloss.md` |
| `bn-dhammasangani.md` (lang_tag `bn`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-bn-gloss.md` |
| `sin-dhammasangani.md` (lang_tag `sin`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-sin-gloss.md` |

If the file already exists, update in place: keep manually filled `\glc` lines, and only refresh `\gla` and `\ex` from the underlying source files (so re-running this skill after the root text or translation is re-formatted does not lose token-gloss work).

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
\glc    <target gloss 1>   <target gloss 2>   <target gloss 3>   ...
\ex     <free translation, verbatim from the translation file>
`​`​`

## ^<next block-id>

`​`​`​gloss
...
`​`​`
```

One `##` heading per verse block, using the block ID with the caret. One `gloss` code block per `##` heading. Verse order matches root-text order.

---

## Format rules — Obsidian Interlinear Glossing plugin

The plugin (`Interlinear Glossing` by the Obsidian community) renders ```` ```gloss ```` blocks as aligned columns where every token on the `\gla` line lines up with the token at the same position on `\glc`. For the rendering to be correct:

1. **One token per column.** Splitting is by whitespace on the `\gla` line. The number of whitespace-separated tokens on `\glc` must match `\gla` exactly.
2. **Compounds may be split on `\gla`.** When a Pali compound is long enough that splitting it produces a cleaner alignment, write its parts as separate space-separated tokens on `\gla` (and add the corresponding gloss cells on `\glc`). For short or familiar compounds, keep them as a single token.
3. **Multi-word concepts are joined with hyphens, not spaces.** If "having paid homage" glosses a single Pali token, write it as `having-paid-homage` on `\glc` so it occupies one column.
4. **Empty cells use `--`.** If a `\glc` entry is genuinely blank (no corresponding word in `\ex`), write `--` so the column count stays consistent.
5. **No trailing punctuation on `\gla`.** Period, comma, semicolon, question mark — strip from the token. They re-appear in the `\ex` line via the translation.
6. **`\ex` is verbatim from the translator.** Do not paraphrase, do not normalise punctuation, do not strip footnote markers. This line is what `glossary-extract-raw` reads as the canonical rendering of the verse.
7. **`\glc` draws exclusively from `\ex`.** The token-level glosses on `\glc` must use only words that appear in the `\ex` line for the same block. Never introduce a synonym, paraphrase, or independently-coined translation on `\glc` — the point of the interlinear is to show how the translator's own words map to the source tokens, not to add a second layer of interpretation. If a source token's meaning is not expressible using words already present in `\ex`, use `--`.

---

## Procedure

The recommended path is the scaffold helper followed by an LLM pass for the `\glc` line.

1. **Run the scaffold script:**

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       1-SOURCES/Text/pi-dhammasangani.md \
       1-SOURCES/Translations/en-dhammasangani-rd.md \
       2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

   The script aligns blocks by `^block-id`, emits one `##` heading per paired block, and scaffolds each `gloss` block with `\gla` populated from the source tokens and `\ex` populated verbatim from the translation. The `\glc` line is scaffolded with `--` placeholders at the right column count.

2. **Spot-check the scaffold.** Confirm: every block in the source has a matching `##` heading; `\gla` tokens look clean (no stray punctuation); the `\ex` line matches the translation file's body. The frontmatter `total_verses` matches the heading count.

3. **Fill `\glc`, verse by verse or in batches.** This is the LLM-driven half. For each verse:
   - On `\glc`, write the token-by-token gloss in the target language. Each cell aligns with the `\gla` token at the same position. Use hyphens to bind multi-word concepts. **Every word used in `\glc` must be taken verbatim from the `\ex` line for that block — do not invent new translations, synonyms, or paraphrases. If a source token's meaning is not expressible using words already present in `\ex`, use `--`.**
   - Where a scaffold token on `\gla` is a long compound that would be clearer split, replace the single compound token with its space-separated parts and extend `\glc` with one cell per part.
   - Keep `--` only when a token genuinely has no gloss expressible from `\ex`.

4. **Verify column count.** Run the scaffold script with `--validate` to re-check that `\glc` has the same number of whitespace-separated tokens as `\gla` for every block:

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       --validate 2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

5. **Set `status: draft`.** A domain specialist marks the file `complete` after review.

---

## Re-running this skill

The scaffold script can be re-run safely:

- Existing `\glc` lines are preserved if their token count still matches `\gla` after the source text is re-read.
- If the source text was re-formatted (e.g. a verse was retokenised), the affected `\glc` lines are reset to `--` placeholders and the change is flagged in stderr so you can review.
- `\gla` and `\ex` are always refreshed from the underlying source files.

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
- [ ] `\gla`, `\glc`, `\ex` all present in every block
- [ ] Token count matches across `\gla` and `\glc` for every block (use `--validate`)
- [ ] `\ex` is verbatim from the translation file
- [ ] Frontmatter `total_verses` matches the heading count
- [ ] `--` placeholders remain only where a true gap exists, not as un-filled work
