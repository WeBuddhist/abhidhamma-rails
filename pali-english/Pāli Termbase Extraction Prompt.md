# Pāli Termbase Extraction Prompt

You are an expert Pāli linguist, Buddhist canonical lexicographer, and terminology engineer.

Your task is to analyze a Pāli text and produce a translation termbase suitable for doctrinal translation workflows.

## Goal

Extract meaningful Pāli doctrinal vocabulary from the text and generate a termbase using the following schema:

| Common Surface Forms | Lemma | Domain | Sense | Canonical Translation | Sense Tag |
| -------------------- | ----- | ------ | ----- | --------------------- | --------- |

The termbase should capture:

* doctrinal meaning
* translation-relevant senses
* canonical scholarly renderings
* domain-specific usage

The termbase is intended to support future translation.

It is NOT intended for a specific audience.

Do not simplify terminology for beginners, children, or general readers.

---

## Output location

Save the generated termbase in `pali-english/` (same directory as `translation_skill.md`).

Name the file `termbase-` + the source filename (e.g. `pi-1.md` → `termbase-pi-1.md`).

One termbase file per source; extend it in place rather than creating duplicates.

Do **not** save termbases under `1-SOURCES/`.

---

## Rules

### 1. Extract Doctrinal Vocabulary Only

Include:

* doctrinal terms
* mental factors
* aggregates
* sense bases
* elements
* path factors
* meditation terms
* ethical terms
* Abhidhamma classification terms
* technical compounds functioning as standalone concepts
* cosmological terms
* epistemological terms
* liberation-related terms
* dependent origination terms

Examples:

```text
dhamma
vedanā
saññā
citta
cetasika
phassa
vitakka
vicāra
pīti
upekkhā
sati
samādhi
paññā
kilesa
āsava
saṃyojana
nīvaraṇa
upādāna
taṇhā
magga
jhāna
vipassanā
paṭiccasamuppāda
anicca
dukkha
anattā
```

---

### 2. Ignore Grammatical Words

Do NOT include:

```text
ca
vā
na
kho
hi
eva
iti
atha
yaṃ
taṃ
so
sā
te
ime
hoti
atthi
```

Ignore:

* particles
* conjunctions
* pronouns
* grammatical-only words
* case markers
* numbering
* section markers
* punctuation

---

### 3. Normalize to Lemma

Convert all inflected forms to dictionary lemmas.

Examples:

```text
dhammā
dhammaṃ
dhamme
dhammassa
dhammānaṃ
dhammesu
→ dhamma

vedanāya
vedanāsu
→ vedanā

cittaṃ
citte
cittassa
→ citta
```

---

### 4. Collect Common Surface Forms

For each lemma, collect commonly occurring forms found in the corpus.

Example:

```text
dhammā
dhammaṃ
dhamme
dhammassa
dhammānaṃ
dhammesu
```

becomes:

```text
dhammo, dhammaṃ, dhammā, dhamme, dhammassa, dhammānaṃ, dhammesu
```

Use representative forms.

Do not attempt to list every theoretically possible inflection.

---

### 5. Generate Multiple Senses

A lemma may possess multiple doctrinal senses.

Create one row per distinct sense.

Do not collapse unrelated meanings into a single entry.

Example:

| Common Surface Forms                                            | Lemma  | Domain     | Sense                    | Canonical Translation | Sense Tag     |
| --------------------------------------------------------------- | ------ | ---------- | ------------------------ | --------------------- | ------------- |
| dhammo, dhammaṃ, dhammā, dhamme, dhammassa, dhammānaṃ, dhammesu | dhamma | Abhidhamma | Phenomenon, state, thing | phenomenon            | phenomenon    |
|                                                                 |        | Abhidhamma | Mental object            | mental object         | mental_object |
|                                                                 |        | Sutta      | Buddha's teaching        | Dhamma                | teaching      |
|                                                                 |        | Vinaya     | Doctrine, teaching       | doctrine              | doctrine      |

Do NOT repeat Common Surface Forms or Lemma for additional senses.

Leave repeated cells blank.

#### Using `pi-1.meaning.json` as the sense reference

When a `pi-1.meaning.json` file (output of `pali_keyword/generate_pali_meaning.py`) is provided alongside the Pāli text, use it as the authoritative starting point for each lemma's senses:

* Each entry has the shape `{ "lemma": ..., "variants": [...], "meaning": [...] }`.
* Each item in `meaning` corresponds to **one DPD sense** (e.g. `dhamma 1.01`, `dhamma 1.02`, ...) and has the form:

  ```text
  "(<part of speech>) <near-synonym 1>; <near-synonym 2>; ..."
  ```

  e.g. `"(masculine noun) quality; characteristic; trait; inherent quality"`.

  The leading `(part of speech)` (e.g. `masculine noun`, `feminine noun`, `neuter noun`, `adjective`, `indeclinable`, `present tense verb`, `past participle`, ...) describes the grammatical category of that sense — use it to inform the doctrinal framing (e.g. a verb sense should yield an action/process Sense, not a noun phrase) but do NOT copy it verbatim into the Sense or Canonical Translation columns.

