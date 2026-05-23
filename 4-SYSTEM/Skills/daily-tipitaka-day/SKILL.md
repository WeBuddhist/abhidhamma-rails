---
name: daily-tipitaka-day
description: Compose one or more Daily Tipitaka per-language day files (day-NNN.md) end-to-end. First gathers the Pāli source verses, the section summary, and the practice notes for each requested day into a per-day assets scratchpad in 0-INBOX/, stops if any asset is missing, then writes the seven-step day file using the plan template and per-language requirements. Use whenever Evan asks to create or fill in day-NNN files in any Daily Tipitaka language track (e.g. "draft days 12–17 in en").
---

# daily-tipitaka-day

This skill produces a **complete Daily Tipitaka day file** — frontmatter, the seven-step session, and the app notification — for one day at a time, in batches as requested. Without this skill, drafting a day file from scratch is slow and unreliable because the agent has to hunt for the right Pāli verses, the right section summary, and the right practice notes across three different files in `1-SOURCES/` and `2-RAILS/`. This skill makes that lookup deterministic: it writes a per-day **assets scratchpad** to `0-INBOX/daily-tipitaka/` first, halts if anything is missing, and only then composes the day file from those assets plus the template and the plan requirements.

A correct output is a day file that (1) cites only `2-RAILS/` (never `1-SOURCES/` directly), (2) matches the section/verse range declared for that day in `<lang>/schedule.md`, (3) carries the exact Pāli source with its block IDs preserved, and (4) respects the template's character caps for the app notification (Title ≤ 40, Body ≤ 120, Button ≤ 15).

---

## Inputs

The skill needs both inputs before it starts. If either is missing, ask the human contributor — do not guess.

| Input | Description | Example |
|---|---|---|
| `day-range` | One or more day numbers in the plan. Accepts `N`, `N-M` (inclusive range), or comma list `N,M,P`. | `7-11`, `12`, `15,17,19` |
| `language-tag` | The target language track. Must already exist as a folder under `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/`. | `en`, `pi`, `bo`, `zh`, `hi` |

Required files the skill reads (must already exist — if missing, stop and report):

- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/schedule.md` — maps each day to its section name and verse range.
- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/requirements.md` — the per-language style contract.
- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/_template/day-template.md` — the day file template.
- The Pāli source text for the book the day's verses come from (e.g. `1-SOURCES/Text/pi-1.md` for Book I, `pi-2.md` for Book II, `pi-3.md` for Book III). Schedule.md identifies which book.
- `2-RAILS/Sections/<book>-summaries.md` — the per-TOC-node summaries (e.g. `pi-1-summaries.md`).
- `2-RAILS/Sections/<book>-practice.md` — the per-TOC-node practice notes (e.g. `pi-1-practice.md`).

## Output

Two files per day in the range:

1. **Assets scratchpad** — `0-INBOX/daily-tipitaka/day-NNN-assets.md` (per-day; overwrite if it exists)
2. **Day file** — `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` (overwrite only if the existing file is still in unfilled template state — see Rules §3)

`NNN` is the three-digit zero-padded day number (e.g. `day-007`, `day-150`).

---

## Output file format

### Assets scratchpad (`0-INBOX/daily-tipitaka/day-NNN-assets.md`)

This is the working file the skill writes during Phase 1 and consumes during Phase 2. It is the single source of truth for what the day file will contain — if it's wrong, fix it here before generating the day file.

```markdown
---
day: <N>
language: <lang>
plan: <plan-number-from-schedule>
section: <section-name-from-schedule, e.g. "1. Cittuppādakaṇḍaṃ">
verses: <verse-range-from-schedule, e.g. "1–26">
book_source: <full path, e.g. 1-SOURCES/Text/pi-1.md>
summary_rail: <full path, e.g. 2-RAILS/Sections/pi-1-summaries.md>
summary_anchor: <e.g. ^toc-2-1-1>
practice_rail: <full path, e.g. 2-RAILS/Sections/pi-1-practice.md>
practice_anchor: <e.g. ^toc-1-1-1>
status: assets-gathered
---

# Day <N> — Assets

## Schedule entry

| Day | Date | Section | Verses |
|---|---|---|---|
| day-NNN | <date from schedule> | <section> | <verse-range> |

## Pāli source verses

