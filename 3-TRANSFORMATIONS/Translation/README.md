# Translation

Language-by-language translations of the Abhidhamma produced from the rails. Each subfolder is one translation track — one audience, one register — and contains just two things:

```
<lang>-<track-name>/
├── requirements.md               # the requirements governing this track
└── <lang>-<source-text>-…  .md   # the translation file(s), one per source-text section
```

## Subfolders

- `en-Contemporary-English-Abhidhamma/` — English, modelled on the NIV translation requirements (optimal equivalence + reader-accessible English + committee review). Requirements in English.
- `bn-Contemporary-Bengali-Abhidhamma/` — Bengali, same NIV-derived approach, adapted to Bengali. Requirements in Bengali.
- `si-Contemporary-Sinhala-Abhidhamma/` — Sinhala, same NIV-derived approach, adapted to Sinhala. Requirements in Sinhala.

Each track's `requirements.md` is written **in its target language** — the working language for that track's drafters and reviewers. Add additional tracks alongside these as they are commissioned (e.g. `bo-Classical-Tibetan-Abhidhamma/`, `zh-Modern-Mandarin-Abhidhamma/`).

## File-level rules

- Translation files name their language with the tag (`en`, `bo`, `zh`, `pi`, `hi`, …) per the vault's convention (see `4-SYSTEM/Guidelines/0-VAULT-Structure.md` §6).
- Each translation file's frontmatter cites the rails it was generated from. The citation chain (`1-SOURCES/` → `2-RAILS/` → `3-TRANSFORMATIONS/`) never skips.
- Only `status: complete` translation files are referenced by other transformations (e.g. published into a Daily Tipiṭaka day-file).
