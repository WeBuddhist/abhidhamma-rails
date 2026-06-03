#!/usr/bin/env python3
"""
translate_with_senses.py
========================
Merges three data sources to produce a sense-tagged Pāli→English glossary:

    pi-en-clustered.md      → how many senses each keyword has, and the
                              top English co-occurrence words per sense cluster
                              (from cluster_senses.py — used for SENSE DETECTION
                              only, NOT as translation source)
    pi-keywords-context.md  → Pāli-only example blocks per keyword
                              (from gather_examples.py)
    pi-en-zero-shot.md      → existing one-per-keyword renderings
                              (AI-authored, requirements-compliant)

Output
------
    pi-en-zero-shot.md  (updated in place)

Each entry gains a sense tag based on the cluster data:

    [mono]                     — 1 sense cluster, unambiguous
    [2 senses]                 — 2 clusters; dominant rendering kept, review
                                 secondary sense in termbase.md
    [N senses — termbase.md]  — 3 or more clusters; dominant rendering kept,
                                 all senses need review in termbase.md
    [unclustered]              — keyword not found in cluster data

Rendering is NEVER changed by this script — only the sense tag is added
or updated. Locked terms (Nibbāna, Buddha, Dhamma, Saṅgha, kamma, jhāna)
are flagged [locked] instead of a sense tag.

Usage
-----
    python3 translate_with_senses.py \\
        --clusters   pi-en-clustered.md \\
        --context    pi-keywords-context.md \\
        --zeroshot   pi-en-zero-shot.md \\
        --out        pi-en-zero-shot.md

Options
-------
    --clusters   Path to pi-en-clustered.md   (default: pi-en-clustered.md)
    --context    Path to pi-keywords-context.md (default: pi-keywords-context.md)
    --zeroshot   Path to existing glossary      (default: pi-en-zero-shot.md)
    --out        Output path                    (default: pi-en-zero-shot.md)
    --dry-run    Print the first 20 entries and exit without writing
"""

import argparse
import re
import sys
from collections import OrderedDict
from pathlib import Path


# ---------------------------------------------------------------------------
# Terms kept as Pāli (untranslated) per requirements.md §1.3.
# Only these get [kept-in-pāli] instead of a cluster-sense tag.
# dhamma, kamma, jhāna are *translated* (phenomenon / kamma / jhāna in context)
# so they still receive cluster-sense tags.
# ---------------------------------------------------------------------------

LOCKED_PALI = {"nibbāna", "nibbana", "buddha", "saṅgha", "sangha"}


# ---------------------------------------------------------------------------
# Parse pi-en-clustered.md  →  {lemma: {"n_senses": int, "clusters": [[str]]}}
# ---------------------------------------------------------------------------

_COMPACT_RE = re.compile(
    r"^-\s+\*\*(.+?)\*\*:\s+(.+)$"
)
_SENSE_GROUP_RE = re.compile(r"\((\d+)\)\s+([^;]+)")


def parse_cluster_file(path: Path) -> dict:
    """Return {lemma: {"n_senses": int, "clusters": [[top_words]]}}."""
    result = {}
    in_compact = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Compact form"):
            in_compact = True
            continue
        if in_compact and line.startswith("## "):
            break  # End of compact section
        if not in_compact:
            continue
        m = _COMPACT_RE.match(line)
        if not m:
            continue
        lemma = m.group(1).strip().lower()
        body = m.group(2).strip()

        if body.startswith("—"):
            # No candidates found
            result[lemma] = {"n_senses": 0, "clusters": []}
            continue

        clusters = []
        for sm in _SENSE_GROUP_RE.finditer(body):
            words = [w.strip() for w in sm.group(2).split(",") if w.strip()]
            clusters.append(words)

        result[lemma] = {
            "n_senses": len(clusters),
            "clusters": clusters,
        }
    return result


# ---------------------------------------------------------------------------
# Parse pi-keywords-context.md  →  {lemma: [example_str, ...]}
# ---------------------------------------------------------------------------

_CONTEXT_HEADING_RE = re.compile(r"^##\s+\d+\.\s+(.+)$")
_CONTEXT_EXAMPLE_RE = re.compile(r"^\*\*pi#\d+:\*\*\s+(.+)$")


def parse_context_file(path: Path) -> dict:
    """Return {lemma: [pali_example_str, ...]}."""
    result = OrderedDict()
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        hm = _CONTEXT_HEADING_RE.match(line)
        if hm:
            current = hm.group(1).strip().lower()
            result.setdefault(current, [])
            continue
        if current is None:
            continue
        em = _CONTEXT_EXAMPLE_RE.match(line)
        if em:
            result[current].append(em.group(1).strip())
    return result


# ---------------------------------------------------------------------------
# Parse pi-en-zero-shot.md
#
# We split the file into:
#   header  — everything before "## Compact form"
#   entries — list of (rank, lemma, rendering, old_tag, raw_line)
#   footer  — everything after the last numbered entry
# ---------------------------------------------------------------------------

