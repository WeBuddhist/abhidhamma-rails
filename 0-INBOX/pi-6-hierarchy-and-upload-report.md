# Yamaka (`pi-6`) commentaries — structure, content, and upload

**Date:** 2026-10-29  
**Scope:** the three pi-6 commentaries, checked against their root text:

- `1-SOURCES/Commentaries/pi-yamaka-atthakatha.md`
- `1-SOURCES/Commentaries/pi-yamaka-mulatiika.md`
- `1-SOURCES/Commentaries/pi-yamaka-anutiika.md`

**Root text (reference):** `1-SOURCES/Text/pi-6.md` (Yamakapāḷi). Every transclusion target, every linked range and every commentary section was checked against it. It was read only, not edited.

**Checked against:** the root text `pi-6.md`, `4-SYSTEM/Guidelines/block-id-spec.md`, the live tipitaka.app data (`/api/children` and `/api/text`), `4-SYSTEM/scripts/linter-commentary/` and `parser-commentary/`.

---

## Verdict

| Part | Result |
|---|---|
| A. Vault hierarchy (parent / child / siblings, IDs) | matches the block-ID spec |
| B. tipitaka.app tree, titles and order | match the site |
| C. Intentional differences | flagged, not changed |
| D. Text quality (glued words) | 41 glued words fixed; body text identical to the site word for word |
| E. Root-verse transclusions | added, aligned with the printed citations |
| F. Linter and parser | lint OK, parse OK (after adding `license: cc0`, `tag_ids` and titles) |
| Upload | done for all three; IDs in frontmatter |

---

## A. Hierarchy (all three files)

```
# Abhidhammapiṭake (…)                         ^0
## Yamaka…-…                                   ^6-0
### Ganthārambhavaṇṇanā                        ^6-1-0   (mūlaṭīkā, anuṭīkā only)
### Mūlayamakaṃ … Indriyayamakaṃ               10 yamakas
#### Paṇṇatti- / Pavatti- / Pariññāvāra…       vāras
##### Uddesa- / Niddesavāra…, Mahāvāra parts   up to 5 levels
### Nigamanakathā                              ^6-11-0  (aṭṭhakathā only)
```

- First heading is level `#`. No heading level skips. Every heading ID ends in `-0` and extends its parent's ID. Siblings run 1…n with no gaps.
- Content IDs are one continuous counter per file, book 6 only, at most 3 parts, no duplicates or gaps:
  - aṭṭhakathā `^6-1` … `^6-195` (46 headings)
  - mūlaṭīkā `^6-1` … `^6-146` (49 headings)
  - anuṭīkā `^6-1` … `^6-174` (48 headings)
- Yamaka positions differ by file because of sibling numbering: in the aṭṭhakathā Mūlayamakaṃ is `^6-1-0`; in the ṭīkās it is `^6-2-0` (after Ganthārambhavaṇṇanā). This is by design.
- Root `pi-6.md` is zoned per yamaka: `^6-{yamaka}-{N}`, each zone `1…max` with no gaps (Mūla 99, Khandha 211, Āyatana 254, Dhātu 19, Sacca 170, Saṅkhāra 159, Anusaya 349, Citta 116, Dhamma 229, Indriya 482).

## B. Match with tipitaka.app

| Layer | Site node | Range | Result |
|---|---|---|---|
| aṭṭhakathā | `atta-ap-pp-6-34` … `-43` | paras 1620–1876 | 45 of 45 headings match in title and order |
| mūlaṭīkā | `tika-ap-pp-4` | paras 864–1057 | 48 of 48 |
| anuṭīkā | `tika2-ap-pp-5` | paras 916–1137 | 47 of 47 |

- Numbered paragraphs: the same count, order and printed numbers as the site (78 / 48 / 48).
- Text (re-checked 2026-10-30): with printed numbers compared separately, the body text is identical to the site word for word (9,053 / 8,104 / 10,779 words). The only extra line is the homage `^T-1` at the top of the two ṭīkā files. The site prints it once at the start of each combined Pañcapakaraṇa ṭīkā (para 0), and pi-5 keeps it the same way.
- Parent and child: the site's sidebar tree is mis-nested for pi-6. For example, in both ṭīkās "3. Āyatanayamakaṃ" through "9. Dhammayamakaṃ" hang under a "1. Paṇṇattivāro" node, and Cittayamakaṃ sits under Mahāvāro. The hierarchy was therefore checked against the site's printed numbering ("1. Mūlayamakaṃ" > "1. Paṇṇattivāro" > "Uddesavāravaṇṇanā", "2. Pavattivāravaṇṇanā", …). The vault follows that numbering in all three files.

