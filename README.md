# abhidhamma-rails

A collaborative [Obsidian](https://obsidian.md) vault for building **interpretive rails** through the Abhidhamma — the third basket of the Pali Canon.

## What rails are and why we build them

We build rails so that AI-powered work on the Abhidhamma — translation, summarisation, study-guide generation, question answering — can be done reliably. A **rail** extracts and structures the traditional interpretation of one verse, one section, or one concept of the text into a compact, citation-grounded note. When we then ask an AI to produce a translation or a lesson plan, it works from the combined rails — not from raw commentary scattered across thousands of pages in multiple languages — and the output stays fast, consistent, and traceable.

It's the same idea as Wikipedia for general knowledge. Almost every fact on Wikipedia exists somewhere else on the open internet, often in more detail. But AI tools reach for Wikipedia because the information has already been gathered, summarised, and organised by people who knew what they were doing — which makes it cheaper to retrieve from and more reliable to cite than the raw web. The rails do the same job for the Abhidhamma. The Abhidhamma is a dense, technical analysis of mind and matter, and every key term has been read in subtly different ways across the commentary tradition. Each rail is the curated, Wikipedia-style entry for one unit of the text — one verse, one section, or one concept — distilled from the commentary tradition, organised consistently, and citing the human source behind every claim.

For the full Wikipedia ↔ rails parallel — information density, structure, context-window fit, citations, tone, licensing, data cleanliness, cross-lingual coverage — see [`4-SYSTEM/Guidelines/why-rails.md`](4-SYSTEM/Guidelines/why-rails.md).

For each verse or analytical unit, a rail records:

- The morphology and syntax of the original
- The senses each commentator attests, with the commentary passages that establish them
- The decisions any translator would have to make
- A direct citation — file, verse, page — backing every claim

Everything downstream cites a rail; every rail cites a source. Nothing is invented along the way.

```
1-SOURCES/   →   2-RAILS/   →   3-TRANSFORMATIONS/
ground truth     compact, curated   AI-generated outputs
                 context per verse, (translations, study
                 section, concept   guides, lesson plans)
```

This is the methodology of a **Railroads vault**: one vault per classical text, holding its complete interpretive ecosystem. This particular vault serves the Abhidhamma.

## How the vault is organised

```
abhidhamma-rails/
├── 0-INBOX/                # drafts and raw downloads — not authoritative
├── 1-SOURCES/              # the Abhidhamma texts, exactly as received
├── 2-RAILS/                # the interpretive packages we build
├── 3-TRANSFORMATIONS/      # outputs generated from completed rails
└── 4-SYSTEM/               # guidelines, skills, templates, how-to guides
```

The folder numbers enforce reading order: sources before rails before transformations. Citation only ever flows one way along that arrow — see `4-SYSTEM/Guidelines/0-VAULT-Structure.md` for the full architectural picture.

## Getting started

If you're joining the project for the first time:

- [Set up the vault on your computer](4-SYSTEM/How-to%20guides/Set%20up%20the%20vault.md) — install Obsidian, install Git, clone the repo, and open it as a vault.
- [Sync and troubleshoot](4-SYSTEM/How-to%20guides/Sync%20and%20troubleshoot.md) — how the vault keeps everyone's edits in sync, how to save on demand, and what to do when something goes wrong.

## Reference documents

The methodology and rules live in `4-SYSTEM/`:

- [`Guidelines/why-rails.md`](4-SYSTEM/Guidelines/why-rails.md) — the Wikipedia analogy in full, with the parallel mapped category by category
- [`Guidelines/0-VAULT-Structure.md`](4-SYSTEM/Guidelines/0-VAULT-Structure.md) — top-level architecture and the citation chain
- [`Guidelines/1-SOURCES-Guideline.md`](4-SYSTEM/Guidelines/1-SOURCES-Guideline.md) — rules for source files
- [`Guidelines/2-RAILS-Guideline.md`](4-SYSTEM/Guidelines/2-RAILS-Guideline.md) — schema for compiling rails
- [`Guidelines/source-formatting.md`](4-SYSTEM/Guidelines/source-formatting.md) — formatting rules for adding new source texts (frontmatter, block IDs, headings)
- [`CLAUDE.md`](4-SYSTEM/CLAUDE.md) — LLM-facing operational instructions

For day-to-day workflows (audio alignment, EPUB conversion, formatting, and so on), see the rest of `4-SYSTEM/How-to guides/` and `4-SYSTEM/Skills/`.

## Translation workflow

Producing a reliable AI-assisted translation from the rails requires three sequential phases: **context preparation**, **translation**, and **QA**. Each phase addresses one of the three core failure modes of AI translation:

| Failure mode | Where it is addressed |
|---|---|
| Hallucinations — fabricated meaning at section or verse level | Context preparation → `2-RAILS/Sections/`, `2-RAILS/Verses/` |
| Inconsistent vocabulary — the same Pali term rendered differently across passages | Context preparation → `2-RAILS/Glossaries/` and the translation's own glossary |
| Inconsistent style over long texts | Translation requirements document + QA phase |

### Phase 1 — Translation context preparation

#### 1a. Section-level factual context (`2-RAILS/Sections/`)

For every node in the table of contents, generate a summary **in the original language** (Pali or the commentary language) drawn directly from each relevant commentary, preserving that commentary's own terminology without translating it. Each commentary gets its own file under `Sections/Raw/`. Then, in `Sections/`, combine the per-commentary summaries for each node and add an English translation of the combined summary. These files are what the translation skill loads to orient itself before tackling a section.

#### 1b. Verse-level factual context (`2-RAILS/Verses/`)

For each verse, create a context file that (1) transcludes the relevant commentary passages, (2) synthesises the commentators' respective interpretations in the original language, and (3) uses that synthesis to produce a **disambiguated version of the verse in the original language** — a restatement precise enough that no misreading or mistranslation of the Pali is possible. The translation skill works from this disambiguated version, not from the raw verse.

#### 1c. Word-level factual context (`2-RAILS/Local-Wiki/`)

For each key term explained in the commentaries, create a Local-Wiki article. Populate it with citations from the commentaries (in the original language) and a short contextual explanation drafted from those citations. All content in the Local-Wiki is in the original language. These articles are the reference of last resort when a glossary entry does not yet capture a term adequately.

#### 1d. Glossaries (`2-RAILS/Glossaries/`)

For each existing translation or relevant reference text, extract every keyword and its rendered form into a raw glossary file under `Glossaries/Raw/`. Then combine the raw files into a consolidated glossary per language pair under `Glossaries/`. When setting up a new translation track, select the preferred rendering for each term from the consolidated glossary — guided by the track's `requirements.md` — and write a translation-specific glossary into `3-TRANSFORMATIONS/Translation/<track-name>/`. If no existing rendering is satisfactory, use the Local-Wiki article for that term to derive a better one.

#### 1e. Translation requirements

Each translation track has a `requirements.md` file written in the target language. Before running any translation, verify that it covers: target audience and register, glossary reference path, preferred rendering for structurally significant terms, style constraints (sentence length, use of transliteration, treatment of lists and verse), and any cultural-adaptation rules. The translation skill will not produce consistent output unless these requirements are complete.

### Phase 2 — Translation

Working section by section through the table of contents (small batches — one or a few nodes at a time):

1. Load the track's glossary from `3-TRANSFORMATIONS/Translation/<track-name>/`.
2. Load the section summary for that node from `2-RAILS/Sections/`.
3. Load the verse context files for every verse in the batch from `2-RAILS/Verses/`.
4. Translate against the disambiguated Pali, the section context, and the glossary simultaneously.
5. Write the result into the translation file (or update it if the file already exists).

Never translate a batch without first loading all three levels of context. Never introduce a keyword rendering that is not in the glossary without recording the new rendering in the glossary first.

### Phase 3 — Translation QA

Review each translated section using the **MQM (Multidimensional Quality Metrics) error taxonomy** as the evaluation framework. For each error found, record the segment, the error category (accuracy, fluency, terminology, style, locale convention, …), the severity (critical / major / minor), and a suggested correction. Compare against `requirements.md` and, where accuracy is in question, against the relevant `2-RAILS/` content.

Record all findings in `3-TRANSFORMATIONS/Translation/<track-name>/qa-report.md`. The QA report drives the next revision pass; a section is not considered complete until it has passed QA with no critical or major errors outstanding.

For the full list of skills that implement each step of this workflow, see [`4-SYSTEM/Skills/SKILLS-CATALOG.md`](4-SYSTEM/Skills/SKILLS-CATALOG.md).
