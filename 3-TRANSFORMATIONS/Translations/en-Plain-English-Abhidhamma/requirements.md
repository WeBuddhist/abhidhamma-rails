---
track: en-Plain-English-Abhidhamma
target_language: en
status: scaffold
last_updated: 2026-07-30
---

# Requirements — en-Plain-English-Abhidhamma

The **style contract** for this track. Binding on every file in this folder. For the category-wide conventions (citation chain, status lifecycle, checklists) see [`../../About Transformations.md`](../../About Transformations.md); for the per-track pipeline see [`../About Translations.md`](../About Translations.md).

## Provenance

Scaffolded after the fact, reconstructed from the one delivered file (`en-vibhanga-khandhavibhanga-plain.md`) rather than written before it. Rules below marked **(observed)** describe what the delivered translation actually does; rules marked **(proposed)** are gaps a reviewer should rule on before the next batch.

## 1. Purpose and distinction from the Contemporary track

This track renders the Abhidhamma for readers with **English as a second or third language** (see `audience.md`). It differs from `../en-Contemporary-English-Abhidhamma/` not primarily in vocabulary — the two agree on *aggregate*, *perception*, *volition* — but in **sentence shape**: shorter units, fewer subordinate clauses, no Latinate chains where a short word will do.

**(proposed)** If review finds no substantive difference beyond register, the two tracks should be merged rather than maintained in parallel.

## 2. Source and citation chain

- Translate from the root text `1-SOURCES/Text/pi-2.md`, oriented by the rails in `2-RAILS/Sections/pi-2-summaries.md` and `2-RAILS/Sections/pi-2-practice.md`.
- **(observed)** Segment IDs are preserved verbatim (`^2-N`), one per source segment, with full parity against source line counts. This is what lets the Daily Tipitaka plan importer locate verse ranges — it must not be relaxed.
- **(observed)** Per-segment line structure mirrors the source exactly; exactly one blank line separates segments.
- **(observed)** Headings carry their structural anchors (`^2-1-0`, `^2-1-1-0`) and are translated, not transliterated — "Khandhavibhaṅgo" → "Analysis of the Aggregates", "Suttantabhājanīyaṃ" → "The Discourse Method".

## 3. Terminology

- One rendering per keyword, per `termbase.md` in this folder. No synonym variation for elegance.
- **(observed)** Pāli technical terms are **not** retained in the running translation; English renderings are used throughout. (Pāli surfaces only in the Daily Tipitaka layer above, where it is always glossed on first use.)

## 4. Sentence and register rules

- **(observed)** Target 8th-grade reading level; Flesch-Kincaid ≤ 9.
- **(observed)** The canonical repetition is **preserved, not collapsed** — the threefold/tenfold lists and the eleven-fold sweep (past/future/present, internal/external, gross/subtle, inferior/superior, far/near) are rendered in full. The repetition is the teaching method (*tayo parivaṭṭa*, the three turnings), not redundancy to be edited out.
- **(observed)** Elisions in the source (`…pe…`) are carried across as `…` rather than expanded.
- **(proposed)** **Grammatical completeness is mandatory.** Every list item must be a well-formed clause. The delivered file violates this in the threefold lists — "feeling that wholesome", "feeling that a result" — where the copula has been dropped. This fails a second-language reader hardest, since they cannot repair the sentence from context. See `known_issues` in the translation's frontmatter; affects `^2-40`, `^2-41`, `^2-57` and neighbouring blocks.

## 5. Status lifecycle

`scaffold` → `draft` → `reviewed` → `complete`. The one delivered file is `draft`. Nothing in this track is `reviewed` until a native dharma reviewer has signed off on both the terminology table and the copula fix.

## 6. Coverage

| Section | File | Segments | Status |
|---|---|---|---|
| Khandhavibhaṅgo (`^2-1-0`) | `en-vibhanga-khandhavibhanga-plain.md` | 169 of 169 (`^2-1` – `^2-153`) | draft |
| Āyatanavibhaṅgo (`^2-2-0`) onward | — | not yet translated | — |

**Note for planning:** the Daily Tipitaka schedule runs Book II through day 178. This track currently covers only the first vibhaṅga, which carries the plan to roughly day 094. Translation of `Āyatanavibhaṅgo` onward is the next dependency for that plan.
