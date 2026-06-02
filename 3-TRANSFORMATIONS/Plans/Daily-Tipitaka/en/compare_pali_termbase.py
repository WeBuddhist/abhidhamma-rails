#!/usr/bin/env python3
"""
compare_pali_termbase.py
========================
Compares vocabulary from rhys_davids_termbase.md (English TF-IDF analysis of the
Rhys Davids 1900 translation) with pi-1.md (Pāli Dhammasaṅgaṇī root text) to produce
a bilingual word map with sense tags.

For each Pāli term found in the root text the script:
  1. Records line numbers and block IDs where it appears.
  2. Looks up the corresponding English rendering used by Rhys Davids.
  3. Looks up the TF-IDF rank of that English word in the termbase.
  4. Assigns a sense tag in Local-Wiki format: "term (disambiguating phrase)".

The mapping is bidirectional:
  - PALI_DICT keys are canonical Pāli lemmas (and common inflected variants).
  - Each maps to (english_rendering, sense_tag).
  - The English rendering is then looked up in the parsed termbase.

Output
------
pali_english_map.md — written alongside this script.

Usage
-----
    python3 compare_pali_termbase.py        # from repo root or this directory
"""

import re
import pathlib
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE      = pathlib.Path(__file__).parent
REPO_ROOT = HERE.parents[3]               # abhidhamma-rails/
TERMBASE  = HERE / "rhys_davids_termbase.md"
PALI_ROOT = REPO_ROOT / "1-SOURCES/Text/pi-1.md"
OUTPUT    = HERE / "pali_english_map.md"

# ---------------------------------------------------------------------------
# Pāli diacritic character class  (shared regex fragment)
# ---------------------------------------------------------------------------
_PI = r"[a-zA-ZāīūṭḍṅñṇḷṃṁĀĪŪṬḌṄÑṆḶṂṀ]"
_PI_TOKEN = re.compile(
    r"(?<![a-zA-ZāīūṭḍṅñṇḷṃṁĀĪŪṬḌṄÑṆḶṂṀ])"
    r"[a-zA-ZāīūṭḍṅñṇḷṃṁĀĪŪṬḌṄÑṆḶṂṀ]+"
    r"(?:[-][a-zA-ZāīūṭḍṅñṇḷṃṁĀĪŪṬḌṄÑṆḶṂṀ]+)*"
)
_BLOCK_ID = re.compile(r"\^([\w\-]+)")

# ---------------------------------------------------------------------------
# Pāli stop-words (structural / grammatical words excluded from the map)
# ---------------------------------------------------------------------------
PALI_STOP: set[str] = {
    # common particles & conjunctions
    "ca", "na", "no", "vā", "ti", "pi", "hi", "tu", "eva", "kho", "pana",
    "nanu", "api", "yeva", "seyyathāpi", "atha", "yathā", "tathā",
    "tena", "tattha", "tasmā", "yato", "yena", "iti", "idha", "ettha",
    # pronouns & demonstratives
    "so", "sā", "taṃ", "te", "tā", "tāni", "yo", "yā", "yaṃ",
    "ye", "yā", "yāni", "eso", "esā", "etaṃ", "ete", "etā", "etāni",
    "ayaṃ", "imaṃ", "ime", "imā", "imāni", "asaṃ",
    # relative/interrogative
    "katamo", "katamā", "katamaṃ", "katame", "katamā", "katamāni",
    "kiṃ", "kena", "kismiṃ", "ko", "kā",
    # prepositions / indeclinables
    "pati", "abhi", "upa", "anu", "adhi", "pari", "paṭi", "nī",
    # numbers as words
    "eka", "dve", "tayo", "tīṇi", "cattāro",
    # common endings used as standalone tokens in mātikā
    "dhammā", "dhamma",  # kept separate – added to PALI_DICT explicitly
    "ceva",
    # editorial markers that appear as tokens
    "ka", "kha", "ga",         # (Ka) (Kha) (Ga) list markers
    "sī", "syā", "pts",        # variant reading sigla
}

