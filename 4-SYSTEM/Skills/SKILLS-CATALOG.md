# Skills Catalog

This file catalogues every skill used in the abhidhamma-rails vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it.

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts tipitaka.org JSON exports of root texts into formatted source-text markdown files.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

### `json-to-commentary` **[exists]**
Converts tipitaka.org JSON exports of Pali commentaries (aṭṭhakathā) into formatted commentary markdown files.
→ [`json-to-commentary/SKILL.md`](json-to-commentary/SKILL.md)

### `format-root-text` **[exists]**
Normalises an existing root-text file: heading structure, block IDs, verse formatting.
→ [`format-root-text/SKILL.md`](format-root-text/SKILL.md)

### `format-commentary` **[exists]**
Normalises an existing commentary file: OCR cleanup, heading structure, paragraph granularity, block IDs.
→ [`format-commentary/SKILL.md`](format-commentary/SKILL.md)

### `add-toc` **[exists]**
Inserts or regenerates a table of contents in a source or rails file.
→ [`add-toc/SKILL.md`](add-toc/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `section-summary-raw` **[planned]**
**Purpose:** Generate a summary of one table-of-contents node in the original language, drawn from a single commentary.
**Inputs:** Commentary file(s) in `1-SOURCES/`, the TOC node to summarise.
**Outputs:** One summary file per commentary under `2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md`.
**Rules:** Use only the terminology the commentary itself uses. No translation. No paraphrase beyond compression. Every claim cites a block ID from the source file.
→ `section-summary-raw/SKILL.md` *(to be written)*

### `section-summary-combined` **[planned]**
**Purpose:** Combine the per-commentary raw summaries for one TOC node and add an English translation of the combined summary.
**Inputs:** All raw summary files for the target node under `2-RAILS/Sections/Raw/`.
**Outputs:** One combined file at `2-RAILS/Sections/<node-id>.md` containing the original-language synthesis and an English translation.
→ `section-summary-combined/SKILL.md` *(to be written)*

### `verse-context` **[planned]**
**Purpose:** Build the verse-level context file for one verse.
**Inputs:** Root-text verse (from `1-SOURCES/`), all commentary passages that discuss it (via block transclusions from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Verses/<verse-id>.md` containing: (1) transclusions of commentary passages, (2) a synthesis of the commentators' interpretations in the original language, (3) a disambiguated restatement of the verse in the original language precise enough to exclude any mistranslation.
→ `verse-context/SKILL.md` *(to be written)*

### `local-wiki-article` **[planned]**
**Purpose:** Create or update a Local-Wiki article for one key term.
**Inputs:** Commentary passages that explain or define the term (via block citations from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Local-Wiki/<term>.md` containing: cited commentary explanations in the original language, and a short contextual definition drafted from those citations (also in the original language).
→ `local-wiki-article/SKILL.md` *(to be written)*

### `glossary-extract-raw` **[planned]**
**Purpose:** Extract every keyword and its rendered form from one existing translation or reference text, producing a raw per-source glossary.
**Inputs:** One translation or reference text file in `1-SOURCES/` or `3-TRANSFORMATIONS/`.
**Outputs:** One glossary file at `2-RAILS/Glossaries/Raw/<source-name>.md` with a table mapping Pali term → rendering used in that source.
→ `glossary-extract-raw/SKILL.md` *(to be written)*

### `glossary-combine` **[planned]**
**Purpose:** Merge all raw glossary files for one language pair into a single consolidated glossary.
**Inputs:** All relevant files under `2-RAILS/Glossaries/Raw/`.
**Outputs:** One consolidated glossary at `2-RAILS/Glossaries/<lang-pair>.md` showing every attested rendering side by side.
→ `glossary-combine/SKILL.md` *(to be written)*

### `glossary-select` **[planned]**
**Purpose:** Build the translation-specific working glossary for one track by selecting the preferred rendering for each term from the consolidated glossary, guided by the track's `requirements.md`. If no existing rendering is satisfactory, derive one from the Local-Wiki article for that term.
**Inputs:** `2-RAILS/Glossaries/<lang-pair>.md`, `3-TRANSFORMATIONS/Translation/<track-name>/requirements.md`, Local-Wiki articles as needed.
**Outputs:** `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md`.
→ `glossary-select/SKILL.md` *(to be written)*

---

## Translation skills

### `translate-section` **[planned]**
**Purpose:** Translate a small batch of TOC nodes into the target language.
**Inputs:**
- `3-TRANSFORMATIONS/Translation/<track-name>/requirements.md`
- `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md`
- `2-RAILS/Sections/<node-id>.md` for each node in the batch
- `2-RAILS/Verses/<verse-id>.md` for each verse in the batch
**Outputs:** Updated translation file(s) in `3-TRANSFORMATIONS/Translation/<track-name>/`.
**Rules:** Every keyword rendering must match the glossary. Introduce no new rendering without first adding it to the glossary. Translate from the disambiguated Pali in the verse-context file, not from the raw root text. The frontmatter of each translation file must list the rail files it was generated from.
→ `translate-section/SKILL.md` *(to be written)*

---

## Translation QA skills

### `translation-qa` **[planned]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:**
- The translated section(s) in `3-TRANSFORMATIONS/Translation/<track-name>/`
- `3-TRANSFORMATIONS/Translation/<track-name>/requirements.md`
- `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md`
- Relevant `2-RAILS/Sections/` and `2-RAILS/Verses/` files
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translation/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category, severity (critical / major / minor), and a suggested correction.
**Completion criterion:** A section is marked `status: complete` only when no critical or major MQM errors remain open in the QA report.
→ `translation-qa/SKILL.md` *(to be written)*

---

## Utility skills

### `source-property-extractor` **[exists]**
Extracts structured metadata (author, date, edition, language, publisher) from a source file and writes it to the frontmatter.
→ [`source-property-extractor/SKILL.md`](source-property-extractor/SKILL.md)

### `property-creator` **[exists]**
Creates or updates Obsidian frontmatter properties on a file.
→ [`property-creator/SKILL.md`](property-creator/SKILL.md)

### `structural-outline-ingest` **[exists]**
Ingests a structural outline (TOC) into a source or rails file.
→ [`structural-outline-ingest/SKILL.md`](structural-outline-ingest/SKILL.md)
