# abhidhamma-rails

A collaborative [Obsidian](https://obsidian.md) vault for building **interpretive rails** through the Abhidhamma — the third basket of the Pali Canon.

## What a "rail" is

The Abhidhamma is a dense, technical analysis of mind and matter. Every key term carries a precise meaning, and most have been read in subtly different ways across the commentary tradition. Reading, teaching, or translating it well means resolving thousands of small interpretive decisions: which sense of *citta* is meant in this passage, what *anusaya* does here, how a compound parses, which commentator's reading to follow when they disagree.

A **rail** is a compiled, citation-grounded resolution of one such decision, attached to one verse or analytical unit. For each verse, the rails record:

- The morphology and syntax of the original
- The senses each commentator attests, with the commentary passages that establish them
- The decisions any translator would have to make
- A direct citation — file, verse, page — backing every claim

The rails sit *between* the source texts and any output built on top of them. Everything downstream — translations, study guides, lesson plans — cites a rail; every rail cites a source. Nothing is invented along the way.

```
1-SOURCES/   →   2-RAILS/   →   3-TRANSFORMATIONS/
ground truth     this vault's      generated outputs
                 interpretive
                 work
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

- [`Guidelines/0-VAULT-Structure.md`](4-SYSTEM/Guidelines/0-VAULT-Structure.md) — top-level architecture and the citation chain
- [`Guidelines/1-SOURCES-Guideline.md`](4-SYSTEM/Guidelines/1-SOURCES-Guideline.md) — rules for source files
- [`Guidelines/2-RAILS-Guideline.md`](4-SYSTEM/Guidelines/2-RAILS-Guideline.md) — schema for compiling rails
- [`Guidelines/source-formatting.md`](4-SYSTEM/Guidelines/source-formatting.md) — formatting rules for adding new source texts (frontmatter, block IDs, headings)
- [`CLAUDE.md`](4-SYSTEM/CLAUDE.md) — LLM-facing operational instructions

For day-to-day workflows (audio alignment, EPUB conversion, formatting, and so on), see the rest of `4-SYSTEM/How-to guides/` and `4-SYSTEM/Skills/`.