# ---------------------------------------------------------------------------
# PALI_DICT
# Map: pāli_lemma_or_inflected_form (lowercase) → (english_rendering, sense_tag)
#
# Conventions
# -----------
# - english_rendering  : the word as it appears in the Rhys Davids termbase
#                        (lowercase, so it matches the parsed termbase table).
# - sense_tag          : Local-Wiki format → "lemma (disambiguating phrase)"
# ---------------------------------------------------------------------------
PALI_DICT: dict[str, tuple[str, str]] = {

    # ── Core ontological terms ────────────────────────────────────────────────
    "dhammā":           ("states",            "dhamma (mental state/phenomenon)"),
    "dhamma":           ("states",            "dhamma (mental state/phenomenon)"),

    # ── Ethical categories ────────────────────────────────────────────────────
    "kusalā":           ("good",              "kusala (wholesome)"),
    "kusala":           ("good",              "kusala (wholesome)"),
    "akusalā":          ("bad",               "akusala (unwholesome)"),
    "akusala":          ("bad",               "akusala (unwholesome)"),
    "abyākatā":         ("indeterminate",     "abyākata (morally indeterminate)"),
    "abyākata":         ("indeterminate",     "abyākata (morally indeterminate)"),
    "avyākata":         ("indeterminate",     "abyākata (morally indeterminate)"),
    "avyākatā":         ("indeterminate",     "abyākata (morally indeterminate)"),

    # ── Kamma result ──────────────────────────────────────────────────────────
    "vipākā":           ("result",            "vipāka (kamma-result)"),
    "vipāka":           ("result",            "vipāka (kamma-result)"),
    "vipākadhammadhammā": ("result",          "vipāka (kamma-result)"),
    "nevavipākanavipākadhammadhammā": ("indeterminate", "nevavipāka (neither-result-nor-resultant)"),

    # ── Feeling (vedanā) ──────────────────────────────────────────────────────
    "vedanā":           ("feeling",           "vedanā (feeling)"),
    "vedanāya":         ("feeling",           "vedanā (feeling)"),
    "sukhāya":          ("ease",              "sukha (pleasure/ease)"),
    "sukha":            ("ease",              "sukha (pleasure/ease)"),
    "dukkhāya":         ("ill",               "dukkha (pain/ill)"),
    "dukkha":           ("ill",               "dukkha (pain/ill)"),
    "upekkhāsahagatā":  ("accompanied by indifference", "upekkhā (equanimity)"),
    "upekkhā":          ("indifference",      "upekkhā (equanimity/indifference)"),
    "adukkhamasukhāya": ("neither-ill-nor-ease", "adukkhamasukha (neutral feeling)"),

    # ── Mental factors ────────────────────────────────────────────────────────
    "cetanā":           ("volition",          "cetanā (volition/intention)"),
    "cetasikā":         ("mental",            "cetasika (mental factor)"),
    "cetasika":         ("mental",            "cetasika (mental factor)"),
    "phassa":           ("contact",           "phassa (sense-contact)"),
    "phasso":           ("contact",           "phassa (sense-contact)"),
    "saññā":            ("perception",        "saññā (perception)"),
    "vitakka":          ("thought",           "vitakka (applied thought)"),
    "vitakko":          ("thought",           "vitakka (applied thought)"),
    "savitakkasavicārā":("applied thought",   "savitakka (with applied thought)"),
    "avitakkavicāramattā":("sustained thought only","avitakka (without applied thought)"),
    "avitakkaavicārā":  ("without thought",   "avitakkāvicāra (without any thought)"),
    "vicāra":           ("sustained",         "vicāra (sustained thought)"),
    "vicāro":           ("sustained",         "vicāra (sustained thought)"),
    "pīti":             ("zest",              "pīti (zest/rapture)"),
    "pītisahagatā":     ("accompanied by zest","pīti (zest/rapture)"),
    "sukhasahagatā":    ("accompanied by ease","sukha (pleasure/ease)"),
    "sati":             ("mindfulness",       "sati (mindfulness/memory)"),
    "samādhi":          ("concentration",     "samādhi (concentration)"),
    "sammāsamādhi":     ("right concentration","sammāsamādhi (right concentration)"),
    "paññā":            ("intuition",         "paññā (wisdom/intuition)"),
    "saddhā":           ("faith",             "saddhā (faith/confidence)"),
    "viriya":           ("energy",            "viriya (energy/effort)"),
    "passaddhi":        ("serenity",          "passaddhi (serenity/calming)"),

    # ── Aggregates (khandhā) ──────────────────────────────────────────────────
    "khandha":          ("skandha",           "khandha (aggregate/group)"),
    "khandhā":          ("skandha",           "khandha (aggregate/group)"),
    "rūpa":             ("form",              "rūpa (material form)"),
    "rūpino":           ("form",              "rūpa (material form)"),
    "arūpino":          ("incorporeal",       "arūpa (formless/incorporeal)"),
    "arūpa":            ("incorporeal",       "arūpa (formless/incorporeal)"),
    "nāma":             ("name",              "nāma (name/mentality)"),

    # ── Consciousness ─────────────────────────────────────────────────────────
    "viññāṇa":          ("consciousness",     "viññāṇa (sense-consciousness)"),
    "viññeyyā":         ("cognition",         "viññeyya (cognisable)"),
    "citta":            ("mind",              "citta (mind/consciousness)"),
    "mano":             ("mind",              "mano (mind-base)"),

    # ── Sense bases & faculties ───────────────────────────────────────────────
    "āyatana":          ("sphere",            "āyatana (sense-sphere/base)"),
    "indriya":          ("faculty",           "indriya (faculty/sense-organ)"),
    "cakkhu":           ("eye",               "cakkhu (eye-faculty)"),
    "sota":             ("ear",               "sota (ear-faculty)"),
    "ghāna":            ("nose",              "ghāna (nose-faculty)"),
    "jivhā":            ("tongue",            "jivhā (tongue-faculty)"),
    "kāya":             ("body",              "kāya (body)"),
    "kāyika":           ("bodily",            "kāyika (bodily)"),

    # ── Elements (dhātu) ──────────────────────────────────────────────────────
    "dhātu":            ("element",           "dhātu (element)"),
    "pathavī":          ("earth",             "pathavī (earth-element)"),
    "āpo":              ("water",             "āpo (water-element)"),
    "tejo":             ("fire",              "tejo (fire-element)"),
    "vāyo":             ("air",               "vāyo (air-element)"),

    # ── Jhāna / Meditation ────────────────────────────────────────────────────
    "jhāna":            ("jhāna",             "jhāna (meditative absorption)"),
    "samatha":          ("calm",              "samatha (tranquillity)"),
    "vipassanā":        ("insight",           "vipassanā (insight)"),
    "samāpatti":        ("attainment",        "samāpatti (meditative attainment)"),

    # ── Āsava (cankers/intoxicants) ───────────────────────────────────────────
    "āsavā":            ("āsavas",            "āsava (canker/intoxicant)"),
    "āsava":            ("āsava",             "āsava (canker/intoxicant)"),
    "sāsavā":           ("with cankers",      "sāsava (with cankers)"),
    "anāsavā":          ("without cankers",   "anāsava (without cankers)"),
    "āsavasampayuttā":  ("associated with cankers","āsavasampayutta (associated with cankers)"),
    "āsavavippayuttā":  ("dissociated from cankers","āsavavippayutta (dissociated from cankers)"),

    # ── Fetters (saṃyojanā) ───────────────────────────────────────────────────
    "saṃyojanā":        ("fetters",           "saṃyojana (fetter)"),
    "saṃyojana":        ("fetters",           "saṃyojana (fetter)"),
    "saṃyojaniyā":      ("liable to fettering","saṃyojaniya (to be fettered)"),
    "asaṃyojaniyā":     ("not liable to fettering","asaṃyojaniya (not liable to fettering)"),

    # ── Knots (ganthā) ────────────────────────────────────────────────────────
    "ganthā":           ("ties",              "gantha (tie/knot)"),
    "ganthaniyā":       ("to be tied",        "ganthaniya (liable to knotting)"),

    # ── Floods (oghā) & Bonds (yogā) ─────────────────────────────────────────
    "oghā":             ("floods",            "ogha (flood)"),
    "yogā":             ("bonds",             "yoga (bond)"),

    # ── Views (diṭṭhi) ────────────────────────────────────────────────────────
    "diṭṭhi":           ("views",             "diṭṭhi (view/opinion)"),
    "micchādiṭṭhi":     ("wrong views",       "micchādiṭṭhi (wrong view)"),
    "sammādiṭṭhi":      ("right view",        "sammādiṭṭhi (right view)"),
    "diṭṭhigata":       ("wrong view",        "diṭṭhigata (fallen into views)"),
    "diṭṭhisampayutta": ("associated with views","diṭṭhisampayutta (associated with views)"),

    # ── Ethical quality of action ─────────────────────────────────────────────
    "micchatta":        ("wrong",             "micchatta (wrong-ness)"),
    "micchattaniyatā":  ("fixed in wrong",    "micchattaniyata (fixed in wrong path)"),
    "sammatta":         ("right",             "sammatta (right-ness)"),
    "sammattaniyatā":   ("fixed in right",    "sammattaniyata (fixed in right path)"),
    "aniyatā":          ("unfixed",           "aniyata (unfixed/undetermined)"),

    # ── Path (magga) ──────────────────────────────────────────────────────────
    "magga":            ("path",              "magga (path)"),
    "maggārammaṇā":     ("having path as object","maggārammaṇa (path-object)"),
    "maggahetukā":      ("with path as cause","maggahetuka (path-caused)"),
    "maggādhipatino":   ("with path as predominance","maggādhipati (path-predominance)"),
    "sammāsati":        ("right mindfulness", "sammāsati (right mindfulness)"),

    # ── Conditioned/Unconditioned ─────────────────────────────────────────────
    "sappaccayā":       ("causally conditioned","sappaccaya (with condition)"),
    "appaccayā":        ("uncaused",          "appaccaya (without condition)"),
    "saṅkhatā":         ("conditioned",       "saṅkhata (conditioned/compounded)"),
    "asaṅkhatā":        ("unconditioned",     "asaṅkhata (unconditioned/uncompounded)"),

    # ── Visible/Invisible ─────────────────────────────────────────────────────
    "sanidassanā":      ("visible",           "sanidassana (visible/with-showing)"),
    "anidassanā":       ("invisible",         "anidassana (invisible/without-showing)"),
    "sanidassanasappaṭighā": ("visible and impingent","sanidassanasappaṭigha (visible and impingent)"),
    "anidassanasappaṭighā": ("invisible and impingent","anidassanasappaṭigha (invisible and impingent)"),
    "anidassanaappaṭighā": ("invisible and non-impingent","anidassanāppaṭigha (invisible and non-impingent)"),

    # ── Resistance ────────────────────────────────────────────────────────────
    "sappaṭighā":       ("reacting",          "sappaṭigha (impingent/with-resistance)"),
    "appaṭighā":        ("non-reacting",      "appaṭigha (non-impingent/without-resistance)"),

    # ── Mundane/Supramundane ──────────────────────────────────────────────────
    "lokiyā":           ("worldly",           "lokiya (mundane/worldly)"),
    "lokuttarā":        ("supramundane",      "lokuttara (supramundane/transcendent)"),
    "loka":             ("world",             "loka (world)"),

    # ── Temporal classification ───────────────────────────────────────────────
    "uppannā":          ("arisen",            "uppanna (arisen/present)"),
    "anuppannā":        ("not yet arisen",    "anuppanna (not yet arisen)"),
    "uppādino":         ("about to arise",    "uppādi (about to arise)"),
    "atītā":            ("past",              "atīta (past)"),
    "anāgatā":          ("future",            "anāgata (future)"),
    "paccuppannā":      ("present",           "paccuppanna (present)"),
    "atītārammaṇā":     ("having past as object","atītārammaṇa (past-object)"),
    "anāgatārammaṇā":   ("having future as object","anāgatārammaṇa (future-object)"),
    "paccuppannārammaṇā":("having present as object","paccuppannārammaṇa (present-object)"),

    # ── Internal/External ────────────────────────────────────────────────────
    "ajjhattā":         ("personal",          "ajjhatta (personal/internal)"),
    "bahiddhā":         ("external",          "bahiddhā (external)"),
    "ajjhattabahiddhā": ("personal and external","ajjhattabahiddhā (internal-and-external)"),
    "ajjhattārammaṇā":  ("personal object",   "ajjhattārammaṇa (internal-object)"),
    "bahiddhārammaṇā":  ("external object",   "bahiddhārammaṇa (external-object)"),

    # ── Object range ─────────────────────────────────────────────────────────
    "parittā":          ("of limited sphere", "paritta (limited/small)"),
    "mahaggatā":        ("exalted",           "mahaggata (exalted/high)"),
    "appamāṇā":         ("measureless",       "appamāṇa (measureless)"),
    "parittārammaṇā":   ("having limited object","parittārammaṇa (limited-object)"),
    "mahaggatārammaṇā": ("having exalted object","mahaggatārammaṇa (exalted-object)"),
    "appamāṇārammaṇā":  ("having measureless object","appamāṇārammaṇa (measureless-object)"),

    # ── Quality ───────────────────────────────────────────────────────────────
    "hīnā":             ("low",               "hīna (inferior/low)"),
    "majjhimā":         ("middling",          "majjhima (middling)"),
    "paṇītā":           ("excellent",         "paṇīta (excellent/sublime)"),

    # ── Learner/Adept ─────────────────────────────────────────────────────────
    "sekkhā":           ("of the learner",    "sekkha (learner/in-training)"),
    "asekkhā":          ("of the adept",      "asekkha (non-learner/adept)"),

    # ── Grasped/Ungrasped ────────────────────────────────────────────────────
    "upādiṇṇupādāniyā": ("grasped at",        "upādiṇṇupādāniya (grasped and liable to grasping)"),
    "anupādiṇṇupādāniyā":("not grasped at",   "anupādiṇṇupādāniya (not grasped but liable)"),
    "anupādiṇṇaanupādāniyā":("not grasped and not liable","anupādiṇṇānupādāniya (not grasped and not liable)"),
    "upādāna":          ("grasp",             "upādāna (grasping/clinging)"),

    # ── Defilement ────────────────────────────────────────────────────────────
    "saṃkiliṭṭhasaṃkilesikā": ("defiled",     "saṃkiliṭṭhasaṃkilesika (defiled and defiling)"),
    "asaṃkiliṭṭhasaṃkilesikā":("undefiled",   "asaṃkiliṭṭhasaṃkilesika (undefiled but defiling)"),
    "asaṃkiliṭṭhaasaṃkilesikā":("undefiled and non-defiling","asaṃkiliṭṭhāsaṃkilesika (undefiled and non-defiling)"),
    "kilesa":           ("evil",              "kilesa (defilement)"),
    "lobha":            ("covetousness",      "lobha (greed/covetousness)"),
    "dosa":             ("hatred",            "dosa (hatred/ill-will)"),
    "moha":             ("delusion",          "moha (delusion/ignorance)"),
    "māna":             ("conceit",           "māna (conceit/pride)"),
    "avijjā":           ("ignorance",         "avijjā (ignorance)"),

    # ── Root conditions (hetu) ────────────────────────────────────────────────
    "hetū":             ("cause",             "hetu (root/cause)"),
    "hetu":             ("cause",             "hetu (root/cause)"),
    "sahetukā":         ("with root",         "sahetuka (with causal root)"),
    "ahetukā":          ("without root",      "ahetuka (without causal root)"),
    "hetusampayuttā":   ("conjoined with root","hetusampayutta (root-conjoined)"),
    "hetuvippayuttā":   ("disjoined from root","hetuvippayutta (root-disjoined)"),

    # ── Arising/Cessation ────────────────────────────────────────────────────
    "uppāda":           ("arising",           "uppāda (arising)"),
    "nirodha":          ("cessation",         "nirodha (cessation)"),
    "nibbāna":          ("nirvana",           "nibbāna (extinction/nirvāṇa)"),
    "ācayagāmino":      ("making for growth", "ācayagāmin (accumulation-going)"),
    "apacayagāmino":    ("making for diminution","apacayagāmin (diminution-going)"),
    "nevācayagāmināpacayagāmino": ("neither making for growth nor diminution",
                                    "nevācayagāminā (neither accumulation nor diminution)"),

    # ── Training / Samaya ────────────────────────────────────────────────────
    "samaya":           ("occasion",          "samaya (occasion/time)"),
    "samaye":           ("at the time of",    "samaya (occasion/time)"),
    "dassanena":        ("by vision",         "dassana (vision/seeing)"),
    "bhāvanāya":        ("by development",    "bhāvanā (meditation/development)"),
    "pahātabbā":        ("to be abandoned",   "pahātabba (to be abandoned)"),
    "pahātabbahetukā":  ("caused by what is to be abandoned",
                         "pahātabbahetuka (abandon-caused)"),

    # ── Absorption levels ────────────────────────────────────────────────────
    "paṭhamajjhāna":    ("first jhāna",       "paṭhamajjhāna (first absorption)"),
    "dutiyajjhāna":     ("second jhāna",      "dutiyajjhāna (second absorption)"),
    "tatiyajjhāna":     ("third jhāna",       "tatiyajjhāna (third absorption)"),
    "catutthajjhāna":   ("fourth jhāna",      "catutthajjhāna (fourth absorption)"),

    # ── Sampayutta / Vippayutta ───────────────────────────────────────────────
    "sampayuttā":       ("associated",        "sampayutta (associated/conjoined)"),
    "sampayutta":       ("associated",        "sampayutta (associated/conjoined)"),
    "vippayuttā":       ("dissociated",       "vippayutta (dissociated)"),
    "vippayutta":       ("dissociated",       "vippayutta (dissociated)"),
    "sahagatā":         ("accompanied by",    "sahagata (accompanied by)"),
    "sahagata":         ("accompanied by",    "sahagata (accompanied by)"),

    # ── Nutriment ────────────────────────────────────────────────────────────
    "āhāra":            ("nutriment",         "āhāra (nutriment/food)"),

    # ── Remaining afflictions ─────────────────────────────────────────────────
    "taṇhā":            ("craving",           "taṇhā (craving/thirst)"),
    "bhava":            ("life",              "bhava (existence/becoming)"),
    "jāti":             ("birth",             "jāti (birth)"),
    "jarā":             ("decay",             "jarā (decay/old age)"),
    "maraṇa":           ("death",             "maraṇa (death)"),

    # ── Wholesome roots ───────────────────────────────────────────────────────
    "alobha":           ("absence of covetousness","alobha (non-greed)"),
    "adosa":            ("absence of hatred", "adosa (non-hatred)"),
    "amoha":            ("absence of delusion","amoha (non-delusion)"),

    # ── Path factors ─────────────────────────────────────────────────────────
    "sammāsaṅkappa":    ("right intentions",  "sammāsaṅkappa (right intention)"),
    "sammāvācā":        ("right speech",      "sammāvācā (right speech)"),
    "sammākammanta":    ("right action",      "sammākammanta (right action)"),
    "sammāājīva":       ("right livelihood",  "sammāājīva (right livelihood)"),
    "sammāvāyāma":      ("right endeavour",   "sammāvāyāma (right effort)"),

    # ── Material form subtypes ────────────────────────────────────────────────
    "oḷārika":          ("gross",             "oḷārika (gross/coarse material form)"),
    "sukhumā":          ("subtle",            "sukhumā (subtle)"),
    "dūre":             ("far",               "dūra (far)"),
    "santike":          ("near",              "santika (near/proximate)"),
    "ajjhatta":         ("personal",          "ajjhatta (personal/internal)"),
    "bahiddha":         ("external",          "bahiddhā (external)"),

    # ── Specific senses ────────────────────────────────────────────────────────
    "vaṇṇa":            ("shape",             "vaṇṇa (colour/shape)"),
    "sadda":            ("sound",             "sadda (sound)"),
    "gandha":           ("smell",             "gandha (smell/odour)"),
    "rasa":             ("taste",             "rasa (taste)"),
    "phoṭṭhabba":       ("tangible",          "phoṭṭhabba (tangible object)"),

    # ── Cognitive process ─────────────────────────────────────────────────────
    "manasikāra":       ("attention",         "manasikāra (attention/mental adverting)"),
    "chanda":           ("intention",         "chanda (intention/wish)"),
    "appanā":           ("application",       "appanā (full absorption)"),
    "vīmaṃsā":          ("investigation",     "vīmaṃsā (investigation)"),

    # ── Special character qualities ───────────────────────────────────────────
    "hirī":             ("moral shame",       "hirī (moral shame)"),
    "ottappa":          ("moral dread",       "ottappa (moral dread)"),
    "ahirika":          ("absence of shame",  "ahirika (absence of moral shame)"),
    "anottappa":        ("absence of dread",  "anottappa (absence of moral dread)"),
    "tatramajjhattatā": ("balance",           "tatramajjhattatā (mental balance/equanimity)"),

    # ── Bojjhaṅgā ────────────────────────────────────────────────────────────
    "bojjhaṅgā":        ("factors of enlightenment","bojjhaṅga (enlightenment factor)"),
    "bojjhaṅga":        ("factors of enlightenment","bojjhaṅga (enlightenment factor)"),
    "dhammavicaya":     ("investigation of states","dhammavicaya (investigation of Dhamma)"),
    "passaddhi":        ("serenity",          "passaddhi (serenity/calming)"),
    "upekkhā":          ("balance",           "upekkhā (equanimity/indifference)"),

    # ── Indriyā ──────────────────────────────────────────────────────────────
    "paññindriya":      ("intuition",         "paññindriya (wisdom-faculty)"),
    "samādhindriya":    ("concentration",     "samādhindriya (concentration-faculty)"),
    "satindriya":       ("mindfulness",       "satindriya (mindfulness-faculty)"),
    "viriyindriya":     ("energy",            "viriyindriya (energy-faculty)"),
    "saddhindriya":     ("faith",             "saddhindriya (faith-faculty)"),

    # ── Iddhipādā ────────────────────────────────────────────────────────────
    "iddhipādā":        ("bases of psychic power","iddhipāda (basis of psychic power)"),
    "iddhipāda":        ("bases of psychic power","iddhipāda (basis of psychic power)"),
}

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class TermEntry:
    """One row from the rhys_davids_termbase.md Full Ranked Table."""
    word:   str
    rank:   int
    count:  int
    score:  float
    idf:    float
    band:   str


