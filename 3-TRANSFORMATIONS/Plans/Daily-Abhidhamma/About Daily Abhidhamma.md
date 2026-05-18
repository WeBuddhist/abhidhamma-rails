# Daily Abhidhamma

A 200-day reading-and-chanting journey through the Abhidhamma, prepared in collaboration with the **International Tipiṭaka Chanting Council (ITCC)** in the run-up to the chanting gathering at Bodhgayā, December 2026.

This is a **Plan track** in the sense of [`../About Plans.md`](../About%20Plans.md): a calendar-driven engagement with the text generated from completed rails. The category-wide rules for plans live there; this file is the cross-language brief and folder map for the Daily-Abhidhamma plan specifically.

## Per-session shape (all languages)

Every day-file follows this seven-step structure, regardless of language. Individual language `requirements.md` files fill in the language-specific rendering of each step.

1. **Opening liturgy** — vandanā / aspiration in the source language
2. **Text of the day** — transcluded from the relevant Translation track output
3. **Pāli Word of the Day** — one term from the Local-Wiki, with the target-language rendering from the termbase
4. **Reading for meaning** — a short commentary passage from the Section or Verse rail
5. **Reflection prompt** — one or two questions for personal practice
6. **Closing liturgy** — aspiration in the target language
7. **Notifications** — push notification, social media copy, email subject line (ready to send)

## Languages published

| Language | Folder | Status |
| -------- | ------ | ------ |
| Pāli (source) | `pi/` | scaffolded days 1–10 |
| English | `en/` | scaffolded days 1–10 |
| Tibetan | `bo/` | scaffolded days 1–10 |
| Chinese | `zh/` | scaffolded days 1–10 |
| Hindi | `hi/` | scaffolded days 1–10 |

Bengali (`bn/`) is a planned addition; not yet started.

## Where to start (per language)

Each language stream is self-contained. For any stream, read in this order:

1. `<lang>/requirements.md` — style contract for that stream (in the target language).
2. `<lang>/termbase.md` — vocabulary contract.
3. `<lang>/schedule.md` — day-by-day calendar.
4. `<lang>/days/day-1.md` — the first day file, as the canonical working example.

## Folder map

```
Daily-Abhidhamma/
├── About Daily Abhidhamma.md   # this file — cross-language brief
└── <lang>/                     # one per published language
    ├── requirements.md         # style contract (in target language)
    ├── termbase.md             # vocabulary contract
    ├── schedule.md             # day-by-day calendar
    ├── days/
    │   ├── day-1.md            # intro day (plan overview + text + notifications)
    │   ├── day-2.md
    │   └── ...                 # days 11–200 created plan-arc by plan-arc
    ├── communications/
    │   └── announcements.md
    └── assets/
        └── images/
```

Days 11–200 are not yet scaffolded. Create them plan-arc by plan-arc as content is written, using `en/days/day-1.md` as the canonical template.

## Rails ↔ days

Every claim in a day-file traces back to a rail in `2-RAILS/`:

- `2-RAILS/Verses/` for each passage chanted
- `2-RAILS/Sections/` for the chanting-guide framing
- `2-RAILS/Local-Wiki/` for the Pāli Word of the Day's attested sense
- `2-RAILS/Bilingual-Glossaries/pi-<lang>.md` for term-by-term consistency

Days also embed the per-language Translation track output for the Reading-for-Meaning step (e.g. `../../../Translations/en-Contemporary-English-Abhidhamma/` for English days). That second-order citation is recorded in the day-file's `context_packages:` frontmatter alongside the rails.

The plan never reaches past the rails to cite `1-SOURCES/` directly.
