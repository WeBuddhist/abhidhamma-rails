"""
en_freq.py — English corpus frequency reference for translation-variant filtering.

Primary source: wordfreq library (Apache 2.0) if installed.
Fallback: bundled COCA-derived frequency table for the top ~5000 lemmas,
          plus a curated override set for words common in Abhidhamma prose
          that tend to appear as co-occurrence noise rather than translations.

Threshold (default 5e-4): words at or above this frequency are considered
"common English" and are excluded from translation-rendering candidates.
At this threshold, the cut-off is approximately COCA rank ~150.

To install wordfreq for better results:
    pip install wordfreq --break-system-packages
"""

# ---------------------------------------------------------------------------
# Curated override: words that are common in general English AND appear as
# co-occurrence noise in Abhidhamma translation prose.  These are added
# regardless of the Zipf-law estimate so the bundled table does not need
# exact rank coverage.
# ---------------------------------------------------------------------------
_COMMON_OVERRIDE = {
    # very common nouns / verbs often appearing in analytical prose
    "time", "one", "two", "three", "four", "five",
    "first", "second", "third", "fourth", "fifth",
    "place", "part", "form", "kind", "type", "class",
    "body", "mind", "life", "world", "group", "order",
    "cause", "effect", "result", "process", "condition",
    "object", "subject", "matter", "nature", "sense",
    'path', 'contact', 'mind', 'thing', "being", "person",
    "point", "level", "stage", "step", "phase", "side",
    "moment", "period", "occasion", "instance", "case",
    "basis", "ground", "source", "origin", "factor",
    "element", "component", "aspect", "feature", "quality",
    "manner", "mode", "way", "means", "method", "approach",
    "field", "area", "domain", "scope", "range", "limit",
    # common verbs appearing in Abhidhamma descriptive prose
    "enters", "abides", "develops", "attains", "arises",
    "ceases", "arisen", "ceased", "arise", "cease",
    "occurs", "appears", "manifests", "produces", "generates",
    "knows", "sees", "perceives", "discerns", "understands",
    "finds", "holds", "makes", "takes", "gives", "shows",
    "becomes", "remains", "continues", "follows", "leads",
    "born", "made", "done", "come", "gone", "seen",
    # common adjectives / adverbs in prose
    "present", "past", "future", "internal", "external",
    "pleasant", "unpleasant", "happy", "painful", "neutral",
    "whole", "full", "complete", "total", "entire",
    "single", "alone", "only", "merely", "simply",
    "quite", "rather", "very", "more", "less", "most",
    "slowly", "quickly", "directly", "further", "indeed",
}

# ---------------------------------------------------------------------------
# Zipf-law frequency table for COCA top ~5000.
# We only enumerate ranks up to ~150 here (freq >= 5e-4); words below that
# threshold are not "common" in the relevant sense.  The curated override
# set above handles domain-specific noise that falls outside this band.
# ---------------------------------------------------------------------------
_TOP_RANKS = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
    "for", "not", "on", "with", "he", "as", "you", "do", "at", "this",
    "but", "his", "by", "from", "they", "we", "say", "her", "she", "or",
    "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know",
    "take", "people", "into", "year", "your", "good", "some", "could",
    "them", "see", "other", "than", "then", "now", "look", "only", "come",
    "its", "over", "think", "also", "back", "after", "use", "two", "how",
    "our", "work", "first", "well", "way", "even", "new", "want", "because",
    "any", "these", "give", "day", "most", "us", "great", "between", "need",
    "large", "often", "hand", "high", "place", "hold", "turn", "ask",
    "found", "here", "part", "still", "tell", "right", "become", "ever",
    "leave", "call", "feel", "seem", "long", "around", "down", "real",
    "keep", "believe", "show", "again", "old", "change", "play", "big",
    "always", "move", "live", "try", "white", "end", "run", "might",
    "next", "same", "far", "start", "let", "small", "form", "mean",
    "stand", "face", # mind is common but also Buddhist term — add to override
    "mind", "fact", "body", "life", "group",
]

# freq ≈ 0.07 / rank  (rank-1 → 0.07, rank-150 → ~4.7e-4 ≈ 5e-4)
_FREQ = {word: 0.07 / (i + 1) for i, word in enumerate(_TOP_RANKS)}

# Merge: override set gets a fixed high frequency so is_common() always returns True
for _w in _COMMON_OVERRIDE:
    if _w not in _FREQ:
        _FREQ[_w] = 5e-4   # exactly at the threshold → classified as common


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
try:
    import wordfreq as _wf

    def get_frequency(word: str) -> float:
        f = _wf.word_frequency(word, "en")
        return f if f > 0 else _FREQ.get(word.lower(), 0.0)

except ImportError:
    def get_frequency(word: str) -> float:
        return _FREQ.get(word.lower(), 0.0)


def is_common(word: str, threshold: float = 5e-4) -> bool:
    """Return True if the word is common English (should be treated as noise)."""
    return get_frequency(word) >= threshold


# ---------------------------------------------------------------------------
# Sanity check
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ("the",           True),   ("time",         True),
        ("first",         True),   ("contact",       True),
        ("path",          True),   ("mind",          True),
        ("enters",        True),   ("abides",        True),
        ("floods",        False),  ("wholesome",     False),
        ("hindrances",    False),  ("yokes",         False),
        ("zest",          False),  ("taints",        False),
        ("cankers",       False),  ("fetters",       False),
        ("nondistraction",False),  ("jhana",         False),
        ("rebirth",       False),  ("consciousness", False),
    ]
    ok = fail = 0
    for w, expected in tests:
        got = is_common(w)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            fail += 1
        else:
            ok += 1
        f = get_frequency(w)
        print(f"  {status}  {w:20s}  freq={f:.2e}  common={got}")
    print(f"\n{ok} OK, {fail} FAIL")
