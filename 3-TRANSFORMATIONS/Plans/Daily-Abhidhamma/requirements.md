---
brief_id: daily-abhidhamma
audience: ITCC participants and prospective participants — practitioners preparing to chant the Abhidhamma Piṭaka together in Bodhgayā, December 2026
output: 200 daily reading-and-chanting sessions, one per day, each delivered in multiple languages
collaborator: International Tipiṭaka Chanting Council (ITCC)
upstream_brief:../../0-INBOX/Daily Abhidhamma Brief.md
status: draft
---

# Daily Abhidhamma — Brief

## 1. Purpose

The Daily Abhidhamma is a 200-day journey of daily Abhidhamma reading and chanting that prepares practitioners for the International Tipiṭaka Chanting Council (ITCC) gathering at Bodhgayā in December 2026, where thousands will chant the Abhidhamma Piṭaka together at the site of the Buddha's enlightenment.

The journey does two things at once. **Meaning** — it lets the Abhidhamma gradually unfold in the practitioner's mind, day by day, page by page. **Voice** — it trains practitioners to carry the Pāli words with confidence and devotion when the chanting in Bodhgayā begins. Every session is both a step toward understanding and an act of offering.

Reference site: <https://lbdfi.org/daily-abhidhamma/>.

## 2. Audience

> Detailed audience profile lives in [`audience.md`](./audience.md). The bullets below are the headline summary; the profiling detail (demographics, prior knowledge, use cases, motivations) lives there.

- Lay practitioners across the Theravāda world, including newcomers to the Abhidhamma.
- Monastic participants of the ITCC chanting cohort.
- Anyone preparing to attend or follow the Bodhgayā gathering online.

No prior mastery of the Abhidhamma is assumed. The brief is _"we don't need to master the Abhidhamma before we begin; we just need to begin."_

## 3. Daily Session Structure (Seven Steps)

Every day follows the same seven-step shape. The order is fixed; the content is what changes day to day. This shape is the contract between this brief and every per-day file under `days/<lang>/day-NNN.md`.

1. 🧭 **Today's Chanting Guide** — a short note orienting us to the day's passage and how it connects to the path.
2. 🪔 **Homage** — Vandanā to the Buddha (Pāli always; gloss in target language).
3. 🌱 **Intention** — the Buddha's own four-line summary of the path (Pāli always; gloss).
4. 💡 **Reading for Meaning** — the day's passage in the reader's language, so the text is alive in mind before chanting.
5. 🔑 **Pāli Word of the Day** — one key word to carry as an anchor.
6. ☸️ **Chanting in Pāli** — the passage chanted unhurried and attentive.
7. ✨ **Aspiration** — a closing dedication: avoid evil, cultivate good, purify the mind.

Seven steps. Every day. For 200 days.

Steps 2, 3, 6, and 7 use **fixed liturgical Pāli** that does not change day to day — see `assets/liturgy/`. Steps 1, 4, 5 are the **variable content** generated from the rails.

## 4. Rails the Content Draws From

Per the vault citation chain (`1-SOURCES/ → 2-RAILS/ → 3-TRANSFORMATIONS/`), every claim in a Daily Abhidhamma file traces back to:

- A **verse rail** under `2-RAILS/Verses/` for each passage chanted that day (the source of the morphology, the senses each commentator attests, and the translation decisions).
- A **section rail** under `2-RAILS/Sections/` for the day's chanting guide (where this passage sits in the larger map of the Abhidhamma).
- A **local-wiki page** under `2-RAILS/Local-Wiki/` for the Pāli Word of the Day (the attested sense being foregrounded).
- A **bilingual glossary entry** under `2-RAILS/Bilingual-Glossaries/pi-<lang>.md` for every translated term in the Reading for Meaning, so each language track stays consistent across the 200 days.

Each day's frontmatter `sources:` field lists the specific rails it draws from.

## 5. Languages

The Daily Abhidhamma is published in multiple languages so practitioners can read the meaning in their own tongue while still chanting in Pāli. The folder `days/` holds one subfolder per language tag:

- `pi/` — Pāli (source language; meaning gloss kept minimal, Pāli analysis foregrounded)
- `en/` — English
- `bo/` — Tibetan
- `zh/` — Chinese
- `hi/` — Hindi

Currently scaffolded: **day-001 through day-010** in each language. The remaining 190 days will be added plan by plan from `days/_template/day-template.md` as content is written.

Adding a new language is a matter of creating a new `days/<tag>/` folder and copying the day files from `_template/`. The Pāli chanting in Step 6 is **identical across every language track** — it is the same chant in every language, just glossed differently in the surrounding steps.

The Reading for Meaning (Step 4) in each language is generated using the translation requirements that govern that target language — for English, see `../Translations/en-Contemporary-English-Abhidhamma/requirements.md`. As other-language translation requirements come online, they sit next to that one.

## 6. The 200-Day Schedule — Plans of a Few Days Each

The 200 days are not a single uninterrupted scroll. They are organised into **plans** — short arcs of a few days each, where each plan covers one coherent unit of the Abhidhamma (a mātikā cluster, a chapter, a topic, etc.). A plan is the smallest committable rhythm: a practitioner can start the next plan even if they missed the last one.

Each plan is one file under `plans/`, naming the days it covers, the passages it walks through, and the arc it traces.

- `plans/plans.md` — the index of all plans, day ranges, and topics.
- `plans/plan-001-<slug>.md`, `plans/plan-002-<slug>.md`, … — one file per plan.
- `schedule/calendar.md` — the master calendar mapping day-001 … day-200 to real-world dates, and plans to weeks.

The plans-of-a-few-days structure is what makes the journey survivable. It is also what makes the communications cadence (announcements, milestone moments) align with natural break-points instead of arbitrary day numbers.

## 7. Communications & Supporting Material

The journey is not just the daily content. It needs an outreach and care layer around it:

- `communications/announcements/` — launch announcements, mid-journey rallies, run-up to Bodhgayā messaging. One file per announcement, dated.
- `communications/notifications/` — the daily push notification copy. Short, warm, anchored to the day's passage.
- `communications/social-media/` — posts for each plan milestone, sample-day teasers, practitioner testimonials.
- `assets/liturgy/` — fixed Pāli liturgy (Vandanā, Buddha-vacana intention, aspiration). Steps 2, 3, 7 transclude from here.
- `assets/audio/` — chanting audio per plan and per language announcer voice.
- `assets/images/` — banner art, plan-milestone graphics.

## 8. Sample Day

A complete sample day, exactly as it will be delivered, lives in the upstream brief (`0-INBOX/Daily Abhidhamma Brief.md`, "Sample Day"). It covers Dukamātikā day with five clusters — Knots, Floods, Yokes, Hindrances, Misapprehensions — and shows the seven steps populated. Use it as the gold standard when drafting any day.

## 9. Status, Review, and Cite-Back

Each day-file carries a `status` field:

- `draft` — generated, not reviewed; sources may be incomplete.
- `partial` — some steps reviewed.
- `complete` — every step reviewed, every claim sources back to a complete rail.

Only `complete` day-files are published to practitioners. The transformation may not skip past `2-RAILS/` to cite `1-SOURCES/` directly.

## 10. Working with this Folder

The day to start with is **day-001**. The plan to start with is **plan-001**. As you build, work plan by plan (not day by day across all 200): finish all five language tracks for one plan, review, lock, and only then begin the next plan. This keeps the rhythm steady and surfaces structural problems early.
