# Daily Tipiṭaka

A 200-day reading-and-chanting journey through the Abhidhamma, prepared in collaboration with the **International Tipiṭaka Chanting Council (ITCC)** in the run-up to the chanting gathering at Bodhgayā, December 2026.

This is a **transformation** in the sense of `4-SYSTEM/Guidelines/0-VAULT-Structure.md`: an output generated from completed rails in `2-RAILS/`, governed by a brief.

## Where to start

1. `brief.md` — the full brief: purpose, audience, the seven-step daily structure, languages, status rules.
2. `plans/README.md` — how the 200 days are organised into short plans.
3. `days/_template/day-template.md` — the per-day file template.
4. `schedule/calendar.md` — the master day-to-date table.

## Folder map

```
Daily-Tipitaka/
├── brief.md                  # the brief governing the whole journey
├── terminology.md            # standard term renderings used across all days/languages
├── schedule/                 # calendar + milestones
├── plans/                    # the 200 days organised into short plans
├── days/                     # the per-day content
│   ├── _template/            # the template each day-file follows
│   ├── pi/   day-001.md … day-010.md (scaffolded)
│   ├── en/   day-001.md … day-010.md (scaffolded)
│   ├── bo/   day-001.md … day-010.md (scaffolded)
│   ├── zh/   day-001.md … day-010.md (scaffolded)
│   └── hi/   day-001.md … day-010.md (scaffolded)
├── communications/           # announcements, daily notifications, social media
└── assets/                   # fixed liturgy, chanting audio, images
```

Days 11–200 are not yet scaffolded; create them plan by plan as content is written, using `days/_template/day-template.md`.

## Rails ↔ days

Every claim in a day-file traces back to a rail in `2-RAILS/`:

- `2-RAILS/Verses/` for each passage chanted
- `2-RAILS/Sections/` for the chanting-guide framing
- `2-RAILS/Local-Wiki/` for the Pāli Word of the Day's attested sense
- `2-RAILS/Glossaries/glossary-pi-<lang>.md` for term-by-term consistency

The transformation never reaches past the rails to cite `1-SOURCES/` directly.
