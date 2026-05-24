---
name: daily-tipitaka-day
description: Compose one or more Daily Tipitaka per-language day files (day-NNN.md) end-to-end. First gathers the Pāli source verses, the section summary, and the practice notes for each requested day into a per-day assets scratchpad in 0-INBOX/, stops if any asset is missing, then writes the seven-step day file using the plan template and per-language requirements. Use whenever Evan asks to create or fill in day-NNN files in any Daily Tipitaka language track (e.g. "draft days 12–17 in en").
---

# daily-tipitaka-day

This skill produces a **complete Daily Tipitaka day file** — frontmatter, the seven-step session, and the app notification — for one day at a time, in batches as requested. Without this skill, drafting a day file from scratch is slow and unreliable because the agent has to hunt for the right Pāli verses, the right section summary, and the right practice notes across three different files in `1-SOURCES/` and `2-RAILS/`. This skill makes that lookup deterministic: it writes a per-day **assets scratchpad** to `0-INBOX/daily-tipitaka/` first, halts if anything is missing, and only then composes the day file from those assets plus the template and the plan requirements.

**Why the day file's §4 and §6 are abbreviated (first verse + last verse only).** The WeBuddhist app pulls the full verse text for a day's range from its own verse library at render time. The day file's job is *not* to reproduce all the verses — it is to give the plan-importer enough to (a) confirm the range and (b) find the first and last verses in the app library so the right range can be selected. The full text of every verse in the range lives only in the **assets scratchpad** in `0-INBOX/`, because the scratchpad is what §1 and §5 are written from. The day file's §4 and §6 print only the *first* and *last* verses of the range, each with its verse number (and, in §6, its block ID). This is a hard constraint, not a stylistic preference — the app's daily-session screen is calibrated for ~5 minutes of reading, of which most of the time is the verses themselves, leaving little room for the orientation prose around them.

