#!/usr/bin/env python3
"""
cluster_senses.py
=================
Phase 3: cluster each Pāli keyword by which OTHER Pāli lemmas co-occur
with it in the same blocks. No English translation is consulted.

Pipeline
--------
    extract_pali_keywords.py  →  pi-keywords.txt / pi-keywords.md
    gather_examples.py        →  pi-keywords-context.md
    cluster_senses.py         →  pi-clustered.md      (this — Phase 3)

Algorithm
---------
For each target Pāli lemma L with block-set B_L:
  1. Score every OTHER Pāli lemma M by Dice coefficient:
         dice(L, M) = 2 * |B_L ∩ B_M| / (|B_L| + |B_M|)
  2. Pre-filter: M must appear in ≥ min-pi-blocks blocks and
     ≤ max-pi-df fraction of all blocks (removes particles/stopwords).
  3. Keep the top-N co-lemmas by Dice score.
  4. For each co-lemma M, compute its sub-block-set:
         S_M = B_L ∩ B_M   (blocks where BOTH L and M appear)
  5. Run average-linkage agglomerative clustering over those sub-sets
     using Jaccard distance with a tunable threshold.
  6. Each resulting cluster = one usage context (likely one sense).
     - Multiple co-lemmas per cluster  ⇒ related usage context.
     - Multiple clusters per lemma     ⇒ likely polysemy.
  7. Senses ordered by max Dice within them (most prominent first).

Why Pāli-only co-occurrence works
----------------------------------
The Abhidhamma uses tightly formulaic language. When the same Pāli words
appear together repeatedly, they form a fixed analytical cluster (e.g.
*phassa*, *vedanā*, *saññā* always appear in the mind-state enumeration).
When a keyword appears in a DIFFERENT set of blocks — alongside different
co-lemmas — that signals a different sense or usage context.

This is more reliable than using a translation as a proxy, because:
  - No translation bias is introduced.
  - Works even for keywords the translators rendered inconsistently.
  - Uses the structure the Abhidhamma itself encodes.

Usage
-----
    python3 cluster_senses.py \\
        --pali      1-SOURCES/Text/pi-1.md \\
        --keywords  pi-keywords.txt \\
        --top       10 \\
        --threshold 0.5 \\
        --out       pi-clustered

Tuning
------
- Lower --threshold (e.g. 0.3) → more, smaller clusters (more senses).
- Higher --threshold (e.g. 0.7) → fewer, larger clusters.
- Raise --top to feed more co-lemmas into clustering (default 10).
- Raise --min-dice to drop weak co-lemmas before clustering.
- Lower --max-pi-df to filter out more high-frequency particles.
"""

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from map_keywords_to_pali import parse_blocks, tokenize_pali, parse_keywords
from flip_to_pali_glossary import normalize_pali


# ---------------------------------------------------------------------------
# Set distance / similarity
# ---------------------------------------------------------------------------

