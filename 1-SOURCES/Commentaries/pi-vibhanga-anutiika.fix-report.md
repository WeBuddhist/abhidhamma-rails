---
title: "Broken-transclusion fix report — pi-vibhanga-anutiika.md"
file_type: fix-report
target_file: 1-SOURCES/Commentaries/pi-vibhanga-anutiika.md
source_file: 1-SOURCES/Text/pi-2.md
---

# Broken-transclusion fix report — 1-SOURCES/Commentaries/pi-vibhanga-anutiika.md

Two `%% TODO %%`-flagged broken transclusions in this file cited root block ids (`^2-252`, `^2-264`) that do not exist in `1-SOURCES/Text/pi-2.md`. Both have been resolved to the correct existing root block id and fixed directly in the live file.

## Summary

| # | Broken id (removed) | Corrected target | Type |
|---|---|---|---|
| 1 | `^2-252` | `^2-253` | single link |
| 2 | `^2-264` | `^2-268` + `^2-269` | merge (2 links) |

## Fix 1

- **Anchor block**: `pi-vibhanga-anutiika.md#^2-484`, now at line 1245.
- **Broken reference removed**: `![[1-SOURCES/Text/pi-2.md#^2-252]]` and its `%% TODO %%` comment.
- **Corrected link inserted**: `![[1-SOURCES/Text/pi-2.md#^2-253]]`, now at line 1243.

## Fix 2

- **Anchor block**: `pi-vibhanga-anutiika.md#^2-486`, now at line 1254.
- **Broken reference removed**: `![[1-SOURCES/Text/pi-2.md#^2-264]]` and its `%% TODO %%` comment.
- **Corrected links inserted** (merge, stacked with no blank line between): `![[1-SOURCES/Text/pi-2.md#^2-268]]` and `![[1-SOURCES/Text/pi-2.md#^2-269]]`, now at lines 1251–1252.

## Mechanics of the edit

Both TODO comment lines and their broken link lines were replaced in place with the corrected link(s), preserving the file's CRLF line endings. No other content in the file was altered, reordered, or deleted.

## Post-fix file statistics

| Stat | Before | After |
|---|---|---|
| Total lines | 2609 | 2608 |
| Total transclusion links to `pi-1.md`... `pi-2.md` | 233 | 234 |
| Remaining `%% TODO %%` markers | 2 | 0 |
| Dangling links to `pi-2.md` (nonexistent target id) | 2 | 0 |

Frontmatter and the file's closing colophon ("Vibhaṅga-anuṭīkā samattā. ^2-917") were confirmed unchanged.

---

*Both fixes applied directly to `pi-vibhanga-anutiika.md`. No other file was modified.*
