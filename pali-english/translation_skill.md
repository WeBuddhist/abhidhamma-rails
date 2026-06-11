---

name: pali-buddhist-translation
description: Translate Pāli Buddhist texts into accurate English using generated termbases, audience profiles, translation requirements, summaries, and commentary-based sense resolution.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Pāli Buddhist Translation Skill

## Purpose

Translate Pāli Buddhist texts into accurate English while preserving doctrinal meaning, terminology consistency, contextual correctness, and audience appropriateness.

Unless the user’s prompt limits scope, translate the **entire** named source file — not just its opening section.

The translation process must use all available reference materials.

Never translate solely from dictionary meanings when project references are available.

The translation workflow is:

```text
Source Text
    ↓
Termbase Generation
    ↓
Requirement Rules
    ↓
Audience Profile
    ↓
Summary Context
    ↓
Commentary Context
    ↓
Translation
```

---

# Reference File Locations

Before translating, locate and load all relevant reference files.

Replace example locations with project-specific paths.

---

## Translation Output Files

**Location:** `pali-english/` (same directory as this skill, `requirements.md`, audience profiles, and termbases).

* Save every translation output and every generated termbase here.
* Do **not** write outputs under `3-TRANSFORMATIONS/`.
* Do **not** read, copy, or continue from older `en-dhammasangani-ai-auto-*.md` files in `3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/` when using this skill.

**Naming:** use this pattern unless the user gives an explicit filename:

```text
<text-slug>-ai-auto-<audience-slug>-<n>.md
```

Examples for *Dhammasaṅgaṇī* (`pi-1.md`):

```text
en-dhammasangani-ai-auto-grade3-1.md
en-dhammasangani-ai-auto-grade3-2.md
en-dhammasangani-ai-auto-grade8-1.md
en-dhammasangani-ai-auto-scholarly-1.md
en-dhammasangani-ai-auto-general-1.md
```

* **`<text-slug>`** — English work slug (e.g. `en-dhammasangani`).
* **`<audience-slug>`** — from the active audience profile filename: drop the `audience_` prefix and use lowercase (e.g. `audience_grade3.md` → `grade3`, `audience_general_readers.md` → `general`, `audience_scholarly.md` → `scholarly`).
* **`<n>`** — sequence number, starting at `1`.
  * `1` — first output file for that source + audience (default).
  * `2`, `3`, … — next file for the **same** source + audience when the user splits output across files or when continuing a multi-file run.

Do **not** use bare `auto-1`, `auto-2` without an audience slug. One audience per file; do not mix audiences in one output file.

If the user supplies an explicit filename, use it; otherwise derive the name from the pattern above.

**Termbase naming:** per-audience termbases live in `pali-english/audience_requirments/termbase/` and are named `termbase-` + source filename + `-audience_<audience-slug>.md`. Example: source `pi-1.md`, audience `grade3` → `termbase-pi-1-audience_grade3.md`. Reuse the existing per-audience file when the same source already has a suitable termbase; extend it in place when vocabulary grows.

---

## Translation Scope

**Default: translate the whole source file.** When the user names a source (e.g. `1-SOURCES/Text/pi-1.md`), translate it **in full** — from the opening through the final block — unless the prompt **explicitly** limits scope.

**Do not** stop after only the first chapter, the Mātikā, the homage, or any other natural breakpoint if the user did not ask for a partial translation.

**Partial translation only when the prompt says so**, for example:

* a verse or block range (`^1-0a-1`–`^1-0a-22`, “§1–22 only”)
* a named section (“Tikamātikā only”, “through Mātikā”)
* an explicit stop point (“translate until ^1-100”)

**Large sources:** The full file may require many sequential passes. Work through the source in order; **append** each completed portion to the output in `pali-english/` until every block in scope is translated. Extend or supplement the termbase when new doctrinal vocabulary appears in later portions. An output that ends before the source ends (without a user limit) is **incomplete**.

**Resume:** If an output file already exists for the same source, audience slug, and sequence number (e.g. `en-dhammasangani-ai-auto-grade8-1.md`), continue from the first untranslated block in that file unless the user asks to redo from the start. When starting a new sequence file (`-2`, `-3`, …), carry terminology forward from the prior file for the same audience.

---

## Requirement Files

Locations:

* \pali-english\requirements.md

Purpose:

* translation workflow
* consistency rules
* formatting rules
* terminology handling
* output behavior

Always load requirement files first.

---

## Audience Files

Locations:

* \pali-english\audience_requirments\skills\audience_scholarly.md
* \pali-english\audience_requirments\skills\audience_translation_study.md
* \pali-english\audience_requirments\skills\audience_practicing_buddhists.md
* \pali-english\audience_requirments\skills\audience_general_readers.md
* \pali-english\audience_requirments\skills\audience_beginner_buddhist.md
* \pali-english\audience_requirments\skills\audience_grade8.md
* \pali-english\audience_requirments\skills\audience_grade3.md

