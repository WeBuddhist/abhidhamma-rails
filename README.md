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
