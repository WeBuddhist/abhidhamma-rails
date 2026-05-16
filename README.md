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

Producing a reliable AI-assisted translation from the rails requires three sequential phases: **context preparation**, **translation**, and **QA**. Each phase exists to defuse one of the three core failure modes of AI translation:

| Failure mode | Where it is addressed |
|---|---|
| Hallucinations — fabricated meaning at section or verse level | Context preparation → `2-RAILS/Sections/`, `2-RAILS/Verses/`, `2-RAILS/Local-Wiki/` |
| Inconsistent vocabulary — the same Pali term rendered differently across passages | Context preparation → `2-RAILS/Glossaries/` and the per-track glossary in `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md` |
| Inconsistent style over long texts | `requirements.md` for the track (binding style contract) + QA phase using the MQM taxonomy |

### Phase 1 — Translation context preparation

#### 1a. Section-level factual context (`2-RAILS/Sections/`)

For every node in the table of contents, generate a summary **in the original language** (Pali or the commentary language) drawn directly from each relevant commentary, preserving that commentary's own terminology without translating it. Each commentary gets its own file under `Sections/Raw/<commentary-name>/<node-id>.md` — one summary per node per commentary, so the per-commentary readings stay separable. Then, in `Sections/<node-id>.md`, combine the per-commentary summaries for that node and add an English translation of the combined summary. These combined files are what the translation skill loads to orient itself before tackling a section.

#### 1b. Verse-level factual context (`2-RAILS/Verses/`)

For each verse, create a context file that (1) transcludes the relevant commentary passages, (2) synthesises the commentators' respective interpretations in the original language, and (3) uses that synthesis to produce a **disambiguated version of the verse in the original language** — a restatement precise enough that no misreading or mistranslation of the Pali is possible. The translation skill works from this disambiguated version, not from the raw verse.

#### 1c. Word-level factual context (`2-RAILS/Local-Wiki/`)

For each key term explained in the commentaries, create a Local-Wiki article. Populate it with citations from the commentaries (in the original language) and a short contextual explanation drafted from those citations. All content in the Local-Wiki is in the original language. These articles are the reference of last resort when a glossary entry does not yet capture a term adequately.

#### 1d. Glossaries (`2-RAILS/Glossaries/`)

For each existing translation or relevant reference text, extract every keyword and the rendering(s) it uses into a raw glossary file under `Glossaries/Raw/<source-name>.md`. Then combine the raw files into a consolidated glossary per language pair under `Glossaries/<source-lang>-<target-lang>.md`, with every attested rendering shown side by side. When setting up a new translation track, select the preferred rendering for each term from the consolidated glossary — guided by the track's `requirements.md` — and write a translation-specific glossary into `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md`. If no existing rendering is satisfactory, use the Local-Wiki article for that term to derive a better one and record the new rendering back into both the per-track glossary and the consolidated glossary.

#### 1e. Translation requirements (`3-TRANSFORMATIONS/Translation/<track-name>/requirements.md`)

Each translation track is governed by a `requirements.md` written in the target language. This file is a binding contract that the translation skill reads on every run; if it is incomplete, the translation will drift in style and the QA phase will catch it as MQM "style" or "locale convention" errors. Before running any translation, verify that the document covers, at minimum:

- **Target audience and register** (scholarly, lay, monastic, …) and reading level.
- **Glossary reference path** — relative path to the per-track glossary.
- **Preferred rendering for structurally significant terms** that recur across the text and must never vary.
- **Style constraints** — sentence length, paragraph length, handling of verse vs. prose, treatment of lists, use vs. transliteration of technical Pali terms, footnote vs. inline glossing policy.
- **Cultural-adaptation rules** — what to translate, what to gloss, what to leave untranslated.
- **Source-rail dependencies** — which rails (`Sections/`, `Verses/`, `Local-Wiki/`) the translator must consult before each batch.

Anything the translation skill needs to know to behave consistently across thousands of verses lives here.

### Phase 2 — Translation

Working in small batches through the table of contents — one or a few TOC nodes at a time, never the whole text at once:

1. **Select** a small batch of nodes from the table of contents.
2. **Fetch the per-track glossary** from `3-TRANSFORMATIONS/Translation/<track-name>/glossary.md`.
3. **Fetch context at every relevant level from `2-RAILS/`**: the combined section summary for each node in the batch (`Sections/`), the verse-context file for every verse it contains (`Verses/`), and any Local-Wiki articles for terms that appear in the batch but aren't covered by the glossary.
4. **Translate and write** the result into `3-TRANSFORMATIONS/Translation/<track-name>/`, creating the file or updating it in place. The translation file's frontmatter must list the rails it was generated from.

Hard rules: never translate a batch without first loading all three levels of context; never introduce a keyword rendering that is not in the per-track glossary without recording the new rendering in the glossary first (and feeding it back into the consolidated glossary under `2-RAILS/Glossaries/`).

### Phase 3 — Translation QA

Review each translated section against the **MQM (Multidimensional Quality Metrics) error taxonomy**, comparing the translation back to `requirements.md` and — wherever an accuracy or terminology question arises — to the corresponding `2-RAILS/Sections/`, `2-RAILS/Verses/`, and `2-RAILS/Local-Wiki/` files. For each issue found, record:

- the segment (verse ID or paragraph anchor),
- the MQM error category (accuracy, fluency, terminology, style, locale convention, …),
- severity (critical / major / minor),
- and a suggested correction.

All findings go into `3-TRANSFORMATIONS/Translation/<track-name>/qa-report.md`. That report drives the next revision pass. A section is not considered complete until it has passed QA with no critical or major errors outstanding.

For the full list of skills that implement each step of this workflow, see [`4-SYSTEM/Skills/SKILLS-CATALOG.md`](4-SYSTEM/Skills/SKILLS-CATALOG.md).
