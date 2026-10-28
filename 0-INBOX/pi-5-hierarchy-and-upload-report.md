# Kathāvatthu (`pi-5`) commentaries — structure, content, root links, and upload

**Date:** 2026-10-28  
**Scope:** the three pi-5 commentaries only:

- `1-SOURCES/Commentaries/pi-kathavatthu-atthakatha.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-mulatiika.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-anutiika.md`

Root `1-SOURCES/Text/pi-5.md` was read for transclusion targets only and not edited. pi-1 to pi-4, pi-6, pi-7 and `.gitignore` were not touched.

**Checked against:** `4-SYSTEM/Guidelines/block-id-spec.md`, the live tipitaka.app data (its `/api/children` and `/api/text` endpoints), `4-SYSTEM/scripts/linter-commentary/` and `parser-commentary/`, and the live library API after upload.

**Nothing is committed.** Uploads were done by hand with curl by the user (see below).

---

## Verdict

| Part | Result |
|---|---|
| A. Vault hierarchy (parent / child / siblings, IDs) | PASS |
| B. tipitaka.app tree, titles and order | PASS |
| C. Intentional differences | flagged, not changed |
| D. Text quality (glued words) | PASS after 93 fixes; 13 forms left for review |
| E. Root-verse transclusions | added (1,534 lines), all resolve |
| F. Linter and parser | PASS (after adding `license: cc0`, title cleanup, `tag_ids`) |
| G. Upload | done by the user for all three; live copies verified identical to local |

---

## A. Hierarchy (all three files)

```
# Abhidhammapiṭake (…)                       ^0
## Kathāvatthu-…                             ^5-0
### Nidānakathā / Ganthārambha…              ^5-1-0 …
### Mahāvaggo, Dutiyavaggo … Tevīsatimavaggo ^5-2-0 … ^5-24-0 (aṭṭhakathā: 23 vaggas)
#### kathā (e.g. Puggalakathā)               ^5-2-1-0 …
##### … ###### sub-sections                  up to 6 levels
### Nigamanakathā                            ^5-25-0 (aṭṭhakathā only)
```

- First heading is level `#`; no heading level skips; every heading ID ends in `-0` and extends its parent's ID. Siblings run 1…n at every level with no gaps.
- Content IDs are one continuous counter per file, book 5 only, none ending in `-0`, no duplicates or gaps:
  - aṭṭhakathā `^5-1` … `^5-815` (278 headings)
  - mūlaṭīkā `^5-1` … `^5-453` (211 headings)
  - anuṭīkā `^5-1` … `^5-491` (206 headings)
- Root `pi-5.md`: 481 headings, IDs `^5-1` … `^5-918`, unique and increasing, no `x`, `U` or zoned IDs, hence **no numbering reset** (matters for section E).

## B. Match with tipitaka.app

| Layer | Site nodes | Result |
|---|---|---|
| mūla | `ap-kvu-…` (479 nodes) | 479 of 479 root headings match `pi-5.md` in title and order |
| aṭṭhakathā | `atta-ap-pp-6-…` (inside Pañcapakaraṇa-aṭṭhakathā) | all 277 headings match in title and order |
| mūlaṭīkā | `tika-ap-pp-3-…` | 210 of 210 match |
| anuṭīkā | `tika2-ap-pp-4-…` | 205 of 205 match |

- Text, word level after ignoring spacing: the only differences left are the centred colophon lines the site renders as headings ("…vaṇṇanā niṭṭhitā", "paṇṇāsako samatto", "…samattā"), which we keep as body text, and the homage line.
- Gāthā paragraph counts: the site splits each verse into half-line paragraphs, so raw paragraph counts differ in verse sections (e.g. the opening section: 11 on the site against 5 here). Same text.

## C. Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| vaggas group their kathās (`^5-2-0` → `^5-2-1-0` …) | site ṭīkā trees are flat, everything hangs under the first "1. Anulomapaccanīkavaṇṇanā" | vault is cleaner |
| `## ^5-0` book parent | aṭṭhakathā book heading sits inside a combined Pañcapakaraṇa tree; Mahāvaggo misfiled under Nidānakathā | vault is cleaner |
| Nigamanakathā `^5-25-0` as sibling of the vaggas | nested under the last vagga | confirmed (same pattern as pi-3 `^3-3-0`, pi-4 `^4-3-0`) |
| heading IDs by sibling position | site prints "1.", "2." numbers | by design, same as pi-3 and pi-4 |
| particle "ti" attached (`atthīti`) | site writes `atthī ti` | site display convention; ours is the correct spelling |

## D. Text quality: 93 glued words fixed

Words fused by the conversion where tipitaka.app has a word boundary. Only spaces were added; with spaces removed each file is identical to the committed text. Fixed by position, not by global replace.

- aṭṭhakathā (25), mūlaṭīkā (47), anuṭīkā (21)
- Examples: `Dibbenacakkhunā` → `Dibbena cakkhunā`, `Atītaṃatthīti` → `Atītaṃ atthīti`, `Kammenasahajātoti` → `Kammena sahajātoti`, `Ājānāhiniggaha` → `Ājānāhi niggaha`, `Arahāchahi` → `Arahā chahi`, `Aniyatonāma` → `Aniyato nāma`.

**Left unchanged for review (13), may be legitimate compounds or sandhi, or the site's own mid-word split:**
`tenahi`, `dvepi`, `navattabbaṃ`, `mahāpathavīādīni`, `rūpantiādi`, `maggotiādi`, `sakkāyadiṭṭhiādīsupi`, `satipaṭṭhānādīsupi`, `somādayo`, `kusalādipañhaṃ`, `sammutiñāṇapañhesu` (aṭṭhakathā); `suññatādiatthaṃ` (mūlaṭīkā); `liṅgākappabhedaṃ` (anuṭīkā).