_ENTRY_RE = re.compile(
    r"^(\d+)\.\s+\*\*(.+?)\*\*:\s+(.+?)(\s+\[.*?\])?\s*$"
)


def parse_zeroshot(path: Path):
    """Return (header_lines, entries, footer_lines).

    entries = list of {rank, lemma, rendering, tag, original_line}
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    header, entries, footer = [], [], []
    state = "header"
    for line in lines:
        if state == "header":
            header.append(line)
            if line.strip() == "<!-- compact -->":
                state = "compact"
            continue

        m = _ENTRY_RE.match(line)
        if m:
            state = "entries"
            entries.append({
                "rank":      int(m.group(1)),
                "lemma":     m.group(2).strip().lower(),
                "rendering": m.group(3).strip(),
                "tag":       m.group(4).strip() if m.group(4) else "",
                "original":  line,
            })
        elif state == "entries":
            # Non-entry line after we started seeing entries → header/footer
            if entries:
                # Could be a section heading or blank line inside the list
                # Attach to footer only after the last real entry
                footer.append(line)
            else:
                header.append(line)
        else:
            header.append(line)

    # Trim trailing blanks from footer and leading blanks accumulated there
    return header, entries, footer


# ---------------------------------------------------------------------------
# Sense tag builder
# ---------------------------------------------------------------------------

def build_sense_tag(lemma: str, cluster_info: dict) -> str:
    """Return the sense tag string for one lemma."""
    # Locked Pāli terms get a special tag
    if lemma in LOCKED_PALI:
        return "[kept-in-pāli]"

    if lemma not in cluster_info:
        return "[unclustered]"

    n = cluster_info[lemma]["n_senses"]
    clusters = cluster_info[lemma]["clusters"]

    if n == 0:
        return "[unclustered]"
    if n == 1:
        return "[mono]"
    if n == 2:
        top1 = clusters[0][0] if clusters[0] else "?"
        top2 = clusters[1][0] if clusters[1] else "?"
        return f"[2 senses: {top1} / {top2}]"
    # 3+
    return f"[{n} senses]"


# ---------------------------------------------------------------------------
# Rebuild the output file
# ---------------------------------------------------------------------------

def rebuild(header, entries, footer, cluster_info, dry_run=False):
    """Return list of output lines."""
    out = list(header)

    for e in entries:
        tag = build_sense_tag(e["lemma"], cluster_info)
        line = f"{e['rank']}. **{e['lemma']}**: {e['rendering']}  {tag}"
        out.append(line)

    out.extend(footer)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Add sense tags to pi-en-zero-shot.md from cluster data."
    )
    ap.add_argument("--clusters",  default="pi-en-clustered.md")
    ap.add_argument("--context",   default="pi-keywords-context.md")
    ap.add_argument("--zeroshot",  default="pi-en-zero-shot.md")
    ap.add_argument("--out",       default="pi-en-zero-shot.md")
    ap.add_argument("--dry-run",   action="store_true",
                    help="Print first 20 entries and exit without writing.")
    args = ap.parse_args()

    cluster_info = parse_cluster_file(Path(args.clusters))
    print(f"Loaded cluster data for {len(cluster_info)} lemmas.", file=sys.stderr)

    context_info = parse_context_file(Path(args.context))
    print(f"Loaded context data for {len(context_info)} lemmas.", file=sys.stderr)

    header, entries, footer = parse_zeroshot(Path(args.zeroshot))
    print(f"Loaded {len(entries)} entries from zero-shot file.", file=sys.stderr)

    # Stats
    n_mono = n_poly2 = n_poly3plus = n_unclustered = n_locked = 0
    for e in entries:
        lemma = e["lemma"]
        if lemma in LOCKED_PALI:
            n_locked += 1
            continue
        elif lemma not in cluster_info or cluster_info[lemma]["n_senses"] == 0:
            n_unclustered += 1
        elif cluster_info[lemma]["n_senses"] == 1:
            n_mono += 1
        elif cluster_info[lemma]["n_senses"] == 2:
            n_poly2 += 1
        else:
            n_poly3plus += 1

    print(
        f"Sense breakdown:\n"
        f"  locked Pāli terms : {n_locked}\n"
        f"  monosemous        : {n_mono}\n"
        f"  2-sense poly      : {n_poly2}\n"
        f"  3+ sense poly     : {n_poly3plus}\n"
        f"  unclustered       : {n_unclustered}",
        file=sys.stderr,
    )

    output_lines = rebuild(header, entries, footer, cluster_info)

    if args.dry_run:
        # Print first 20 entry lines
        count = 0
        for line in output_lines:
            if re.match(r"^\d+\. \*\*", line):
                print(line)
                count += 1
                if count >= 20:
                    break
        return

    out_path = Path(args.out)
    out_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}  ({len(entries)} entries)", file=sys.stderr)


if __name__ == "__main__":
    main()
