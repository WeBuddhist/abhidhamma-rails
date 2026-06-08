"""
lookup.py
---------
Fetches English translations for Pali words from the DPD database.
Handles both root forms ("dhamma") and inflected forms ("dhammā").
"""

import re
import sqlite3

from .connect_db import DBConnection
from .models import PaliEntry


class PaliLookup:
    """
    Looks up English translations for Pali words from dpd_headwords.

    Usage:
        lookup = PaliLookup()
        entries = lookup.get_translations("dhammā")   # inflected form works too
        entries = lookup.get_translations("dhamma")   # root form also works
    """

    def __init__(self):
        self.conn: sqlite3.Connection = DBConnection.get_connection()
        self.inflection_map: dict[str, str] = self._build_inflection_map()

    def _build_inflection_map(self) -> dict[str, str]:
        """
        Builds reverse map: inflected_form (lowercase) -> lemma_1

        DPD stores all inflections as a comma-separated string
        in the `inflections` column of dpd_headwords.

        e.g. "dhamma,dhammā,dhammaṃ,dhammassa,..." -> all map to "dhamma 1.01"
        """
        print("Building inflection map...")
        cursor = self.conn.cursor()
        cursor.execute("SELECT lemma_1, inflections FROM dpd_headwords")

        inflection_map = {}
        for row in cursor.fetchall():
            lemma_1 = row["lemma_1"]

            # Map the clean lemma itself (strip trailing " 1.03" etc.)
            lemma_clean = self._clean_word(lemma_1)
            if lemma_clean not in inflection_map:
                inflection_map[lemma_clean] = lemma_1

            # Map every inflected form
            if row["inflections"]:
                for form in row["inflections"].split(","):
                    form = form.strip().lower()
                    if form and form not in inflection_map:
                        inflection_map[form] = lemma_1

        print(f"Inflection map built: {len(inflection_map):,} forms indexed.")
        return inflection_map

    def resolve_root(self, pali_word: str) -> str | None:
        """
        Resolves any inflected Pali word to its root form.

        e.g. "dhammā"    -> "dhamma"
             "dhammaṃ"   -> "dhamma"
             "dhammassa" -> "dhamma"
             "dhamma"    -> "dhamma"

        Returns None if the word is not found in DPD.
        """
        word = pali_word.strip().lower()
        lemma_1 = self.inflection_map.get(word)
        if not lemma_1:
            return None
        return self._clean_word(lemma_1)

    def get_translations(self, pali_word: str) -> list[PaliEntry]:
        """
        Takes any Pali word (inflected or root) and returns all its
        English translations across all senses from the DPD.

        e.g. get_translations("dhammā") returns:
            dhamma 1.01  →  nature; character
            dhamma 1.02  →  quality; characteristic; trait
            dhamma 1.03  →  teaching; discourse; doctrine
            ...

        Returns empty list if word not found.
        """
        root = self.resolve_root(pali_word)
        if not root:
            return []

        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT lemma_1, pos, meaning_1, meaning_lit, meaning_2
            FROM dpd_headwords
            WHERE lemma_1 = ? OR lemma_1 LIKE ?
            ORDER BY lemma_1
        """, (root, f"{root} %"))

        entries = []
        for row in cursor.fetchall():
            entries.append(PaliEntry(
                lemma       = row["lemma_1"],
                lemma_clean = self._clean_word(row["lemma_1"]),
                pos         = row["pos"] or "",
                meaning_1   = row["meaning_1"] or "",
                meaning_lit = row["meaning_lit"] or "",
                meaning_2   = row["meaning_2"] or "",
            ))
        return entries

    @staticmethod
    def _clean_word(word: str) -> str:
        """Strip trailing sense numbers e.g. 'dhamma 1.03' -> 'dhamma'."""
        return re.sub(r'\s*[\d.]+$', '', word).strip().lower()