@dataclass
class PaliEntry:
    """Occurrences of a Pāli token in pi-1.md."""
    token:     str
    lines:     list[int] = field(default_factory=list)
    block_ids: list[str] = field(default_factory=list)

    @property
    def first_line(self) -> int:
        return self.lines[0] if self.lines else 0


# ---------------------------------------------------------------------------
# Step 1 — Parse the Full Ranked Table from rhys_davids_termbase.md
# ---------------------------------------------------------------------------
# Table row format:
#   | 1 | **states** | 743 | 100,449.04 | 2.8 | 🔴 extremely high — text-exclusive |
# ---------------------------------------------------------------------------
_TB_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*([\d,]+)\s*\|\s*([\d,\.]+)\s*\|\s*([\d\.]+)\s*\|\s*(.+?)\s*\|$"
)

def parse_termbase(path: pathlib.Path) -> dict[str, TermEntry]:
    entries: dict[str, TermEntry] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _TB_ROW.match(line.strip())
        if m:
            rank  = int(m.group(1))
            word  = m.group(2).strip().lower()
            count = int(m.group(3).replace(",", ""))
            score = float(m.group(4).replace(",", ""))
            idf   = float(m.group(5))
            band  = m.group(6).strip()
            entries[word] = TermEntry(word=word, rank=rank, count=count,
                                      score=score, idf=idf, band=band)
    return entries


