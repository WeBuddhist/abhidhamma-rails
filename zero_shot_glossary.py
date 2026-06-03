#!/usr/bin/env python3
"""
zero_shot_glossary.py
=====================
For each Pāli keyword in pi-keywords.txt (or .md), call the OpenAI API to
produce a short English definition anchored in actual example blocks from
the aligned source + translation.

What it does per keyword
------------------------
1. Finds up to `--examples` aligned blocks from pi-1.md that contain the
   keyword (or any inflected form).
2. Pairs each Pāli block with the same-anchor English block from
   en-1-rhys_davids.md.
3. Sends a zero-shot prompt to GPT:
      "Given these Pāli-English aligned passages, define the term <lemma>..."
4. Parses the JSON response into:
      - primary_gloss  (concise English equivalent, ≤5 words)
      - senses         [{"label": ..., "definition": ...}]
      - notes          (optional translator notes)
5. Writes pi-en-zero-shot.md with one entry per keyword in bb-glossary style.

Rate limiting / cost
--------------------
- Batches keywords into groups of 20 per API call (one call per batch) to
  reduce round-trips and cost.
- Uses gpt-4o-mini by default (cheap; override with --model).
- Set --dry-run to see the prompts without calling the API.

Usage
-----
    export OPENAI_API_KEY=sk-...
    python3 zero_shot_glossary.py \\
        --keywords   pi-keywords.md \\
        --pali       1-SOURCES/Text/pi-1.md \\
        --english    1-SOURCES/Translations/en-1-rhys_davids.md \\
        --examples   3 \\
        --batch      20 \\
        --model      gpt-4o-mini \\
        --out        pi-en-zero-shot

Options
-------
    --start N     Skip the first N keywords (for resuming a partial run).
    --end N       Stop after keyword N (for partial runs / testing).
    --dry-run     Print prompts without calling the API.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from map_keywords_to_pali import parse_blocks, tokenize_pali, parse_keywords
from flip_to_pali_glossary import normalize_pali

# ---------------------------------------------------------------------------
# Block retrieval helpers
# ---------------------------------------------------------------------------

def build_index(pi_text, en_text):
    """Return (pi_blocks, en_blocks, lemma_to_bids).

    lemma_to_bids maps every Pāli lemma to the list of aligned block IDs
    (sorted by natural block order) that contain an inflected form of it.
    """
    from collections import defaultdict
    pi_blocks = parse_blocks(pi_text)
    en_blocks = parse_blocks(en_text)
    common = set(pi_blocks) & set(en_blocks)

    lemma_to_bids = defaultdict(list)
    # Preserve source order by building a sorted bid list first.
    def bid_sort_key(b):
        parts = b.replace('-', ' ').split()
        return [(0, int(x)) if x.isdigit() else (1, x) for x in parts]

    sorted_bids = sorted(common, key=bid_sort_key)
    for bid in sorted_bids:
        seen = set()
        for tok in tokenize_pali(pi_blocks[bid]):
            lemma = normalize_pali(tok)
            seen.add(lemma)
        for lemma in seen:
            lemma_to_bids[lemma].append(bid)

    return pi_blocks, en_blocks, lemma_to_bids


def get_examples(lemma, pi_blocks, en_blocks, lemma_to_bids, max_examples):
    """Return a list of (pi_text, en_text) pairs for the given lemma."""
    bids = lemma_to_bids.get(lemma, [])
    out = []
    for bid in bids[:max_examples]:
        pi = pi_blocks[bid].strip()
        en = en_blocks.get(bid, "").strip()
        if pi and en:
            out.append((pi, en))
    return out


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert Pāli lexicographer specialising in the Abhidhamma Piṭaka.
You will be given one or more Pāli keywords together with aligned example
passages (Pāli original + English translation from C.A.F. Rhys Davids 1900).
For EACH keyword, produce a concise lexical entry in JSON.

Return a JSON array — one object per keyword — with these fields:
{
  "lemma": "<pali lemma>",
  "primary_gloss": "<1-5 word English equivalent, no parentheses>",
  "senses": [
    {"label": "(1)", "gloss": "<concise rendering>", "note": "<optional clarification>"},
    ...
  ],
  "pos": "<noun|verb|adjective|indeclinable>",
  "note": "<optional: compound structure, alternate renderings, usage warning>"
}

Rules:
- Give at most 3 senses. If the term is monosemous, give only 1.
- primary_gloss = the MOST common / important sense in the given passages.
- Do not copy the Rhys Davids gloss verbatim if it is archaic or misleading;
  prefer modern, accurate Buddhist English (e.g. "volition" over "co-efficients").
- If the term does not occur in the examples but is clearly known
  (e.g. nibbāna), give the standard scholarly gloss.
- Respond ONLY with the JSON array. No prose outside the JSON.
"""


def make_prompt(batch):
    """batch = list of (lemma, [(pi_text, en_text), ...])"""
    lines = []
    for lemma, examples in batch:
        lines.append(f"## Keyword: {lemma}")
        if examples:
            for i, (pi, en) in enumerate(examples, 1):
                lines.append(f"### Example {i}")
                lines.append(f"Pāli:    {pi[:400]}")
                lines.append(f"English: {en[:400]}")
        else:
            lines.append("(no aligned example found; use general Abhidhamma knowledge)")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# OpenAI call
# ---------------------------------------------------------------------------

