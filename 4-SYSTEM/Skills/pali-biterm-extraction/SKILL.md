---
name: pali-biterm-extraction
description: For a block-aligned Pāli source file and an English translation file, extract English keywords and their Pāli equivalents, producing frequency-weighted bilingual tables keyed by English. Two modes — full YAML (for glossary-combine pipeline) or focused Markdown per term (two files: en-to-pali primary and pali-to-en reverse index), which Claude then groups into semantic clusters.
---

# pali-biterm-extraction

Produces bilingual frequency tables from block-aligned Pāli/English markdown files, keyed by **English keyword → Pāli equivalents**.

**Two output modes:**

- **YAML mode** (default): flat `english_keyword: pāli_token-N, …` table for the `glossary-combine` pipeline.
- **Markdown mode** (`--format md --focus TERM`): two Markdown files — primary (`en-to-pali`) lists each English keyword with its Pāli equivalents; secondary (`pali-to-en`) is the reverse index — which Claude then post-processes into semantic clusters for human review.

The algorithm runs in two passes:

1. **TF-IDF keyword extraction (English), with n-gram phrase detection.** Compound translation terms (2–4 words, e.g. "right view", "initial application") are detected and treated as single tokens. A phrase qualifies when: all components have high IDF; it appears in ≥ 3 blocks; it appears in this word order ≥ 4× more often than reversed; and it accounts for ≥ 30 % of the rarest component's occurrences.

2. **Weighted sub-block co-occurrence (Pāli).** Each aligned block is split on `(Ka)/(Kha)/(Ga)` markers before alignment so triad entries match at the line level. For each English keyword (unigram or phrase), weighted Pāli co-occurrence is accumulated (weight = 1 / |unique Pāli tokens in that sub-block|). Pāli tokens appearing in more than `--max-pi-df` of all pairs are suppressed.

**No Pāli stemming.** Exact token forms are preserved. Morphological merging is done by the human contributor during semantic grouping.

---

## Inputs

| Input | Description | Path pattern |
|---|---|---|
| Source file | Pāli root-text markdown with Obsidian block IDs | `1-SOURCES/Text/<lang-tag>-<text>.md` |
| Target file | English translation markdown with matching block IDs | `3-TRANSFORMATIONS/Translations/<track>/<lang-tag>-<text>-<translator>.md` |
| Output path | Base path for Markdown mode; `.yaml` path for YAML mode | `0-INBOX/<term>` or `0-INBOX/<name>.yaml` |
| Focus term *(Markdown mode)* | Pāli root form to focus on (e.g. `āsava`, `dhamma`) | — |

---

## Output — Markdown mode

The script writes two **flat draft** files (one section per English keyword). Claude then applies semantic grouping in Step 3.

### `0-INBOX/{term}-en-to-pali.md` — primary file, final grouped format

```markdown
# {term} — English keywords with Pāli equivalents

## 1. {english-keyword} — {Sense label}
pali:
  pali-form1: N
  pali-form2: N

## 2. {english-phrase} — {Sense label}
pali:
  pali-form1: N
```

### `0-INBOX/{term}-pali-to-en.md` — reverse index, final grouped format

```markdown
# {term} — Pāli tokens with English keywords

## 1. {pali-form} — {Sense label}
english-keyword1: N
english-keyword2: N

## 2. {pali-form2} — {Sense label}
english-keyword1: N
```

---

## Output — YAML mode

One YAML file with compact lines:

```yaml
# English keyword → Pāli equivalents (frequency-weighted)
right concentration: sammāsamādhi-28
right mindfulness: sammāsati-21
initial application: vitakko-27
unconditioned: asaṅkhatā-83
```

---

## Rules

1. **Never modify source files.** Reads `1-SOURCES/` and `3-TRANSFORMATIONS/`; writes only to the output path.
2. **Run from the vault root.** All paths in the command are relative to the vault root.
3. **Both files must have matching block IDs.** If the aligned count is zero, stop and report the mismatch.
4. **Output goes to `0-INBOX/` first.** Move to `2-RAILS/Bilingual-Glossaries/Raw/` only after human review.
5. **This skill is descriptive, not prescriptive.** It records what the translation *did*; prescriptive choices belong in `termbase.md`.
6. **Inflected forms are separate keys.** Merge only during the semantic grouping step (Step 3) or in `glossary-combine`.

---

## Procedure — Markdown mode (focused on a root term)

### Step 1 — Confirm inputs

