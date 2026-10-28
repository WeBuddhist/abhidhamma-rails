# Puggalapaññatti (`pi-4`) commentaries — structure, content, and upload

**Date:** 2026-10-28  
**Scope:** the three pi-4 commentaries only:

- `1-SOURCES/Commentaries/pi-puggalapannatti-atthakatha.md`
- `1-SOURCES/Commentaries/pi-puggalapannatti-mulatiika.md`
- `1-SOURCES/Commentaries/pi-puggalapannatti-anutiika.md`

Root `1-SOURCES/Text/pi-4.md` was read for transclusion targets only and not edited. pi-1, pi-2, pi-3, pi-5, pi-6, pi-7 and `.gitignore` were not touched.

**Checked against:** `4-SYSTEM/Guidelines/block-id-spec.md`, the live tipitaka.app data (its own `/api/children` and `/api/text` endpoints), `4-SYSTEM/scripts/linter-commentary/` and `parser-commentary/`.

**Nothing is committed.** Uploads were done by hand by the user (see below).

---

## Verdict

| Part | Result |
|---|---|
| A. Vault hierarchy (parent / child / siblings, IDs) | PASS |
| B. tipitaka.app tree, titles and order | PASS |
| C. Intentional differences | flagged, not changed |
| D. Text quality (glued words) | PASS after 21 fixes |
| E. Linter and parser | PASS (after adding `license: cc0`) |
| Upload | done by the user for all three; IDs in frontmatter |

---

## A. Hierarchy (all three files)

```
# Abhidhammapiṭake                        ^0
## Puggalapaññatti-…                      ^4-0
### Mātikāvaṇṇanā                         ^4-1-0
### Niddesavaṇṇanā                        ^4-2-0
#### Ekaka … Dasakaniddesavaṇṇanā         ^4-2-1-0 … ^4-2-8-0   (8 siblings)
### Nigamanakathā                         ^4-3-0   (aṭṭhakathā only)
```

- First heading is level `#`; no heading level skips; every heading ID ends in `-0`.
- Each child ID extends its parent's ID. Siblings under `^4-2-0` are 1…8 with no gaps. Dasaka is `^4-2-8-0` (sibling position), not 10.
- Content IDs are one continuous counter per file, book 4 only, at most 3 parts, none ending in `-0`, no duplicates or gaps:
  - aṭṭhakathā `^4-1` … `^4-272`
  - mūlaṭīkā `^4-1` … `^4-90`
  - anuṭīkā `^4-1` … `^4-85`
- All transclusions of `pi-4.md` resolve (148 / 71 / 57) and sit under the right niddesa heading.
- mūlaṭīkā and anuṭīkā have the same 12 heading nodes as the aṭṭhakathā except `^4-3-0`. Counts: aṭṭhakathā 13 TOC nodes, the other two 12.
- Note: the `^0` piṭaka root does not end in `-0`. That is correct (`block-id-spec.md` §2).

## B. Match with tipitaka.app

| Layer | Site node | What the site has |
|---|---|---|
| aṭṭhakathā | `atta-ap-pp-4`, `-5` | 1. Mātikāvaṇṇanā, 2. Niddesavaṇṇanā |
| | `atta-ap-pp-5-1` … `5-7`, `5-10` | Ekaka … Sattaka, "10." Dasaka. No Aṭṭhaka or Navaka vaṇṇanā |
| mūlaṭīkā | `tika-ap-pp-2`, `2-1` … `2-10` | same 8-niddesa pattern |
| anuṭīkā | `tika2-ap-pp-3`, `3-1` … `3-10` | same 8-niddesa pattern |

- Section titles and order match in all three.
- Per-section paragraph counts match. The aṭṭhakathā Nigamanakathā was 14 in ours against 15 in the site range, but the extra site paragraph is the next book's homage line.
- Root-verse references per section are identical to the site's (e.g. `^4-209` in Dasaka, `^4-203`, `^4-207` in Sattaka).
- Text: 99.86 to 99.92 percent word match after the fixes. The only differences left are the homage line.
- Root: the site's 10 uddesa and 10 niddesa headings match `pi-4.md`.

## C. Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| Dasaka `^4-2-8-0` (sibling position) | printed "10." | by design, same as pi-3 |
| `## ^4-0` book parent | aṭṭhakathā book heading is misfiled under the end of Dhātukathā; Mātikā and Niddesa sit flat | vault is cleaner |
| niddesas nested under `^4-2-0` | mūlaṭīkā and anuṭīkā list them as siblings of Niddesavaṇṇanā | vault is cleaner |
| Nigamanakathā `^4-3-0` under the book | nested under Dasaka | placement is a judgement call; confirm |
| homage `^T-1` at file top | "Namo tassa…" at the end of the previous section | excluded from the word diff |

Heading IDs use sibling position even where the source prints a number (`block-id-spec.md` §5).

