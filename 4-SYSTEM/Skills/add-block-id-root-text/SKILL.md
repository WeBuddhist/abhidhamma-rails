---
name: add-block-id-root-text
description: Apply block IDs to Pali Abhidhamma root-text files (mātikā/kaṇḍa prose) in 1-SOURCES/Text/. Derives IDs from headings + leading N. numbers. Sole run → ^book-N; multiple runs → principal run stays ^book-N, others get ^book-k-N. Headings numbered by sibling position, may be longer.
---

# Add Block ID — Pali Mātikā/Kaṇḍa Texts

> Shared address space: `4-SYSTEM/Guidelines/block-id-spec.md` is the authoritative spec for ID grammar, the reserved-character registry, and cross-skill invariants. Register any new marker there before using it.

Apply block IDs to Pali Abhidhamma prose whose source prints paragraph numbers (`1.`, `2.`, `58.`…) that sometimes restart. **Ignore every existing `^…` ID in the file.** Rebuild from two signals only:

1. **Headings** (`#` … `#####`) — sibling order under each parent
2. **Leading verse numbers** — the integer before the first `.` on a content line, e.g. `1. (Ka) hetū dhammā.` → `1`

---

## Inputs (what counts)

| Signal | Use | Ignore |
|---|---|---|
| `N. text…` at start of a content line | `N` is the content address | Any trailing `^old-id` |
| `#` / `##` / `###` / `####` / `#####` title lines | Heading hierarchy + sibling counters | Any trailing `^old-id` |
| Homage / plain lines before `#` | Pre-title blocks | — |
| Unnumbered continuation lines | Same block as the preceding `N.` | Do not invent a new `N` |

Example (Dukamātikā):

```text
1. (Ka) hetū dhammā.        → take 1
2. (Ka) sahetukā dhammā.    → take 2
```

---

## Content IDs — choose `n-n` or `n-n-n`

Content IDs use **at most 3** segments. Prefer the **shortest form that stays unambiguous**.

### Step A — find numbering runs

Walk the file in order. A **run** is one unbroken sequence of leading numbers (`N.`).

- A new run starts at the first `N.` in the file.
- Another new run starts whenever the leading number returns to `1` after a previous number that was not `1`.
- Most headings do **not** start a run — a run often continues across many `####` / `#####` headings.

### Step B — the zone is a collision-breaker, nothing more

**Do not classify runs by genre or position.** Earlier versions of this skill used Roman numerals for "front matter" and reserved other vocabularies for "body" / "back matter". That was a mistake: those labels claimed to describe *what content is* (matrix, intro, closing) when they actually only recorded *where a counter happened to reset*. The two come apart constantly — a mātikā can sit mid-body, an `Uddesa` can be numerically fused to the body, matrix content can be indistinguishable from prose by numbering alone.

The middle segment exists for exactly one reason: **to stop two blocks with the same printed `N` from colliding inside one book.** Nothing else. It carries no meaning about genre, position, or importance.

It follows that:

- A book whose printed numbers are already unique book-wide (one single run) needs **no** middle segment at all.
- A book with several runs needs one only for the runs that would otherwise collide.

### Step C — pick the ID shape (do not hard-code book-specific patterns)

For each run, build the content ID from `book` + optional middle label + source `N`:

```
book  = Abhidhammapiṭaka order of this file (1…7), from ## title
N     = the printed leading number on that paragraph (never recomputed)
```

| Condition | Content ID | Shape |
|---|---|---|
| **Exactly one** run in the whole file | `^{book}-{N}` | `n-n` — **omit** the middle segment |
| **Two or more** runs | principal run `^{book}-{N}`; every other run `^{book}-{1}-{N}`, `^{book}-{2}-{N}`, … | `n-n` / `n-n-n` |

**Which run is "principal"?** The one you want cheapest to cite — normally the main body, which is usually also the longest. It keeps the bare `^{book}-{N}` namespace. Every *other* run takes the next sequential Arabic label in document order (`1`, `2`, …). Because those labels are pure collision-breakers, they are assigned by position, not by what the run contains.

