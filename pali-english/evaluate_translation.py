#!/usr/bin/env python3
"""
Evaluation script for pali-english translations.

Anchors on the verse-id markers (e.g. ^1-0a-5) that are carried through from
source to translation, so it is robust to differences in numbering scheme,
heading wording, and (Ka)/(Kha)/(Ga) vs (A)/(B)/(C) labelling between source
and output.

Checks:

1. COMPLETENESS - every "leaf" verse-id in the (auto- or explicitly-scoped)
   source section has a corresponding item in the output, and vice versa.

2. SUB-CLAUSE COUNT - for each shared verse-id, the number of (Ka)/(Kha)/(Ga)/
   (Gha)-style clauses in the source matches the number of (A)/(B)/(C)/(D)-
   style clauses in the output.

3. TERMBASE COVERAGE - for each Pali surface form in a source item that is
   listed in the active audience's termbase, report whether the expected
   Translation (for that Sense Tag) appears (loosely) in the corresponding
   output item. Heuristic flag for human/LLM follow-up.

4. SENSE-TAG CONSISTENCY - across the output, for any termbase Sense Tag
   whose expected Translation phrase is detectable in some occurrences but
   not others, flag the inconsistency.

Usage (any audience / any output file):
    python3 evaluate_translation.py \
        --source ../1-SOURCES/Text/pi-1.md \
        --output en-dhammasangani-ai-auto-<audience>-<n>.md

Optional overrides:
  --termbase      defaults to <output-dir>/audience_requirments/termbase/
                   termbase-pi-1-audience_<audience>.md, where <audience> is
                   parsed from the --output filename.
  --start-marker / --end-marker
                   explicit source headings to scope the check to. If
                   omitted, the source is auto-scoped to the span between the
                   first and last leaf verse-ids that appear in the output
                   (so partial / in-progress translations are checked against
                   just the corresponding source slice). If the output has no
                   verse-ids at all, the whole source file is used.
"""

import argparse
import os
import re
import unicodedata

