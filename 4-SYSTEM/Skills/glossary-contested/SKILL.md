---
name: glossary-contested
description: Scan the consolidated bilingual glossary and identify terms with genuine rendering variation — terms where an explicit termbase decision is needed before zero-shot translation. Outputs a ranked shortlist sorted by contestedness score.
---

# glossary-contested

This skill reads the consolidated bilingual glossary produced by `glossary-combine` and surfaces the terms most likely to be rendered inconsistently by a zero-shot LLM translation. A term is contested when it has multiple attested renderings and no single rendering dominates strongly enough to be assumed safe. The output is the prioritised input to `glossary-select` for termbase curation.

Without this filter, `glossary-select` must work through hundreds of terms; most have one clear rendering and need no decision. This skill collapses the problem to the ~20–60 terms that actually matter.

---

## Inputs

- **Consolidated bilingual glossary** — `2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md` (output of `glossary-combine`). Must exist before this skill runs.

## Output

```
0-INBOX/<pair>-contested.md
```

e.g. `0-INBOX/pi-en-contested.md`

---

## Output file format

```markdown
---
source: 2-RAILS/Bilingual-Glossaries/pi-en.md
total_contested: <N>
---

# Contested terms — termbase candidates

Terms are ranked by variation score (1 − max_freq / total_freq).
A score of 0 means one rendering dominates; 1 means renderings are equally split.
These are the terms most likely to be rendered inconsistently in zero-shot translation.

| Term | Top rendering | Alternatives | Total | Score |
|------|---------------|--------------|-------|-------|
| āsava | taint (29) | canker (24), influx (14) | 67 | 0.57 |
| dhamma | phenomena (608) | states (374), factor (57) | ... | 0.40 |

---

## Term details

### āsava

**Variation score:** 0.57  **Total attestations:** 67  **Distinct renderings:** 3
**Local-Wiki:** [[āsava]]

| Rendering | Frequency | Share |
|-----------|-----------|-------|
| taint | 29 | 43% |
| canker | 24 | 36% |
| influx | 14 | 21% |
```

---

## Rules

1. **Never modify source files.** Reads only from `2-RAILS/Bilingual-Glossaries/`; writes only to `0-INBOX/`.
2. **Three thresholds must all be met** for a term to appear in the output: `min_total` (default 5) total attestations, `min_second` (default 2) attestations for the second-most-frequent rendering, and `min_variation` (default 0.15) variation score.
3. **Capitalisation-only variants are not separate renderings.** `glossary-combine` should have merged these; flag any that slipped through rather than counting them as genuine variation.
4. **Sense-split keywords are evaluated independently.** `dhamma (phenomenon)` and `dhamma (teaching)` are separate keywords — each is assessed on its own rendering table.
5. **The output is descriptive, not prescriptive.** It records observed variation; the choice of which rendering to standardise on is made by `glossary-select`.

---

## Procedure

### Step 1 — Confirm input

```bash
wc -l 2-RAILS/Bilingual-Glossaries/<pair>.md
```

Confirm the file exists and has content.

### Step 2 — Run the analysis script

```bash
python3 4-SYSTEM/Skills/glossary-contested/scripts/find_contested.py \
    2-RAILS/Bilingual-Glossaries/<pair>.md \
    0-INBOX/<pair>-contested.md
```

The script prints a summary:
```
Reading: 2-RAILS/Bilingual-Glossaries/pi-en.md
Keywords: 312
Contested: 47
Output: 0-INBOX/pi-en-contested.md
```

Optional flags:

| Flag | Default | Effect |
|------|---------|--------|
| `--min-total N` | 5 | Minimum total attestations |
| `--min-second N` | 2 | Minimum second-rendering count |
| `--min-variation F` | 0.15 | Minimum variation score |
| `--top N` | all | Only output top N terms |

### Step 3 — Review for noise

Scan the term details section. Flag any terms where the variation is artefactual:
- Capitalisation variants not caught by `glossary-combine` (fix upstream)
- Renderings that differ only by a trailing footnote marker or parenthetical gloss (merge upstream)
- Terms where one "rendering" is a phrase fragment from a mis-parsed block (discard)

### Step 4 — Move after review

```bash
cp 0-INBOX/<pair>-contested.md 2-RAILS/Bilingual-Glossaries/<pair>-contested.md
```

The `glossary-select` skill reads from `2-RAILS/Bilingual-Glossaries/<pair>-contested.md` as its prioritisation guide.

---

## Completion check

- [ ] Consolidated glossary confirmed present at `2-RAILS/Bilingual-Glossaries/<pair>.md`
- [ ] Script ran without errors and reported > 0 contested terms
- [ ] Output written to `0-INBOX/<pair>-contested.md`
- [ ] Term details section reviewed for artefactual variation
- [ ] Output moved to `2-RAILS/Bilingual-Glossaries/<pair>-contested.md` after review
