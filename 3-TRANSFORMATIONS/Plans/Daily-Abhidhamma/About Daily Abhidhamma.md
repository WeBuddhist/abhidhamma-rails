# Daily Abhidhamma

A 200-day reading-and-chanting journey through the Abhidhamma, prepared in collaboration with the **International Tipiṭaka Chanting Council (ITCC)** in the run-up to the chanting gathering at Bodhgayā, December 2026.

This is a **Plan track** in the sense of [`../About Plans.md`](../About Plans.md): a calendar-driven engagement with the text generated from completed rails. The category-wide rules for plans live there; this README is the per-plan brief pointer plus the folder map.

## Where to start

1. [`requirements.md`](requirements.md) — the full brief: purpose, audience, the seven-step daily structure, languages, status rules.
2. [`plans/About Plan Arcs.md`](plans/About Plan Arcs.md) — how the 200 days are organised into short plans (arcs).
3. [`days/_template/day-template.md`](days/_template/day-template.md) — the per-day file template.
4. [`schedule/calendar.md`](schedule/calendar.md) — the master day-to-date table.

## Folder map

```
Daily-Abhidhamma/
├── requirements.md # the brief governing the whole journey
├── termbase.md # standard term renderings used across all days/languages
├── schedule/ # calendar + milestones
├── plans/ # the 200 days organised into short plans (internal arcs)
├── days/ # the per-day content
│ ├── _template/ # the template each day-file follows
│ ├── pi/ day-001.md … day-010.md (scaffolded)
│ ├── en/ day-001.md … day-010.md (scaffolded)
│ ├── bo/ day-001.md … day-010.md (scaffolded)
│ ├── zh/ day-001.md … day-010.md (scaffolded)
│ └── hi/ day-001.md … day-010.md (scaffolded)
├── communications/ # announcements, daily notifications, social media
└── assets/ # fixed liturgy, chanting audio, images
```

Days 11–200 are not yet scaffolded; create them plan-arc by plan-arc as content is written, using `days/_template/day-template.md`.

## Rails ↔ days

Every claim in a day-file traces back to a rail in `2-RAILS/`:

- `2-RAILS/Verses/` for each passage chanted
- `2-RAILS/Sections/` for the chanting-guide framing
- `2-RAILS/Local-Wiki/` for the Pāli Word of the Day's attested sense
- `2-RAILS/Bilingual-Glossaries/pi-<lang>.md` for term-by-term consistency

Days also embed the per-language Translation track output for the Reading-for-Meaning step (e.g. `../../../Translations/en-Contemporary-English-Abhidhamma/` for English days). That second-order citation is recorded in the day-file's `context_packages:` frontmatter alongside the rails.

The plan never reaches past the rails to cite `1-SOURCES/` directly.
