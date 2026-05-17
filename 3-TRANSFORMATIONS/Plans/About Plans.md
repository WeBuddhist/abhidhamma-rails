# Plans

Calendar-driven study and practice arcs — daily readings, weekly retreat sessions, a year-long course, a chanting preparation arc. A plan organises engagement with the text along a calendar: each day or session is generated from rails (and often from completed Translation or Adaptation outputs), then arranged into a publishable schedule with surrounding communications and assets.

Each subfolder is one **plan track** — one coherent calendar-organised output stream:

```
Plans/
└── <plan-id>/
 ├── requirements.md # narrative brief governing the plan
 ├── termbase.md # (optional) standard term renderings across all sessions
 ├── schedule/ # calendar + milestones
 ├── plans/ # internal arc structure (if the plan has multiple sub-arcs)
 ├── days/ # per-session content, typically one subfolder per language
 │ ├── _template/ # the template each session file follows
 │ ├── <lang>/ # e.g. pi/, en/, bo/, zh/, hi/
 │ └──...
 ├── communications/ # announcements, notifications, social media
 └── assets/ # fixed liturgy, audio, images
```

For the category-wide convention (what `requirements.md` must contain, the citation chain, the status lifecycle), see [`../About Transformations.md`](../About Transformations.md).

---

## Why plans use `requirements.md` instead of `requirements.md + termbase.md`

Plans cover so much surface area — multiple languages, multiple session formats, communications cadence, supporting assets, calendar mapping — that a single narrative brief is easier to keep coherent than a split style-plus-vocabulary pair. The brief still functions as the binding contract, but it reads like a project brief rather than a translator's specification.

Plans that lock specific renderings across all sessions/languages add a `termbase.md` alongside; plans that work from per-language Translation track outputs (e.g. Daily-Abhidhamma) inherit those translations' termbases instead.

---

## Per-track convention

### `requirements.md`

Required. Written in English (or the primary working language of the plan team). Covers:

- **Purpose** — what does completing this plan give a practitioner?
- **Audience** — who is it for? what prior practice do they have?
- **Per-session shape** — the fixed structure every session follows (e.g. Daily-Abhidhamma's seven-step daily structure).
- **Calendar policy** — how many sessions, how organised into arcs, where the major milestones fall.
- **Languages** — which language streams are published.
- **Source-rail dependencies** — which rails each session draws from, and which prior-track outputs (Translations, Adaptations) are embedded.
- **Communications convention** — what surrounding outreach the plan ships (announcements, daily notifications, social media), what the voice is.
- **Sample session** — at least one fully-built session, used as the gold standard for drafting subsequent ones.

### `termbase.md`

Use only when the plan locks specific term renderings across all sessions and all languages. For plans that inherit renderings from per-language Translation tracks, point to those termbases instead.

---

## Working order

Build plan-by-plan, not session-by-session across all sessions: finish all language tracks for one arc, review, lock, and only then begin the next arc. This keeps the rhythm steady and surfaces structural problems early.

---

## Current plans

- **[`Daily-Abhidhamma/`](Daily-Abhidhamma/)** — a 200-day reading-and-chanting journey through the Abhidhamma prepared with the International Tipiṭaka Chanting Council (ITCC) for the chanting gathering at Bodhgayā, December 2026. Five language streams (`pi`, `en`, `bo`, `zh`, `hi`). The plan that the per-track convention above was first written against.

Add new plans alongside as they are commissioned.
