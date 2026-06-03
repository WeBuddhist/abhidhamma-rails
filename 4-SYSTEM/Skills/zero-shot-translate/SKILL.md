---
name: zero-shot-translate
description: Translate a batch of Pāli source blocks to the target language using the track's bilingual glossary as a hard constraint for contested terms. Produces a translation file with matching Obsidian block IDs.
---

# zero-shot-translate

This skill translates Pāli source text block-by-block, using the per-track bilingual glossary (output of `glossary-select`) as a hard constraint: every term that appears in the glossary must be rendered with its chosen rendering, not whatever the LLM would choose unprompted. Terms not in the glossary are translated freely.

The key design principle is a **minimal, high-signal termbase**: the glossary passed to the LLM contains only the ~20–60 contested terms identified by `glossary-contested`, not every term in the vocabulary. A bloated termbase creates noise and contradictions; a focused one enforces consistency where it matters.

Processes text in batches of 30–50 blocks to stay within context limits. Each output block carries the same `^block-id` as its source.

---

## Inputs

- **Track folder** — `3-TRANSFORMATIONS/Translation/<track-name>/`. Must contain:
  - `bilingual glossary.md` — per-track glossary (output of `glossary-select`)
  - `requirements.md` — translation style requirements
- **Source file** — Pāli root text with Obsidian block IDs, e.g. `1-SOURCES/Text/pi-dhammasangani.md`
- **Block range** — which blocks to translate. Accepts: `all`, a single block ID, or a range like `1-0 to 1-100`
- **Output path** — where to write the translation, e.g. `3-TRANSFORMATIONS/Translations/<track-name>/en-dhammasangani-<track-name>.md`

## Output

```
3-TRANSFORMATIONS/Translations/<track-name>/<lang-tag>-<text-name>-<track-name>.md
```

---

## Output file format

```markdown
---
track: <track-name>
source: 1-SOURCES/Text/<pi-text>.md
target_language: <en | bn | sin | ...>
glossary: 3-TRANSFORMATIONS/Translation/<track-name>/bilingual glossary.md
blocks_translated: <N>
last_updated: <ISO date>
status: draft
---

# <Text title> — <track-name> translation

<translated text for block 1> ^<block-id>

<translated text for block 2> ^<block-id>
```

Each paragraph ends with the same `^block-id` as the corresponding Pāli source block. This preserves alignment with the source for downstream bilingual tools (`pali-biterm-extraction`, `interlinear-gloss`).

---

## Rules

1. **Termbase renderings are hard constraints.** If a Pāli token in the source appears as a keyword in the bilingual glossary, its English rendering in the output must match the glossary's chosen rendering exactly — no synonyms, no paraphrases.
2. **Block IDs must be preserved.** Every output block carries the same `^block-id` as its source block. Missing or mismatched IDs break all downstream alignment tools.
3. **Translate in batches of 30–50 blocks.** Larger batches risk exceeding context limits and cause the LLM to drift from the termbase constraints.
4. **Never translate more blocks than exist.** If the requested range includes block IDs not present in the source file, stop and report the missing IDs rather than skipping them silently.
5. **The glossary injected into the prompt must be filtered to terms actually present in the batch.** Injecting the full glossary for every batch adds noise; scan each batch's Pāli tokens against the glossary and include only the relevant entries.
6. **Mark output `status: draft`.** A human or QA skill reviews before promotion.
7. **Never modify source files.** Reads from `1-SOURCES/` and `3-TRANSFORMATIONS/Translation/<track>/`; writes only to `3-TRANSFORMATIONS/Translations/<track>/`.

---

## Procedure

### Step 1 — Load inputs

1. Read `3-TRANSFORMATIONS/Translation/<track>/bilingual glossary.md`. Extract the table: build a dict `{pali_token: (rendering, rationale)}` for every row.
2. Read `3-TRANSFORMATIONS/Translation/<track>/requirements.md`. Note: target register, style constraints, script, any explicit prohibitions.
3. Parse the source file blocks (same parser as `pali-biterm-extraction`): collect `{block_id: pali_text}` for all blocks in the requested range.

### Step 2 — Build the termbase index

For efficient per-batch filtering, build a lookup from plain-ASCII Pāli root forms to glossary entries. A source block "matches" a glossary entry when the plain-ASCII form of any Pāli token in the block is a substring of the plain-ASCII glossary keyword (or vice-versa, for inflected forms).

### Step 3 — Translate in batches

For each batch of 30–50 blocks:

1. **Filter the termbase** to entries relevant to this batch (Step 2 lookup).
2. **Construct the prompt:**

```
You are translating Pāli Buddhist text into <target language>.

TERMBASE — render these Pāli terms exactly as shown, without substitution:
<pali_token_1> → <rendering_1>  [<rationale>]
<pali_token_2> → <rendering_2>  [<rationale>]
...

REQUIREMENTS:
<paste relevant clauses from requirements.md>

INSTRUCTIONS:
- Translate each numbered verse below from Pāli to <target language>.
- Preserve the verse numbers exactly.
- Apply the termbase renderings wherever those Pāli forms appear.
- Do not transliterate Pāli terms unless the termbase says to.
- Keep translations concise and faithful to the source.

VERSES:
[1] <pali_text_1>
[2] <pali_text_2>
...
```

3. **Parse the response.** Match each `[N]` label to its source block ID. If any block is missing from the response, flag it and retry that block individually.
4. **Append to the output file** with `^block-id` suffixes.

### Step 4 — Post-batch checks

After each batch:
- Confirm every source block ID has a corresponding output block.
- Spot-check 2–3 blocks for termbase compliance: search the output for the Pāli tokens from the glossary and confirm the correct rendering was used.
- If a termbase violation is found, re-run the batch with a stricter prompt (add the violation as a negative example).

### Step 5 — Finalise output file

After all batches are complete:
1. Write the YAML frontmatter (`blocks_translated`, `last_updated`, `status: draft`).
2. Confirm block count matches the requested range.

---

## Completion check

- [ ] `bilingual glossary.md` and `requirements.md` confirmed present in track folder
- [ ] All source blocks in the requested range parsed successfully
- [ ] Every output block has a `^block-id` matching its source
- [ ] Spot-check confirms termbase renderings applied correctly
- [ ] Output written to `3-TRANSFORMATIONS/Translations/<track>/`
- [ ] `status: draft` in frontmatter
- [ ] No source files modified
