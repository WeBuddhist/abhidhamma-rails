# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault is a specialized research and translation environment dedicated to the **Pāli Abhidhamma Piṭaka**, with a current focus on the *Dhammasaṅgaṇī*. It functions as a production pipeline for building **interpretive rails**—structured, citation-grounded notes that bridge the gap between ancient commentaries and modern AI-assisted translations.

The goal is to create a reliable knowledge base that allows for the generation of contemporary translations, daily readings, and study guides in multiple languages (English, Bengali, and Sinhala) while strictly adhering to traditional Pāli interpretations. It operates as a highly automated workspace utilizing over 20 custom 'Skills' for text processing.

## Organization

The vault follows a strict, numbered pipeline architecture designed to track information from raw input to processed knowledge:

- **`0-INBOX/`**: Scratchpad for drafts, temporary files, and raw data ingestion.
- **`1-SOURCES/`**: Read-only ground truth. Contains root texts (e.g., `pi-1`), Pāli commentaries (Aṭṭhakathā, Mūlaṭīkā, Anuṭīkā), historical translations, and reference materials.
- **`2-RAILS/`**: The primary work area. Contains structured interpretive context organized by verse (e.g., `1-0a-1`) and section summaries, along with a **Local-Wiki** for technical terms and **Bilingual-Glossaries**.
- **`3-TRANSFORMATIONS/`**: The output layer. Contains AI-generated adaptations, extensive `Daily-Tipitaka` study plans, and contemporary translations (organized by language prefix like `en-`, `bn-`, `si-`).
- **`4-SYSTEM/`**: The operational core. Includes detailed guidelines, templates, and a comprehensive catalog of technical 'Skills' (automated workflows for text processing, glossary extraction, formatting, etc.).

Linking is highly structured, moving one-way from Sources to Rails to Transformations to ensure a clear citation chain.

## Key Topics

- **Pāli Abhidhamma Piṭaka**: Specifically the *Dhammasaṅgaṇī* and its structural outlines (*mātikā*).
- **Traditional Commentaries**: Focused study and structured formatting of the *Aṭṭhakathā*, *Mūlaṭīkā*, and *Anuṭīkā*.
- **Buddhist Technical Philosophy**: Deep dives into concepts like *kusala* (wholesome), *akusala* (unwholesome), *abyākata* (undetermined), and *dhamma*.
- **Multilingual Translation**: Cross-referencing Pāli with Bengali, Sinhala, and English to create contemporary translations.
- **Structured Knowledge Engineering**: Utilizing 'interpretive rails' and combined section summaries to provide context for Large Language Models.
- **Workflow Automation**: Documented 'Skills' for tasks like interlinear glossing, glossary extraction, JSON-to-markdown conversion, and commentary formatting.

## User Preferences

The user prefers a highly technical, structured, and citation-heavy approach. Precision is paramount; Pāli diacritics and specific transliteration styles must be preserved exactly as found in the sources. Use of the pipeline is non-negotiable; information should never bypass the 'Rails' stage when moving from source to transformation.

Responses should be concise and action-oriented, reflecting the 'Skills-based' nature of the vault. The user values strict consistency in metadata (frontmatter) and file naming conventions (specifically using language-tag prefixes like `pi-`, `en-`, `bn-`, `sin-`).

The vault is actively managed with Git, so the user appreciates technical exactness and careful handling of file structures to align with their version control workflows.

## Custom Instructions

- **Citation Chain**: Always verify that information in [[3-TRANSFORMATIONS]] is grounded in [[2-RAILS]], which must in turn cite [[1-SOURCES]].
- **Terminology**: Prioritize definitions found in [[2-RAILS/Local-Wiki/]] and [[2-RAILS/Bilingual-Glossaries/]] over general AI knowledge or external web searches.
- **Formatting**: Preserve all diacritics (e.g., ā, ī, ū, ṭ, ñ) and block IDs (e.g., `^1-0a-1`). Do not normalize or simplify Pāli terms.
- **Writing Constraints**: Never write to `1-SOURCES/` or `4-SYSTEM/`. Draft new content in `0-INBOX/` or the appropriate subfolder of `2-RAILS/` or `3-TRANSFORMATIONS/`.
- **Structural Awareness**: When drafting verses or summaries, consult `4-SYSTEM/Guidelines/abhidhamma-annex` for specific indexing and tagging conventions.
- **Skill Utilization**: When performing text processing, formatting, or extraction tasks, consult the relevant automated workflows in `4-SYSTEM/Skills/` (e.g., `interlinear-gloss`, `format-commentary`).
