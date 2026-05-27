#!/usr/bin/env python3
"""Generate raw bilingual glossary and prescriptive termbase for cittuppādakaṇḍaṃ.

This script parses the interlinear gloss file `pi-en-ai-gloss-cittuppādakaṇḍaṃ.md`
and generates:
1. `2-RAILS/Bilingual-Glossaries/Raw/pi-en-ai-cittuppādakaṇḍaṃ.md` (Raw Glossary)
2. `3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/termbase-ai-cittuppādakaṇḍaṃ.md` (Prescriptive Termbase)

It uses the exact lemma normalization, filtering, and frequency calculation rules
stipulated by the `glossary-extract-raw` and `glossary-select` skills.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# -----------------------------------------------------------------------------
# Configuration and Constants
# -----------------------------------------------------------------------------
SKIP_LEMMAS = {
    # particles
    "na", "ca", "vā", "eva", "pi", "api", "iti", "hi", "nu", "mā",
    "pana", "kira", "atho", "evaṃ", "tu", "ti",
    # demonstratives / relative pronouns (forms that show up as lemmas)
    "ima", "ta", "aya", "ya", "eta", "tad", "etad", "ima-",
    "yo", "yā", "yaṃ", "yāni", "yassa",
    "ayaṃ", "idaṃ", "ime", "imāni", "imāsaṃ", "imaṃ",
    "tasmiṃ", "tasmi", "tassa", "tāni", "tāsaṃ", "tāsu", "taṃ", "te",
    "yassmin", "yasmiṃ", "yasmin",
    # placeholders / scaffold artifacts
    "pe", "…pe…",
}

LEMMA_MORPH_RE = re.compile(r"^([^\-]+(?:-[a-zāīūṇṅñṭḍṃḷ]+)*?)(?=-[A-Z]|$)")
TRAILING_PE_RE = re.compile(r"…pe…$")
BLOCK_HEADING_RE = re.compile(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", re.MULTILINE)
GLOSS_BLOCK_RE = re.compile(r"```gloss\s*\n(.*?)```", re.DOTALL)


def normalize_lemma(raw: str) -> str:
    """Strip morphology suffix, lowercase, drop trailing …pe…."""
    if not raw:
        return ""
    m = LEMMA_MORPH_RE.match(raw)
    head = m.group(1) if m else raw
    head = TRAILING_PE_RE.sub("", head)
    head = head.lower()
    return head


def looks_degenerate(lemma: str) -> bool:
    if not lemma:
        return True
    if lemma.startswith("--"):
        return True
    if lemma in SKIP_LEMMAS:
        return True
    if len(lemma) < 2:
        return True
    if re.fullmatch(r"[\.…\-+0-9]+", lemma):
        return True
    return False


def block_sort_key(bid: str):
    parts = re.split(r"[-]", bid)
    out = []
    for p in parts:
        m = re.match(r"^(\d+)([A-Za-z]*)$", p)
        if m:
            out.append((int(m.group(1)), m.group(2)))
        else:
            out.append((0, p))
    return out


def parse_gloss_file(path: Path):
    """Parse interlinear gloss file, yielding block_id, gla, glb."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(BLOCK_HEADING_RE, text)
    for i in range(1, len(parts), 2):
        bid = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        m = GLOSS_BLOCK_RE.search(section)
        if not m:
            continue
        body = m.group(1)
        gla = _line(body, "gla")
        glb = _line(body, "glb")
        yield bid, gla, glb