Purpose:

* audience definition
* reading level
* terminology adaptation
* stylistic adaptation

Only one audience profile should be active during translation.

Each audience profile references its own per-audience termbase under `pali-english/audience_requirments/termbase/termbase-pi-1-audience_<audience-slug>.md` (see [Audience Termbase Files](#audience-termbase-files)). Loading the active audience profile and its paired termbase together is required before translation begins.

---

## Commentary Files

Locations:

* \1-SOURCES\Commentaries\pi-dhammasangani-anutiika.md

Purpose:

* doctrinal interpretation
* ambiguity resolution
* technical clarification
* contextual understanding

Consult commentary before translating difficult passages.

---

## Summary Files

Locations:

* 2-RAILS\Verses\

Purpose:

* section overview
* topic identification
* doctrinal context
* subject continuity

Review summaries before translating individual passages.

---

## Termbase Extraction Skill

Location:

* \pali-english\Pāli Termbase Extraction Prompt.md

Purpose:

Generate translation termbases from source Pāli texts.

The extraction skill produces termbases containing:

* lemmas
* doctrinal senses
* canonical translations
* sense tags
* domain information

The generated termbase becomes an authoritative translation reference, and is in turn split into the per-audience termbases described below.

---

# Termbase Generation

Before translation begins, determine whether a suitable per-audience termbase already exists for the source text and the active audience.

If no termbase exists for the source at all:

1. Load the source Pāli file.
2. Apply:

```text
Pāli Termbase Extraction Prompt.md
```

3. Generate a draft termbase covering all audiences.
4. Split the draft into one 6-column termbase per audience (see [Audience Termbase Files](#audience-termbase-files)) and save each under `pali-english/audience_requirments/termbase/`.
5. Name each file `termbase-` + the source filename + `-audience_<audience-slug>.md` (e.g. source `pi-1.md`, audience `scholarly` → `termbase-pi-1-audience_scholarly.md`).
6. Do not create a second termbase file for the same source + audience unless the user asks; extend the existing `termbase-<source>-audience_<audience-slug>.md` instead.
7. Reuse existing per-audience termbases whenever possible.

If new vocabulary appears mid-translation, add the new lemma/sense row to **all 7** per-audience termbase files (Translation column wording adapted per audience, per [Audience Termbase Files](#audience-termbase-files)), so Sense Tags stay consistent across audiences.

---

## Audience Termbase Files

Location:

`pali-english/audience_requirments/termbase/` — one file per audience, named `termbase-pi-1-audience_<audience-slug>.md`:

* termbase-pi-1-audience_scholarly.md
* termbase-pi-1-audience_translation_study.md
* termbase-pi-1-audience_practicing_buddhists.md
* termbase-pi-1-audience_general_readers.md
* termbase-pi-1-audience_beginner_buddhist.md
* termbase-pi-1-audience_grade8.md
* termbase-pi-1-audience_grade3.md

Do **not** save termbases under `1-SOURCES/`.

Each per-audience termbase follows this schema:

| Common Surface Forms | Lemma | Domain | Sense | Translation | Sense Tag |
| -------------------- | ----- | ------ | ----- | ----------- | --------- |

Example (scholarly):

| Common Surface Forms            | Lemma  | Domain     | Sense                    | Translation | Sense Tag     |
| -------------------------------- | ------ | ---------- | ------------------------ | ----------- | ------------- |
| dhammo, dhammaṃ, dhammā, dhamme | dhamma | Abhidhamma | Phenomenon, state, thing | phenomenon  | phenomenon    |
|                                  |        | Abhidhamma | Mental object            | mental object | mental_object |
|                                  |        | Sutta      | Buddha's teaching        | Dhamma      | teaching      |

For translation, only load the **one** termbase file matching the active audience profile. Translation is keyed by **Sense Tag**: the same Sense Tag must always receive the same Translation wording within a given audience's output.

---

# Reference Usage

## Requirement Files

Requirement files govern:

* translation workflow
* formatting
* consistency
* output structure
* terminology policy

All translations must comply with requirement files.

Requirement files define how translation is performed.

---

## Audience Files

Audience files govern:

* reading level
* sentence complexity
* vocabulary complexity
* terminology adaptation
* stylistic presentation

Audience files determine how meaning is expressed.

Audience files must never alter meaning.

Audience files must never override doctrinal accuracy.

---

## Commentary Files

Use commentary to:

* resolve ambiguity
* determine doctrinal meaning
* distinguish competing interpretations
* understand technical discussions
* identify implied relationships

Commentary is an interpretation aid.

Commentary must never be translated into the output.

Commentary must never replace the source text.

---

## Summary Files

Use summaries to:

* identify the topic
* determine doctrinal context
* understand section purpose
* maintain consistency across related passages

Summaries provide context.

Summaries must never appear in the output.

---

## Termbase Files

The per-audience termbase matching the active audience profile is authoritative for terminology.

For each significant Pāli term:

1. Identify the surface form.
2. Identify the lemma.
3. Retrieve available senses (rows) for that lemma in the active audience's termbase.
4. Determine the correct sense.
5. Select the corresponding Translation for that sense's Sense Tag.
6. Produce the final rendering — Translation values in the per-audience termbase are already audience-adapted, so no further register adjustment should be needed.
7. If the lemma/sense is not yet in the termbase, choose a clear rendering consistent with the audience profile and reuse it for that sense everywhere.

Never assume a lemma has only one meaning.

Context determines sense selection.

---

# Translation Workflow

## Step 0 — Ensure Termbase Exists

Before translation:

1. Determine the active audience profile.
2. Check whether a suitable per-audience termbase already exists at `pali-english/audience_requirments/termbase/termbase-<source-filename>-audience_<audience-slug>.md`.
3. If no termbase exists for this source at all:

   * Run `Pāli Termbase Extraction Prompt.md`
   * Generate a draft termbase
   * Split it into the 7 per-audience termbases under `pali-english/audience_requirments/termbase/`
4. Load the per-audience termbase matching the active audience.
5. Continue with translation.

Termbase generation normally occurs once per source text (then split per audience).

---

## Step 1 — Load References

Load:

1. requirement.md
2. active audience profile (`pali-english/audience_requirments/skills/audience_<audience-slug>.md`)
3. commentary files
4. summary files
5. the per-audience termbase matching the active audience profile (`pali-english/audience_requirments/termbase/termbase-<source-filename>-audience_<audience-slug>.md`)

---

## Step 2 — Determine Translation Environment

Identify:

* active audience
* translation style
* terminology requirements
* formatting requirements
* project conventions

Apply these rules throughout translation.

---

## Step 3 — Establish Context

Review:

* summaries
* commentary
* surrounding passages

Determine:

* doctrinal category
* analytical context
* subject under discussion
* relationship to nearby passages

Maintain context throughout translation.

---

## Step 4 — Resolve Terminology

For each significant Pāli term:

1. Search Common Surface Forms.

2. Identify the lemma.

3. Retrieve candidate senses.

4. Determine the correct sense using:

   * local context
   * section summary
   * commentary
   * doctrinal domain

5. Select the Canonical Translation associated with the chosen sense.

6. Apply audience-specific adaptation rules.

Do not choose a sense merely because it appears first.

Context determines meaning.

---

## Step 5 — Translate

Confirm **translation scope** (see [Translation Scope](#translation-scope)): whole file by default; partial only if the user limited it.

Translate using:

1. Source text
2. requirement.md
3. active audience profile
4. generated termbase
5. commentary guidance
6. summary context

Translate every block in scope before finishing. For a whole-file job, keep working through the source until the final block is done.

Priority:

1. Doctrinal accuracy
2. Correct sense selection
3. Terminology consistency
4. Audience appropriateness
5. Readability

---

## Step 6 — Consistency Review

Within the current passage:

* maintain consistent sense selection
* maintain consistent terminology
* maintain consistent audience style
* avoid unnecessary synonym variation

The same sense should normally receive the same rendering.

---

# Authority Order

When conflicts occur:

1. Source Pāli Text
2. requirement.md
3. active audience's per-audience termbase
4. commentary.md
5. summary.md
6. audience profile

Meaning comes from the source text.

Terminology comes from the per-audience termbase.

Interpretation comes from commentary.

Expression comes from the audience profile.

---

# Special Instructions

* Many Pāli terms are polysemous.
* Never assume a fixed translation for a lemma.
* Determine meaning before selecting a rendering.
* Use commentary to resolve ambiguity.
* Use summaries to establish context.
* Use the active audience's termbase Translation (keyed by Sense Tag) as the semantic foundation.
* Audience profiles may adapt wording but must not change meaning.
* Preserve doctrinal distinctions.
* Preserve analytical structures.
* Preserve classifications and enumerations.
* Avoid paraphrasing away important technical concepts.
* Never invent termbase entries.
* Never invent commentary interpretations.
* Never invent doctrinal meanings.
* Never override a valid sense selection solely to improve readability.

---

# Output Requirements

Output only the final translation.

Do not output:

* termbase entries
* glossary data
* lemmas
* sense tags
* commentary excerpts
* summaries
* reasoning
* analysis
* translation notes

unless explicitly requested.

The final translation should accurately represent **all** of the source text in scope (normally the **entire** file) while conforming to the active audience profile and all project requirements.

A deliverable that covers only the opening section of a source, when the user did not limit scope, does **not** meet this skill’s requirements.
