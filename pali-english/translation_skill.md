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

**Termbase naming:** `termbase-` + source filename (in `pali-english/`). Example: source `pi-1.md` → `termbase-pi-1.md`. Reuse the existing file when the same source already has a suitable termbase; extend it in place when vocabulary grows.

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

* \pali-english\audience_scholarly.md
* \pali-english\audience_practicing_buddhists.md
* \pali-english\audience_general_readers.md
* \pali-english\audience_beginner_buddhist.md
* \pali-english\audience_grade8.md
* \pali-english\audience_grade3.md

Purpose:

* audience definition
* reading level
* terminology adaptation
* stylistic adaptation

Only one audience profile should be active during translation.

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

The generated termbase becomes an authoritative translation reference.

---

# Termbase Generation

Before translation begins, determine whether a suitable termbase already exists for the source text.

If no termbase exists:

1. Load the source Pāli file.
2. Apply:

```text
Pāli Termbase Extraction Prompt.md
```

3. Generate a termbase.
4. Save the termbase in `pali-english/` (same directory as `translation_skill.md`).
5. Name the file `termbase-` + the source filename (e.g. source `pi-1.md` → `termbase-pi-1.md`).
6. Do not create a second termbase file for the same source unless the user asks; extend the existing `termbase-<filename>.md` instead.
7. Reuse existing termbases whenever possible.

---

## Generated Termbase Locations

Location:

`pali-english/` (same directory as `translation_skill.md`, `requirements.md`, and translation outputs). Do **not** save termbases under `1-SOURCES/`.

The generated termbase must follow this schema:

| Common Surface Forms | Lemma | Domain | Sense | Canonical Translation | Sense Tag |
| -------------------- | ----- | ------ | ----- | --------------------- | --------- |

Example:

| Common Surface Forms            | Lemma  | Domain     | Sense                    | Canonical Translation | Sense Tag     |
| ------------------------------- | ------ | ---------- | ------------------------ | --------------------- | ------------- |
| dhammo, dhammaṃ, dhammā, dhamme | dhamma | Abhidhamma | Phenomenon, state, thing | phenomenon            | phenomenon    |
|                                 |        | Abhidhamma | Mental object            | mental object         | mental_object |
|                                 |        | Sutta      | Buddha's teaching        | Dhamma                | teaching      |

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

The generated termbase is authoritative for terminology.

For each significant Pāli term:

1. Identify the surface form.
2. Identify the lemma.
3. Retrieve available senses.
4. Determine the correct sense.
5. Select the corresponding Canonical Translation.
6. Apply audience adaptation.
7. Produce the final rendering.

Never assume a lemma has only one meaning.

Context determines sense selection.

---

# Translation Workflow

## Step 0 — Ensure Termbase Exists

Before translation:

1. Check whether a suitable termbase already exists.
2. If none exists:

   * Run `Pāli Termbase Extraction Prompt.md`
   * Generate a termbase
   * Save it in `pali-english/` as `termbase-<source-filename>.md`
3. Load the generated termbase.
4. Continue with translation.

Termbase generation normally occurs once per source text.

---

## Step 1 — Load References

Load:

1. requirement.md
2. active audience profile
3. commentary files
4. summary files
5. generated termbase files

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
3. generated termbase(s)
4. commentary.md
5. summary.md
6. audience profile

Meaning comes from the source text.

Terminology comes from the termbase.

Interpretation comes from commentary.

Expression comes from the audience profile.

---

# Special Instructions

* Many Pāli terms are polysemous.
* Never assume a fixed translation for a lemma.
* Determine meaning before selecting a rendering.
* Use commentary to resolve ambiguity.
* Use summaries to establish context.
* Use Canonical Translation as the semantic foundation.
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
