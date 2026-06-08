---
name: pali-context-builder
description: Build a compact reusable translation context package from Pāli source text, summary, and commentary for later audience-specific translation.
---

# Pāli Context Builder Skill

## Purpose

Build a reusable translation context package from:

- Source Pāli text
- Summary files
- Commentary files

The output is a compact, translation-ready context file that can be reused for multiple audience-specific translations without rereading the full source materials.

This skill does **not** translate the text.

This skill does **not** produce a glossary or termbase.

This skill does **not** expand commentary into full prose.

Its job is to distill durable translation knowledge into a reusable context artifact.

---

# Core Goal

Read the source, summary, and commentary once.
Extract only the information needed for later translation.
Save that distilled knowledge as a reusable context file in the same directory as the source.

The context file should be small, structured, and stable.

It should preserve:

- doctrinal context
- resolved ambiguities
- section purpose
- key translation constraints
- important terminology notes
- commentary conclusions that affect translation

It should omit:

- long commentary discussion
- repeated explanation
- source text duplication
- full summary duplication
- translation output
- audience-specific rewriting

---

# Input Files

Load only these inputs:

1. Source Pāli file
2. Summary file(s)
3. Commentary file(s)

Do not require the termbase for this skill.
Do not require audience profiles for this skill.
Do not require translation requirements for this skill.

Those are used later during translation.

---

# Output File

Create a reusable context file in the same directory as the source file.

Suggested names:

- `Context-1.md`
- `Context-2.md`
- `Context-3.md`

Use sequential numbering when multiple context files are needed for different source sections or source files.

If the project uses section-level files, name them consistently, for example:

- `Context-1-0a.md`
- `Context-1-0b.md`
- `Context-1-1.md`

The exact naming scheme must be consistent within the project.

---

# Output Purpose

The generated context file will later be reused by translation prompts for:

- scholarly audience
- practicing Buddhists
- general readers
- beginner Buddhist readers
- grade 8 students
- grade 3 students

The context file should be audience-neutral.

It should describe meaning, not style.

---

# What to Extract

## 1. Section Topic

Identify the main topic of the source section.

Examples:

- analysis of consciousness
- classification of mental factors
- dependent arising
- wholesome and unwholesome states
- sense bases
- aggregates

Write this as a short, direct phrase.

---

## 2. Doctrinal Framework

Identify the doctrinal framework used in the passage.

Examples:

- Abhidhamma analytical classification
- Sutta-style exposition
- Vinaya disciplinary context
- commentarial explanation
- enumerative taxonomy

---

## 3. Important Concepts

List the key doctrinal concepts that the passage depends on.

Examples:

- consciousness
- feeling tone
- perception
- formations
- wholesome states
- unwholesome states
- mental factors
- defilements
- path factors

Keep the list short and relevant.

---

## 4. Resolved Term Meanings

Extract the meanings that the commentary and summary establish for important ambiguous terms.

Examples:

- `dhamma` here means analyzed phenomenon, not teaching
- `citta` here means consciousness
- `kusala` here means wholesome
- `vedanā` here means feeling tone

Use the resolved meaning, not the full dictionary range.

If a term remains ambiguous, state that it is unresolved and list the likely senses briefly.

---

## 5. Commentary Conclusions

Extract only the commentary conclusions that matter for translation.

Examples:

- the passage is classificatory rather than narrative
- the list is taxonomic and should remain structured
- the term is used technically, not colloquially
- the commentary restricts the scope of a term
- a repeated phrase is being used in a fixed doctrinal sense

Do not copy the commentary itself.
Do not include long argumentative detail.

---

## 6. Translation Constraints

Record practical translation rules implied by the source and commentary.

Examples:

- preserve list structure
- preserve parallel phrasing
- preserve singular/plural distinctions
- preserve technical labels
- avoid paraphrasing doctrinal categories
- keep repeated formulae consistent

These constraints help later translation runs stay faithful.

---

## 7. Potential Pitfalls

