# Create and upload Daily Tipitaka days

How to generate the next batch of Daily Tipitaka day files and upload them into WeBuddhist Studio.

## Set up the skill (one-time)

Open a Cowork session in Claude with the `abhidhamma-rails` vault selected as the working folder. Ask Claude to install the `daily-tipitaka-day` skill — for example:

> Please install the daily-tipitaka-day skill.

Claude will fetch it and confirm. You only do this once per computer.

## 1. Find the next days to generate

Open `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/` and note the highest-numbered day file. Then open `<lang>/schedule.md` to see the next dates and verse ranges.

Pick the next 5 days.

## 2. Run the skill

In Claude, ask:

> Use `/daily-tipitaka-day` to create days N–M in `<lang>`.

For example: `days 19–23 in en`.

Claude writes two files per day:

- `0-INBOX/daily-tipitaka/day-NNN-assets.md` — working file with the full verse range, summary, practice notes, and English translation.
- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` — the draft day file.

It also appends new term renderings to `<lang>/termbase.md` as `candidate` rows.

## 3. Review and edit

Open each new day file and read it. Edit anything that needs tightening — register, tone, word choice. Promote or correct termbase rows as needed.

## 4. Upload to WeBuddhist Studio

Create the day in Studio. Use the day file for the variable content and the block below for the fixed content.

**From the day file, copy:**

- §1 → 🧭 Today's Chanting Guide
- §5 → 🔑 Pāli Word of the Day
- §8 → app notification (title, body, button)

**For the passage sections (💡 Reading for Meaning and ☸️ Chanting in Pali):** the day file prints the first and last verses only. Use those to find the span in Studio's verse library. If a phrase has many matches, open the day's assets file in `0-INBOX/daily-tipitaka/` — it holds the full range with surrounding context (subsection headings, citta numbers, closing seals) to disambiguate.

**Fixed content — paste into every day:**

Section titles:

```
🧭 Today's Chanting Guide
🪔 Homage
🌱 Intention
💡 Reading for Meaning
🔑 Pāli Word of the Day
☸️ Chanting in Pali
✨ Aspiration
```

🪔 Homage:

```
NAMO TASSA BHAGAVATO ARAHATO SAMMĀ SAMBUDDHASSA

Homage to him, the Blessed One, the Perfect One, the Supremely Enlightened One.

BUDDHAṂ VANDĀMI, DHAMMAṂ VANDĀMI,
SAṄGHAṂ VANDĀMI, AHAṂ VANDĀMI SABBADĀ.

I pay homage to the Buddha, to the Dhamma, to the Sangha — always.

DUTIYAMPI BUDDHAṂ VANDĀMI, DHAMMAṂ VANDĀMI,
SAṄGHAṂ VANDĀMI, AHAṂ VANDĀMI SABBADĀ.

For the second time, I pay homage to the Buddha, to the Dhamma, to the Sangha — always.

TATIYAMPI BUDDHAṂ VANDĀMI, DHAMMAṂ VANDĀMI,
SAṄGHAṂ VANDĀMI, AHAṂ VANDĀMI SABBADĀ.

For the third time, I pay homage to the Buddha, to the Dhamma, to the Sangha — always.
```

🌱 Intention:

```
SABBAPĀPASSA AKARAṆAṂ
KUSALASSA UPASAMPADĀ
SACITTAPARIYODAPANAṂ
ETAṂ BUDDHĀNA SĀSANAṂ

To avoid all evil.
To cultivate what is good.
To purify the mind.
This is the teaching of the Buddhas.
```

✨ Aspiration:

```
IMINĀ PUÑÑAKAMMENA,
MĀ ME BĀLA-SAMĀGAMO;
SATAṂ SAMĀGAMO HOTU,
YĀVA NIBBĀNAPATTIYĀ.

By the power of this meritorious deed,
May I not suffer the company of unwise people.
May I be blessed with the company of wise people,
Until deliverance is won!

IDAṂ ME PUÑÑA KAMMAṂ
ĀSAVAKKHAYAṂ VAHAṂ HOTU
SABBADUKKHĀ PAMUCCATU
NIBBĀNASSA PACCAYO HOTU!

May this meritorious deed of mine
Conduce to the destruction of cankers,
And lead to freedom from all suffering,
May it be a condition for spiritual Liberation!

SĀDHU! SĀDHU! SĀDHU! 🙏
```

## 5. Clean up

Once a day is uploaded and confirmed in Studio, delete that day's assets file from `0-INBOX/daily-tipitaka/`.

## Feedback

If the skill output needs adjusting — register, structure, anything — tell Evan so the skill can be updated.