<Verbatim copy of the Pāli verses from <book_source>, including their block IDs (^1-N). Preserve all heading levels (#### / ##### etc.) that fall inside the verse range. Do NOT paraphrase, translate, or reformat.>

## Section summary (from `<summary_rail>`)

<Verbatim copy of the relevant section-summary block, including its TOC anchor (^toc-N-N-N) and the commentary back-citations beneath it.>

## Practice notes (from `<practice_rail>`)

<Verbatim copy of the relevant practice block, including its TOC anchor and back-citations.>

## English translation (if a translation file exists)

<If `3-TRANSFORMATIONS/Translations/<lang>-…/<book>-…-ai.md` exists for the target language, copy the verses in the day's range here verbatim. Otherwise note "No translation file found — Reading for Meaning will be drafted from the section summary + practice + commentary back-citations." This is the only acceptable source of English prose for §4 of the day file; the skill does not translate from raw Pāli on its own.>
```

### Day file (`3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md`)

```markdown
---
day: <N>
language: <lang>
plan: <plan-number>
passage: "<Section-name>, <Subsection chain if any> — vv. <range>"
status: draft
sources:
  - 2-RAILS/Sections/<book>-summaries.md
  - 2-RAILS/Sections/<book>-practice.md
---

# Day <N> — <Thematic title drawn from the section summary>

## 1. Today's Chanting Guide

<3–5 paragraphs in the per-language register declared in requirements.md. Where the passage sits in the larger map (drawn from the section summary). One concrete question to carry into the chant. Closes with: "Today's question to carry into the chant: *…*">

## 2. Homage

![[../../assets/liturgy/vandana.md]]

## 3. Intention

![[../../assets/liturgy/intention.md]]

## 4. Reading for Meaning

### <Heading drawn from the section + verse range>

<Per-verse English (or target-language) rendering for every verse in the day's range. Each verse ends with the verse number in italics, e.g. *(v. 1)*. Drawn from the assets file's "English translation" section if present; otherwise from the section-summary synthesis. Do not invent content not present in the assets file.>

*Source: [[2-RAILS/Sections/<book>-summaries.md]], [[2-RAILS/Sections/<book>-practice.md]]*

## 5. Pāli Word of the Day

### <TERM> — <Gloss>

**Pronunciation:** <syllabified guide>

**Literal sense:** <one paragraph drawn from the practice rail or the section summary>

**In today's passage:** <one paragraph relating the term to the specific verses in this day's range>

**Why it matters:** <one paragraph drawn from the practice rail>

## 6. Chanting in Pāli

<Verbatim copy of the Pāli source verses, formatted for chanting — line breaks at clause boundaries, the closing formula in bold, every block ID preserved at the end of its verse. Heading levels preserved from the source (e.g. `##### Padabhājanī`).>

## 7. Aspiration

![[../../assets/liturgy/aspiration.md]]

## 8. App Notification

**Title:** <≤ 40 chars, e.g. "Day N — <Thematic title>">
**Body:** <≤ 120 chars, one-sentence hook>
**Button:** <optional, ≤ 15 chars, e.g. "Begin">
```

---

## Rules

1. **Phase order is fixed: assets first, day file second.** Never write the day file before its assets scratchpad exists and is complete. The assets scratchpad is the single source of truth for what goes into the day file.
2. **Stop on missing assets — do not invent content.** If the Pāli source for any verse in the day's range cannot be located by block ID, or if no summary block matches the day's section, or if no practice block matches it, halt the entire batch and report the gap to the human contributor. Do not write a partial assets file and do not move on to the next day in the batch.
3. **Do not overwrite a filled day file.** If `<lang>/days/day-NNN.md` already exists and contains anything beyond the unfilled template, stop and ask. "Unfilled template" means the file matches `day-template.md` line-for-line except for the frontmatter `day:` and `language:` values.
4. **Citation chain stays in 2-RAILS/.** The day file's `sources:` frontmatter and §4 source line cite only `2-RAILS/` paths. Never cite `1-SOURCES/` from the day file. The assets scratchpad may quote `1-SOURCES/` verbatim because it lives in `0-INBOX/` and is not cited from anywhere downstream.
5. **Pāli source is verbatim, with block IDs preserved.** §6 of the day file copies the Pāli from the assets file unchanged except for clause-level line-breaking for chant flow. Every `^1-N` block ID stays at the end of its verse.
6. **App notification character caps are hard limits.** Title ≤ 40 characters. Body ≤ 120 characters. Button (if present) ≤ 15 characters. Re-count after writing; if any cap is exceeded, tighten the wording before reporting completion.
7. **English Reading for Meaning content sources only from the assets file.** If the assets file has an "English translation" section drawn from a translation track file, §4 uses that. Otherwise §4 paraphrases the section-summary synthesis and practice notes. The skill never translates from raw Pāli on its own.
8. **Frontmatter `sources:` lists every rail the day file draws from.** At minimum: the summaries rail and the practice rail. Add the verse-rails path if `2-RAILS/Verses/<ref>.md` files exist for any verse in the day's range.
9. **One assets file per day, never one per batch.** Even if days share a section, each day gets its own `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
10. **Do not modify any file in `1-SOURCES/` or `2-RAILS/`.** This skill writes only to `0-INBOX/daily-tipitaka/` and `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/`.

---

## Procedure

### Phase 0 — Resolve inputs

1. Parse `day-range` into a sorted list of day numbers (e.g. `7-11` → `[7, 8, 9, 10, 11]`).
2. Confirm `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<language-tag>/` exists. If not, stop and report.
3. Read `<lang>/schedule.md`. For each day in the parsed list, locate the row in the "Day-by-Day Calendar" tables and record: date, plan number, section name, verse range. If a day is not in the schedule, stop and report.
4. Identify the book file for the section. The schedule's plan tables are grouped by book — Book I → `1-SOURCES/Text/pi-1.md`, Book II → `pi-2.md`, Book III → `pi-3.md`. The corresponding rails are `2-RAILS/Sections/pi-<N>-summaries.md` and `2-RAILS/Sections/pi-<N>-practice.md`.
5. Read `<lang>/requirements.md` and `<lang>/days/_template/day-template.md` once at the start of the run; cache them in working memory for use in Phase 2.

### Phase 1 — Gather assets (one per day)

For each day `N` in the range:

1. Create the directory `0-INBOX/daily-tipitaka/` if it does not exist.
2. In the book source file, locate every block from `^<chapter>-<first-verse>` to `^<chapter>-<last-verse>` inclusive. Include any `##### …` or deeper headings that fall inside the range. Copy them verbatim.
3. In the summaries rail, identify the section heading that matches the day's section + subsection. The summaries rail uses TOC anchors like `^toc-2-1-1`. Find the heading whose anchor matches the day's section position. Copy the heading, the paragraph(s) beneath it, and the commentary back-citations verbatim.
4. In the practice rail, do the same — find the heading matching the same TOC position and copy verbatim.
5. Check whether a translation file exists at `3-TRANSFORMATIONS/Translations/<lang>-*/…-ai.md` (any `<lang>-*` track). If yes, copy the verses in the day's range from that file. If no, record the note specified in the output format.
6. **If any of steps 2, 3, or 4 fail to find content, halt the entire batch.** Report which day's which asset is missing and stop. Do not write a partial assets file.
7. Write `0-INBOX/daily-tipitaka/day-NNN-assets.md` using the format above. Three-digit zero-pad the day number.

### Phase 2 — Compose the day file (one per day)

For each day `N` in the range (only after every assets file in the batch is written):

1. Read `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
2. Check whether `<lang>/days/day-NNN.md` exists and whether it is in unfilled-template state. If it is filled, stop for that day and report — do not overwrite.
3. Compose §1 (Today's Chanting Guide): 3–5 paragraphs locating the day's passage in the larger map. Draw the orientation from the section-summary block in the assets file. End with one question of the form: "Today's question to carry into the chant: *…*"
4. §2, §3, §7: copy the liturgy-transclude lines from the template unchanged.
5. Compose §4 (Reading for Meaning): per-verse renderings for every verse in the day's range, each ending with `*(v. N)*`. Source content per Rule §7.
6. Compose §5 (Pāli Word of the Day): pick a term that is named in the practice rail block as central to today's passage. Provide a pronunciation guide, literal sense, role in today's passage, and why it matters — each one paragraph. Sources: the practice rail and section summary in the assets file.
7. Compose §6 (Chanting in Pāli): copy the Pāli source section from the assets file. Break long verses at clause boundaries for chant flow. Bold the closing formula of each verse (e.g. `**ime dhammā kusalā.**`). Keep every block ID at the end of its verse.
8. Compose §8 (App Notification): thematic Title (≤ 40 chars), one-sentence Body hook (≤ 120 chars), optional Button (≤ 15 chars, default `Begin`). Re-count characters after writing — if any cap is exceeded, tighten before moving on.
9. Write the day file at `<lang>/days/day-NNN.md`. Frontmatter populated per the format above. `status: draft` always — the human contributor flips it to `partial` or `complete` after review.

### Phase 3 — Self-verification

After the whole batch is written:

1. For each day, confirm: assets file exists at `0-INBOX/daily-tipitaka/day-NNN-assets.md`; day file exists at `<lang>/days/day-NNN.md`.
2. Re-count Title and Body chars on every day's notification. Report any over-cap.
3. Confirm every day file's `sources:` frontmatter lists at least the summaries and practice rails.
4. Confirm every day file's §6 has the same number of block-ID-bearing verses as the source range. (E.g. for `verses: 1–26`, §6 should contain 26 distinct `^1-N` block IDs.)
5. Report the day numbers written, the assets file paths, and any verification warnings.

---

## Completion check

- [ ] `day-range` and `language-tag` both supplied; language folder exists
- [ ] Schedule row located for every day in the range
- [ ] Assets file written at `0-INBOX/daily-tipitaka/day-NNN-assets.md` for every day in the range
- [ ] Every assets file has non-empty Pāli source, section summary, and practice notes sections (or the batch was halted with a report)
- [ ] Day file written at `<lang>/days/day-NNN.md` for every day where assets were complete
- [ ] No existing filled day file was overwritten
- [ ] Every day file cites only `2-RAILS/` paths in `sources:` and §4
- [ ] Every day file's §6 preserves every block ID from the source range
- [ ] Every day file's app notification Title ≤ 40 chars, Body ≤ 120 chars, Button (if present) ≤ 15 chars
- [ ] Final report names every day written and flags any verification warnings