# Verse-ids look like ^1-0a-5, ^1-1-1-2-3, ^abhidhamma-0, etc. Section/heading
# ids conventionally end in "-0" (e.g. ^1-1-1-0 = a heading); leaf
# (translatable) items end in a non-zero number. Match any verse-id whose
# final segment is a non-zero integer.
LEAF_ID_RE = re.compile(r"\^([\w]+(?:-[\w]+)*-(?!0\b)\d+)\b")
SUBCLAUSE_RE = re.compile(r"\(([A-Za-z]{1,4})\)")
# Any run of unicode letters (covers Pali diacritics, e.g. a, A-with-macron,
# etc.) without needing to spell out the diacritic ranges in source code.
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def strip_diacritics(s):
    nfkd = unicodedata.normalize("NFD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def slice_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1:
        raise ValueError("start marker %r not found" % (start_marker,))
    end = text.find(end_marker, start) if end_marker else len(text)
    if end_marker and end == -1:
        raise ValueError("end marker %r not found" % (end_marker,))
    return text[start:end]


def group_by_leaf_verse_id(text):
    """Return {verse_id: full_text_of_item} for each leaf verse-id block.

    A block is the run of lines from just after the previous leaf verse-id
    (or start of text) up to and including the line containing the current
    leaf verse-id.
    """
    blocks = {}
    buf = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        buf.append(line)
        m = LEAF_ID_RE.search(line)
        if m:
            vid = m.group(1)
            blocks[vid] = " ".join(buf)
            buf = []
    return blocks


def parse_termbase(text):
    rows = []
    current_lemma = None
    current_surface = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 6:
            continue
        surface, lemma, domain, sense, translation, tag = cells
        if surface == "Common Surface Forms":
            continue
        if surface:
            current_surface = [s.strip() for s in surface.split(",") if s.strip()]
        if lemma:
            current_lemma = lemma
        rows.append({
            "surface_forms": current_surface or [],
            "lemma": current_lemma,
            "domain": domain,
            "sense": sense,
            "translation": translation,
            "sense_tag": tag,
        })
    return rows


def build_surface_index(rows):
    idx = {}
    for r in rows:
        for sf in r["surface_forms"]:
            idx.setdefault(strip_diacritics(sf), []).append(r)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True,
                    help="Source Pali file, e.g. ../1-SOURCES/Text/pi-1.md")
    ap.add_argument("--output", required=True,
                    help="Translated output file, e.g. "
                         "en-dhammasangani-ai-auto-<audience>-<n>.md")
    ap.add_argument("--termbase", default=None,
                    help="Per-audience termbase. If omitted, derived from "
                         "the --output filename's <audience> slug, looked "
                         "up next to the --output file as "
                         "audience_requirments/termbase/"
                         "termbase-pi-1-audience_<audience>.md")
    ap.add_argument("--start-marker", default=None,
                    help="Heading marking the start of the section to check "
                         "in the source. If omitted, auto-scoped from the "
                         "output's verse-ids (or whole file if none).")
    ap.add_argument("--end-marker", default=None,
                    help="Heading marking the end of the section (exclusive). "
                         "Only used together with --start-marker.")
    args = ap.parse_args()

    source_text = open(args.source, encoding="utf-8").read()
    output_text = open(args.output, encoding="utf-8").read()

    termbase_path = args.termbase
    if termbase_path is None:
        m = re.search(r"ai-auto-([a-z0-9_]+)-\d+\.md$", args.output)
        if not m:
            raise ValueError(
                "--termbase not given and audience slug could not be "
                "derived from --output filename "
                "(expected en-dhammasangani-ai-auto-<audience>-<n>.md)")
        audience = m.group(1)
        termbase_path = os.path.join(
            os.path.dirname(args.output),
            "audience_requirments", "termbase",
            "termbase-pi-1-audience_%s.md" % audience)
        print("(derived termbase: %s)" % termbase_path)
    termbase_text = open(termbase_path, encoding="utf-8").read()

    out_blocks = group_by_leaf_verse_id(output_text)

    if args.start_marker:
        # Explicit scoping: use the given heading markers.
        src_section = slice_section(source_text, args.start_marker, args.end_marker)
    elif out_blocks:
        # Auto-scoping: find the first and last leaf verse-ids that appear
        # (in document order) in the output, locate those same verse-ids in
        # the source, and check only that slice of the source. This makes
        # completeness/coverage checks meaningful for partial translations
        # without requiring the caller to know section headings.
        out_order = []
        for raw_line in output_text.splitlines():
            for vm in LEAF_ID_RE.finditer(raw_line):
                out_order.append(vm.group(1))
        first_id, last_id = out_order[0], out_order[-1]

        first_re = re.compile(r"\^" + re.escape(first_id) + r"\b")
        last_re = re.compile(r"\^" + re.escape(last_id) + r"\b")

        fm = first_re.search(source_text)
        start = source_text.rfind("\n", 0, fm.start()) + 1 if fm else 0

        lm = None
        for lm in last_re.finditer(source_text):
            pass
        if lm:
            nl = source_text.find("\n", lm.end())
            end = nl if nl != -1 else len(source_text)
        else:
            end = len(source_text)

        src_section = source_text[start:end]
        print("(auto-scoped source to verse-ids %s..%s)" % (first_id, last_id))
    else:
        src_section = source_text

    src_blocks = group_by_leaf_verse_id(src_section)

    tb_rows = parse_termbase(termbase_text)
    tb_index = build_surface_index(tb_rows)
    tag_to_translation = {}
    for r in tb_rows:
        if r["sense_tag"]:
            tag_to_translation.setdefault(r["sense_tag"], r["translation"].strip().lower())

    src_ids = set(src_blocks)
    out_ids = set(out_blocks)

    print("Source leaf items : %d" % len(src_ids))
    print("Output leaf items : %d" % len(out_ids))
    print()

    # ---- 1. Completeness ----
    print("=== 1. COMPLETENESS ===")
    missing = sorted(src_ids - out_ids)
    extra = sorted(out_ids - src_ids)
    if missing:
        print("MISSING from output (%d): %s" % (len(missing), missing))
    if extra:
        print("EXTRA in output, not in source section (%d): %s" % (len(extra), extra))
    if not missing and not extra:
        print("OK - all %d verse-id items present in both." % len(src_ids))
    print()

    # ---- 2. Sub-clause counts ----
    print("=== 2. SUB-CLAUSE COUNTS ===")
    mismatches = 0
    for vid in sorted(src_ids & out_ids, key=lambda v: [int(x) for x in re.findall(r"\d+", v)]):
        src_clauses = len(SUBCLAUSE_RE.findall(src_blocks[vid]))
        out_clauses = len(SUBCLAUSE_RE.findall(out_blocks[vid]))
        if src_clauses and src_clauses != out_clauses:
            mismatches += 1
            print("  %s: source has %d clauses, output has %d" % (vid, src_clauses, out_clauses))
    if mismatches == 0:
        print("OK - sub-clause counts match for all shared items.")
    print()

    # ---- 3. Termbase coverage ----
    print("=== 3. TERMBASE COVERAGE (heuristic flags) ===")
    flagged = 0
    checked = 0
    for vid in sorted(src_ids & out_ids, key=lambda v: [int(x) for x in re.findall(r"\d+", v)]):
        src_text = src_blocks[vid]
        out_text = out_blocks[vid].lower()
        words = WORD_RE.findall(src_text)
        seen_tags = set()
        for w in words:
            if len(w) < 4:
                continue  # skip short particles/letter-labels (Ka, Kha, Ca...)
            key = strip_diacritics(w)
            entries = tb_index.get(key, [])
            if len(entries) != 1:
                continue  # skip ambiguous/polysemous lemmas (needs context)
            for r in entries:
                tag = r["sense_tag"]
                if not tag or tag in seen_tags:
                    continue
                seen_tags.add(tag)
                expected = r["translation"].strip().lower()
                expected_words = [x for x in re.findall(r"[a-z]+", expected) if len(x) > 3]
                checked += 1
                hit = expected and (expected in out_text or
                                     (expected_words and all(ew in out_text for ew in expected_words)))
                if not hit:
                    flagged += 1
                    print("  %s: lemma '%s' (sense_tag '%s') expects '%s' - not clearly found in output" %
                          (vid, r['lemma'], tag, r['translation']))
    print("(%d lemma/sense checks, %d flagged)" % (checked, flagged))
    print()

    # ---- 4. Sense-tag consistency ----
    print("=== 4. SENSE-TAG CONSISTENCY ACROSS OUTPUT ===")
    occurrences = {}
    for vid in src_ids & out_ids:
        src_text = src_blocks[vid]
        out_text = out_blocks[vid].lower()
        words = WORD_RE.findall(src_text)
        for w in words:
            if len(w) < 4:
                continue
            key = strip_diacritics(w)
            entries = tb_index.get(key, [])
            if len(entries) != 1:
                continue
            for r in entries:
                tag = r["sense_tag"]
                if tag:
                    occurrences.setdefault(tag, []).append((vid, out_text))

    inconsistent = 0
    for tag, occs in occurrences.items():
        if len(occs) < 2:
            continue
        expected = tag_to_translation.get(tag, "")
        expected_words = [x for x in re.findall(r"[a-z]+", expected) if len(x) > 3]
        if not expected_words:
            continue
        hits = [vid for vid, out in occs if all(ew in out for ew in expected_words)]
        misses = [vid for vid, _ in occs if vid not in hits]
        if hits and misses:
            inconsistent += 1
            print("  sense_tag '%s' (~'%s'): rendered consistently in %s%s, but not in %s%s" %
                  (tag, expected, hits[:5], '...' if len(hits) > 5 else '',
                   misses[:5], '...' if len(misses) > 5 else ''))
    if inconsistent == 0:
        print("OK - no cross-item inconsistencies detected for repeated sense tags.")


if __name__ == "__main__":
    main()
