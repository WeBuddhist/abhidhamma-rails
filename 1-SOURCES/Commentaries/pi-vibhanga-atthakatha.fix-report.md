---
title: "Broken-transclusion fix report — pi-vibhanga-atthakatha.md"
file_type: fix-report
target_file: 1-SOURCES/Commentaries/pi-vibhanga-atthakatha.md
source_file: 1-SOURCES/Text/pi-2.md
---

# Broken-transclusion fix report — 1-SOURCES/Commentaries/pi-vibhanga-atthakatha.md

Three `%% TODO %%`-flagged broken transclusions in this file cited root block ids (`^2-185`, `^2-252`, `^2-264`) that do not exist in `1-SOURCES/Text/pi-2.md`. All three have now been resolved to the correct existing root block id and fixed directly in the live file (these are the same corrections already verified against the independently-rebuilt `.no-transclusion.md` copy).

## Summary

| # | Broken id (removed) | Corrected target | Type |
|---|---|---|---|
| 1 | `^2-185` | `^2-186` | single link |
| 2 | `^2-252` | `^2-253` | single link |
| 3 | `^2-264` | `^2-268` + `^2-269` | merge (2 links) |

## Fix 1

- **Anchor block**: `pi-vibhanga-atthakatha.md#^2-272` (Dhātuvibhaṅgo → Pañhāpucchakavaṇṇanā), now line 691.
- **Broken reference removed**: `![[1-SOURCES/Text/pi-2.md#^2-185]]` and its `%% TODO %%` comment.
- **Corrected link inserted**: `![[1-SOURCES/Text/pi-2.md#^2-186]]`, now line 689.

## Fix 2

- **Anchor block**: `pi-vibhanga-atthakatha.md#^2-834` (Paṭiccasamuppādavibhaṅgo), now line 2130.
- **Broken reference removed**: `![[1-SOURCES/Text/pi-2.md#^2-252]]` and its `%% TODO %%` comment.
- **Corrected link inserted**: `![[1-SOURCES/Text/pi-2.md#^2-253]]`, now line 2128.

## Fix 3

- **Anchor block**: `pi-vibhanga-atthakatha.md#^2-837` (Paṭiccasamuppādavibhaṅgo), now line 2143.
- **Broken reference removed**: `![[1-SOURCES/Text/pi-2.md#^2-264]]` and its `%% TODO %%` comment.
- **Corrected links inserted** (merge, stacked with no blank line between): `![[1-SOURCES/Text/pi-2.md#^2-268]]` and `![[1-SOURCES/Text/pi-2.md#^2-269]]`, now lines 2140–2141.

## Mechanics of the edit

Each TODO comment line and its broken link line were replaced in place with the corrected link(s), preserving the file's CRLF line endings. No other content in the file was altered, reordered, or deleted.

## Post-fix file statistics

| Stat | Before | After |
|---|---|---|
| Total lines | 5170 | 5168 |
| Total transclusion links to `pi-2.md` | 337 | 338 |
| Remaining `%% TODO %%` markers | 3 | 0 |
| Dangling links to `pi-2.md` (nonexistent target id) | 3 | 0 |

Frontmatter and the file's closing colophon ("Sammohavinodanī nāma vibhaṅga-aṭṭhakathā niṭṭhitā. ^2-1980") confirmed unchanged.

A copy of the fixed file was also saved as `pi-vibhanga-atthakatha.fixed.md` alongside the live file for direct review.

---

*All three fixes applied directly to `pi-vibhanga-atthakatha.md`. No other file was modified.*
