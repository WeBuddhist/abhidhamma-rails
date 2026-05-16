# Outputs

English Abhidhamma renderings produced under `../brief.md`.

## Per-file frontmatter

```yaml
---
brief_id: en-Contemporary-English-Abhidhamma
source_rails:
  - 2-RAILS/Verses/<...>
  - 2-RAILS/Sections/<...>
  - 2-RAILS/Local-Wiki/<...>
status: draft        # draft | partial | complete
reviewers:
  pali:               # name of the Pāli reviewer once signed off
  readability:        # name of the readability reviewer once signed off
---
```

## Status gates

- `draft` — produced by the drafter.
- `partial` — Pāli reviewer has signed off; readability review still pending.
- `complete` — both reviewers have signed off; safe to use downstream.

Only `complete` files are referenced by other transformations (e.g. published into a Daily Tipiṭaka day-file, included in a printed edition).