def jaccard_distance(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    union = len(a | b)
    if union == 0:
        return 1.0
    return 1.0 - len(a & b) / union


def jaccard_similarity(a: set, b: set) -> float:
    return 1.0 - jaccard_distance(a, b)


# ---------------------------------------------------------------------------
# Average-linkage agglomerative clustering (stdlib only)
# ---------------------------------------------------------------------------

def average_linkage_cluster(sets, threshold):
    """Cluster block-sets by Jaccard distance, average linkage.

    Returns a list of clusters; each cluster is a list of original indices.
    Stops merging when the closest pair exceeds the threshold.
    """
    n = len(sets)
    if n <= 1:
        return [list(range(n))]
    clusters = [[i] for i in range(n)]
    while len(clusters) > 1:
        best_i = best_j = -1
        best_d = float("inf")
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                ci, cj = clusters[i], clusters[j]
                pair_count = len(ci) * len(cj)
                d = sum(
                    jaccard_distance(sets[a], sets[b])
                    for a in ci for b in cj
                ) / pair_count
                if d < best_d:
                    best_d = d
                    best_i, best_j = i, j
        if best_d > threshold:
            break
        merged = clusters[best_i] + clusters[best_j]
        clusters = [
            c for k, c in enumerate(clusters)
            if k != best_i and k != best_j
        ]
        clusters.append(merged)
    return clusters


def cluster_cohesion(cluster_indices, sets):
    """Average pairwise Jaccard similarity within a cluster."""
    if len(cluster_indices) <= 1:
        return 1.0
    total = 0.0
    n = 0
    for i in range(len(cluster_indices)):
        for j in range(i + 1, len(cluster_indices)):
            total += jaccard_similarity(
                sets[cluster_indices[i]], sets[cluster_indices[j]]
            )
            n += 1
    return total / n if n else 1.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Cluster Pāli keywords by co-lemma context (Pāli-only, no English)."
    )
    ap.add_argument("--pali",      required=True, help="Pāli root markdown (pi-1.md)")
    ap.add_argument("--keywords",  required=True, help="Pāli keyword list (.txt or .md)")
    ap.add_argument("--top",       type=int,   default=10,
                    help="Keep top N co-lemmas per keyword before clustering (default 10)")
    ap.add_argument("--threshold", type=float, default=0.5,
                    help="Jaccard distance threshold; lower = more senses (default 0.5)")
    ap.add_argument("--min-pi-blocks", type=int,   default=2,
                    help="Co-lemma must appear in ≥ N blocks (default 2)")
    ap.add_argument("--max-pi-df",     type=float, default=0.30,
                    help="Co-lemma must appear in ≤ this fraction of blocks (default 0.30)")
    ap.add_argument("--min-dice",      type=float, default=0.10,
                    help="Minimum Dice score to include a co-lemma (default 0.10)")
    ap.add_argument("--out", default="pi-clustered")
    args = ap.parse_args()

    pi_text   = Path(args.pali).read_text(encoding="utf-8")
    pi_blocks = parse_blocks(pi_text)
    all_bids  = sorted(pi_blocks.keys())
    n_blocks  = len(all_bids)
    print(f"Pāli blocks: {n_blocks}", file=sys.stderr)

    # Index: lemma → set of block IDs it appears in
    lemma_blocks   = defaultdict(set)
    forms_per_lemma = defaultdict(set)

    for bid in all_bids:
        for tok in set(tokenize_pali(pi_blocks[bid])):
            lemma = normalize_pali(tok)
            lemma_blocks[lemma].add(bid)
            forms_per_lemma[lemma].add(tok)

    pi_df_cap = args.max_pi_df * n_blocks

    keywords = parse_keywords(Path(args.keywords))
    print(f"Clustering {len(keywords)} keywords...", file=sys.stderr)

    rows = []
    matched = 0
    n_senses_total = 0

    for lemma in keywords:
        lemma_lc = lemma.lower()
        pi_set = lemma_blocks.get(lemma_lc, set())
        if not pi_set:
            rows.append((lemma_lc, set(), []))
            continue

        # Score every other Pāli lemma by Dice co-occurrence with this lemma.
        scored = []  # (co_lemma, dice, co_lemma_df, sub_block_set)
        for collemma, col_set in lemma_blocks.items():
            if collemma == lemma_lc:
                continue
            if len(col_set) < args.min_pi_blocks or len(col_set) > pi_df_cap:
                continue
            co = len(pi_set & col_set)
            if co == 0:
                continue
            dice = 2 * co / (len(pi_set) + len(col_set))
            if dice < args.min_dice:
                continue
            scored.append((collemma, dice, len(col_set), pi_set & col_set))

        if not scored:
            rows.append((lemma_lc, pi_set, []))
            continue

        scored.sort(key=lambda x: -x[1])
        scored = scored[: args.top]
        matched += 1

        # Cluster on the sub-block-sets.
        sub_sets = [s for *_, s in scored]
        clusters = average_linkage_cluster(sub_sets, args.threshold)

        senses = []
        for cluster in clusters:
            members = sorted([scored[k] for k in cluster], key=lambda x: -x[1])
            senses.append({
                "members":  [(col, dice, df, len(s))
                             for (col, dice, df, s) in members],
                "cohesion": cluster_cohesion(cluster, sub_sets),
                "max_dice": max(m[1] for m in members),
            })
        senses.sort(key=lambda s: -s["max_dice"])
        n_senses_total += len(senses)
        rows.append((lemma_lc, pi_set, senses))

    # -------------------------------------------------------------------
    # Write output
    # -------------------------------------------------------------------
    out_path = Path(f"{args.out}.md")
    with out_path.open("w", encoding="utf-8") as f:
        f.write("# Pāli keyword sense clusters (Pāli-only co-occurrence)\n\n")
        f.write(f"- Pāli source  : `{args.pali}`\n")
        f.write(f"- English used : **none** (Pāli-only pipeline)\n")
        f.write(f"- Keyword list : `{args.keywords}`\n")
        f.write(f"- Pāli blocks  : {n_blocks}\n")
        f.write(f"- Cluster threshold: Jaccard distance ≤ {args.threshold}\n")
        f.write(
            f"- Pre-cluster filters: pi blocks ≥ {args.min_pi_blocks}, "
            f"pi DF ≤ {args.max_pi_df:.2f}, Dice ≥ {args.min_dice}, "
            f"top {args.top} co-lemmas\n"
        )
        f.write(f"- Mapped {matched}/{len(rows)} lemmas → {n_senses_total} sense clusters\n\n")
        f.write(
            "> Each sense cluster is a group of Pāli co-lemmas that tend to "
            "appear in the same blocks as the target keyword. Multiple co-lemmas "
            "in one cluster ⇒ related usage context. Multiple clusters ⇒ likely "
            "polysemy or distinct grammatical roles. Cohesion = average pairwise "
            "Jaccard similarity of co-lemma block-sets within the cluster.\n\n"
        )
        f.write("---\n\n")

        # Compact form
        f.write("## Compact form\n\n")
        for lemma, pi_set, senses in rows:
            if not senses:
                note = "no blocks found" if not pi_set else "no co-lemmas above threshold"
                f.write(f"- **{lemma}**: —  _({note})_\n")
                continue
            parts = []
            for i, sense in enumerate(senses, 1):
                names = ", ".join(col for col, *_ in sense["members"])
                parts.append(f"({i}) {names}")
            f.write(f"- **{lemma}**: {'; '.join(parts)}\n")

        # Detailed entries
        f.write("\n---\n\n## Detailed entries\n\n")
        for lemma, pi_set, senses in rows:
            f.write(f"### {lemma}\n\n")
            forms = ", ".join(sorted(forms_per_lemma.get(lemma, ())))
            f.write(
                f"_pi blocks: {len(pi_set)}; sense clusters: {len(senses)}; "
                f"inflected forms: {forms or '—'}_\n\n"
            )
            if not senses:
                f.write("_No Pāli co-lemmas above thresholds._\n\n")
                continue
            for i, sense in enumerate(senses, 1):
                top_name = sense["members"][0][0]
                size = len(sense["members"])
                f.write(
                    f"#### cluster ({i}) — top co-lemma: **{top_name}** "
                    f"(cohesion {sense['cohesion']:.2f}, "
                    f"{size} co-lemma{'s' if size != 1 else ''})\n\n"
                )
                f.write("| pāli co-lemma | dice | pi blocks | sub-blocks |\n")
                f.write("| --- | ---: | ---: | ---: |\n")
                for col, dice, df, sb in sense["members"]:
                    f.write(f"| {col} | {dice:.2f} | {df} | {sb} |\n")
                f.write("\n")

    print(f"Wrote: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
