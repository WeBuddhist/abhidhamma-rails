---
name: practice-summaries
description: Extract practical information from commentaries to provide guidance on doing less harm, doing more good, and cultivating the mind based on the root text.
---

# Skill: Practice Summaries

**Purpose:** Create structured practice-oriented summaries for each Table of Contents (TOC) level of a root text, based on its commentaries (Aṭṭhakathā, Mūlaṭīkā, or Anuṭīkā), focusing on ethical conduct and mental development.

## Execution Steps

### 1. Extract TOC and Initialize Rails
- Read the target root text in `1-SOURCES/`.
- Extract the complete Table of Contents (TOC) tree.
- Create a new file at `2-RAILS/Sections/<text name>-practice.md`.
- At the very top of the file, before any section headings, insert a **TOC block** (see format below).
- Then outline the rest of the file using Markdown headings that match the extracted TOC tree.

#### TOC Block Format
The TOC block is a nested bullet list using Obsidian within-file heading links (`[[#Heading Name]]`). It must reflect the full heading hierarchy of the document. Example:

```
## Contents

- [[#Section A]]
  - [[#Subsection A1]]
- [[#Section B]]
```

#### Heading Backlink Format
Immediately after every Markdown heading (on its own line, before the summary content), insert a link back to the TOC:

```
[[#Contents|↑]]
```

### 2. Match with Commentaries
- For each TOC level, search `1-SOURCES/` for the corresponding commentary sections. Look specifically for:
    - Definitions of wholesome (*kusala*) and unwholesome (*akusala*) behaviors.
    - Instructions on abandonment of faults.
    - Methods for developing specific mental qualities or meditation subjects.

### 3. Draft Practice Summaries
- Under the corresponding heading in `<text name>-practice.md`, write a summary structured around three pillars:
    - **Doing Less Harm**: Practical advice on avoiding the unwholesome states described in the section.
    - **Doing More Good**: Practical advice on cultivating the wholesome states described in the section.
    - **Cultivating the Mind**: Meditative or mindfulness-based applications derived from the commentary's analysis.
- **Constraints:**
    - The summary must be grounded in the traditional commentary's interpretation.
    - Use technical Pāli terms with correct diacritics (e.g., ā, ī, ū, ṭ, ñ).
    - Maintain a clear, instructional tone.

### 4. Append Citations
- Immediately following the summary content, insert a direct wikilink to the exact source section used (e.g., `[[pi-1-at#Section-Name]]`).

### 5. Update Existing Documents
When adding new sections to an already-existing practice file:
- Add the new entries to the TOC block at the top (maintaining hierarchy).
- Add `[[#Contents|↑]]` backlinks to each new heading.
