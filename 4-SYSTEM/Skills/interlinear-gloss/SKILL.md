---
name: interlinear-gloss
description: For one root text + one translation, build a word-by-word gloss file at 2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md. Each verse consists of the translation followed by a ```gloss``` block containing a vertical list of Pāli-to-target word pairs. This format supports long compounds and bracketed semantic expansions.
---

# interlinear-gloss

This skill creates the **interlinear gloss file** that pairs one root text against one translation, verse by verse. Each verse is rendered with the verbatim translation followed by a vertical gloss block:

```markdown
<Translator's free translation, verbatim from the source>

`​`​`​gloss
<pali-token-1> <target-gloss-1>
<pali-token-2> <target-gloss-2>
...
`​`​`
```

- **Translation** — The translator's free translation of the verse, verbatim from the translation file.
- **Gloss Block** — A `gloss` code block containing one line per Pāli token.
- **Pāli Token** — The source-language word (Pali, in PTS Roman diacritics).
- **Target Gloss** — The word or phrase from the translation that corresponds to the Pāli token.

This vertical format allows for long, descriptive glosses and bracketed fallbacks (e.g., for the "neither" category in triads) without breaking horizontal alignment.

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

---

## Format rules

1. **One line per Pāli token.** The first word on the line is the Pāli token. The remainder of the line is the gloss.
2. **Translation is outside the block.** The free translation appears immediately above the `gloss` block.
3. **No trailing punctuation on Pāli tokens.** Period, comma, semicolon, question mark — strip from the token.
4. **Gloss draws primarily from the translation.** Every gloss should use words that appear verbatim in the translation line above.
5. **Bracketed fallbacks for untranslated terms.** If a Pāli token is not translated in the free translation, use the Rhys Davids (`en-rd`) rendering in square brackets: `[good]`.
6. **Expansion of summary terms (The "Neither" Rule).** In triads (e.g., wholesome / unwholesome / neither), the third category is often translated as "neither". The gloss for the corresponding Pāli word (e.g., `anupādiṇṇaanupādāniyā`) should include the summary word and the bracketed expansion of the categories it negates.
   - *Example:* `anupādiṇṇaanupādāniyā neither [grasped-at-favourable-to-grasping not-grasped-at-favourable-to-grasping]`
7. **Hyphens for joined concepts.** Use hyphens to join words in the gloss if they form a single unit of meaning, but spaces are permitted in the vertical format if they improve readability within the gloss part of the line.

---

## Procedure

1. **Run the scaffold script:**

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       1-SOURCES/Text/pi-dhammasangani.md \
       1-SOURCES/Translations/en-dhammasangani-rd.md \
       2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

   The script aligns blocks by `^block-id`, emits one `##` heading per paired block, and scaffolds each verse with the translation and a `gloss` block containing Pāli tokens and `--` placeholders.

2. **Fill the glosses.** For each Pāli token, identify its rendering in the translation line.
   - Apply the **Neither Rule** for summary terms in triads.
   - Use bracketed fallbacks from Rhys Davids for untranslated particles or technical terms.

3. **Verify.** Ensure every Pāli token in the source text has a corresponding line in the `gloss` block.

---

## Re-running this skill

The scaffold script preserves manually filled gloss lines if the Pāli token still matches. If the source text is updated and a token is removed or changed, the script will flag the block for re-review.

---

## Completion check

- [ ] One `##` heading per source-text block, in source order.
- [ ] Translation text appears verbatim above the `gloss` block.
- [ ] One `gloss` code block per verse, containing a vertical list of `token gloss` pairs.
- [ ] The "Neither" rule is applied to summary terms in triads.
- [ ] No Pāli token contains trailing punctuation.
- [ ] Frontmatter `total_verses` is correct.