## C. Intentional differences from the website

| Ours | Site | Note |
|---|---|---|
| each yamaka is a `###` sibling with its vāras nested | the ṭīkā sidebars nest later yamakas inside earlier vāras | the vault is cleaner |
| aṭṭhakathā Cittayamaka: Puggalavāravaṇṇanā `^6-8-2-1-0` under Niddeso | flat siblings | Niddeso has no body of its own; its child is printed "1." |
| Nigamanakathā `^6-11-0` as a sibling of the yamakas | nested under Indriyayamakaṃ | same pattern as pi-3, pi-4, pi-5 |
| aṭṭhakathā opening verses `^6-1`…`^6-3` directly under `## ^6-0` | the same (the source has no Ganthārambha heading here) | matches the site |
| heading IDs by sibling position | the site prints "1.", "2.", and skips numbers in Mahāvāro (1, 2, 3, 5, 7) | by design (`block-id-spec.md` §5) |
| centred end-lines ("Uddesavāravaṇṇanā.", "… niṭṭhitā.") | the same | kept as body text |

## D. Text quality: 41 glued words fixed

In every case the site has a bold lemma split by a page marker with spaces around it (e.g. `**Yassa** |V0.0296| **rūpakkhandho**`). The conversion dropped both the marker and the spaces. Each fix only inserts a space.

- aṭṭhakathā (14): Satte vāti (`^6-155`, split as the site prints it; the same paragraph keeps `sattevāti` twice, also as printed), Tīṇeva kusalamūlānīti, Ahetukaṃ abyākatanti, Sahetukaṃ nāmaṃ, Yassa rūpakkhandho, na parijānitthāti, Cittassa bhaṅgakkhaṇeti, Dvinnaṃ puggalānaṃ, kāmarāgānusayo nānusetīti, Na kāmadhātunti, Uppādakkhaṇe anāgatañcāti, anantarā aggamagganti, Yassa cittassa, Pavatte somanassavippayuttacittassa
- mūlaṭīkā (12): Kusalākusalamūlasaṅkhātānaṃ dvinnaṃ, Aññamaññayamake ye, ca ṭhapetvā, Imināyeva ca, Puggalokāsavāro labbhamānopīti, Dukkhaṃ dukkhasaccanti, Antamaso suddhāvāsānampīti, vā pana, Anuseti uppajjatīti, Pahīnavāre phalaṭṭhavaseneva, Tathārūpasseva khīṇāsavassa, Sacakkhukānaṃ vinā
- anuṭīkā (15): Vuttabyañjanatthasseva sambhavatoti, Mūlayogaṃ dīpetunti, Evaṃ vuttanti, vedanādayo daṭṭhabbā, tīraṇapariññāva vuttā, Saṅkhārānaṃ puggalānañca, bhūmīnaṃ okāsabhāvasseva, Samudāyavasena gahetvāti, Desanā saṃkiṇṇā, Yathā mūlayamake, Sanniṭṭhānena gahitesu, Indriyayamake vibhaṅge, Koci sabhāvo, Apāye opapātikavasenāti, Bhāvetabbapahātabbabhāvehi vināpi

Nothing is left for review: the text follows the site everywhere.

A re-scan against the site found no other glued words.

## E. Root-verse transclusions

Each numbered paragraph has one `![[1-SOURCES/Text/pi-6.md#^6-{yamaka}-{N}]]` line per root verse directly above it. Ranges expand to consecutive lines. The yamaka zone is taken from the `###` yamaka the paragraph sits under.

| | Numbered paragraphs | Transclusion lines | Distinct root targets |
|---|---|---|---|
| aṭṭhakathā | 78 | 1,276 | 1,276 |
| mūlaṭīkā | 48 | 979 | 979 |
| anuṭīkā | 48 | 1,009 | 1,009 |

- Every target exists in `pi-6.md`. No printed range runs backwards (end < start), and no truncated-tail ranges occur, so no entry was needed in `known-source-irregularities.md`.
- Cross-check: each citation's first root verse sits in the matching root section (Paṇṇatti → Paṇṇattivāro, Pavatti → Paccuppanna/Atīta/…, Pariññā → Pariññāvāro, Mahāvāra parts → the same vāra).
- **Reset-aware check (2026-10-30).** Root pi-6 restarts its numbering in every yamaka, so a printed number `A` has up to 10 candidate blocks (`^6-1-A` … `^6-10-A`). For each numbered paragraph, the candidates were every zone where all of `A…B` exist. Each candidate was scored on two things: whether the paragraph's quoted/bold lemmas occur in that zone's verses `A…B` (meaning), and whether the yamaka's subject word appears in the paragraph and its neighbours (context).
  - 147 of 174 paragraphs: the clear winner is the block already transcluded.
  - 27 ties or close calls were read by hand against the candidate root verses. All 27 confirm the current block. Examples: aṭṭhakathā `1-19.` says "dhātuyamakassa vaṇṇanā" → `^6-4`; aṭṭhakathā `99.` "kusalākusalānaṃ ekato anirujjhanato 'no'" matches `^6-9-99` ("yassa kusalā dhammā nirujjhanti … No"), not `^6-8-99`; mūlaṭīkā `22-254.` cites "(yama. 1.āyatanayamaka.22)" → `^6-3-22`; anuṭīkā `74-85.` "abyākatamūlena na ekamūlakaṃ" matches `^6-1-74` ("abyākatā … abyākatamūlā"), not `^6-9-74`.
  - Result: no transclusion changed.
