---
title: "Verify report — pi-dhammasangani-mulatiika.md transclusion coverage"
file_type: verify-report
target_file: 1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md
source_file: 1-SOURCES/Text/pi-1.md
verse_range: all
---

# Verify report — 1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md against 1-SOURCES/Text/pi-1.md (all)

Independent re-derivation performed by close-reading the entire mūlaṭīkā (2100 lines, 613 paragraphs, 97 headings) in document order against the root text (1782 blocks), cross-checked at every step against the file's existing transclusion links (222 linked comm-block insertion points, 429 total root-id link instances) rather than trusting them as a starting point. `pi-1.md` was left completely untouched throughout. `pi-dhammasangani-mulatiika.md` was also left untouched during the audit itself; the one confirmed GAP finding below was subsequently fixed by explicit request, as documented in [Fixes applied](#fixes-applied) at the end of this report — the file now carries 430 links (429 original + 1 inserted), and the GAP section below is kept in its original audit form for the record, marked resolved.

> **Status: the GAP found by this audit has since been fixed.** See [Fixes applied](#fixes-applied) at the end of this report for exactly what was inserted and where.

**Important structural note, unlike the aṭṭhasālinī audit**: the mūlaṭīkā is a sub-commentary on the *aṭṭhakathā's own wording* (it glosses difficult terms in the Aṭṭhasālinī's prose), not a running word-by-word commentary on the root Dhammasaṅgaṇī text directly. Its opening ~165 lines (`Vīsatigāthāvaṇṇanā` and most of `Nidānakathāvaṇṇanā`, i.e. the mūlaṭīkā's remarks on the aṭṭhakathā's own introductory narrative and homage verses) legitimately carry **zero** links to `pi-1.md`, exactly like the aṭṭhasālinī's own Nidānakathā did in the earlier audit — there is no root-text content to anchor to until the mūlaṭīkā reaches the mātikā padavaṇṇanā at line 186 (`Cittuppādakaṇḍaṃ`). From that point on, coverage is inherently much sparser than the aṭṭhakathā's own coverage was (429 link instances across 613 paragraphs, vs. the aṭṭhakathā's 510 across 1951) — this is expected and correct, since a sub-commentary only glosses *some* of the root's own padas (the ones whose aṭṭhakathā treatment needs further unpacking), not every one of them. A root item with no mūlaṭīkā discussion anywhere is not a gap; it simply isn't glossed at this tier, per the skill's own Rule 5.

## Summary

| Category | Count |
|---|---|
| MATCHED | 222 linked comm-blocks / 429 root-id link instances — see breakdown below |
| MISMATCHED-TARGET | 0 |
| MISPLACED | 0 |
| DUPLICATE-IN-RUN | 0 |
| MISSING-REANCHOR | 0 |
| GAP | 1 found, **fixed** — see [Fixes applied](#fixes-applied) |
| AMBIGUOUS | 0 |
| MALFORMED | 0 |
| OUT-OF-SCOPE | 0 |

**Bottom line, in answer to the standing question ("is the current transclusion wrong, and is it missing any — e.g. a block that discusses two root items but only one was transcluded"):** the existing 429-instance transclusion coverage is not wrong anywhere — no link points at the wrong root item, sits at the wrong block, duplicates within a run, or fails to re-anchor after a heading. And this file *does* have exactly the kind of gap the question describes: one comm block explicitly discusses **two** root padas together, but only the first of the two was ever linked. Full detail below.

## MATCHED

The file's 429 link instances (222 comm-block insertion points, including 22 merges) were checked in full against the mūlaṭīkā's own structure — six kaṇḍa-level sections mirroring the aṭṭhakathā's own (Cittuppādakaṇḍaṃ, Rūpakaṇḍaṃ, Nikkhepakaṇḍaṃ, Aṭṭhakathākaṇḍaṃ), preceded by the narrative Sumedhakathāvaṇṇanā. All matched — correct root id(s), correct insertion point (first block of the run), correct run boundaries, correct heading-forced re-anchoring, no duplicates within an open run.

- **Sumedhakathāvaṇṇanā** (`Vīsatigāthāvaṇṇanā` + `Nidānakathāvaṇṇanā`, lines 24–185): 0 links — legitimate. This is the mūlaṭīkā's own commentary on the aṭṭhakathā's introductory homage verses and narrative preamble; no root-item content exists here to anchor to (exactly parallel to the aṭṭhasālinī's own Nidānakathā, which likewise carried 0 links in the earlier audit).
- **Tikamātikāpadavaṇṇanā / Dukamātikāpadavaṇṇanā / Suttantikadukamātikāpadavaṇṇanā** (lines 186–515): mātikā triad/pair items matched to their root block(s), including the 15 gocchaka-grouped `1-MII-*` merges (comm ^1-125 through ^1-145) — all confirmed contiguous, no skipped id inside any claimed merge range.
- **Kāmāvacarakusalapadabhājanīyavaṇṇanā** (dvārakathā/kammapathakathā, Dhammuddesavārakathā rāsi-vaṇṇanās, Niddesavārakathā/Koṭṭhāsavāra/Suññatavāra, the four rūpāvacara jhāna nayas with kasiṇa/abhibhāyatana/vimokkha/brahmavihāra/asubha excursuses, arūpāvacara, tebhūmaka, lokuttara, all 12 akusala cittas, the abyākata vipāka/kiriya cittas including the vipākuddhāra material): lines 516–1434 — every dedicated-commentary root item matched.
- **Rūpakaṇḍaṃ** (Uddesavaṇṇanā, rūpasaṅgaha varieties, Rūpavibhatti Ekakaniddesa, Dukaniddesa [Upādā/Noupādābhājanīya, Catukka/Pañcaka], Pakiṇṇakakathā): lines 1435–1636 — every dedicated-commentary root item matched.
- **Nikkhepakaṇḍaṃ** (Tikanikkhepakathā, Dukanikkhepakathā, Suttantikadukanikkhepakathā — including the ajjava/maddava/khanti stretch discussed under GAP below): lines 1637–2000 — every item matched except the one gap.
- **Aṭṭhakathākaṇḍaṃ** (Tikaatthuddhāravaṇṇanā, Dukaatthuddhāravaṇṇanā): lines 2001–2100 — every dedicated-commentary root item matched.

**Legitimate no-link stretches (not gaps).** Two patterns account for the large majority of unlinked paragraphs, both checked systematically:
1. **Section-closing colophons** — every `<Section>vaṇṇanā niṭṭhitā` closing line (50 instances found and checked) is a structural marker with no lemma content of its own; correctly unlinked.
2. **Sparse-by-design tika coverage** — since the mūlaṭīkā only glosses padas whose aṭṭhakathā treatment needs further unpacking, the majority of root items simply have no dedicated mūlaṭīkā paragraph anywhere, which is not a gap per the skill's Rule 5. Every candidate flagged by automated lemma-overlap screening (53 paragraphs, out of which 45 fell after the narrative preamble) was individually read in context; all but one resolved to either (a) noise from a short, generic Pali word shared across many unrelated root blocks (e.g. "sattā", "dhamme", "cattāro", "rūpa" — words appearing in hundreds of blocks with no bearing on the paragraph's actual topic), or (b) a genuine but purely comparative citation of another pada's exact wording used to explain the currently-linked item (e.g. quoting "diṭṭhaṃ sutaṃ mutaṃ viññātaṃ" or "katame dhammā appaccayā" as a cross-reference formula while glossing something else entirely). The one exception is reported below.

## MISMATCHED-TARGET

None found. Every existing link's cited root id matches what the mūlaṭīkā immediately following it actually discusses.

## MISPLACED

None found. Every run-opening link sits at the first block of its run, not mid-run. (Automated structural check: 0 backward-order jumps within any open run.)

## DUPLICATE-IN-RUN

None found. No root item's link is repeated inside a single open run. (Automated structural check: 0 duplicates.)

## MISSING-REANCHOR

None found. Every heading in the file was checked as a run-closing boundary; nowhere does the mūlaṭīkā resume discussing the same root item after a heading without a fresh link.

## GAP

One confirmed.

### GAP 1 — root ^1-1347 (maddavo)

- **Root text** (`1-SOURCES/Text/pi-1.md#^1-1347`): "Tattha katamo maddavo? Yā mudutā maddavatā akakkhaḷatā akathinatā **nīcacittatā** – ayaṃ vuccati maddavo."
- **Where the gap sits**: `1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md#^1-553` (line 1919, under `Suttantikadukanikkhepakathāvaṇṇanā`), currently linked only to root `^1-1346` (ajjavo). The block's own text explicitly names **both** padas together: "**Ajjavaniddese** ajjavo ajjavatāti ujutā ujukatā icceva vuttaṃ hotīti **ajjavamaddavaniddesesu** ujukatāmudutāniddesehi visesaṃ **maddavaniddese** vuttaṃ 'nīcacittatā'tipadamāha. Tattha 'nīcacittatā mudutā'ti puna mudutāvacanaṃ nīcacittatāya visesanatthaṃ..." — i.e. "In the exposition of *ajjava*... but, distinguishing it from the [plain] 'straightness/softness' wording, **in the exposition of *maddava*** [specifically], the word 'nīcacittatā' is used..." The block explicitly compares the *ajjava* niddesa's wording against the *maddava* niddesa's wording (which is quoted verbatim: "nīcacittatā", matching root ^1-1347's own definition word-for-word) — this is not a passing citation, it is the block's second half of substantive content.
- **Existing coverage either side**: comm ^1-553 links root `1-1346` (ajjavo) only. The very next linked block, comm ^1-554, links root `1-1348` (khanti) — so `1-1347` (maddavo) is skipped entirely between them, even though its defining term is directly quoted and explained in ^1-553.
- **Why this is a genuine gap, not sparse-coverage-by-design**: this is exactly the "one paragraph, two padas, only one transcluded" pattern the standing question asked about. The block gives real, dedicated exegesis of *maddava*'s specific wording ("nīcacittatā"), not a bare cross-reference — it just does so as the second half of a block that opens by discussing *ajjava*.
- **Fix — APPLIED**: a second link — `![[1-SOURCES/Text/pi-1.md#^1-1347]]` — was inserted as a **merge**, stacked directly beneath the existing `![[1-SOURCES/Text/pi-1.md#^1-1346]]` line (line 1917 before the edit; both link lines now sit at lines 1917–1918), with no blank line between the two link lines, per `transclusion-root-into-commentary`'s merge format. Comm block ^1-553 (now starting at line 1920) is otherwise untouched, and the surrounding blocks — ^1-552 above and ^1-554/root `1-1348` below (now shifted to line 1922) — were left completely alone. The block now correctly carries both root ids it discusses.

No other candidate anywhere else in the file showed this "two padas explicitly named and both defined/quoted, only one linked" pattern — confirmed by grepping the whole file for every instance of the dual-exposition marker "niddesesu" (5 total hits): four of the five are generic plural references to a class of earlier-established formulas (not naming two specific unlinked padas), and only this one names and quotes two adjacent padas' defining terms directly.

## AMBIGUOUS

None found. Every root item the independent re-derivation could match, it could match to exactly one root id with confidence — including GAP 1 above, where both padas discussed are individually unambiguous (a merge case, not an ambiguity case).

## MALFORMED

None found. Every in-scope transclusion uses the full vault-relative path `1-SOURCES/Text/pi-1.md#^<id>`, and every cited block id was confirmed to exist in `pi-1.md` (0 dangling ids out of 429).

## OUT-OF-SCOPE

None found. Every transclusion link in the file targets `1-SOURCES/Text/pi-1.md`; none targets any other file.

---

## Cross-check: merge-completeness, stripped copy, and coverage corroboration

**1. Merge-completeness check.** All 22 comm-blocks that link more than one root id at once were enumerated: 15 are the mūla-mātikā gocchaka merges (comm ^1-125–^1-145, linking `1-MII-1` through `1-MII-142`), and 7 are contiguous kāmāvacarakusala-padabhājanīya merges (comm ^1-274–^1-300, linking runs such as `1-42..1-43`, `1-58..1-120`, `1-121..1-145`, `1-176..1-180`). Every merge's linked root-id list was confirmed contiguous in `pi-1.md`'s own block order — 0 issues found programmatically.

**2. Stripped no-transclusion copy.** Created at `1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.no-transclusion.md`, generated mechanically by removing every standalone `![[1-SOURCES/Text/pi-1.md#^...]]` line (and collapsing the resulting doubled blank lines) from the original — no other content touched. Verified programmatically:
- Original: 2100 lines. Link lines removed: exactly 429 (matching the report's MATCHED total precisely). Stripped copy: 1449 lines.
- All 710 of the mūlaṭīkā's own native block ids (paragraphs + headings) appear in the stripped copy in exactly the same order as in the original, with the 429 link-target ids excluded from the comparison: identical, zero discrepancy.
- Zero residual `![[1-SOURCES/Text/pi-1.md#^...]]` links remain in the stripped copy.
- Frontmatter and all non-link content preserved verbatim.

**3. Coverage / lemma-overlap corroboration.** Since this file's own prose only rarely uses literal quotation marks around root-text lemmas (unlike the aṭṭhasālinī, much of the mūlaṭīkā paraphrases rather than quotes), an automated quoted-substring scan was run as a first-pass screen (not a substitute for reading) against all 613 paragraphs: 104 had at least one quoted phrase matching root-text wording, and cross-referencing those against the existing link structure flagged 53 paragraphs for manual review (16 "candidate quote, no open link", 37 "candidate quote conflicting with the active link"). Every one of the 53 was read in its full surrounding context; 8 fell inside the legitimately-zero-link narrative preamble (noise), and of the remaining 45, all but the one reported above resolved to shared generic vocabulary or genuine cross-reference citations, not missed matches. A separate full-file grep for the structural signal that actually caught GAP 1 — a comm block naming two padas' expositions together ("...niddesesu") — surfaced only that one true positive among 5 total hits.

**Conclusion of cross-check:** all checks corroborate the close-read's finding. No additional gaps, mismatches, or structural issues were surfaced. The one GAP finding (root ^1-1347, "maddavo") stands as the only place this file's existing transclusion coverage is incomplete.

---

## Fixes applied

The GAP finding above was, by explicit follow-up request, fixed directly in the live `1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md` after this audit was completed and the match was confirmed. This section documents exactly what was changed. `1-SOURCES/Text/pi-1.md` was **not** touched — this section is about the commentary file only.

**Insertion — GAP 1 fix.** `![[1-SOURCES/Text/pi-1.md#^1-1347]]` was inserted as a standalone line, stacked directly beneath the existing `![[1-SOURCES/Text/pi-1.md#^1-1346]]` link with no blank line between them (a merge, not a new run), immediately before comm block `^1-553` ("Ajjavaniddese ajjavo ajjavatāti..."). In the live file the two stacked links now sit at **lines 1917–1918**; the block they anchor (`^1-553`) now starts at line 1920. The existing link before it (`^1-1346`, ajjavo) was left in place and untouched, and the existing link that follows (`^1-1348`, khanti, now at line 1922) was likewise left untouched — this is a single fresh insertion merged into the existing link group, not a new separate run.

**Mechanics of the edit.** The link line was inserted directly into the file with a short script, preserving the file's CRLF line endings throughout. No existing line was altered, reordered, or deleted — only the one new link line was added.

**Post-fix file statistics** (verified directly against the live file after the insertion):

| Stat | Before | After |
|---|---|---|
| Total lines | 2100 | 2101 |
| Total transclusion links to `pi-1.md` | 429 | 430 |

Frontmatter and the file's closing colophon ("Dhammasaṅgaṇī-mūlaṭīkā samattā. ^1-612") were confirmed unchanged. No other content in the file was modified.

**Note on the stripped no-transclusion copy.** `1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.no-transclusion.md` (see Cross-check §2 above) was generated from the file's **pre-fix** state (429 links, 2100 lines) and has not been regenerated since this insertion was applied. Its prose content is unaffected either way (stripping removes link lines regardless of how many there are), but it is not a byte-for-byte reflection of the current live file's link layout and should be regenerated if an up-to-date stripped copy is needed.

---

*Report generated by an independent full-file close-read (all 2100 lines / 613 paragraphs / 97 headings), cross-checked block-by-block against the file's 429 existing link instances, followed by the merge-completeness, stripped-copy, and lemma-overlap cross-checks above. `pi-1.md` was not modified at any point. `pi-dhammasangani-mulatiika.md` was not modified during the verification itself; it was subsequently modified, by explicit follow-up request, to apply the GAP fix documented in "Fixes applied" above.*