**Why keep the body bare?** If the body is a single continuous counter, `^{book}-{N}` already cites it uniquely, and it is the text people cite most. Adding a redundant middle segment only lengthens the IDs that matter most.

### The `M` zone — a matrix that opens the book's first counter

One narrow exception to "zones are sequential and meaningless". When a **mātikā/matrix section is what starts the book's first numbering run** — i.e. it precedes the body and owns its own counter(s) — it is genuinely introductory material, and gets the `M` vocabulary instead of a plain sequential number:

| Track | Shape | Example (book 1) |
|---|---|---|
| Heading — the matrix parent | `^{book}-M-0` | `### Mātikā ^1-M-0` |
| Heading — its children | `^{book}-M-{Roman}-0` | `#### Tikamātikā ^1-M-I-0`, `#### Dukamātikā ^1-M-II-0` |
| Heading — deeper levels | Roman all the way down | `##### Hetugocchakaṃ ^1-M-II-I-0` … `^1-M-II-XIV-0` |
| Content of a matrix run | `^{book}-M{Roman}-{N}` | `^1-MI-1`…`^1-MI-22`, `^1-MII-1`…`^1-MII-142` |

Heading and content use the **same Roman label** for the same object — heading `^1-M-I-0` ↔ content `^1-MI-{N}`; heading `^1-M-II-0` ↔ content `^1-MII-{N}`. The only difference is that the heading track keeps its segments separated (and may nest deeper), while content fuses `M` + Roman into a single token so it stays within 3 segments.

Body `###` numbering then starts at `1` **after** the `M` section (`### Cittuppādakaṇḍaṃ ^1-1-0`), since `M` occupies its own slot rather than a numeric one.

**The test is counter behaviour, not the word "mātikā".** Matrices are common and recur throughout these books — book 1 has a second `#### Mātikā` inside Rūpakaṇḍaṃ, book 2 has 23 mātikā headings and *no* opening matrix at all, book 3 has five inside its `Uddesa`. None of those get `M`, because none of them starts the first counter: their numbers continue the surrounding run, so they are ordinary content under ordinary zones. Only a matrix that **opens** the book's numbering qualifies.

### Duplicate printed `N` within one run

When the source repeats the same leading number without resetting the run (often consecutive):

```text
4. …
5. …
5. …
6. …
```

Keep the first as bare `N`; disambiguate later copies with an `x` suffix on the **last** segment:

| Printed | Content ID (sole body) | Content ID (zoned run) |
|---|---|---|
| first `5.` | `^{book}-5` | `^{book}-{zone}-5` |
| second `5.` | `^{book}-5x1` | `^{book}-{zone}-5x1` |
| third `5.` | `^{book}-5x2` | `^{book}-{zone}-5x2` |

`apply.py` does this automatically (occurrence order within each run). Do **not** invent a new run for a repeated `N` that is not a reset to `1`.

### Unnumbered body segments (`U` = Unnumbered)

Some body blocks have **no** leading `N.` and are **not** continuations of the previous numbered verse (blank-line separated units that must keep their own ID — e.g. an unlabelled matrix list under `##### Dukaṃ`).

Classify the gap first:

| Role | ID |
|---|---|
| Homage / pre-`#` (outside any numbering run) | `^T-1`, `^T-2`… — Step 4, **not** `U` |
| Numbered block in a non-principal run | usual zone label from Step C (`^{book}-{zone}-{N}`) |
| Continuation of the previous `N.` (same verse) | merge into that block; one ID on the last line |
| Standalone unnumbered **body** segment | `^{book}-U{k}` |

`U` means Unnumbered. Number `k` in **document order** across the whole file (every standalone unnumbered body block that sits inside a numbering run):

```text
^{book}-U1
^{book}-U2
…
```

Examples (`book=1`): `^1-U1`, `^1-U2`.

Prefer merging intro/outro lines into the adjacent numbered verse when they clearly belong to it. Use `U` only when the block must remain separate. Do **not** use `x` here (`x` = duplicate printed `N.` only). Do **not** use `^1-0U1` (collides conceptually with heading `^1-0`).