- One placement to know about: the aṭṭhakathā Indriyayamaka paragraph printed `1-86.` (root Paṇṇattivāro) sits under Pavattivāravaṇṇanā. The site places it the same way. It is linked as printed.

## F. Linter and parser

`license: cc0`, `tag_ids: [296WZOr8MXWteSqBBI7pl]` and titles were added: `Yamakappakaraṇa-aṭṭhakathā`, `Yamakapakaraṇa-mūlaṭīkā`, `Yamakapakaraṇa-anuṭīkā`. Titles are the book headings as printed in the source; tipitaka.app uses the same names. The linter patched `commentary_of: IZ74xHeWa9xortlOhL6cc` and `category_id: MZUUxphQ0yFwLBon3Vng8` from `pi-6.md`. All three lint OK and parse OK. `languages.py` was restored with `git checkout`.

Outputs: `4-SYSTEM/scripts/linter-commentary/output/pi-yamaka-*.lint.json` and `4-SYSTEM/scripts/parser-commentary/output/pi-yamaka-*/` (text, edition, toc and alignment JSON).

| | aṭṭhakathā | mūlaṭīkā | anuṭīkā |
|---|---|---|---|
| Content (characters) | 92,417 | 83,787 | 114,816 |
| Segments | 196 | 147 | 175 |
| TOC nodes / max depth | 46 / 4 | 49 / 4 | 48 / 4 |
| Alignment pairs | 6,517 | 5,499 | 6,162 |

Alignment pairs are high because a paragraph that follows a large group (e.g. `22-254.`, 233 verses) aligns to every verse in the group, per the parser's scope rule.

Warnings (none block): author/translator missing, `alt_titles` missing.

## Kept as the source prints it

- **The anuṭīkā Khandhayamaka has two "Paṇṇattivāro" headings** (`^6-3-1-0` › Uddesavāravaṇṇanā, `^6-3-2-0` › Niddesavāravaṇṇanā). The site prints "1. Paṇṇattivāro" twice (https://tipitaka.app/latn/tika2-ap-pp-5-4 and https://tipitaka.app/latn/tika2-ap-pp-5-5), so the vault keeps both. The mūlaṭīkā source prints it once, and the vault follows that too.

## Upload

Root edition: `vYtNelE9z5AWQ0jAv82cC` (`pi-6.md`).

| | text_id | edition_id | toc_id |
|---|---|---|---|
| aṭṭhakathā | `cUpbK3Y0ljPyLDcAirNbP` | `kocWHwHRuH3lc5Odf6Xfy` | `uO0m1mTDQ4fPsefPOPQxC` |
| mūlaṭīkā | `mTZwGbmllr9P0WOwBj6DI` | `2GNMKB0g0zr1YzbBosLuE` | `IWi4VypR4Mb369LOT6sJr` |
| anuṭīkā | `1dUcj3Ct12ccgItOuslPV` | `GwnGsBoL586jz6lrD0Va6` | `zr3RFZ2uHXESixIYIXGAf` |

IDs are saved in each file's frontmatter. Live alignments were re-checked on 2026-10-30 and match the files pair for pair (6,517 / 5,499 / 6,162). There is no alignment between layers (mūlaṭīkā to aṭṭhakathā, anuṭīkā to mūlaṭīkā), as for pi-3 to pi-5.

**Titles in the library:** the mūlaṭīkā and anuṭīkā titles and the aṭṭhakathā title were changed to the source names after upload. They were updated in the library with `PATCH /v2/texts/{text_id}` on 2026-10-30; the live titles match the files.


## Files to commit (when ready)

The three `.md` files, the three `.lint.json` files, the three parser output folders and this report. Not `languages.py`, `.gitignore`, `4-SYSTEM/scripts/.env.example`, or the other `0-INBOX` files. Never `.env`.