**Length discipline on §1 and §5.** The casual-Buddhist audience this plan serves is calibrated for ~5-minute sessions on a phone. §1 (Today's Chanting Guide) and §5 (Pāli Word of the Day) are the two prose sections that compete with the verses for that budget, so both are kept short. See Phase 2 step 3 and step 6 for the per-section caps. The plan's outcome statement — *"come away each day ready to do a little less harm, a little more good, and know your mind a little better than before"* — is the yardstick: every paragraph in §1 and §5 should be earning its place against that, not against academic completeness.

A correct output is a day file that (1) cites only `2-RAILS/` (never `1-SOURCES/` directly), (2) matches the section/verse range declared for that day in `<lang>/schedule.md`, (3) carries the *first* and *last* Pāli verses of the range with their block IDs preserved in §6 (not the whole range), (4) respects the §1 and §5 length caps, and (5) respects the template's character caps for the app notification (Title ≤ 40, Body ≤ 120, Button ≤ 15).

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
practice_rail: <full path, e.g. 2-RAILS/Sections/pi-1-practice.md>
subsections:
  - <subsection heading text, e.g. "Padabhājanī">
  # If the day's verse range straddles two or more subsections, list each one in source order.
  # If part of the range falls outside any deeper subsection (e.g. between two ##### blocks), record the parent #### heading text instead and add a note in the relevant content section.
status: assets-gathered
---

# Day <N> — Assets

## Schedule entry

| Day | Date | Section | Verses |
|---|---|---|---|
| day-NNN | <date from schedule> | <section> | <verse-range> |

## Pāli source verses

<Verbatim copy of the Pāli verses from <book_source>, including their block IDs (^1-N). Preserve every heading at any level (`###`, `####`, `#####`, `######`) that falls inside the verse range or sits immediately above the first verse — chapter and section headings carry orientation context, do not strip them. Do NOT paraphrase, translate, or reformat.>

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

<**Hard cap: ~2 short paragraphs (max ~180 words total) plus the closing question.** Plain language. One sentence that locates the passage in the larger map (drawn from the section summary), then one short paragraph naming what the day's verses actually walk through and why it matters for a casual practitioner. Skip exhaustive structural commentary — that belongs in the rails, not here. Closes with: "Today's question to carry into the chant: *…*">

## 2. Homage

![[../../assets/liturgy/vandana.md]]

## 3. Intention

![[../../assets/liturgy/intention.md]]

## 4. Reading for Meaning

**Verses <A>–<B>.** *(Full text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below so the plan-importer can find the right entries.)*

**v. <A>.** <First verse of the range in the target language, taken verbatim from the assets file's "English translation" section.>

…

**v. <B>.** <Last verse of the range in the target language, taken verbatim from the assets file's "English translation" section.>

*Source: [[2-RAILS/Sections/<book>-summaries.md]], [[2-RAILS/Sections/<book>-practice.md]]*

## 5. Pāli Word of the Day

### <TERM> — <Gloss>

**Pronunciation:** <syllabified guide, one line>

**In today's passage:** <2–4 sentences: what the word does in this specific day's verses, drawn from the practice rail and section summary.>

**Why it matters:** <2–4 sentences: how the word changes how the practitioner sees their own mind, drawn from the practice rail. End on something a casual reader can carry into the day — less harm, more good, knowing their mind a little better.>

**Hard cap on §5: ~140 words total across pronunciation + the two paragraphs.** Do not add a separate "Literal sense" or "Etymology" paragraph — fold any literal-sense note into "In today's passage" if it earns its place.

## 6. Chanting in Pāli

**Verses <A>–<B>.** *(Full Pāli text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below — with their block IDs — so the plan-importer can find the right entries.)*

<If the verse range opens inside a named subsection of the source text, name it on one line before the first verse — e.g. `Section: Suññatavāro → Rūpāvacarakusalaṃ → Catukkanayo`. If the range straddles one or more new headings, name those too. Do **not** print full heading blocks; the plan-importer needs orientation, not the full TOC.>

**<A>.** <First Pāli verse of the range, verbatim from the assets file, formatted for chanting (clause-level line breaks, closing formula in bold). Block ID preserved at the end: `^<book>-<A>`.>

…

**<B>.** <Last Pāli verse of the range, verbatim from the assets file, same formatting. Block ID preserved at the end: `^<book>-<B>`.>

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
2. **Stop on missing assets — do not invent content.** Halt the entire batch and report the gap to the human contributor if any of the following is true for any day in the range. "Missing" covers both shapes:
   - **Shape A — not found at all.** The Pāli source for a verse in the range cannot be located by block ID; or the source text file itself doesn't exist; or the summary/practice rail file doesn't exist; or no heading matching the day's subsection text appears in the rail.
   - **Shape B — found but empty.** The heading exists in the rail but the content beneath it is empty, is only a TOC back-link, or contains scaffold-only markers (e.g. `[[#^toc-…|↑↑↑]]` with no narrative paragraphs underneath).
   In both shapes, do not write a partial assets file and do not move on to the next day in the batch. Report which day, which asset, and which shape so the human contributor can fix the rail or the schedule.
3. **Do not overwrite a filled day file.** If `<lang>/days/day-NNN.md` already exists and contains anything beyond the unfilled template, stop and ask. "Unfilled template" means the file matches `day-template.md` line-for-line except for the frontmatter `day:` and `language:` values.
4. **Citation chain stays in 2-RAILS/.** The day file's `sources:` frontmatter and §4 source line cite only `2-RAILS/` paths. Never cite `1-SOURCES/` from the day file. The assets scratchpad may quote `1-SOURCES/` verbatim because it lives in `0-INBOX/` and is not cited from anywhere downstream.
5. **Day file's §4 and §6 print first verse + last verse only.** Not the whole range. The WeBuddhist app pulls the full verses from its own library at render time; the day file's job is to give the plan-importer enough to find the right range. The two verses are taken verbatim from the assets file (§6 from the Pāli source section, §4 from the English translation section). Both block IDs (`^<book>-<first>` and `^<book>-<last>`) are preserved at the end of their verses in §6.
6. **Assets scratchpad always carries the full verse range.** This is the source of truth §1 and §5 are written from. The "first verse + last verse only" rule applies to the *day file*, never to the assets file.
7. **§1 length cap: ~180 words.** Two short paragraphs maximum, plus the closing question. If the draft exceeds the cap, cut — do not add a third paragraph and trim the first two.
8. **§5 length cap: ~140 words.** Pronunciation line + "In today's passage" (2–4 sentences) + "Why it matters" (2–4 sentences). No separate "Literal sense" paragraph; fold any literal-sense note into "In today's passage" if it pays its way.
9. **App notification character caps are hard limits.** Title ≤ 40 characters. Body ≤ 120 characters. Button (if present) ≤ 15 characters. Re-count after writing; if any cap is exceeded, tighten the wording before reporting completion.
10. **English Reading for Meaning content sources only from the assets file.** If the assets file has an "English translation" section drawn from a translation track file, §4 uses the first and last verses from it verbatim. If no translation file exists, §4 falls back to a *one-line* gloss of the first and last verses drawn from the section summary — never a fresh translation from Pāli.
11. **Frontmatter `sources:` lists every rail the day file draws from.** At minimum: the summaries rail and the practice rail. Add the verse-rails path if `2-RAILS/Verses/<ref>.md` files exist for any verse in the day's range.
12. **One assets file per day, never one per batch.** Even if days share a section, each day gets its own `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
13. **Do not modify any file in `1-SOURCES/` or `2-RAILS/`.** This skill writes only to `0-INBOX/daily-tipitaka/` and `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/`.

---

## Procedure

### Phase 0 — Resolve inputs

The goal of Phase 0 is to turn each requested day number into a concrete lookup plan: *which range of verses to fetch, from which source file, with which rail files alongside it.* Nothing is read from the source text yet — that's Phase 1.

1. Parse `day-range` into a sorted list of day numbers (e.g. `7-11` → `[7, 8, 9, 10, 11]`).
2. Confirm `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<language-tag>/` exists. If not, stop and report.
3. **Get the verse range for each day from `<lang>/schedule.md`.** This is the schedule's primary job — it owns the day → verse-range mapping. Open `<lang>/schedule.md`, find the row for each requested day in the "Day-by-Day Calendar" tables, and record from that row: the date, the plan number (from the surrounding `### Plan N — Days A–B …` heading), the section name, and the verse range (the rightmost column, e.g. `1–26`). If a day is not in the schedule, stop and report.
4. **Resolve the verse range to a source file and a block-ID range.** Schedule rows are grouped by book: Plans 1–5 = Book I (Dhammasaṅgaṇī), Plans 6–23 = Book II (Vibhaṅga), Plans 24–27 = Book III (Dhātukathā). Map the book to its files:

   | Book | Source text | Summaries rail | Practice rail | Block-ID prefix |
   |---|---|---|---|---|
   | I | `1-SOURCES/Text/pi-1.md` | `2-RAILS/Sections/pi-1-summaries.md` | `2-RAILS/Sections/pi-1-practice.md` | `^1-` |
   | II | `1-SOURCES/Text/pi-2.md` | `2-RAILS/Sections/pi-2-summaries.md` | `2-RAILS/Sections/pi-2-practice.md` | `^2-` |
   | III | `1-SOURCES/Text/pi-3.md` | `2-RAILS/Sections/pi-3-summaries.md` | `2-RAILS/Sections/pi-3-practice.md` | `^3-` |

   The block IDs in these source files follow the Bible-style scheme `^<book>-<verse>` (declared in each file's `verse_id_format: book-verse` frontmatter — see `4-SYSTEM/Guidelines/abhidhamma-annex.md`). So for day-007 in Book I with range `1–26`, the lookup target is "every block from `^1-1` through `^1-26` in `1-SOURCES/Text/pi-1.md`."

The per-language `requirements.md` and `day-template.md` are not read in Phase 0 — they are read in Phase 2 at the moment of composition, so a Phase 1 halt doesn't waste a read.

#### Worked example — day-007

Phase 0 turns the schedule row into a lookup plan; Phase 1 executes the lookups. For day-007:

| What | Value | Where the skill finds it |
|---|---|---|
| Day number | 7 | Input |
| Schedule row | `\| day-007 \| 20 May (Thu) \| 1. Cittuppādakaṇḍaṃ \| 1–26 \|` | `<lang>/schedule.md` |
| Plan heading above the row | `### Plan 2 — Days 7–37 · Consciousness (20 May–19 Jun)` | `<lang>/schedule.md` |
| Book | Book I | Plans 1–5 = Book I (lookup table above) |
| Source text file | `1-SOURCES/Text/pi-1.md` | Lookup table above |
| Block-ID range | `^1-1` through `^1-26` (26 blocks) | Source text file |
| Subsection containing the range | `Padabhājanī` | `##### Padabhājanī ^1-1-1-1-0` heading just before `^1-1` in the source text |
| Summary rail | `2-RAILS/Sections/pi-1-summaries.md` | Lookup table above |
| Summary block to copy | `#### Padabhājanī` (lines 313–322) | Summary rail, matched by subsection text |
| Practice rail | `2-RAILS/Sections/pi-1-practice.md` | Lookup table above |
| Practice block to copy | `### Padabhājanī` (lines 110–120) | Practice rail, matched by subsection text |

### Phase 1 — Gather assets (one per day)

The goal of Phase 1 is to copy the actual verse text (and the matching summary + practice blocks) out of the source files and into a per-day scratchpad in `0-INBOX/`. By the end of Phase 1 every day's scratchpad is self-contained — Phase 2 never needs to touch `1-SOURCES/` or `2-RAILS/` again.

For each day `N` in the range:

1. Create the directory `0-INBOX/daily-tipitaka/` if it does not exist.
2. **Copy the Pāli verses for the day's range.** Open the source text file resolved in Phase 0 step 4. Find every block whose ID is in the day's range — i.e. for a range of `A–B` with block-ID prefix `^P-`, every block from `^P-A` to `^P-B` inclusive. Copy each block verbatim, in source order, preserving **every heading at any level** (`###`, `####`, `#####`, `######` — any that appear inside the range or immediately above the first verse). Chapter (`###`) and section (`####`) headings carry orientation the chanter needs, even though they may seem "too high level"; do not strip them. Do not paraphrase, translate, or reformat.

   *Examples:*
   - *Day-007: scans `1-SOURCES/Text/pi-1.md` and copies the blocks ending in `^1-1`, `^1-2`, … `^1-26` — 26 blocks in total, including the `##### Padabhājanī ^1-1-1-1-0` heading just before `^1-1`.*
   - *Day-012 (verses 151–163): the range straddles the closing definition-blocks of the 5th–8th kāmāvacaramahākusalacittāni (following the `##### Suññatavāro` pattern established at v145) and opens the new `#### Rūpāvacarakusalaṃ` section with its `##### Catukkanayo` subsection — both the closing `Dutiyabhāṇavāro` marker at the end of v159 and the new `####` and `#####` headings between v159 and v160 must be preserved in the assets file.*
3. **Identify the subsection(s) the day's verse range falls inside.** The schedule.md row only names the top-level section (e.g. `1. Cittuppādakaṇḍaṃ`); the summary and practice rails are organized by *subsection* (Padabhājanī, Koṭṭhāsavāro, Suññatavāro). So the skill has to derive the subsection from the source text:

   1. While scanning the source text in step 2, track the most recent `##### …` heading above each verse. That heading is the subsection.
   2. Record the *text* of every distinct subsection heading the day's range falls under — usually one, occasionally two if the range straddles a boundary.
   3. The heading text alone is the lookup key for steps 4 and 5. Heading text is identical across the source text, the summary rail, and the practice rail — only the heading level and anchor format differ. (For day-007 the recorded subsection is `Padabhājanī`. For day-011 the range `121–150` straddles `Suññatavāro` (verses 121–145) and the un-headed Cittas 2–5 block (146–150) — record `Suññatavāro` and note in the assets file that 146–150 sit under the parent `Kāmāvacarakusalaṃ` rather than under any deeper subsection.)

4. **Copy the matching section summary from the summary rail.** Open the summaries rail resolved in Phase 0 step 4 (e.g. `2-RAILS/Sections/pi-1-summaries.md`). For each subsection text recorded in step 3, find a heading whose text matches — **match by text, not by heading level**. The heading level varies depending on how deeply the subsection sits in the TOC (in `pi-1-summaries.md`, chapter-level sections like `Kāmāvacarakusalaṃ` sit at `###` while deeper subsections like `Padabhājanī` sit at `####`). Copy: the heading line, the `[[#^toc-…|↑↑↑]]` back-link, the paragraph(s) beneath, and the commentary back-citation lines, up to (but not including) the **next heading at the same level or shallower**. If the same heading text appears more than once in the rail (rare — `Catasso paṭipadā (Rūpāvacara)` is the only known case in Book I), disambiguate by walking up the heading hierarchy to find the one whose parent heading matches the top-level section named in the schedule row.

   *Example: for day-007 the skill looks for `Padabhājanī` in `2-RAILS/Sections/pi-1-summaries.md`. It finds `#### Padabhājanī` at line 313 and copies down to just before the next `####` heading (`#### Koṭṭhāsavāro` at line 323).*
5. **Copy the matching practice notes from the practice rail.** Open the practice rail resolved in Phase 0 step 4 (e.g. `2-RAILS/Sections/pi-1-practice.md`). Same procedure as step 4 — **match by heading text, not by level**. The practice rail's heading levels run one level shallower than the summary rail (in `pi-1-practice.md`, chapter-level sections like `Kāmāvacarakusalaṃ` sit at `##` and deeper subsections like `Padabhājanī` sit at `###`), but the heading *text* is identical across both rails and the source text. Copy from the matching heading down to the next heading at the same level or shallower, or the next `---` divider if the rail uses dividers between entries.

   *Example: for day-007 the skill looks for `Padabhājanī` in `2-RAILS/Sections/pi-1-practice.md`. It finds `### Padabhājanī` at line 110 and copies down to just before `### Koṭṭhāsavāro` at line 121.*
6. **Copy the English translation if a translation track exists.** Check `3-TRANSFORMATIONS/Translations/<lang>-*/…-ai.md` (any `<lang>-*` track folder, e.g. `en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md`). If found, locate the same block-ID range as in step 2 and copy those verses. If not, record the note specified in the assets-file format above.
7. **If any of steps 2, 4, or 5 fail to find content, halt the entire batch.** Report which day's which asset is missing (verses, summary, or practice) and stop. Do not write a partial assets file and do not move on to the next day. A missing translation file (step 6) is not a halt condition — the assets file records the note and Phase 2 falls back to paraphrasing from the summary + practice.
8. Write `0-INBOX/daily-tipitaka/day-NNN-assets.md` using the format in the *Output file format* section above. Three-digit zero-pad the day number (e.g. day 7 → `day-007-assets.md`).

#### Phase 1 completion check (gate)

After Phase 1 has run for every day in the batch, verify *all* of the following before moving on. **If any check fails, stop. Do not start Phase 2.** Report the gap to the human contributor.

- [ ] One assets file exists at `0-INBOX/daily-tipitaka/day-NNN-assets.md` for every day in the requested range.
- [ ] Every assets file's frontmatter has a non-empty `section`, `verses`, `book_source`, `summary_rail`, and `practice_rail`.
- [ ] Every assets file's "Pāli source verses" section contains the same number of distinct block IDs as the day's verse range. (For range `A–B` with prefix `^P-`, the section should contain `B − A + 1` blocks from `^P-A` to `^P-B`.)
- [ ] Every assets file's "Section summary" section is non-empty and contains the matching `#### <subsection-text>` heading from the summary rail.
- [ ] Every assets file's "Practice notes" section is non-empty and contains the matching `### <subsection-text>` heading from the practice rail.
- [ ] No day was silently skipped because of a missing asset — every halt was reported.

If every check passes, report the list of assets files written and proceed to Phase 2. If you want to inspect or edit the assets files before composition, this is the natural pause point.

### Phase 2 — Compose the day file (one per day)

Read these files once at the start of Phase 2 (before the per-day loop). They are the same for every day in the batch:

- `<lang>/days/_template/day-template.md` — the seven-step day file shape and the liturgy transclude lines.
- `<lang>/requirements.md` — the per-language plan style contract (register, format conventions, tone) that governs how §1, §4, §5, and §8 are written. **Important:** at the bottom of this file there is a pointer to a *translation track requirements file* — for English the pointer reads `../Translations/en-Contemporary-English-Abhidhamma/requirements.md`. Follow that pointer and read the translation track requirements too. It is the file that actually governs how Pāli renders into the target language (handling of repeated formulas, treatment of compound terms, sentence length, transliteration policy) — without it, §4 (Reading for Meaning) will drift in style from the rest of the translation track.
- `3-TRANSFORMATIONS/Translations/<lang>-<TrackName>/requirements.md` — the per-language translation track style contract, located via the pointer above. The track-name suffix varies (e.g. `en-Contemporary-English-Abhidhamma`); use the path the plan requirements names, do not guess. If the plan requirements does not point to a translation track requirements file for this language (e.g. for a newly-scaffolded language with no translation track yet), record that gap in the run report and proceed using the plan requirements alone — do not invent translation conventions.

Then for each day `N` in the range (only after every assets file in the batch is written):

1. Read `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
2. Check whether `<lang>/days/day-NNN.md` exists and whether it is in unfilled-template state. If it is filled, stop for that day and report — do not overwrite.
3. Compose §1 (Today's Chanting Guide). **Hard cap ~180 words** (two short paragraphs + closing question). One short paragraph that says where the passage sits in the larger map (drawn from the section summary). One short paragraph that says what the day's verses walk through, in plain language. End with the closing line: "Today's question to carry into the chant: *…*" Write for a casual practitioner with five minutes — the test is whether they could read it before reaching the verses and still feel oriented, not whether it covers every structural feature of the passage. Cut, don't expand.
4. §2, §3, §7: copy the liturgy-transclude lines from the template unchanged.
5. Compose §4 (Reading for Meaning) using **only the first and last verses** of the day's range, in this shape:
   - One header line: `**Verses A–B.** *(Full text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below so the plan-importer can find the right entries.)*`
   - Then `**v. A.** <first verse, verbatim from the assets file's "English translation" section>`
   - Then a separator line containing only `…`
   - Then `**v. B.** <last verse, verbatim from the assets file's "English translation" section>`
   - Then `*Source: [[2-RAILS/Sections/<book>-summaries.md]], [[2-RAILS/Sections/<book>-practice.md]]*`
   Do not paraphrase the verses; take them verbatim from the assets file (Rule §10). The translation track requirements file is what governs the wording of the assets-file translation, not this skill — by the time §4 is being composed, those decisions are already baked into the assets text.
6. Compose §5 (Pāli Word of the Day). **Hard cap ~140 words.** Pick a term named in the practice rail block as central to today's passage. Three parts in this order:
   - `### <TERM> — <short English gloss>`
   - `**Pronunciation:** <syllabified guide, one line>`
   - `**In today's passage:** <2–4 sentences on what the word does in the day's verses, drawn from the practice rail and section summary. Fold any literal-sense note in here if it earns its place.>`
   - `**Why it matters:** <2–4 sentences on how the word changes how the practitioner sees their own mind, drawn from the practice rail. End on something a casual reader can carry — less harm, more good, knowing their mind a little better.>`
   No separate "Literal sense" or "Etymology" paragraph. Re-count words after writing; cut if over cap.
7. Compose §6 (Chanting in Pāli) using **only the first and last Pāli verses** of the day's range, in this shape:
   - One header line: `**Verses A–B.** *(Full Pāli text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below — with their block IDs — so the plan-importer can find the right entries.)*`
   - If the verse range opens inside a named subsection of the source text, name it on one orientation line before the first verse — e.g. `**Section:** Suññatavāro → Rūpāvacarakusalaṃ → Catukkanayo`. If the range straddles new headings, name them too. Do **not** print full heading blocks; the plan-importer needs orientation, not the full TOC.
   - Then `**A.** <first Pāli verse, verbatim from the assets file, formatted for chanting (clause-level line breaks, closing formula in bold). Block ID `^<book>-<A>` at the end.>`
   - Then a separator line containing only `…`
   - Then `**B.** <last Pāli verse, same shape, ending with block ID `^<book>-<B>`.>`
8. Compose §8 (App Notification): thematic Title (≤ 40 chars), one-sentence Body hook (≤ 120 chars), optional Button (≤ 15 chars, default `Begin`). Re-count characters after writing — if any cap is exceeded, tighten before moving on.
9. Write the day file at `<lang>/days/day-NNN.md`. Frontmatter populated per the format above. `status: draft` always — the human contributor flips it to `partial` or `complete` after review.

#### Phase 2 completion check

After Phase 2 has run for every day in the batch:

- [ ] One day file exists at `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` for every day whose Phase 1 assets file was complete.
- [ ] No pre-existing filled day file was overwritten — any conflict was reported instead.
- [ ] Every day file's `sources:` frontmatter lists at least the summaries rail and the practice rail.
- [ ] Every day file's §4 (Reading for Meaning) contains **exactly two** verse-numbered entries: the first verse of the range (`**v. A.**`) and the last (`**v. B.**`), separated by a `…` divider line. No other verses.
- [ ] Every day file's §6 (Chanting in Pāli) contains **exactly two** distinct block IDs: `^<book>-A` (on the first verse) and `^<book>-B` (on the last verse), separated by a `…` divider line. No other block IDs.
- [ ] §1 word count ≤ ~180 words (re-count after writing). Cut if over.
- [ ] §5 word count ≤ ~140 words (re-count after writing). Cut if over.
- [ ] Every day file's §8 app notification has: Title ≤ 40 chars, Body ≤ 120 chars, Button (if present) ≤ 15 chars. Re-count after writing.

Report the day numbers written, the assets file paths, the day file paths, and any verification warnings.

---

## Completion check

This skill has two internal gates. A run is complete only when both pass.

**Phase 0 + Phase 1 (assets):**

- [ ] `day-range` and `language-tag` both supplied; language folder exists
- [ ] Schedule row located for every day in the range
- [ ] Phase 1 completion check passes for every day — assets file written and verified (see *Phase 1 completion check (gate)* above)
- [ ] No day silently skipped; every halt reported

**Phase 2 (day files):**

- [ ] Phase 2 completion check passes for every day (see *Phase 2 completion check* above) — day file written, no overwrites, citations clean, block IDs preserved, notification character caps respected
- [ ] Final report names every assets file path, every day file path, and any verification warnings
