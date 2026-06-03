---
name: pali-keyword-extraction
description: Extract domain-specific English keywords from a translation file using TF-IDF against the Google-10k Zipf IDF table. Produces a ranked keyword list (unigrams and compound phrases) for use in pali-biterm-extraction or independent review.
---

# pali-keyword-extraction

Runs **Pass 1 only** of the bilingual extraction pipeline: TF-IDF keyword selection on an English translation file, with n-gram compound phrase detection.

Use this skill when you want the keyword list independently — for tuning, debugging, or feeding into a separate co-occurrence step.

---

## Inputs

| Input | Description | Path pattern |
|---|---|---|
| Target file | English translation markdown with block IDs | `3-TRANSFORMATIONS/Translations/<track>/<lang-tag>-<text>-<translator>.md` |
| Output path | Path for the keyword list | `0-INBOX/<name>-keywords.md` |

---

## Output

A ranked Markdown file — one keyword per line with its TF-IDF score — sorted descending:

```
# English keywords — <source filename>
# Method: block-level TF-IDF × Google-10k Zipf IDF; compound phrases via n-gram detection
# N blocks, K keywords selected

phenomena: 8.24
wholesome: 7.91
right concentration: 7.55
initial application: 7.43
contact: 6.88
feeling: 6.71
perception: 6.62
volition: 6.54
sustained application: 6.40
jhāna: 6.31
```

---

## Procedure

### Step 1 — Run keyword extraction

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    <en_file> \
    0-INBOX/<name>-keywords.md \
    --keywords-only
```

Example:

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md \
    0-INBOX/dhammasangani-keywords.md \
    --keywords-only
```

Optional flags:

| Flag | Default | Effect |
|---|---|---|
| `--top N` | 600 | Maximum keywords to output |
| `--max-phrase N` | 4 | Maximum phrase length in words |

### Step 2 — Review

Open the output file and check that:
- Core Abhidhamma terms appear near the top (e.g. `phenomena`, `wholesome`, `right concentration`)
- Compound phrases are correctly detected (e.g. `initial application`, `right mindfulness`)
- Common English words with low IDF are absent

---

## Completion check

- [ ] Script ran without errors
- [ ] Output written to `0-INBOX/`
- [ ] Core domain terms appear in top 20
- [ ] Compound phrases detected for major multi-word terms