def call_openai(prompt, model, api_key, max_retries=3):
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    for attempt in range(1, max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
                response_format={"type": "json_object"},
            )
            raw = resp.choices[0].message.content
            # The model may return {"entries": [...]} or just [...]
            parsed = json.loads(raw)
            if isinstance(parsed, list):
                return parsed
            # unwrap any wrapper key
            for v in parsed.values():
                if isinstance(v, list):
                    return v
            return []
        except Exception as e:
            print(f"  API error (attempt {attempt}/{max_retries}): {e}", file=sys.stderr)
            if attempt < max_retries:
                time.sleep(2 ** attempt)
    return []


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_entry(entry):
    """Format one JSON entry into a markdown block."""
    lemma = entry.get("lemma", "?")
    primary = entry.get("primary_gloss", "")
    pos = entry.get("pos", "")
    senses = entry.get("senses", [])
    note = entry.get("note", "")

    lines = [f"### {lemma}"]
    pos_str = f" _({pos})_" if pos else ""
    lines.append(f"**{primary}**{pos_str}")
    lines.append("")
    if senses:
        for s in senses:
            label = s.get("label", "")
            gloss = s.get("gloss", "")
            snote = s.get("note", "")
            if snote:
                lines.append(f"{label} {gloss} — _{snote}_")
            else:
                lines.append(f"{label} {gloss}")
    if note:
        lines.append(f"\n> {note}")
    lines.append("")
    return "\n".join(lines)


def compact_line(entry):
    """One-line bb-glossary style: lemma: (1) gloss; (2) gloss ..."""
    lemma = entry.get("lemma", "?")
    senses = entry.get("senses", [])
    if not senses:
        return f"- **{lemma}**: {entry.get('primary_gloss', '—')}"
    parts = "; ".join(
        f"{s.get('label','')} {s.get('gloss','')}" for s in senses
    )
    return f"- **{lemma}**: {parts}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keywords", default="pi-keywords.md")
    ap.add_argument("--pali",    default="1-SOURCES/Text/pi-1.md")
    ap.add_argument("--english", default="1-SOURCES/Translations/en-1-rhys_davids.md")
    ap.add_argument("--examples", type=int, default=3,
                    help="Aligned example blocks to include per keyword (default 3)")
    ap.add_argument("--batch", type=int, default=20,
                    help="Keywords per API call (default 20)")
    ap.add_argument("--model", default="gpt-4o-mini")
    ap.add_argument("--out", default="pi-en-zero-shot")
    ap.add_argument("--start", type=int, default=0,
                    help="Skip first N keywords (for resuming)")
    ap.add_argument("--end", type=int, default=None,
                    help="Stop after keyword index N (exclusive)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print prompts without calling the API")
    args = ap.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key and not args.dry_run:
        print("Error: set OPENAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)

    print("Loading source files...", file=sys.stderr)
    pi_text = Path(args.pali).read_text(encoding="utf-8")
    en_text = Path(args.english).read_text(encoding="utf-8")

    print("Building block index...", file=sys.stderr)
    pi_blocks, en_blocks, lemma_to_bids = build_index(pi_text, en_text)

    keywords = parse_keywords(Path(args.keywords))
    keywords = keywords[args.start: args.end]
    print(f"Processing {len(keywords)} keywords (batch size {args.batch})...",
          file=sys.stderr)

    out_path = Path(f"{args.out}.md")
    # Append mode so we can resume.
    mode = "a" if args.start > 0 else "w"
    results = []     # list of JSON entry dicts

    with out_path.open(mode, encoding="utf-8") as f:
        if mode == "w":
            f.write("# Pāli → English zero-shot glossary\n\n")
            f.write(f"- Source: `{args.pali}` + `{args.english}`\n")
            f.write(f"- Model: `{args.model}`\n")
            f.write(f"- Keywords: {len(keywords)} (slice [{args.start}:{args.end}])\n\n")
            f.write("> Status: AI-generated. Each entry is grounded in aligned example\n"
                    "> blocks from the Rhys Davids translation. Verify against\n"
                    "> `2-RAILS/Bilingual-Glossaries/pi-en.md` before promoting to rails.\n\n")
            f.write("---\n\n## Compact form\n\n")
            # placeholder — we'll rewrite after all batches
            f.write("<!-- compact -->\n\n")
            f.write("---\n\n## Detailed entries\n\n")

        # Process in batches.
        for batch_start in range(0, len(keywords), args.batch):
            batch_keys = keywords[batch_start: batch_start + args.batch]
            batch_data = []
            for lemma in batch_keys:
                examples = get_examples(
                    lemma, pi_blocks, en_blocks, lemma_to_bids, args.examples
                )
                batch_data.append((lemma, examples))

            prompt = make_prompt(batch_data)
            abs_start = args.start + batch_start
            abs_end = abs_start + len(batch_keys)
            print(f"Batch [{abs_start}:{abs_end}]...", file=sys.stderr, end=" ")

            if args.dry_run:
                print(f"\n{'='*60}\n{prompt}\n{'='*60}")
                continue

            entries = call_openai(prompt, args.model, api_key)
            print(f"{len(entries)} entries returned", file=sys.stderr)

            for entry in entries:
                results.append(entry)
                f.write(format_entry(entry))
                f.flush()

            # Be polite to rate limits.
            if batch_start + args.batch < len(keywords):
                time.sleep(0.5)

    if args.dry_run:
        return

    # Rewrite the compact section.
    content = out_path.read_text(encoding="utf-8")
    compact = "\n".join(compact_line(e) for e in results)
    content = content.replace("<!-- compact -->", compact, 1)
    out_path.write_text(content, encoding="utf-8")

    print(f"\nWrote: {out_path} ({len(results)} entries)", file=sys.stderr)


if __name__ == "__main__":
    main()
