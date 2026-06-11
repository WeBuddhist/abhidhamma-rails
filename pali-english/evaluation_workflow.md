# Translation Evaluation Workflow

Two-stage evaluation for any `en-dhammasangani-ai-auto-<audience>-<n>.md`
output file — works for a finished section, a whole audience file, or a
still-in-progress draft.

---

## Stage 1 — Script (deterministic, run first)

`pali-english/evaluate_translation.py`

```bash
python3 evaluate_translation.py \
  --source "../1-SOURCES/Text/pi-1.md" \
  --output "en-dhammasangani-ai-auto-<audience>-<n>.md"
```

That's it for the common case — no other flags needed:

- **Termbase** is auto-derived from the `<audience>` slug in the `--output`
  filename (`audience_requirments/termbase/termbase-pi-1-audience_<audience>.md`).
  Pass `--termbase <path>` to override.
- **Source scope** is auto-detected: the script finds the first and last
  leaf verse-ids that appear (in order) in the output file, and checks only
  that slice of the source. This works for partial/in-progress translations
  without needing to know section headings. Pass `--start-marker "<heading>"`
  (and optionally `--end-marker "<heading>"`) to scope explicitly instead —
  e.g. when the output's verse-ids aren't contiguous in the source, or when
  you want to check a specific section regardless of what's in the output.

Anchors on the `^<id>` verse-id markers carried from source to output, so
it's robust to different numbering/heading schemes and to (Ka)/(Kha)/(Ga)
vs (A)/(B)/(C) labelling.

Checks:

1. **Completeness** — every source verse-id item in the scoped section has a
   matching output item and vice versa. Hard pass/fail.
2. **Sub-clause counts** — number of (Ka)/(Kha)/(Ga)/... clauses in source
   matches (A)/(B)/(C)/... clauses in output, per item. Hard pass/fail
   (note: items that aren't actually multi-part triplets/dyads, e.g. the
   opening homage verse, will show a benign mismatch here — use judgment).
3. **Termbase coverage** — for unambiguous, non-particle Pali terms (≥4
   chars, single sense in the termbase), checks whether the termbase
   Translation (or its key words) appears in the corresponding output item.
   **Heuristic** — flags are candidates for Stage 2 review, not failures
   (audience profiles permit paraphrase).
4. **Sense-tag consistency** — flags any termbase Sense Tag rendered with
   the termbase wording in some occurrences but not others (possible
   inconsistent terminology).

## Stage 2 — LLM review (judgment, on flagged items + samples)

For each item flagged in Stage 1 §3/§4, and for a random sample of
unflagged items:

1. Read the source line(s) and the output item side by side.
2. Confirm the rendering preserves the **doctrinal meaning** of the
   flagged lemma (not necessarily the exact termbase wording — paraphrase
   is fine if meaning is intact and audience-appropriate).
3. Confirm the **same Pali lemma/sense** is rendered with the **same
   English wording** everywhere it recurs in the output (even if that
   wording differs from the termbase's literal Translation column) —
   this is the actual consistency requirement, the script's §4 is just an
   approximation of it.
4. Check the rendering matches the **audience profile's** Style/Priority
   (e.g. grade3: short, concrete, no jargon; scholarly: precise, retains
   key Pali terms with gloss).
5. For a small sample, compare against a reference translation (PTS /
   Bodhi) to catch doctrinal drift.

Record any genuine issues found, and if a wording should become the fixed
standard for a Sense Tag, update the per-audience termbase accordingly.

---

## Example run — grade3, Mātikā (`en-dhammasangani-ai-auto-grade3-1.md`)

```bash
python3 evaluate_translation.py \
  --source "../1-SOURCES/Text/pi-1.md" \
  --output "en-dhammasangani-ai-auto-grade3-1.md"
```

Result: source/output auto-scoped to verse-ids `1-0a-1..1-0b-142` (164/164
items, complete). Sub-clause counts OK except item `1-0a-1` (the opening
homage verse — 1 source clause vs 3 output clauses; benign, not a real
triplet). Termbase coverage: 57 checks, 56 flagged. Sense-tag consistency:
OK, no internal inconsistencies.

Spot-check of flags (Stage 2): all sampled flags (e.g. upādāna →
"things we grab", kilesa → "things that are bad habits", nīvaraṇa →
"things that block the mind", saṃyojana → "things that tie the mind down")
are valid grade3 simplifications that preserve meaning and are used
consistently — not errors. The high flag count reflects that the grade3
termbase's own Translation column is sometimes still too wordy
(e.g. "something that ties the mind down", "a deep bad habit of the mind")
for the actual prose style achieved in the output, rather than mistakes in
the output itself.

**Optional follow-up:** simplify the grade3 termbase Translation column for
these Sense Tags (āsava, saṃyojana, nīvaraṇa, upādāna, kilesa, padhāna,
vimutti, etc.) to match the shorter phrasing already used in the output, so
future Stage 1 runs produce fewer noise flags.
