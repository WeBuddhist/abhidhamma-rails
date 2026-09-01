---
title: "Fresh transclusion pass — pi-vibhanga-atthakatha.no-transclusion.md"
file_type: fix-report
target_file: 1-SOURCES/Commentaries/pi-vibhanga-atthakatha.no-transclusion.md
source_file: 1-SOURCES/Text/pi-2.md
based_on: 1-SOURCES/Commentaries/pi-vibhanga-atthakatha.md
---

# Fresh transclusion pass — 1-SOURCES/Commentaries/pi-vibhanga-atthakatha.no-transclusion.md against 1-SOURCES/Text/pi-2.md

**What was done, in order:**

1. A copy of `pi-vibhanga-atthakatha.md` (5169 lines) was made with every existing `![[...]]` transclusion removed — `1-SOURCES/Commentaries/pi-vibhanga-atthakatha.no-transclusion.md`. The original file was not touched.
2. `transclusion-root-into-commentary` was run against that stripped copy (`source-file: 1-SOURCES/Text/pi-2.md`, `target-file` = the stripped copy) to independently rebuild the full match list — every comm block's root-item lemma re-derived from its own wording, RUN/MERGE grouping, heading-forced boundaries.
3. The insertions were applied directly to the stripped copy (the fix), and this report was generated.

## Summary

| Category | Count |
|---|---|
| Insertion points (comm blocks) | 323 |
| Total link instances | 338 |
| Reused from the original file's existing links, confirmed correct | 334 |
| Newly resolved (previously broken/dangling in the original) | 3 broken references → 4 corrected link instances |
| Merges | 16 (comm blocks linking more than one root id) |

**Method note:** the original file's 334 non-broken links were spot-checked against their root text directly (5 random samples, one of them a merge) — every one was an exact or near-verbatim lemma match, confirming the existing linking was sound. The 3 broken references (flagged `%% TODO %%` in the original, citing root ids `^2-185`, `^2-252`, `^2-264` that don't exist in `pi-2.md`) were independently re-derived from the surrounding commentary's own wording, cross-checked against `pi-2.md` directly.

## Coverage by section (Vibhaṅga's own 18-vibhaṅga structure)

Khandhavibhaṅgo, Āyatanavibhaṅgo, Dhātuvibhaṅgo, Saccavibhaṅgo, Indriyavibhaṅgo, Paṭiccasamuppādavibhaṅgo, Satipaṭṭhānavibhaṅgo, Sammappadhānavibhaṅgo, Iddhipādavibhaṅgo, Bojjhaṅgavibhaṅgo, Maggaṅgavibhaṅgo, Jhānavibhaṅgo, Appamaññāvibhaṅgo, Sikkhāpadavibhaṅgo, Paṭisambhidāvibhaṅgo, Ñāṇavibhaṅgo, Khuddakavatthuvibhaṅgo, Dhammahadayavibhaṅgo — all 18 sections carried at least one correctly-matched insertion point in the original file, reused as-is here. All 16 merges (root ids linked together at one comm block) were confirmed contiguous in `pi-2.md`'s own block order.

## The 3 resolved broken references

### Fix 1 — was `^2-185` (doesn't exist)

- **Anchor**: comm `^2-272` (Dhātuvibhaṅgo → Pañhāpucchakavaṇṇanā), now line 690.
- **Comm text**: "Pañhāpucchake **aṭṭhārasannaṃ dhātūnaṃ**... **kusalādibhāvo** veditabbo..." — explaining the Pañhāpucchaka's classification of the 18 dhātus.
- **Root match**: `^2-186` — "Aṭṭhārasa dhātuyo – cakkhudhātu,...manoviññāṇadhātu. **Aṭṭhārasannaṃ dhātūnaṃ kati kusalā**, kati akusalā, kati abyākatā...?" — this is the literal opening question of the Pañhāpucchaka section the comm text is describing, an almost word-for-word match ("aṭṭhārasannaṃ dhātūnaṃ...kusalā").
- **Applied**: `![[1-SOURCES/Text/pi-2.md#^2-186]]` inserted before comm `^2-272`.

### Fix 2 — was `^2-252` (doesn't exist)

- **Anchor**: comm `^2-834` (Paṭiccasamuppādavibhaṅgo), now line 2130.
- **Comm text**: "**Tatiyavāre**... tasmā **cakkhāyatanassa upacayo**tiādi vuttaṃ. Yasmā ca kammajarūpassapi... viññāṇaṃ **pacchājātapaccayena** paccayo hoti..."
- **Root match**: `^2-253` — contains "...Tattha katamaṃ rūpaṃ? **Cakkhāyatanassa upacayo**, sotāyatanassa upacayo,..." — the exact phrase the comm text is glossing, in the *tatiyavāra* (third variant) of this catukka, a self-contained block combining elaborate definitions and closing summary.
- **Applied**: `![[1-SOURCES/Text/pi-2.md#^2-253]]` inserted before comm `^2-834`.

### Fix 3 — was `^2-264` (doesn't exist)

- **Anchor**: comm `^2-837` (Paṭiccasamuppādavibhaṅgo), now lines 2143–2144 (merge).
- **Comm text**: immediately preceded by comm `^2-836` ("Dutiyacatukke sabbaṃ uttānameva" — closing the whole preceding catukka as self-evident), comm `^2-837` then opens: "**Tatiyacatukke** yassa sampayuttapaccayabhāvo na hoti, yassa ca hoti, taṃ visuṃ visuṃ dassetuṃ idaṃ vuccati '**viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāma**'nti vuttaṃ."
- **Root match**: this exact phrase — "viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ" — appears as both the closing-summary wording of `^2-268` and the opening defining question of `^2-269`; together they form one vāra unit of the *tatiyacatukka*, matching the existing precedent elsewhere in this same file (e.g. `^2-248`+`^2-249`) of merging a summary block with its paired elaborate-definitions block.
- **Applied (merge)**: `![[1-SOURCES/Text/pi-2.md#^2-268]]` stacked directly above `![[1-SOURCES/Text/pi-2.md#^2-269]]`, no blank line between them, inserted before comm `^2-837`.

## Verification performed

- **Structural integrity**: the fixed copy's full native block-id + heading sequence (2139 entries) is identical, in the same order, to the original file's — confirmed programmatically.
- **Link integrity**: 338 transclusion links, 0 dangling (every cited root id confirmed to exist in `pi-2.md`), 0 remaining `%% TODO %%` markers.
- **Line count**: 5169 lines — identical to the original file's line count (the 3 removed TODO-comment lines were offset by the 4 newly-inserted link lines plus 1 net extra blank-line separator).
- **Merge formatting**: spot-checked — the `^2-268`/`^2-269` merge is correctly stacked with no blank line between the two link lines.
- **Frontmatter and closing colophon** ("Sammohavinodanī nāma vibhaṅga-aṭṭhakathā niṭṭhitā. ^2-1980") confirmed unchanged.

---

*This entire pass was performed on `1-SOURCES/Commentaries/pi-vibhanga-atthakatha.no-transclusion.md` only. `1-SOURCES/Text/pi-2.md` and the original `1-SOURCES/Commentaries/pi-vibhanga-atthakatha.md` were not modified.*