`apply.py` assigns `^{book}-U{k}` automatically to unnumbered content blocks **inside** a numbering run. Stray blocks before the first run are left for Step 4 (`^T-N`).

### Step D — check your work

After labeling, verify:

- If there is only one run in the file, content IDs are `^{book}-{N}` with **no** middle segment.
- If there are several runs, the principal run stays bare and every other run has its own sequential Arabic middle segment (`1`, `2`, …) in document order; no two share a label.
- Repeated printed `N` in one run → first `…-{N}`, then `…-{N}x1`, `…-{N}x2`, …
- Standalone unnumbered body blocks inside a run → `^{book}-U1`, `^{book}-U2`, … (not `^T-N`)
- No content ID exceeds 3 hyphen-separated segments; headings may be longer and end in `-0` (except `^0`, `^T-N`). The `xK` / `U{k}` markers sit on the last segment (`5x1`, `U1`), not as an extra hyphen part.
- Stripped `N.` prefixes; ID on the last line of each numbered block.

After assigning the ID, **strip** the `N.` prefix from the rendered line. Put the ID on the **last** line of the block (continuations / closers stay in the same block).

### Abhidhammapiṭaka `book` numbers

| `book` | Treatise |
|---|---|
| `1` | Dhammasaṅgaṇīpāḷi |
| `2` | Vibhaṅgapāḷi |
| `3` | Dhātukathāpāḷi |
| `4` | Puggalapaññattipāḷi |
| `5` | Kathāvatthupāḷi |
| `6` | Yamakapāḷi |
| `7` | Paṭṭhānapāḷi |

---

## Heading IDs — may exceed `n-n-n`

Every heading gets an ID. Trailing `-0` marks a heading (never content).

**Headings are a separate track from content zones.** A heading's ID records *where it sits in the document tree*; a content zone records *which numbering run a paragraph belongs to*. Do not try to make one mirror the other — that is what forced the old Roman/front-matter scheme, and it does not survive contact with real books.

Each heading segment is its **sequential position among its siblings** under the same parent (Roman inside an `M` subtree, Arabic elsewhere).

Note that some headings *do* carry printed numbers — book 2 has ~170 `#####` headings like `##### (25. Ka) arati` and `##### (1) Rūpadukaṃ`. **Use sibling position anyway, not those printed numbers**: they collide (two different `(1) …` headings under the same parent would produce the same ID) and they desync wherever lettered sub-headings intervene (`(24. Kha)`, `(24. Ga)` push `(25. Ka)` to sibling 27). Verbatim-number preservation is a rule for *content* IDs only.

| Heading | ID | Example (`book=1`) |
|---|---|---|
| Homage / pre-`#` prose | `^T-1`, `^T-2`… | `Namo tassa… ^T-1` |
| `#` collection | `^0` | `# Abhidhammapiṭake ^0` |
| `##` book | `^{book}-0` | `## Dhammasaṅgaṇīpāḷi ^1-0` |
| `###` (any) | `^{book}-{h3}-0` | `### Mātikā ^1-1-0`, `### Cittuppādakaṇḍaṃ ^1-2-0` |
| `####` | `^{book}-{h3}-{h4}-0` | `#### Tikamātikā ^1-1-1-0`, `#### Dukamātikā ^1-1-2-0` |
| `#####` | `^{book}-{h3}-{h4}-{h5}-0` | `##### Hetugocchakaṃ ^1-1-2-1-0` |

`###` counters run straight through **all** `###` siblings in document order — Mātikā is simply the 1st, Cittuppādakaṇḍaṃ the 2nd, and so on. There is no separate counter for "front" vs "body" sections, because that distinction no longer exists.

Heading depth may produce **4+** segments. Content stays ≤3 segments. The heading's trailing `-0` keeps e.g. `### Cittuppādakaṇḍaṃ ^1-2-0` distinct from paragraph `^1-2`.

Because the two tracks are independent, the same digits can appear in both with different meanings — e.g. Dukamātikā's **content** is `^1-2-{N}` (2nd non-principal run) while its **heading** is `^1-1-2-0` (2nd `####` under the 1st `###`). No literal collision is possible, since content IDs never end in `-0`.

---

## Workflow

