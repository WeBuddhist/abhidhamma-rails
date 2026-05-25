# Create and upload Daily Tipitaka days

How to generate the next batch of Daily Tipitaka day files and upload them into WeBuddhist Studio.

## Prerequisite: Set up the skill

1. Open a Cowork session in Claude with the `abhidhamma-rails` vault selected as the working folder.
2. Ask Claude to install the `daily-tipitaka-day` skill — for example:
	> Please install the daily-tipitaka-day skill.
3. After Claude sets up the skill,  click **Save Skill** to install it.

## 1. Find the next days to generate

Open `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/` and note the highest-numbered day file

## 2. Run the skill

1. In Claude, ask:

	> Use `/daily-tipitaka-day` to create days the next five days in `<lang>`.

	For example: `days 19–23 in en`. (Note: If you quickly use up your tokens for a time period, pick fewer.)

2. Wait for Claude to finish. It writes two files per day:

	- `0-INBOX/daily-tipitaka/day-NNN-assets.md` — working file with the full verse range, summary, practice notes, and English translation.
	- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` — the draft day file.

	It also appends new term renderings to `<lang>/termbase.md` as `candidate` rows.

## 3. Review and edit

1. Open each new day file and read it.
2. Edit anything that needs tightening — tone, style, word choice.
3. Check the new `candidate` rows the skill added to `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/termbase.md` and confirm, correct, or promote them.
4. Cross-check against the upstream translation-track lock at `3-TRANSFORMATIONS/Translations/<lang>-<TrackName>/termbase.md` (for English: `en-Contemporary-English-Abhidhamma`) when needed.

## 4. Upload to WeBuddhist Studio

Create the day in Studio. The content has three parts to add:
- Fixed content (same every day)
- Today's Chanting Guide and Pāli Word of the Day from the abhidhamma-rails day file
-  Reading for Meaning and Chanting in Pali from Studio's verse library.
### 4a. Paste the fixed content

These blocks go into every day. Section titles:

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

### 4b. Paste the prose from the day file

Open the new day file in `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` and copy:

- §1 → 🧭 Today's Chanting Guide
- §5 → 🔑 Pāli Word of the Day
- §8 → app notification (title, body, button). The app notification is coming soon to Studio. For now, update and copy into the notifications tab of [this sheet](https://docs.google.com/spreadsheets/d/1YU2X3KkjPdmPZ7fPYIBIUHSoxo9z15ObLcwhaigs7pg/edit?gid=951664328#gid=951664328).

### 4c. Pick the verse spans from Studio's verse library

The day file prints only the first and last verses for 💡 Reading for Meaning and ☸️ Chanting in Pali. Use those two verses to pick the span in Studio.

1. Find the first verse in Studio's verse library and mark the start of the span.
2. Find the last verse and mark the end of the span.
3. If a search returns more than one match — the Abhidhamma is very repetitive — open the day's assets file in `0-INBOX/daily-tipitaka/`. The assets file holds the whole range with the headings, citta numbers, and closing seals around it, so you can see which match is the right one.

## 5. Clean up

Once a day is uploaded and confirmed in Studio, delete that day's assets file from `0-INBOX/daily-tipitaka/`.

## Feedback

If the skill output needs adjusting — tone, structure, anything — tell Evan so the skill can be updated.
