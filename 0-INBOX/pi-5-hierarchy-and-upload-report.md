# Kathāvatthu (`pi-5`) commentaries — structure, content, and upload

**Date:** 2026-10-29  
**Scope:** the three pi-5 commentaries only:

- `1-SOURCES/Commentaries/pi-kathavatthu-atthakatha.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-mulatiika.md`
- `1-SOURCES/Commentaries/pi-kathavatthu-anutiika.md`

Root `1-SOURCES/Text/pi-5.md` was read for transclusion targets only and not edited.

**Checked against:** `4-SYSTEM/Guidelines/block-id-spec.md`, the live tipitaka.app data, `4-SYSTEM/scripts/linter-commentary/` and `parser-commentary/`.

---

## Verdict

| Part | Result |
|---|---|
| A. Vault hierarchy (parent / child / siblings, IDs) | PASS |
| B. tipitaka.app tree, titles and order | PASS |
| C. Intentional differences | flagged, not changed |
| D. Text quality (glued words) | PASS after 93 fixes |
| E. Root-verse transclusions | added, aligned with the source |
| F. Linter and parser | PASS |
| Upload | done for all three; IDs in frontmatter |

---

## A. Hierarchy (all three files)

```
# Abhidhammapiṭake (…)                       ^0
## Kathāvatthu-…                             ^5-0
### Nidānakathā / Ganthārambha…              ^5-1-0 …
### Mahāvaggo … Tevīsatimavaggo              ^5-2-0 … (vaggas)
#### kathā (e.g. Puggalakathā)               ^5-2-1-0 …
##### … ###### sub-sections                  up to 6 levels
### Nigamanakathā                            ^5-25-0 (aṭṭhakathā only)
```

- First heading is level `#`; no heading level skips; every heading ID ends in `-0` and extends its parent's ID. Siblings run 1…n with no gaps.
- Content IDs are one continuous counter per file, book 5 only, no duplicates or gaps:
  - aṭṭhakathā `^5-1` … `^5-815` (278 headings)
  - mūlaṭīkā `^5-1` … `^5-453` (211 headings)
  - anuṭīkā `^5-1` … `^5-491` (206 headings)
- Root `pi-5.md`: IDs `^5-1` … `^5-918`, no numbering reset.

## B. Match with tipitaka.app

| Layer | Site node | Result |
|---|---|---|
| mūla | `ap-kvu` | 479 of 479 root headings match `pi-5.md` |
| aṭṭhakathā | `atta-ap-pp-6` | 277 of 277 headings match in title and order |
| mūlaṭīkā | `tika-ap-pp-3` | 210 of 210 match |
| anuṭīkā | `tika2-ap-pp-4` | 205 of 205 match |

- Numbered paragraphs: same count, order, heading and text as the site (388 / 223 / 208).
- Text: the only differences are the centred colophon lines the site renders as headings, which we keep as body text.

## C. Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| vaggas group their kathās | site trees are flat or misfiled | vault is cleaner |
| Nigamanakathā `^5-25-0` as sibling of the vaggas | nested under the last vagga | same pattern as pi-3, pi-4 |
| heading IDs by sibling position | site prints "1.", "2." | by design, same as pi-3 and pi-4 |
| particle "ti" attached (`atthīti`) | site writes `atthī ti` | site display convention |

## D. Text quality: 93 glued words fixed

Words fused by the conversion where tipitaka.app has a word boundary; only spaces were added.

- aṭṭhakathā (25), mūlaṭīkā (47), anuṭīkā (21)
- Examples: `Dibbenacakkhunā` → `Dibbena cakkhunā`, `Atītaṃatthīti` → `Atītaṃ atthīti`, `Ājānāhiniggaha` → `Ājānāhi niggaha`.
- Left for specialist review (13 possible compounds): `tenahi`, `dvepi`, `navattabbaṃ`, `mahāpathavīādīni`, `rūpantiādi`, `maggotiādi`, `sakkāyadiṭṭhiādīsupi`, `satipaṭṭhānādīsupi`, `somādayo`, `kusalādipañhaṃ`, `sammutiñāṇapañhesu`, `suññatādiatthaṃ`, `liṅgākappabhedaṃ`.

## E. Root-verse transclusions

Each numbered paragraph has one `![[1-SOURCES/Text/pi-5.md#^5-N]]` line per root verse directly above it; ranges expand to consecutive lines.

| | Numbered paragraphs | Transclusion lines | Distinct root targets |
|---|---|---|---|
| aṭṭhakathā | 388 | 892 | 890 |
| mūlaṭīkā | 223 | 433 | 433 |
| anuṭīkā | 208 | 505 | 505 |

- Every target exists in `pi-5.md`.
- Aligned with the source: each paragraph links to the root verses its printed citation names, exactly as on tipitaka.app, including the three irregular citations below.

Irregular citations (as printed in CST / tipitaka.app; see `4-SYSTEM/Guidelines/known-source-irregularities.md`):

| Block | Printed | Linked to |
|---|---|---|
| aṭṭhakathā `^5-544` | `618-820.` | `^5-618`…`^5-820` (as printed) |
| aṭṭhakathā `^5-568` | `541-545.` | `^5-541`…`^5-545` (as printed) |
| anuṭīkā `^5-381` | `706-608.` | `^5-608`…`^5-706` (as printed, low to high) |
| mūlaṭīkā `^5-270` | `557-8.` → `557-558.` | `^5-557`, `^5-558` |
| mūlaṭīkā `^5-281` | `571-2.` → `571-572.` | `^5-571`, `^5-572` |

## F. Linter and parser

`license: cc0`, `tag_ids: [296WZOr8MXWteSqBBI7pl]` and clean titles were added; the linter patched `commentary_of` and `category_id` from `pi-5.md`. All three lint OK and parse OK.

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 264,111 | 76,777 | 142,897 |
| Segments | 816 | 454 | 492 |
| TOC nodes | 278 | 211 | 206 |
| Alignment pairs | 1,841 | 903 | 1,124 |

Titles: `Kathāvatthu-aṭṭhakathā`, `Kathāvatthu-mūlaṭīkā`, `Kathāvatthu-anuṭīkā`.

## Upload

Root edition: `WjnE60LMIzQETFlXoh9Hd` (`pi-5.md`).

| | text_id | edition_id | toc_id |
|---|---|---|---|
| aṭṭhakathā | `ynjwNOhnRKJzbfpL8fMY1` | `v5HrRlZFp7thp2aGTJJLm` | `bMmNIN47MJsaZlv02IyYT` |
| mūlaṭīkā | `Awq6BwDSyKA3BEvodcEmk` | `4rL7eOexrXBXN7UydZNnI` | `t4pwbvl4zFrGIx3hQe20b` |
| anuṭīkā | `s2GMCzOo9FrV9znoTCAM7` | `nkSDSS7ezbdrXo0XCxdvo` | `Cl385DCm70UPWZbQ1A5O1` |

The live library matches the files. IDs are saved in each file's frontmatter.

## Things to know

- There is no alignment between layers (mūlaṭīkā to aṭṭhakathā, anuṭīkā to mūlaṭīkā), as for pi-3 and pi-4.
- Running the linter refreshes the tracked `4-SYSTEM/scripts/linter-commentary/languages.py`; restore it with `git checkout`.

## Files to commit

The three `.md` files, the three `.lint.json` files, the three parser output folders and this report. Not `.gitignore`, `4-SYSTEM/scripts/.env.example`, or the other `0-INBOX` files. Never `.env`.