# ---------------------------------------------------------------------------
# Step 2 — Parse the Pāli root text, extracting tokens with line numbers
# ---------------------------------------------------------------------------
# Only retain tokens that:
#   - are at least 4 characters long
#   - are not in PALI_STOP
#   - are not pure-ASCII common English words (editorial markers)
# ---------------------------------------------------------------------------
_PURE_ASCII = re.compile(r"^[a-zA-Z]+$")

_EN_EDITORIAL: set[str] = {
    "and", "or", "not", "the", "of", "in", "for", "by", "with",
    "from", "into", "etc", "see", "cf", "ed", "ibid", "op", "cit",
    "vol", "pp", "also", "note", "comp", "lit",
}

def is_pali_token(tok: str) -> bool:
    """True if the token looks like a Pāli word worth keeping."""
    if len(tok) < 4:
        return False
    lower = tok.lower()
    if lower in PALI_STOP:
        return False
    if _PURE_ASCII.match(tok) and lower in _EN_EDITORIAL:
        return False
    return True


def parse_pali_root(path: pathlib.Path) -> dict[str, PaliEntry]:
    entries: dict[str, PaliEntry] = defaultdict(lambda: PaliEntry(token=""))
    current_block: str | None = None

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        # skip frontmatter and markdown headings
        if raw.startswith("---") or raw.startswith("#"):
            continue

        # extract block ID on this line (may be at end of line)
        block_match = _BLOCK_ID.search(raw)
        if block_match:
            current_block = block_match.group(1)

        # tokenize Pāli words from the line
        for tok in _PI_TOKEN.findall(raw):
            lower = tok.lower()
            if not is_pali_token(lower):
                continue
            if lower not in entries:
                entries[lower] = PaliEntry(token=lower)
            entry = entries[lower]
            entry.lines.append(lineno)
            if current_block and current_block not in entry.block_ids:
                entry.block_ids.append(current_block)

    return dict(entries)