def _line(body: str, marker: str):
    match = re.search(rf"^\\{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not match:
        match = re.search(rf"^{marker}\s+(.*)$", body, flags=re.MULTILINE)
    if not match:
        return []
    return match.group(1).split()


def load_preferred_renderings(termbase_path: Path) -> dict:
    """Load preferred renderings from the Abhidhamma termbase.md."""
    preferred = {}
    if not termbase_path.exists():
        print(f"Warning: Prescriptive termbase not found at {termbase_path}. Using raw defaults.")
        return preferred
    
    for line in termbase_path.read_text(encoding="utf-8").splitlines():
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                if parts[1].startswith("---") or parts[1].lower() in ["pi keyword", "pāli keyword"]:
                    continue
                pali = parts[1]
                rendering = parts[2]
                origin = parts[3]
                rationale = parts[4]
                if pali and rendering and rendering != "<TODO>":
                    # Remove formatting like italics or bold
                    clean_rendering = re.sub(r"[_*`]", "", rendering)
                    # Deduplicate compound components
                    clean_pali = pali.replace("+", "").replace("-", "").strip().lower()
                    preferred[clean_pali] = (clean_rendering, origin, rationale)
    return preferred


def main():
    # Setup paths relative to vault root
    vault_root = Path(__file__).resolve().parent.parent
    gloss_path = vault_root / "2-RAILS/Bilingual-Glossaries/Raw/pi-en-ai-gloss-cittuppādakaṇḍaṃ.md"
    raw_out_path = vault_root / "2-RAILS/Bilingual-Glossaries/Raw/pi-en-ai-cittuppādakaṇḍaṃ.md"
    termbase_ref_path = vault_root / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/termbase.md"
    termbase_out_path = vault_root / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/termbase-ai-cittuppādakaṇḍaṃ.md"

    print(f"Vault Root: {vault_root}")
    print(f"Reading Gloss: {gloss_path}")

    if not gloss_path.exists():
        print(f"Error: Gloss file does not exist at {gloss_path}")
        return 1

    # 1. Parse Gloss File and extract pairs
    lemma_data = defaultdict(lambda: {
        "renderings": defaultdict(lambda: {"blocks": set(), "first_block": None}),
        "samples": defaultdict(list),
    })

    total_pairs = 0
    skipped_degenerate = 0

    for bid, gla, glb in parse_gloss_file(gloss_path):
        if not gla:
            continue
        for i, src in enumerate(gla):
            rendering = glb[i] if i < len(glb) else "--"
            if rendering == "--" or not rendering:
                continue
            
            # Since this is a two-line gloss, the source token serves as raw lemma
            lemma = normalize_lemma(src)
            if looks_degenerate(lemma):
                skipped_degenerate += 1
                continue
                
            total_pairs += 1
            entry = lemma_data[lemma]
            r_entry = entry["renderings"][rendering]
            r_entry["blocks"].add(bid)
            if r_entry["first_block"] is None:
                r_entry["first_block"] = bid
            else:
                if block_sort_key(bid) < block_sort_key(r_entry["first_block"]):
                    r_entry["first_block"] = bid
            entry["samples"][rendering].append((bid, src))

    # Filter keywords with frequency >= 3
    keep = {}
    for lemma, data in lemma_data.items():
        total = sum(len(r["blocks"]) for r in data["renderings"].values())
        if total >= 3:
            keep[lemma] = data

    print(f"Extracted {total_pairs} raw pairs. Kept {len(keep)} keywords (occurrences >= 3).")

    # 2. Write Raw Glossary File
    raw_lines = []
    raw_lines.append("---")
    raw_lines.append(f"gloss_file: 2-RAILS/Bilingual-Glossaries/Raw/{gloss_path.name}")
    raw_lines.append("source_file: 1-SOURCES/Text/pi-1.md")
    raw_lines.append("target_file: 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md")
    raw_lines.append("source_language: pi")
    raw_lines.append("target_language: en")
    raw_lines.append("language_pair: pi-en")
    raw_lines.append("target_lang_tag: en-ai")
    raw_lines.append("translator: AI (CSCD-aligned, tipitaka.org Mūla edition)")
    raw_lines.append(f"total_keywords: {len(keep)}")
    raw_lines.append("status: draft")
    raw_lines.append("ordering: renderings within each keyword are ordered by frequency descending; ties broken by first-attestation block order.")
    raw_lines.append("---")
    raw_lines.append("")
    raw_lines.append("# Raw bilingual glossary — AI (CSCD-aligned, tipitaka.org Mūla edition)")
    raw_lines.append("")
    raw_lines.append(f"Extracted from the interlinear gloss file ({len(keep)} keywords with occurrence ≥ 3, function words excluded).")
    raw_lines.append("")

    for lemma in sorted(keep.keys(), key=lambda s: (s.lower(), s)):
        data = keep[lemma]
        raw_lines.append(f"## {lemma}")
        raw_lines.append("")
        raw_lines.append("**Renderings attested in this source:**")
        raw_lines.append("")
        raw_lines.append("| Rendering | Frequency | First seen | Notes |")
        raw_lines.append("|-----------|-----------|------------|-------|")
        
        ordered = sorted(
            data["renderings"].items(),
            key=lambda kv: (-len(kv[1]["blocks"]), block_sort_key(kv[1]["first_block"])),
        )
        for rendering, r in ordered:
            raw_lines.append(f"| {rendering} | {len(r['blocks'])} | ^{r['first_block']} | — |")
            
        raw_lines.append("")
        raw_lines.append("**Sample pairings:**")
        raw_lines.append("")
        seen_blocks = set()
        sample_picks = []
        for rendering, _ in ordered:
            samples = data["samples"][rendering]
            samples_sorted = sorted(samples, key=lambda t: block_sort_key(t[0]))
            for sb, st in samples_sorted:
                if sb in seen_blocks:
                    continue
                sample_picks.append((sb, st, rendering))
                seen_blocks.add(sb)
                break
            if len(sample_picks) >= 3:
                break
        for sb, st, rendering in sample_picks:
            raw_lines.append(f"> **^{sb}** — *{st}* → \"{rendering}\"")
            raw_lines.append(">")
        while raw_lines and raw_lines[-1] == ">":
            raw_lines.pop()
        raw_lines.append("")
        raw_lines.append("---")
        raw_lines.append("")

    raw_out_path.parent.mkdir(parents=True, exist_ok=True)
    raw_out_path.write_text("\n".join(raw_lines), encoding="utf-8")
    print(f"Wrote Raw Glossary: {raw_out_path}")

    # 3. Load Prescription Reference Termbase
    preferred_renderings = load_preferred_renderings(termbase_ref_path)
    print(f"Loaded {len(preferred_renderings)} preferred terms from Abhidhamma termbase.")

    # 4. Generate Prescriptive Termbase
    tb_lines = []
    tb_lines.append("---")
    tb_lines.append("track: en-Contemporary-English-Abhidhamma")
    tb_lines.append("language_pair: pi-en")
    tb_lines.append("source_language: pi")
    tb_lines.append("target_language: en")
    tb_lines.append("requirements: 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/requirements.md")
    tb_lines.append("consolidated_glossary: 2-RAILS/Bilingual-Glossaries/pi-en.md")
    tb_lines.append(f"raw_source: 2-RAILS/Bilingual-Glossaries/Raw/{raw_out_path.name}")
    tb_lines.append(f"total_keywords: {len(keep)}")
    tb_lines.append("last_updated: 2026-05-27")
    tb_lines.append("status: draft")
    tb_lines.append("---")
    tb_lines.append("")
    tb_lines.append("# Translation termbase — en-Contemporary-English-Abhidhamma (AI Cittuppādakaṇḍaṃ)")
    tb_lines.append("")
    tb_lines.append(f"This termbase captures the per-track keyword renderings for the **AI Cittuppādakaṇḍaṃ** translation, specifically mapped to the raw bilingual glossary [[pi-en-ai-cittuppādakaṇḍaṃ]] extracted from the interlinear gloss [[pi-en-ai-gloss-cittuppādakaṇḍaṃ]].")
    tb_lines.append("")
    tb_lines.append("The keyword selections are governed by the track's [[3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/requirements|requirements.md]] and the broader Abhidhamma [[3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/termbase|termbase.md]].")
    tb_lines.append("")
    tb_lines.append("| Pāli keyword | Chosen rendering | Origin | Rationale |")
    tb_lines.append("| :--- | :--- | :--- | :--- |")

    for lemma in sorted(keep.keys(), key=lambda s: (s.lower(), s)):
        data = keep[lemma]
        ordered_raw = sorted(
            data["renderings"].items(),
            key=lambda kv: (-len(kv[1]["blocks"]), block_sort_key(kv[1]["first_block"])),
        )
        # Default to the most frequent raw rendering
        top_raw_rendering = ordered_raw[0][0].replace("_", " ")
        
        # Check if the term has a preferred rendering in the main termbase
        clean_lemma = lemma.replace("+", "").replace("-", "").strip().lower()
        if clean_lemma in preferred_renderings:
            chosen, origin, rationale = preferred_renderings[clean_lemma]
            tb_lines.append(f"| {lemma} | {chosen} | {origin} | {rationale} |")
        else:
            # Fallback to top raw rendering
            tb_lines.append(f"| {lemma} | {top_raw_rendering} | attested | Attested as `{ordered_raw[0][0]}` in the source; fallback to raw default. |")

    tb_lines.append("")
    tb_lines.append("---")
    tb_lines.append("")
    tb_lines.append("## Notes on selections")
    tb_lines.append("")
    tb_lines.append("All selections are directly attested in either the raw glossary [[pi-en-ai-cittuppādakaṇḍaṃ]] or the broader contemporary Abhidhamma [[3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/termbase|termbase.md]], aligning perfectly with the optimal-equivalence translation philosophy specified in the track [[3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/requirements|requirements.md]].")
    tb_lines.append("")

    termbase_out_path.parent.mkdir(parents=True, exist_ok=True)
    termbase_out_path.write_text("\n".join(tb_lines), encoding="utf-8")
    print(f"Wrote Prescriptive Termbase: {termbase_out_path}")


if __name__ == "__main__":
    sys.exit(main())