Helper: `apply.py` next to this `SKILL.md`.

### 1 — Audit

```bash
python "<this-skill-dir>/apply.py" audit "<path-to-file.md>"
```

Prints (no writes): detected `book`, each numbering run (lines, `first→last`, heading candidates), anomalies (non-sequential jumps that are not a clean reset to `1`).

**Ignore existing `^` IDs** when judging structure — treat them as noise to be stripped on apply.

### 2 — Confirm runs and assign labels (follow Step C)

For each audited run:

1. Confirm the boundary is a real restart (not OCR / interpolation).
2. Decide which run is **principal** (normally the main body — the longest, most-cited run).
3. Choose `--zones` label from Step C:
   - Principal run → **empty** label (`3=` or `1=`) so content is `^{book}-{N}`
   - Every other run → `1`, `2`, … in document order

### 3 — Apply content IDs

```bash
# Example: three runs, the third (body) is principal → its label is empty
python "<this-skill-dir>/apply.py" apply "<path>" --zones "1=1@25,2=2@116,3=@588"

# Entire file is one run → empty label
python "<this-skill-dir>/apply.py" apply "<path>" --zones "1="
```

`--zones "K=LABEL"` maps audit run index `K` → middle segment `LABEL`. Empty `LABEL` (`K=` or `K=@line`) yields `^{book}-{N}`.

The script strips all existing `^` IDs, tags numbered paragraphs, strips `N.` prefixes, normalises blanks. It may put a temporary ID on the chosen run-opening heading; Step 4 replaces heading IDs fully.

### 4 — Headings + leftovers

1. Pre-title → `^T-N`
2. `#` → `^0`; `##` → `^{book}-0`
3. Every `###`/`####`/`#####` → hierarchical IDs by sibling position under each parent (one continuous `###` counter across the whole book)
4. Fix anomaly paragraphs the script skipped (e.g. `N.` not on the first line of a blank-line block)
5. Pre-title stray unnumbered blocks → `^T-N` (script does not assign `U` outside runs)

Confirm: no bare headings; every leading `N.` has a content ID; standalone unnumbered body blocks have `U{k}`; no content ID exceeds 3 hyphen segments.

---

## Dos and Don'ts

- **DO** derive structure from headings + leading `N.` only — strip and ignore legacy `^` IDs.
- **DO** copy `N` verbatim into the last segment of the content ID.
- **DO** when the same printed `N` appears again in the same run, keep the first as `…-{N}` and use `…-{N}x1`, `…-{N}x2`, … for later copies.
- **DO** give standalone unnumbered body segments `^{book}-U{k}` (`U` = Unnumbered); keep homage as `^T-N`.
- **DO** start a new run only when the printed number resets to `1` (or at the first number in the file).
- **DON'T** start a new run at every heading — gocchakas and kaṇḍas often sit inside one run.
- **DON'T** classify runs by genre or position — the zone is a collision-breaker only, never a claim that content is "matrix", "intro" or "front matter".
- **DO** give the principal (normally body) run the bare `^{book}-{N}` namespace; label every other run `1`, `2`, … in document order.
- **DO** collapse a **sole** run to `^{book}-{N}` — no middle segment at all.
- **DO** ID every heading; headings may be longer than 3 segments and are numbered by sibling position, independently of content zones.
- **DON'T** assign IDs to `![[...]]` transclusions.
- **DO** collapse multiple blank lines to one before parsing blocks.

---

## Open design notes — deep combinatorial books (e.g. Paṭṭhāna / book 7)

**Status: provisional, not implemented.** `pi-7.md` does not exist in this workspace yet. Everything below comes from reasoning about a pasted outline/excerpt, not a real audit — treat it as a starting proposal to revisit once the actual file is available, not as a rule to apply.

### The core problem this book exposes

Book 7 is what forced the Step B rewrite above (zone = collision-breaker, never a genre or position claim). Its `paccayuddesa` / `paccayaniddesa` / `Pucchāvāro` → `1. Kusalattikaṃ` boundary is the clearest case: the printed numbers never reset there. `Pucchāvāro` ends and `Kusalattikaṃ`'s own exposition begins at `53` with no reset back to `1`. Any scheme that tried to call the first stretch "front matter" and the second "body" would have to invent a boundary the numbering simply doesn't contain. Every tika *after* Kusalattikaṃ (`2. Vedanāttikaṃ` onward) does reset cleanly, confirming this is a one-off fusion at the very first tika, not a general pattern.