## D. Text quality: 21 glued words fixed

Words were fused where the site has a word boundary (for example a `|V0.00xx|` page marker between words). All 21 were found by comparing against tipitaka.app, and each was fixed by inserting a space. Cause is inferred, not traced in the converter.

- aṭṭhakathā (9): Labhanto sappāyāni, Tesaṃ taṃ hotīti, Hīno hoti, Na kumbhimukhāti, Imesaṃ bhedāyāti, So abhikkante, evaṃ passatoti, Ummujjitvā pataratīti, Idha vihāyāti
- mūlaṭīkā (8): Khandhāti paññāpanāti, sabbākārenapi anupalabbhaneyya, jīvitindriyaṃ cuticittaṃ, Evaṃ maggakkhaṇepīti, Acchamaṃsaṃ labhitvā, Tattha tatthāti, Tattha sikkhanabhāvenāti, Saddhā nāma
- anuṭīkā (4): Pāḷiyaṃ anāgatatanti, Kiñci natthīti, Rūpato aññaṃ, rūpataṇhāvikkhambhanena rūpakāyato

A re-scan found no glues left. Other books were not checked and may carry the same conversion glue.

## E. Linter and parser

First lint run failed on all three with one error: `license` required. `license: cc0` was added by the user's approval (matches every other commentary and root text, including `pi-4.md`). The linter also patched `commentary_of: leKc1Ei0OBaZN2FNMqlpL` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-4.md`. After that all three linted OK and parsed OK.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 139,279 | 30,006 | 32,807 |
| Segments | 273 (272 paragraph, 1 top) | 91 (90 + 1) | 86 (85 + 1) |
| TOC nodes / max depth | 13 / 3 | 12 / 3 | 12 / 3 |
| Alignment pairs | 267 | 91 | 86 |
| Distinct root targets | 148 | 71 | 57 |

Warnings (none block upload): author/translator missing, `alt_titles` missing.

Titles (frontmatter and upload payload): `Puggalapaññatti-aṭṭhakathā`, `Puggalapaññatti-mūlaṭīkā`, `Puggalapaññatti-anuṭīkā` (the earlier "(extract from …)" suffix was removed). `tag_ids: [296WZOr8MXWteSqBBI7pl]` added, the same Abhidhamma tag as the other commentaries.

Outputs: `4-SYSTEM/scripts/linter-commentary/output/pi-puggalapannatti-*.lint.json` and `4-SYSTEM/scripts/parser-commentary/output/pi-puggalapannatti-*/` (text, edition, toc and alignment JSON each).

## Upload (done by hand with curl)

Per file: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/{root_edition}/alignments/{edition}` (pairs flipped to root, then commentary), `POST /v2/editions/{edition}/table-of-contents`. Root edition used: `4bCOP5KnJqlcTxSBZXYA3` (`pi-4.md`).

| | text_id | edition_id | toc_id |
|---|---|---|---|
| aṭṭhakathā | `zFpVKiUlHeRzziqpg6eeM` | `OslFzzW2jMdRIk8CuYIKx` | `XMG53zN2ej55HHK6cw5d5` |
| mūlaṭīkā | `2l1OAALDrKc9eEb4y8w7T` | `OBfpVFQNrYSWvCzFyvFiL` | `36JZciSCTXV9iqLvclMl9` |
| anuṭīkā | `kERYN9A8Z6DUE4kuEIu1R` | `VMuk7Vt3e5Ip9xM9ayJb4` | `9X2gXaqsGMOTic318C639` |

IDs are saved in each file's frontmatter. The alignment is the same kind as pi-3's (commentary paragraph to root verse); there is no alignment between layers (mūlaṭīkā to aṭṭhakathā, anuṭīkā to mūlaṭīkā), as for pi-3.

## Things to know

- **Aṭṭhakathā title and tag:** the first title and `tag_ids` edit to the aṭṭhakathā frontmatter was lost when the IDs were saved (the file reverted to the old title and no tag). It was re-applied on 2026-10-28. The aṭṭhakathā was uploaded with the old title, so the live text may still show "(extract from …)" and lack the tag until patched (`PATCH /v2/texts/{id}` for the title, `POST /v2/texts/{id}/tags/296WZOr8MXWteSqBBI7pl` for the tag). Verify on the live text.
- Running the linter refreshes the tracked `4-SYSTEM/scripts/linter-commentary/languages.py` from the live API; it was restored with `git checkout` each time.
- The live root edition for `pi-4` came from an older parser; commentary alignment targets use only verse and mātikā references, so this should not matter.
- Not compared: the site's rendered page or sidebar in the browser, or the live library pages after upload. Open each text in the reader to confirm the TOC tree.

## Files to commit

The three `.md` files, the three `.lint.json` files and the three parser output folders. Not `.gitignore`, `4-SYSTEM/scripts/.env.example`, or the other `0-INBOX` files. Never `.env`.
