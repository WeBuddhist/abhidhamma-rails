---
name: pali-biterm-extraction
description: For a block-aligned Pāli source file and an English translation file, extract every attested English rendering for each Pāli token and write a compact YAML frequency table (pāli_token: rendering1-N, rendering2-N, …). No Pāli stemming is applied — exact token forms are used throughout.
---

# pali-biterm-extraction

Produces a compact YAML bilingual frequency table from any pair of block-aligned
Pāli and English markdown files.  Intended as input for the `glossary-combine`
skill and as a fast sanity-check on translation consistency before full
interlinear glossing.

The algorithm runs in two passes:

1. **TF-IDF keyword extraction (English), with n-gram phrase detection.**
   Before scoring, the script scans the English blocks for compound translation
   terms of 2–4 words (e.g. "right view", "initial application",
   "right concentration").  A candidate phrase qualifies when: all component
   words have high IDF (domain terms, not common English); the phrase appears
   in at least 3 blocks; it appears in this word order at least 4× more often
   than reversed (filtering accidental list adjacency like "states wholesome"
   vs "wholesome states"); and the phrase accounts for ≥ 30 % of the rarest
   component word's occurrences (filtering synonym-list co-occurrences like
   "nondelusion investigation" where each word appears in many other contexts).
   Qualified phrases are treated as single tokens using greedy longest-match
   so the Pāli alignment maps to the full phrase.

2. **Weighted sub-block co-occurrence (Pāli).** Each aligned block is split on
   `(Ka)/(Kha)/(Ga)` section markers before alignment so that triad entries
   like `kusalā dhammā ↔ Wholesome states` are matched at the *line* level
   rather than the block level.  For each English keyword (unigram or phrase)
   the weighted Pāli co-occurrence is accumulated (weight = 1 / |unique Pāli
   tokens in that sub-block|, so short mātikā entries outweigh long prose
   paragraphs).  Pāli tokens appearing in more than 30 % of all aligned pairs
   are suppressed as high-frequency function words.

**No Pāli stemming.**  Exact token forms are preserved.  This avoids the
mis-grouping caused by algorithmic suffix-stripping on Pāli, at the cost of
having multiple inflected forms as separate keys (e.g. `kusalā`, `kusalaṃ`,
`kusalehi`).  The human contributor merges forms during the `glossary-combine`
step.

---

## Inputs

| Input | Description | Path pattern |
|---|---|---|
| Source file | Pāli root-text markdown with Obsidian block IDs | `1-SOURCES/Text/<lang-tag>-<text>.md` |
| Target file | English translation markdown with matching block IDs | `3-TRANSFORMATIONS/Translations/<track>/<lang-tag>-<text>-<translator>.md` |
| Output path | Where to write the YAML result | `0-INBOX/<src>-<tgt>-biterm.yaml` |

## Output

```
<output_path>.yaml
```

One YAML file with compact lines:

```yaml
# Translation variant frequencies
# Method: English TF-IDF (Google-10k Zipf IDF) + weighted sub-block co-occurrence
# Pāli: exact token forms, no stemming; compound phrases merged (n-gram)
# source: 1-SOURCES/Text/pi-1.md
# target: 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md

sammāsamādhi: right concentration-28
sammāsati: right mindfulness-21
sammāsaṅkappo: right intention-16
sammāvāyāmo: right effort-21, energy faculty-21
sammādiṭṭhi: right view-29, wisdom understanding-21
vitakko: initial application-27
vicāro: sustained application-29
cetanā: volition-11
asaṅkhatā: unconditioned-83
```

- `pāli_token` — exact token form from the source text (lowercased), no stemming.
- `rendering-N` — English domain keyword with raw co-occurrence count, descending.

---

## Rules