# ---------------------------------------------------------------------------
# Step 3 — Build the mapping rows
# ---------------------------------------------------------------------------

@dataclass
class MapRow:
    pali_token:    str
    sense_tag:     str
    en_rendering:  str
    tb_rank:       int | None        # rank in termbase, or None
    tb_count:      int | None
    tb_score:      float | None
    tb_band:       str
    first_line:    int
    line_count:    int
    block_ids:     list[str]


def build_mapping(
    termbase: dict[str, TermEntry],
    pali_entries: dict[str, PaliEntry],
    pali_dict: dict[str, tuple[str, str]],
) -> list[MapRow]:
    rows: list[MapRow] = []

    for token, pi_entry in pali_entries.items():
        if token not in pali_dict:
            continue  # only include tokens with a known mapping

        en_rendering, sense_tag = pali_dict[token]

        # look up the English rendering in the termbase
        tb = termbase.get(en_rendering.lower())
        if tb is None:
            # try singular/plural variants
            for variant in (en_rendering + "s", en_rendering.rstrip("s"),
                            en_rendering.rstrip("es")):
                tb = termbase.get(variant.lower())
                if tb:
                    break

        rows.append(MapRow(
            pali_token   = token,
            sense_tag    = sense_tag,
            en_rendering = en_rendering,
            tb_rank      = tb.rank  if tb else None,
            tb_count     = tb.count if tb else None,
            tb_score     = tb.score if tb else None,
            tb_band      = tb.band  if tb else "—",
            first_line   = pi_entry.first_line,
            line_count   = len(pi_entry.lines),
            block_ids    = pi_entry.block_ids,
        ))

    # sort by first appearance in pi-1.md
    rows.sort(key=lambda r: r.first_line)
    return rows