Other books were not checked and may carry the same conversion glue.

## E. Root-verse transclusions

Before this work the pi-5 commentaries had no `![[…]]` lines, so there was no commentary-to-root alignment (pi-3 has 54, pi-4 has 148).

- Rule: root has no numbering reset, so the leading printed number maps directly to `^5-N`. Each numbered paragraph gets one `![[1-SOURCES/Text/pi-5.md#^5-N]]` line per root ID directly above it. The printed number stays in the text. Ranges expand to consecutive lines.

| | Numbered paragraphs | Transclusion lines | Ranges | Distinct root targets |
|---|---|---|---|---|
| aṭṭhakathā | 388 | 692 | 144 | 690 |
| mūlaṭīkā | 223 | 433 | 93 | 433 |
| anuṭīkā | 208 | 409 | 87 | 409 |

- Five irregular citations resolved from each file's `source_note`: aṭṭhakathā `618-820.` → 618–620 and `541-545.` → 641–645; anuṭīkā `706-608.` → 706–708; mūlaṭīkā CST truncated tails `557-8.` → 557–558 and `571-2.` → 571–572.
- Checks: every target exists in `pi-5.md` and in the live root edition; cited numbers only move forward; every cited root range sits in the root section matching the commentary heading. Removing the inserted lines gives back the pre-insertion file.
- Note: `4-SYSTEM/Guidelines/known-source-irregularities.md`, which the source notes point to, does not exist. The exceptions are recorded only in the frontmatter `source_note`.

## F. Linter and parser

First lint run failed on all three with one error: `license` required. `license: cc0` was added by the user's approval (matches `pi-5.md` and pi-4). The linter also patched `commentary_of: HE6FGm4AAqwlDOTnCT0Yd` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-5.md`. Titles had the "(extract from …)" suffix removed and `tag_ids: [296WZOr8MXWteSqBBI7pl]` added, as for pi-4. After that all three linted OK and parsed OK.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 264,111 | 76,773 | 142,897 |
| Segments | 816 (815 paragraph, 1 top) | 454 (453 + 1) | 492 (491 + 1) |
| TOC nodes / max depth | 278 / 5 | 211 / 5 | 206 / 5 |
| Alignment pairs | 1,441 | 903 | 932 |

Pair counts exceed the transclusion lines because the parser also attaches each unnumbered paragraph to the transclusion above it (same as pi-4: 267 pairs for 272 paragraphs). Warnings, none blocking: author/translator missing, `alt_titles` missing.

Titles (frontmatter and upload payload): `Kathāvatthu-aṭṭhakathā`, `Kathāvatthu-mūlaṭīkā`, `Kathāvatthu-anuṭīkā`.

Outputs: `4-SYSTEM/scripts/linter-commentary/output/pi-kathavatthu-*.lint.json` and `4-SYSTEM/scripts/parser-commentary/output/pi-kathavatthu-*/` (text, edition, toc and alignment JSON each).

## G. Upload (done by hand with curl) and live check

Per file: `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `PUT /v2/editions/{root_edition}/alignments/{edition}` (pairs flipped to root, then commentary), `POST /v2/editions/{edition}/table-of-contents`. Root edition used: `WjnE60LMIzQETFlXoh9Hd` (`pi-5.md`; root text `HE6FGm4AAqwlDOTnCT0Yd`). No API key was needed.

| | text_id | edition_id | toc_id |
|---|---|---|---|
| aṭṭhakathā | `ynjwNOhnRKJzbfpL8fMY1` | `v5HrRlZFp7thp2aGTJJLm` | `bMmNIN47MJsaZlv02IyYT` |
| mūlaṭīkā | `Awq6BwDSyKA3BEvodcEmk` | `4rL7eOexrXBXN7UydZNnI` | `t4pwbvl4zFrGIx3hQe20b` |
| anuṭīkā | `s2GMCzOo9FrV9znoTCAM7` | `nkSDSS7ezbdrXo0XCxdvo` | `Cl385DCm70UPWZbQ1A5O1` |

Live copies were read back from the API and compared with the local payloads:

- text, language, license `cc0`, tag `296WZOr8MXWteSqBBI7pl`, `commentary_of` = root text: correct, and the root text now lists exactly these three commentaries
- edition content: character-for-character identical to local
- TOC: 278 / 211 / 206 nodes, depth, title and span identical
- segments: 816 / 454 / 492, every reference and span identical
- alignments: 1,441 / 903 / 932, the set of (root, commentary) pairs identical, root edition on the source side

## Things to know

- **Upload IDs are in frontmatter** on all three files (`text_id`, `edition_id`, `toc_id` from section G), matching pi-4 after upload.
- There is no alignment between layers (mūlaṭīkā to aṭṭhakathā, anuṭīkā to mūlaṭīkā), as for pi-3 and pi-4.
- Running the linter refreshes the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; it was restored with `git checkout` each time.
- Not compared: the reader's rendered TOC and verse links in the browser. Open each text in the reader to confirm.
- Aṭṭhakathā `^5-1`–`^5-5` (opening verses before the first heading) and `T-1` (homage) have no root block to align to, as expected.
- The 13 forms listed in section D still need a specialist decision.

## Files to commit

The three `.md` files, the three `.lint.json` files, the three parser output folders and this report. Not `.gitignore`, `4-SYSTEM/scripts/.env.example`, or the other `0-INBOX` files. Never `.env`.