1. **Never modify source files.**  Reads `1-SOURCES/` and `3-TRANSFORMATIONS/`; writes only to the output path.
2. **Run from the vault root.**  All paths in the command are relative to the vault root.
3. **Both files must have matching block IDs.**  If the aligned count is zero, stop and report the mismatch.
4. **Output goes to `0-INBOX/` first.**  Move to `2-RAILS/Bilingual-Glossaries/Raw/` only after human review.
5. **This skill is descriptive, not prescriptive.**  It records what the translation *did*; prescriptive choices belong in `termbase.md`.
6. **Inflected forms are separate keys.**  Do not attempt to merge `kusalā` / `kusalaṃ` / `kusalehi` — leave that for `glossary-combine`.

---

## Procedure

### Step 1 — Confirm inputs

```bash
grep -c '\\^' 1-SOURCES/Text/pi-1.md
grep -c '\\^' 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md
```

Both counts must match (or be very close).

### Step 2 — Run the extraction script

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \\
    <source_file> \\
    <target_file> \\
    <output_yaml>
```

Example for the Dhammasaṅgaṇī AI translation:

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \\
    1-SOURCES/Text/pi-1.md \\
    3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md \\
    0-INBOX/pi-en-ai-biterm.yaml
```

The script prints a summary:

```
source : … (N blocks)
target : … (N blocks)
aligned: N block pairs
Pass 1 : TF-IDF keyword extraction …
         N keywords selected
         top 10: […]
Building sub-block pairs …
         N sub-block pairs
Pass 2 : weighted co-occurrence …
terms  : N Pāli tokens in output
output : …
```

Optional flags (run `--help` for full list):

| Flag | Default | Effect |
|---|---|---|
| `--top N` | 600 | English keywords to consider |
| `--min-co N` | 2 | Minimum raw co-occurrence count |
| `--min-score F` | 0.25 | Minimum weighted alignment score |
| `--max-pi-df F` | 0.30 | Max Pāli doc-freq fraction (suppresses ubiquitous tokens) |
| `--max-pi-per-kw N` | 2 | Max Pāli tokens linked to one English keyword |
| `--max-phrase N` | 4 | Maximum phrase length in words |

### Step 3 — Spot-check the output

Open the YAML and verify key terms appear with expected renderings:

| Pāli term | Expected top rendering(s) |
|---|---|
| `phasso` | contact |
| `vedanā` / `vedanākkhandho` | feeling |
| `saññā` / `saññākkhandho` | perception |
| `cetanā` | volition |
| `vitakko` | initial application |
| `vicāro` | sustained application |
| `sammādiṭṭhi` | right view |
| `sammāsamādhi` | right concentration |
| `sammāsati` | right mindfulness |
| `sammāvāyāmo` | right effort |
| `sammāsaṅkappo` | right intention |
| `asaṅkhatā` | unconditioned |
| `jhānaṃ` | jhāna |
| `kusalā` / `kusalaṃ` | wholesome |

Common noise patterns to note (not errors):
- A term that closes every long enumeration paragraph will co-occur with many English terms; its top rendering is still correct.
- Inflected forms of the same root appear as separate keys — merge in `glossary-combine`.
- The phrase detector may produce some spurious multi-word entries from the `…pe…` abbreviation pattern used in highly repetitive definition blocks. These are easily identified by their unusual appearance (e.g. "arisespenondistraction") and should be discarded during review.

### Step 4 — Move to final location (after human review)

```bash
cp 0-INBOX/pi-en-ai-biterm.yaml \\
   2-RAILS/Bilingual-Glossaries/Raw/pi-en-ai-biterm.yaml
```

---

## Completion check

- [ ] Both source and target files confirmed present with matching block IDs
- [ ] Script ran without errors and reported > 0 aligned block pairs
- [ ] Output YAML written to `0-INBOX/`
- [ ] Key terms spot-checked against expected renderings table above
- [ ] Obvious noise noted for the human contributor
- [ ] Output moved from `0-INBOX/` to `2-RAILS/Bilingual-Glossaries/Raw/` only after human review