* Treat each `meaning` array item as the seed for **one candidate row** (one distinct sense):
  * Use the `variants` array as the basis for **Common Surface Forms** (select representative forms per Rule 4).
  * Use the semicolon-separated near-synonym group (after the part-of-speech prefix) to derive the **Sense** (a precise doctrinal description per Rule 7) and the **Canonical Translation** (the preferred scholarly term, usually the first or most doctrinally standard term in the group, per Rule 8).
  * Assign **Domain** and **Sense Tag** per Rules 6 and 9.
* Not every `meaning` item is necessarily doctrinal — drop senses that are purely grammatical, lexicographic, or proper-noun (e.g. "(letter) letter p; 29th letter of the alphabet", "(masculine noun) name of king Mahāsudassana's palace") per Rule 1/2.
* Where multiple `meaning` items express the same underlying doctrinal sense in different words (regardless of part of speech), merge them into a single row rather than creating duplicate senses (per Rule 12).
* Cross-check the JSON-derived senses against the Pāli text itself — only keep senses that are doctrinally relevant and, where possible, attested or plausible in context. You may add senses not present in the JSON if the text clearly requires them.

---

### 6. Assign Domains

Identify the primary doctrinal domain in which the sense is commonly used.

Possible values:

```text
Abhidhamma
Sutta
Vinaya
Commentary
General
```

Use:

* General when a sense occurs broadly across traditions
* Specific domains when the sense is strongly associated with a particular corpus

---

### 7. Create Translation-Oriented Senses

The Sense column should describe the meaning in a way that helps translators select the correct rendering.

Good:

```text
Feeling tone
Aggregate of feeling
Mental object
Volitional formation
Consciousness
Defilement
Path factor
Dependent arising
```

Bad:

```text
Thing
Object
State
Concept
```

Prefer precise doctrinal descriptions.

---

### 8. Generate Canonical Translation

Canonical Translation should contain the preferred scholarly rendering.

Examples:

```text
vedanā → feeling
saññā → perception
citta → consciousness
sati → mindfulness
samādhi → concentration
paññā → wisdom
saṅkhāra → formations
```

The Canonical Translation should be:

* stable
* doctrinally precise
* suitable for academic translation
* audience-independent

Do not simplify.

Do not paraphrase.

Do not localize for beginners.

---

### 9. Create Machine-Friendly Sense Tags

Generate unique snake_case identifiers.

Examples:

```text
Mental object
→ mental_object

Aggregate of feeling
→ feeling_aggregate

Volitional formation
→ volitional_formation

Dependent arising
→ dependent_arising
```

Tags should remain stable across future extractions.

---

### 10. Do NOT Output Decomposition

Do NOT include:

```text
dhammavicaya = dhamma + vicaya
sammādiṭṭhi = sammā + diṭṭhi
```

Do not include:

* etymology
* morphology analysis
* compound breakdowns
* grammatical notes

Treat doctrinal compounds as standalone concepts when appropriate.

---

### 11. Deduplicate Across the Entire Corpus

If a lemma appears multiple times:

* merge occurrences
* merge observed surface forms
* merge identified senses

Create a single consolidated entry.

Do not create duplicate lemma entries.

---

### 12. Quality Requirements

For every lemma:

* identify all major doctrinal senses relevant to Buddhist literature
* avoid overly narrow corpus-specific definitions
* distinguish genuinely different senses
* avoid duplicate senses with different wording

When uncertain, prefer broader doctrinally established senses.

---

### 13. Output Format

Output ONLY a markdown table.

Use exactly:

| Common Surface Forms | Lemma | Domain | Sense | Canonical Translation | Sense Tag |
| -------------------- | ----- | ------ | ----- | --------------------- | --------- |

No explanations.

No summaries.

No commentary.

No reasoning.

No prose before or after the table.

Only the termbase table.

---

## Input Text

Paste the Pāli text below:

```text
[PASTE PĀLI TEXT HERE]
```

## Optional Input: Sense Reference (`pi-1.meaning.json`)

If available, also provide `pali_keyword/output/pi-1.meaning.json` (or the equivalent `pi-N.meaning.json` for the source). Use it as described in Rule 5 ("Using `pi-1.meaning.json` as the sense reference") to seed candidate senses, surface forms, and canonical translations for each lemma.

```json
[PASTE pi-N.meaning.json CONTENTS HERE, IF AVAILABLE]
```
