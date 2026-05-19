---
name: atthakatha-summaries
description: Create structured, introductory summaries for each Table of Contents (TOC) level of a root text, based strictly on its Aṭṭhakathā (commentary).
---

# Skill: Aṭṭhakathā Summaries

**Purpose:** Create structured, introductory summaries for each Table of Contents (TOC) level of a root text, based strictly on its Aṭṭhakathā (commentary).

## Execution Steps

### 1. Extract TOC and Initialize Rails
- Read the target root text in `1-SOURCES/Texts/`.
- Extract the complete Table of Contents (TOC) tree.
- Create a new file at `2-RAILS/Sections/<text name>-summaries.md`.
- Outline the file using Markdown headings that match the extracted TOC tree.

### 2. Match with Aṭṭhakathā
- For each TOC level, search `1-SOURCES/Commentaries/` (or the specific Aṭṭhakathā file) to find the corresponding commentary section.

### 3. Draft Pāli Summaries
- Read the commentary's presentation of the section.
- Write a **single summary paragraph in Pāli** under the corresponding heading in `<text name>-summaries.md`.
- **Constraints:**
  - The summary must act as an effective introduction to the section for someone new to the text.
  - You must use the specific terms and vocabulary found in the commentary.
  - Preserve all Pāli diacritics exactly (e.g., ā, ī, ū, ṭ, ñ).

### 4. Append Citations
- Immediately following the summary paragraph, insert a direct wikilink to the exact commentary section used (e.g., `[[Aṭṭhakathā-File#Section-Name]]`).