```bash
grep -c '\^' 1-SOURCES/Text/pi-dhammasangani.md
grep -c '\^' 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md
```

Both counts must match (or be very close).

### Step 2 — Run focused extraction

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    <pali_file> \
    <en_file> \
    0-INBOX/<term> \
    --focus <term> \
    --format md
```

Example for āsava:

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    1-SOURCES/Text/pi-dhammasangani.md \
    3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md \
    0-INBOX/āsava \
    --focus āsava \
    --format md
```

In Markdown mode, `--max-pi-per-kw` defaults to 20 (captures the full morphological family) and `--max-pi-df` defaults to 0.99 (retains even high-frequency focus terms). Override with explicit flags if needed.

The script produces flat drafts — one section per English keyword — plus a progress summary:

```
source : …
target : …
focus  : āsava
format : md
blocks : N src / N tgt
aligned: N block pairs
Pass 1 : TF-IDF keyword extraction …
         N keywords selected
Building sub-block pairs …
Pass 2 : weighted co-occurrence …
terms  : N Pali tokens in output
output : 0-INBOX/āsava-en-to-pali.md
         0-INBOX/āsava-pali-to-en.md
focus  : N English keywords matched — [taint, canker, influx, ...]
```

### Step 3 — Apply semantic grouping (Claude step)

Read both flat draft files from `0-INBOX/`. Then:

1. **Identify semantic clusters** among the English keywords:
   - Keywords whose Pāli equivalents overlap → typically one cluster (same semantic field)
   - Keywords that map to distinct Pāli families → separate clusters
   - The same English word covering different Pāli forms in different senses → flag for disambiguation

2. **Write a sense label** for each cluster, e.g.:
   - `taint / canker / influx — āsava family (active defilements)`
   - `tainted — sāsava family (subject to taints)`
   - `untainted — anāsava family (free from taints)`

3. **Aggregate Pāli counts** across synonymous English keywords in the cluster (sum raw co-occurrence counts per Pāli token).

4. **Rewrite both files** in the final grouped format shown above, replacing the flat draft. Sort clusters by total count descending; sort Pāli tokens within each cluster by count descending.

### Step 4 — Spot-check the output

Verify the expected English keywords appear and map to plausible Pāli equivalents:

| Expected English keyword | Expected top Pāli equivalent(s) |
|---|---|
| taint / canker / influx | āsava, kāmāsava, bhavāsava |
| phenomena / states | dhamma, dhammā |
| wholesome | kusalā, kusalaṃ |
| contact | phasso |
| feeling | vedanā |
| perception | saññā |
| volition | cetanā |
| initial application | vitakko |
| sustained application | vicāro |
| jhāna | jhānaṃ, jhānā |

### Step 5 — Move after human review

```bash
cp 0-INBOX/<term>-pali-to-en.md 2-RAILS/Bilingual-Glossaries/Raw/<term>-pali-to-en.md
cp 0-INBOX/<term>-en-to-pali.md 2-RAILS/Bilingual-Glossaries/Raw/<term>-en-to-pali.md
```

---

## Procedure — YAML mode (full extraction for glossary-combine)

### Step 1 — Confirm inputs

Same as above.

### Step 2 — Run full extraction

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    <pali_file> \
    <en_file> \
    0-INBOX/pi-en-biterm.yaml
```

Optional flags:

| Flag | Default | Effect |
|---|---|---|
| `--top N` | 600 | English keywords to consider |
| `--min-co N` | 2 | Minimum raw co-occurrence count |
| `--min-score F` | 0.25 | Minimum weighted alignment score |
| `--max-pi-df F` | 0.30 | Max Pāli doc-freq fraction |
| `--max-pi-per-kw N` | 2 | Max Pāli tokens linked to one English keyword |
| `--max-phrase N` | 4 | Maximum phrase length in words |

### Step 3 — Spot-check and move

Same key terms table as above. Move to `2-RAILS/Bilingual-Glossaries/Raw/` after review.

---

## Completion check

- [ ] Both source and target files confirmed present with matching block IDs
- [ ] Script ran without errors and reported > 0 aligned block pairs
- [ ] Output written to `0-INBOX/`
- [ ] *(Markdown mode)* Flat draft post-processed into semantic clusters with sense labels
- [ ] *(Markdown mode)* `focus: N English keywords matched` line in script output lists expected translation terms
- [ ] Key terms spot-checked against expected renderings table
- [ ] Output moved from `0-INBOX/` to `2-RAILS/Bilingual-Glossaries/Raw/` after human review
