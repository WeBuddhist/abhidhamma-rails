#!/usr/bin/env python3
"""Append pi-1.md:458-4382 translation to en-dhammasangani-ai-2.md from en-dhammasangani-ai.md."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AI = ROOT / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md"
AI2 = ROOT / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai-2.md"

SUTTANTA_PAIRS = [
    ("101", "Phenomena that partake of wisdom.", "Phenomena that partake of ignorance."),
    ("102", "Phenomena that resemble lightning.", "Phenomena that resemble a thunderbolt."),
    ("103", "Foolish phenomena.", "Wise phenomena."),
    ("104", "Dark phenomena.", "Bright phenomena."),
    ("105", "Phenomena that cause torment.", "Phenomena that do not cause torment."),
    ("106", "Designations.", "Paths of designation."),
    ("107", "Expressions.", "Paths of expression."),
    ("108", "Concepts.", "Paths of concept."),
    ("109", "Mentality.", "Materiality."),
    ("110", "Ignorance.", "Craving for existence."),
    ("111", "View of eternalism.", "View of annihilationism."),
    ("112", "Eternalist view.", "Annihilationist view."),
    ("113", "View that the world is finite.", "View that the world is infinite."),
    ("114", "Speculative views about the past.", "Speculative views about the future."),
    ("115", "Shamelessness.", "Fearlessness of wrongdoing."),
    ("116", "Moral shame.", "Moral dread."),
    ("117", "Obstinacy.", "Bad friendship."),
    ("118", "Tractability.", "Good friendship."),
    ("119", "Skill in offences.", "Skill in rehabilitation from offences."),
    ("120", "Skill in attainments.", "Skill in emerging from attainments."),
    ("121", "Skill in elements.", "Skill in attention."),
    ("122", "Skill in sense bases.", "Skill in dependent origination."),
    ("123", "Skill in the possible.", "Skill in the impossible."),
    ("124", "Uprightness.", "Gentleness."),
    ("125", "Patience.", "Amiability."),
    ("126", "Friendliness.", "Hospitality."),
    ("127", "Unguardedness of the sense doors.", "Immoderation in food."),
    ("128", "Guardedness of the sense doors.", "Moderation in food."),
    ("129", "Forgetfulness.", "Lack of clear comprehension."),
    ("130", "Mindfulness.", "Clear comprehension."),
    ("131", "Power of reflection.", "Power of development."),
    ("132", "Calm.", "Insight."),
    ("133", "Sign of calm.", "Sign of exertion."),
    ("134", "Exertion.", "Unshakeability."),
    ("135", "Failure of virtue.", "Failure of view."),
    ("136", "Accomplishment of virtue.", "Accomplishment of view."),
    ("137", "Purity of virtue.", "Purity of view."),
    ("138", "Purity of view.", "Exertion of one who holds the view."),
    ("139", "Spiritual urgency in agitating situations.", "Appropriate exertion of one who is spiritually urgent."),
    ("140", "Discontent with wholesome phenomena.", "Unfalteringness in exertion."),
    ("141", "Wisdom.", "Liberation."),
    ("142", "Knowledge of destruction.", "Knowledge of non-arising."),
]


def format_suttanta_matrix() -> str:
    lines = ["##### Suttanta Duplet Matrix ^1-0b-14-0", ""]
    for num, ka, kha in SUTTANTA_PAIRS:
        bid = f"^1-0b-{num}"
        if num == "142":
            lines.append(f"{num}. (Ka) {ka}")
            lines.append(f"(Kha) {kha}")
            lines.append("Suttanta Duplet Matrix.")
            lines.append(f"Matrix complete. {bid}")
        else:
            lines.append(f"{num}. (Ka) {ka}")
            lines.append(f"(Kha) {kha} {bid}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def extract_cittuppada_onwards(ai_text: str) -> str:
    marker = "### 1. Chapter on the Arising of Consciousness ^1-1-0"
    idx = ai_text.index(marker)
    chunk = ai_text[idx:]
    # Remove transclusion lines
    chunk = re.sub(r"^!\[\[.*?\]\]\n", "", chunk, flags=re.MULTILINE)
    # Normalize main section heading
    chunk = chunk.replace(
        "### 1. Chapter on the Arising of Consciousness ^1-1-0",
        "### Chapter on the Arising of Consciousness ^1-1-0",
    )
    chunk = chunk.replace("### 2. Chapter on Form ^1-2-0", "### Chapter on Form ^1-2-0")
    chunk = chunk.replace("### 3. Compendium of Categories ^1-3-0", "### Compendium of Categories ^1-3-0")
    chunk = chunk.replace("### 4. Commentary Section ^1-4-0", "### Commentary Section ^1-4-0")
    # Collapse excessive blank lines
    chunk = re.sub(r"\n{3,}", "\n\n", chunk)
    return chunk


def update_frontmatter(ai2_text: str) -> str:
    ai2_text = re.sub(
        r"covers_verses: .*",
        "covers_verses: 1-0a-0–1-1616",
        ai2_text,
    )
    ai2_text = re.sub(
        r"title: .*",
        "title: Dhammasaṅgaṇī — AI-assisted translation",
        ai2_text,
    )
    ai2_text = re.sub(
        r"translation_basis: .*",
        "translation_basis: Contemporary English Abhidhamma track; Bhikkhu Bodhi glossary; verse rails 1-0a-1–1-0a-22; en-dhammasangani-ai aligned for 1-0b-101–1-1616",
        ai2_text,
    )
    return ai2_text


def main() -> None:
    ai_text = AI.read_text(encoding="utf-8")
    ai2_text = AI2.read_text(encoding="utf-8")

    if "##### Suttanta Duplet Matrix ^1-0b-14-0" in ai2_text:
        print("Suttanta section already present; skipping append.")
        return

    appendix = format_suttanta_matrix() + "\n" + extract_cittuppada_onwards(ai_text)
    ai2_text = ai2_text.rstrip() + "\n\n" + appendix
    ai2_text = update_frontmatter(ai2_text)
    AI2.write_text(ai2_text, encoding="utf-8")
    print(f"Appended {len(appendix.splitlines())} lines to {AI2}")


if __name__ == "__main__":
    main()