This means the zone boundary here cannot be found by reset-detection alone (which is all `apply.py` currently does) — it has to be a manual decision made at a heading, overriding what the numbers alone would suggest. This skill doesn't currently have a mechanism for "split one auto-detected run into two zones at a chosen heading with no number reset between them."

### Proposed middle-zone vocabulary for this book (unconfirmed against real content)

Book 7 is the one place where plain sequential zone labels may not be enough: it has hundreds of resets, and its own structure already supplies stable indices worth reusing rather than recounting. This is the sole anticipated exception to Step C's "sequential Arabic in document order" rule, and it should not be generalised to other books.

| Content | Proposed zone | Example |
|---|---|---|
| `paccayuddesa` + `paccayaniddesa` + `Pucchāvāro` (one continuous run) | sequential label per Step C | `^7-1-1` … `^7-1-24` … `^7-1-25`… |
| `1. Kusalattikaṃ` (numerically fused to the previous run, no reset) | `T1` — **manual override, not detectable from resets** | `^7-T1-53`, `^7-T1-54`… (N stays verbatim even though the zone changed) |
| Tikas 2–22, each a clean reset | `T{tika's own number}` | `^7-T2-1`… (Vedanāttikaṃ), `^7-T22-1`… |
| Individual dukas (flat 1–100 numbering, each a clean reset) | `D{duka's own number}` | `^7-D1-…` (Hetuduka), `^7-D7-…` (Sappaccayaduka) |
| Duka×tika cross-reference sections, duka-led heading order | `D{duka}T{tika}` (token order mirrors source's own heading order) | `7-1. Sappaccayaduka-kusalattikaṃ` → `^7-D7T1-…` |
| Duka×tika cross-reference, tika-led heading order (reversed) | `T{tika}D{duka}` | `1-99. Kusalattika-sauttaradukaṃ` → `^7-T1D99-…` |
| Deepest layer: 4 modes (Anuloma `A`, Paccanīya `P`, Anuloma-Paccanīya `AP`, Paccanīya-Anuloma `PA`) × 6 pairing types (`T`, `D`, `TT`, `DD`, `DT`, `TD`) | `{mode}{pairing}` stacked into one token | `Dhammapaccanīye dukatikapaṭṭhānaṃ` → zone `PDT` |

The `D{n}`/`T{n}` markers exist so tika-zone and duka-zone numbers don't collide (both count independently from `1`).

### Unresolved / needs the real file

- The 12 "gocchaka" group headings (`1. Hetugocchakaṃ` … `12. Kilesagocchakaṃ`) are organizational only — they are **not** content zones themselves. The actual duka zones use each duka's flat 1–100 position, and only 14 of those 100 are confirmed from examples seen so far (`D1, D2, D7, D14, D20, D26, D44, D50, D55, D69, D75, D83, D99, D100`); the rest need the real duka list. `Cūḷantaradukaṃ` and `Mahantaradukaṃ` look like standalone single dukas (not groups) but their flat duka-number isn't derivable from outline position alone.
- The 20 mode×pairing-type headers (`Dhammānulome tikatikapaṭṭhānaṃ` etc.) almost certainly contain their own internal reset structure underneath (quite possibly another full front-matter + resetting-tikas/dukas pattern, mirroring the book's outer shape) — a paragraph inside one of these would need a further nested zone dimension beyond a single token, which may exceed the 3-segment `book-zone-N` shape this skill otherwise holds to everywhere else. Not designable without real numbered content from inside one of these sections.
- No `apply.py` changes have been made to support any of this (no manual run-splitting, no compound zone tokens beyond what `parse_zones` already accepts as an arbitrary label string). If this scheme is adopted, `apply.py`'s zone-to-heading assignment logic would need to support splitting a single detected run at a chosen line, which it cannot currently do.