# ---------------------------------------------------------------------------
# Step 4 — Render output markdown
# ---------------------------------------------------------------------------

def fmt_rank(r: MapRow) -> str:
    return str(r.tb_rank) if r.tb_rank is not None else "—"

def fmt_score(r: MapRow) -> str:
    return f"{r.tb_score:,.0f}" if r.tb_score is not None else "—"

def fmt_count(r: MapRow) -> str:
    return str(r.tb_count) if r.tb_count is not None else "—"

def fmt_blocks(r: MapRow, limit: int = 5) -> str:
    ids = r.block_ids[:limit]
    tail = f" +{len(r.block_ids) - limit} more" if len(r.block_ids) > limit else ""
    return " · ".join(f"^{b}" for b in ids) + tail

def fmt_band_short(band: str) -> str:
    """Strip the prose description, keep only the emoji + label."""
    # e.g. "🟠 very high — domain-specific" → "🟠 domain-specific"
    parts = band.split("—")
    if len(parts) == 2:
        emoji_label = parts[0].strip().split()
        emoji = emoji_label[0] if emoji_label else ""
        return f"{emoji} {parts[1].strip()}"
    return band


def render_md(rows: list[MapRow], termbase: dict[str, TermEntry],
              termbase_count: int, pali_count: int) -> str:
    today   = date.today().isoformat()
    matched = len(rows)
    L: list[str] = []

    # ── Frontmatter ─────────────────────────────────────────────────────────
    L += [
        "---",
        "title: Pāli–English Term Map — Dhammasaṅgaṇī × Rhys Davids Termbase",
        "source_pali: 1-SOURCES/Text/pi-1.md",
        "source_english: 3-TRANSFORMATIONS/Plans/Daily-Tipitaka/en/rhys_davids_termbase.md",
        "method: token-level Pāli→English mapping with sense tags and TF-IDF cross-reference",
        f"generated: {today}",
        f"pali_tokens_scanned: {pali_count}",
        f"termbase_terms: {termbase_count}",
        f"mapped_pali_terms: {matched}",
        "status: draft",
        "---",
        "",
    ]

    # ── Title ────────────────────────────────────────────────────────────────
    L += [
        "# Pāli–English Term Map — Dhammasaṅgaṇī × Rhys Davids Termbase",
        "",
        f"Generated **{today}** · **{matched} Pāli terms** mapped, sorted by first line of appearance"
        f" in `pi-1.md`.",
        "",
        "## How to read this table",
        "",
        "| Column | Meaning |",
        "|--------|---------|",
        "| **Pāli Term** | Token as found in `pi-1.md` (lowercase, IAST) |",
        "| **Sense Tag** | Local-Wiki sense ID: `lemma (disambiguating phrase)` |",
        "| **Rhys Davids rendering** | English word as used in the 1900 translation |",
        "| **Termbase rank** | Rank in `rhys_davids_termbase.md` (1 = most distinctive) |",
        "| **EN count** | Raw count of the English word in the translation |",
        "| **TF-IDF** | TF × IDF × 10⁶ — how distinctive the word is in this translation |",
        "| **Band** | Distinctiveness band (🔴 = text-exclusive … ⚪ = universal) |",
        "| **First line** | Line number of first occurrence in `pi-1.md` |",
        "| **Occurrences** | Total number of lines where the Pāli token appears |",
        "| **Block IDs** | First five block anchors (`^1-1` …) where the token appears |",
        "",
        "---",
        "",
    ]

    # ── Table ────────────────────────────────────────────────────────────────
    L += [
        "## Mapped Terms",
        "",
        "| Pāli Term | Sense Tag | Rhys Davids rendering | Rank | EN count | TF-IDF | Band | First line | Occurrences | Block IDs |",
        "|-----------|-----------|----------------------|------|----------|--------|------|------------|-------------|-----------|",
    ]
    for r in rows:
        band_short = fmt_band_short(r.tb_band) if r.tb_band != "—" else "—"
        blocks_str = fmt_blocks(r)
        L.append(
            f"| `{r.pali_token}` | {r.sense_tag} | {r.en_rendering} "
            f"| {fmt_rank(r)} | {fmt_count(r)} | {fmt_score(r)} | {band_short} "
            f"| {r.first_line} | {r.line_count} | {blocks_str} |"
        )

    L += ["", "---", ""]

    # ── Ranked by IDF (most domain-exclusive first) ──────────────────────────
    tb_rows = [r for r in rows if r.tb_rank is not None]
    # primary sort: IDF descending (highest = most rare in general English)
    # secondary sort: TF-IDF rank ascending (most distinctive within the text)
    tb_rows_idf = sorted(
        tb_rows,
        key=lambda r: (-(termbase.get(r.en_rendering.lower(),
                          TermEntry("", 0, 0, 0.0, 1.0, "")).idf),
                       r.tb_rank or 9999),
    )

    L += [
        "## Mapped Terms by IDF (domain-exclusivity)",
        "",
        "Only the **{} Pāli terms** whose English rendering appears in the Rhys Davids termbase, "
        "sorted by IDF descending (most domain-exclusive / rarest in general English first).".format(len(tb_rows_idf)),
        "",
        "| # | Pāli Term | Sense Tag | Rhys Davids rendering | IDF | TF-IDF rank | TF-IDF score | Band |",
        "|---|-----------|-----------|----------------------|-----|-------------|--------------|------|",
    ]
    for i, r in enumerate(tb_rows_idf, 1):
        te = termbase.get(r.en_rendering.lower())
        idf_val = f"{te.idf}" if te else "—"
        band_short = fmt_band_short(r.tb_band)
        L.append(
            f"| {i} | `{r.pali_token}` | {r.sense_tag} | {r.en_rendering} "
            f"| {idf_val} | {fmt_rank(r)} | {fmt_score(r)} | {band_short} |"
        )

    L += ["", "---", ""]

    # ── Summary by TF-IDF band ────────────────────────────────────────────────
    band_groups: dict[str, list[MapRow]] = defaultdict(list)
    no_tb: list[MapRow] = []
    for r in rows:
        if r.tb_rank is None:
            no_tb.append(r)
        else:
            band_groups[r.tb_band].append(r)

    # order: highest first
    band_order = [
        "🔴 extremely high — text-exclusive",
        "🟠 very high — domain-specific",
        "🟡 high — specialist register",
        "🟢 medium — moderately distinctive",
        "🔵 low — common in general English",
        "⚪ very low — function / universal word",
    ]

    L += [
        "## Summary by TF-IDF Band",
        "",
        "| Band | Mapped Pāli terms | Examples |",
        "|------|-------------------|---------|",
    ]
    for band_label in band_order:
        group = band_groups.get(band_label, [])
        if not group:
            continue
        examples = ", ".join(f"`{r.pali_token}`" for r in group[:5])
        if len(group) > 5:
            examples += f" …+{len(group)-5}"
        L.append(f"| {band_label} | {len(group)} | {examples} |")
    if no_tb:
        ex = ", ".join(f"`{r.pali_token}`" for r in no_tb[:5])
        if len(no_tb) > 5:
            ex += f" …+{len(no_tb)-5}"
        L.append(f"| *(Pāli word used directly — not in EN termbase)* | {len(no_tb)} | {ex} |")

    L += ["", "---", ""]

    # ── Sense-tag index ───────────────────────────────────────────────────────
    L += [
        "## Sense-Tag Index",
        "",
        "Pāli sense tags, alphabetically. Use these as Local-Wiki article headings.",
        "",
    ]
    seen: set[str] = set()
    for r in sorted(rows, key=lambda r: r.sense_tag):
        tag = r.sense_tag
        if tag not in seen:
            seen.add(tag)
            L.append(f"- **{tag}** → *{r.en_rendering}* (first at line {r.first_line})")

    L += [
        "",
        "---",
        "",
        f"*Generated {today} by `compare_pali_termbase.py`.*  ",
        f"*Sources: `1-SOURCES/Text/pi-1.md` · `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/en/rhys_davids_termbase.md`.*",
    ]

    return "\n".join(L)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    for p, label in [(TERMBASE, "Termbase"), (PALI_ROOT, "Pāli root text")]:
        if not p.exists():
            raise FileNotFoundError(f"{label} not found:\n  {p}")

    print(f"Reading termbase  …  {TERMBASE.name}")
    termbase = parse_termbase(TERMBASE)
    print(f"  {len(termbase):,} English terms loaded")

    print(f"Reading root text …  {PALI_ROOT.name}")
    pali_entries = parse_pali_root(PALI_ROOT)
    print(f"  {len(pali_entries):,} unique Pāli tokens extracted")

    print("Building mapping  …")
    rows = build_mapping(termbase, pali_entries, PALI_DICT)
    print(f"  {len(rows):,} Pāli terms mapped to English renderings")

    md = render_md(rows, termbase, len(termbase), len(pali_entries))
    OUTPUT.write_text(md, encoding="utf-8")
    print(f"Written  → {OUTPUT}")

    # brief coverage report
    with_tb  = sum(1 for r in rows if r.tb_rank is not None)
    without  = len(rows) - with_tb
    print(f"\nCoverage")
    print(f"  {with_tb:>4} Pāli terms found in the English termbase")
    print(f"  {without:>4} Pāli terms mapped (sense tag) but English word not in termbase")


if __name__ == "__main__":
    main()