Record anything that may cause translation errors.

Examples:

- term has more than one doctrinal sense
- commentary uses a narrower sense than the dictionary
- phrase looks ordinary but is technical here
- same word changes sense across sections
- list items are not interchangeable synonyms

Keep this section brief.

---

# What Not to Include

Do not include:

- full source text
- full summary text
- full commentary text
- glossary tables
- termbase entries
- audience instructions
- translation style rules
- English translation of the source
- line-by-line commentary reproduction
- etymological breakdowns unless they directly affect translation

The context file should be compact.

---

# Compression Rule

The context file should be a distilled artifact.

A good context file is smaller and more useful than the raw source materials.

Do not inflate it by copying entire sections of commentary or summary.

Prefer short, decisive statements.

---

# Recommended Structure of Output File

Use the following structure:

```md
# Translation Context

## Source / Section ID

[identifier]

## Topic

[short phrase]

## Doctrinal Framework

[short phrase]

## Important Concepts

- [concept 1]
- [concept 2]
- [concept 3]

## Resolved Term Meanings

- [lemma] → [resolved meaning]
- [lemma] → [resolved meaning]

## Commentary Conclusions

- [translation-relevant conclusion 1]
- [translation-relevant conclusion 2]

## Translation Constraints

- [constraint 1]
- [constraint 2]

## Potential Pitfalls

- [pitfall 1]
- [pitfall 2]
```

---

# Extraction Workflow

## Step 1: Read the Source

Determine:

- section boundaries
- topic
- structure
- repeated formulae
- key doctrinal terms

---

## Step 2: Read the Summary

Determine:

- section purpose
- broader context
- doctrinal direction
- topic continuity

Use the summary to avoid overfitting to one sentence.

---

## Step 3: Read the Commentary

Determine:

- technical clarifications
- ambiguous term resolutions
- doctrinal constraints
- interpretive conclusions

Use commentary only for translation-relevant information.

---

## Step 4: Distill the Conclusions

Convert the source, summary, and commentary into compact notes.

Prefer short bullet points.

Prefer stable statements over verbose prose.

---

## Step 5: Save the Context File

Write the resulting context package to the same directory as the source file.

Use the project’s naming convention consistently.

If a context file already exists for the same source version, update it only if the source or commentary has changed.

---

# Reuse Rules

The generated context file is the reusable layer for later translation runs.

Later translation should load:

- source text
- context file
- active audience profile
- requirement file

The translation step should **not** reread the full commentary and summary unless the context file is being rebuilt.

---

# Regeneration Rules

Regenerate the context file only when one of the following changes:

- source text changes
- summary changes
- commentary changes
- project conventions change in a way that affects translation meaning

If the source is unchanged, reuse the saved context file.

---

# Quality Rules

A good context file should:

- be concise
- be explicit
- preserve doctrinal meaning
- capture only translation-relevant conclusions
- help later sense selection
- reduce token usage in future runs
- remain valid across multiple audience profiles

---

# Output Requirements

Output only the generated context file.

Do not output:

- explanation of your process
- commentary quotations
- source excerpts beyond what is needed for identifiers
- translation
- glossary entries
- audience advice
- reasoning notes

Return only the compact reusable context package.

---

# Example Output Skeleton

```md
# Translation Context

## Source / Section ID

1-0a

## Topic

Classification of consciousness and mental factors.

## Doctrinal Framework

Abhidhamma analytical classification.

## Important Concepts

- consciousness
- feeling tone
- perception
- formations
- wholesome states

## Resolved Term Meanings

- dhamma → analyzed phenomenon
- citta → consciousness
- kusala → wholesome

## Commentary Conclusions

- The passage is taxonomic.
- The list items are technical categories.

## Translation Constraints

- Preserve list structure.
- Preserve parallel phrasing.
- Avoid paraphrasing technical categories.

## Potential Pitfalls

- dhamma has multiple senses elsewhere.
- The passage uses a technical rather than general meaning.
```

