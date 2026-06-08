from dataclasses import dataclass


@dataclass
class PaliEntry:
    lemma: str
    lemma_clean: str
    pos: str
    meaning_1: str
    meaning_lit: str
    meaning_2: str
