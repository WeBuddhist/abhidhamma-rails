# 4-SYSTEM — Methodology and tooling

This folder holds everything the vault needs to *operate*: the guidelines that define the methodology, the skills that automate every workflow step, the how-to guides for contributors, the templates for new files, and the LLM-facing operational instructions.

Nothing here is project content. Project content lives in `1-SOURCES/`, `2-RAILS/`, and `3-TRANSFORMATIONS/`. This folder is the *operating system* of the vault: read the guidelines to understand the rules, invoke the skills to do the work, follow the how-to guides for hand operations.

## What's here

- **[`CLAUDE.md`](CLAUDE.md)** — operational instructions for an AI agent. Citation chain, write permissions, do-nots, standard operations. The first thing any agent reads when it picks up work in this vault.
- **[`Guidelines/`](Guidelines/)** — the rules. Text-agnostic by default, with one Abhidhamma-specific annex.
 - [`why-rails.md`](Guidelines/why-rails.md) — the Wikipedia ↔ rails analogy.
 - [`0-VAULT-Structure.md`](Guidelines/0-VAULT-Structure.md) — top-level architecture and citation chain.
 - [`../../1-SOURCES/About Sources.md`](../1-SOURCES/About Sources.md) — rules for source files (frontmatter, block IDs, language tags, file format per type, linking).
 - [`../../2-RAILS/About Rails.md`](../2-RAILS/About Rails.md) — rails schema (disambiguation stack, verse package layout, bilingual glossary chain).
 - [`../../3-TRANSFORMATIONS/About Transformations.md`](../3-TRANSFORMATIONS/About Transformations.md) — rules for translation tracks and other output streams.
 - [`abhidhamma-annex.md`](Guidelines/abhidhamma-annex.md) — conventions specific to *this* vault (Pāli Bible-style addressing, the commentary roster, the language tracks).
- **[`Skills/`](Skills/)** — the operators. Each skill is a SKILL.md (instructions for an LLM) and optional helper scripts. See [`SKILLS-CATALOG.md`](Skills/SKILLS-CATALOG.md) for the full list grouped by pipeline phase: source ingestion → rails-building → translation requirements → translation → QA.
- **[`How-to guides/`](How-to%20guides/)** — human-facing instructions for non-AI tasks (set up the vault, sync and troubleshoot, oTranscribe workflow, Obsidian Git troubleshooting).
- **[`Templates/`](Templates/)** — blank templates for new files in each folder.
- **`gemini-scribe/`** — configuration and instructions for the Gemini Scribe plugin (`AGENTS.md`, Prompts/, Scheduled-Tasks/, Background-Tasks/, Agent-Sessions/, Skills/).

## Reading order

The canonical reading orders live in the top-level [`README.md`](../README.md) — one path for human contributors, one path for AI agents. This folder's content slots into both of those paths. Don't read this folder in isolation; start at the top-level README.
