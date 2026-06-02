---
title: TF-IDF Vocabulary Analysis — Rhys Davids Dhammasaṅgaṇī (1900)
source: 1-SOURCES/Translations/en-1-rhys_davids.md
corpus: BNC (100 M words) · COCA (450 M words) · General Service List (West 1953)
method: TF × IDF — term frequency in translation vs. inverse document frequency in general English
generated: 2026-06-02
unique_terms: 2247
total_content_tokens: 20,711
status: draft
---

# TF-IDF Vocabulary Analysis — Rhys Davids Translation

Generated **2026-06-02** · source: `en-1-rhys_davids.md` · **2,247 unique content terms** ranked.

This report answers two questions:

1. **Which words in this translation are most frequent here but rare in everyday English?**  
   → High TF-IDF score. These are the lexical signatures of the text.
2. **Which words appear in the text but are also very common in general English?**  
   → Low TF-IDF score. These look familiar but carry specialist meaning here.

---

## Methodology

**Term Frequency (TF)** — count of each word in the translation, normalised by total content-token count.
Frontmatter, verse markers (`^1-2`), numbers and markdown syntax are stripped before counting.

**Inverse Document Frequency (IDF)** — pre-seeded from BNC and COCA reference corpora (cross-checked
against the General Service List and Oxford 3000). Scale:

| IDF range | Meaning |
|-----------|---------|
| 0.01 – 0.15 | Function word — present in virtually every English document |
| 1.0 – 3.5 | Common content word — high general-English frequency |
| 4.0 – 7.0 | Moderately rare — limited domain or register |
| 7.0 – 11.0 | Uncommon / archaic — rare in contemporary corpora |
| 11.0 – 15.0 | Absent from general English — domain-exclusive or coined |

**TF-IDF score** = TF × IDF × 10⁶ (scaled for readability).

**Colour bands** used in the table:

| Band | Score range | Interpretation |
|------|-------------|----------------|
| 🔴 | ≥ 50,000 | Text-exclusive — word essentially does not exist outside this translation |
| 🟠 | 10,000 – 49,999 | Domain-specific — Buddhist / Abhidhamma vocabulary |
| 🟡 | 3,000 – 9,999 | Specialist register — unusual in general English |
| 🟢 | 500 – 2,999 | Moderately distinctive — identifiable domain presence |
| 🔵 | 50 – 499 | Moderately common — has general English presence |
| ⚪ | 0 – 49 | Universal / function word |

---

## Distribution by Band

| Band | Terms | % of vocabulary |
|------|-------|----------------|
| 🔴 extremely high — text-exclusive | 4 | 0.2% |
| 🟠 very high — domain-specific | 34 | 1.5% |
| 🟡 high — specialist register | 61 | 2.7% |
| 🟢 medium — moderately distinctive | 321 | 14.3% |
| 🔵 low — common in general English | 867 | 38.6% |
| ⚪ very low — function / universal word | 960 | 42.7% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.
These are the genuine lexical fingerprints of the Rhys Davids translation.

**1. states** — count: 743, TF-IDF: 100,449, IDF: 2.8 🔴 extremely high — text-exclusive
**2. jhāna** — count: 143, TF-IDF: 93,211, IDF: 13.5 🔴 extremely high — text-exclusive
**3. form** — count: 560, TF-IDF: 54,078, IDF: 2.0 🔴 extremely high — text-exclusive
**4. occasion** — count: 308, TF-IDF: 52,050, IDF: 3.5 🔴 extremely high — text-exclusive
**5. indeterminate** — count: 115, TF-IDF: 49,973, IDF: 9.0 🟠 very high — domain-specific
**6. skandha** — count: 64, TF-IDF: 44,807, IDF: 14.5 🟠 very high — domain-specific
**7. contact** — count: 258, TF-IDF: 43,600, IDF: 3.5 🟠 very high — domain-specific
**8. synergies** — count: 69, TF-IDF: 43,310, IDF: 13.0 🟠 very high — domain-specific
**9. self-collectedness** — count: 57, TF-IDF: 38,530, IDF: 14.0 🟠 very high — domain-specific
**10. faculty** — count: 143, TF-IDF: 37,975, IDF: 5.5 🟠 very high — domain-specific
**11. āsavas** — count: 50, TF-IDF: 35,006, IDF: 14.5 🟠 very high — domain-specific
**12. thought** — count: 244, TF-IDF: 32,987, IDF: 2.8 🟠 very high — domain-specific
**13. volition** — count: 83, TF-IDF: 32,060, IDF: 8.0 🟠 very high — domain-specific
**14. perception** — count: 117, TF-IDF: 28,246, IDF: 5.0 🟠 very high — domain-specific
**15. incorporeal** — count: 45, TF-IDF: 22,814, IDF: 10.5 🟠 very high — domain-specific
**16. indifference** — count: 84, TF-IDF: 22,307, IDF: 5.5 🟠 very high — domain-specific
**17. consciousness** — count: 114, TF-IDF: 22,017, IDF: 4.0 🟠 very high — domain-specific
**18. zest** — count: 52, TF-IDF: 21,341, IDF: 8.5 🟠 very high — domain-specific
**19. associated** — count: 105, TF-IDF: 20,279, IDF: 4.0 🟠 very high — domain-specific
**20. mindfulness** — count: 58, TF-IDF: 18,203, IDF: 6.5 🟠 very high — domain-specific
**21. feeling** — count: 149, TF-IDF: 17,986, IDF: 2.5 🟠 very high — domain-specific
**22. mind** — count: 141, TF-IDF: 17,701, IDF: 2.6 🟠 very high — domain-specific
**23. mental** — count: 118, TF-IDF: 17,092, IDF: 3.0 🟠 very high — domain-specific
**24. material** — count: 348, TF-IDF: 16,803, IDF: 1.0 🟠 very high — domain-specific
**25. concentration** — count: 69, TF-IDF: 16,658, IDF: 5.0 🟠 very high — domain-specific
**26. wieldiness** — count: 25, TF-IDF: 15,692, IDF: 13.0 🟠 very high — domain-specific
**27. absence** — count: 79, TF-IDF: 15,258, IDF: 4.0 🟠 very high — domain-specific
**28. intuition** — count: 52, TF-IDF: 13,809, IDF: 5.5 🟠 very high — domain-specific
**29. balance** — count: 77, TF-IDF: 13,012, IDF: 3.5 🟠 very high — domain-specific
**30. insight** — count: 59, TF-IDF: 12,819, IDF: 4.5 🟠 very high — domain-specific
**31. faculties** — count: 48, TF-IDF: 12,747, IDF: 5.5 🟠 very high — domain-specific
**32. sustained** — count: 65, TF-IDF: 12,554, IDF: 4.0 🟠 very high — domain-specific
**33. energy** — count: 71, TF-IDF: 11,998, IDF: 3.5 🟠 very high — domain-specific
**34. views** — count: 80, TF-IDF: 11,588, IDF: 3.0 🟠 very high — domain-specific
**35. gladness** — count: 38, TF-IDF: 11,009, IDF: 6.0 🟠 very high — domain-specific
**36. āsava** — count: 15, TF-IDF: 10,502, IDF: 14.5 🟠 very high — domain-specific
**37. sense** — count: 98, TF-IDF: 10,410, IDF: 2.2 🟠 very high — domain-specific
**38. born** — count: 92, TF-IDF: 10,217, IDF: 2.3 🟠 very high — domain-specific
**39. sphere** — count: 207, TF-IDF: 9,995, IDF: 1.0 🟡 high — specialist register
**40. applied** — count: 63, TF-IDF: 9,734, IDF: 3.2 🟡 high — specialist register
**41. ease** — count: 64, TF-IDF: 9,270, IDF: 3.0 🟡 high — specialist register
**42. element** — count: 192, TF-IDF: 9,270, IDF: 1.0 🟡 high — specialist register
**43. life** — count: 106, TF-IDF: 9,212, IDF: 1.8 🟡 high — specialist register
**44. bad** — count: 117, TF-IDF: 9,039, IDF: 1.6 🟡 high — specialist register
**45. bodily** — count: 182, TF-IDF: 8,788, IDF: 1.0 🟡 high — specialist register
**46. covetousness** — count: 19, TF-IDF: 8,715, IDF: 9.5 🟡 high — specialist register
**47. grasp** — count: 36, TF-IDF: 7,822, IDF: 4.5 🟡 high — specialist register
**48. endeavour** — count: 29, TF-IDF: 7,001, IDF: 5.0 🟡 high — specialist register
**49. having** — count: 136, TF-IDF: 6,567, IDF: 1.0 🟡 high — specialist register
**50. ideation** — count: 15, TF-IDF: 6,518, IDF: 9.0 🟡 high — specialist register

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English,
giving them a near-zero TF-IDF score despite sometimes occurring hundreds of times here.

**1. every** — count: 7, TF-IDF: 40.56, IDF: 0.12 ⚪ very low — function / universal word
**2. dukaatthuddhāro** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**3. tikaatthuddhāro** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**4. aṭṭhakathākaṇḍaṃ** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**5. deposition** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**6. entitled** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**7. nirvāna** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**8. twofold** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**9. intoxicants** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**10. renascence** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**11. decease** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**12. births** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**13. reminiscent** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**14. attend** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**15. repetition** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**16. assiduous** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**17. stagnation** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**18. performance** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**19. unresting** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**20. persevering** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**21. thorough** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**22. shrinking** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**23. dissatisfied** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**24. forward** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**25. reaches** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**26. a-going** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**27. uses** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**28. abound** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**29. practised** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**30. frequently** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**31. confused** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**32. firm** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**33. brings** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**34. bhikkhu** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**35. refers** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**36. earnest** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**37. implies** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**38. fallacies** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**39. immorality** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**40. multiplying** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**41. pursuing** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**42. computation** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**43. oblivion** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**44. non-remembrance** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**45. non-recollection** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**46. memory** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**47. lapse** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**48. unmindfulness** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**49. comfort** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word
**50. blamelessness** — count: 1, TF-IDF: 48.28, IDF: 1.0 ⚪ very low — function / universal word

---

## Full Ranked Table

All 2,247 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **states** | 743 | 100,449.04 | 2.8 | 🔴 extremely high — text-exclusive |
| 2 | **jhāna** | 143 | 93,211.34 | 13.5 | 🔴 extremely high — text-exclusive |
| 3 | **form** | 560 | 54,077.54 | 2.0 | 🔴 extremely high — text-exclusive |
| 4 | **occasion** | 308 | 52,049.64 | 3.5 | 🔴 extremely high — text-exclusive |
| 5 | **indeterminate** | 115 | 49,973.44 | 9.0 | 🟠 very high — domain-specific |
| 6 | **skandha** | 64 | 44,807.11 | 14.5 | 🟠 very high — domain-specific |
| 7 | **contact** | 258 | 43,600.02 | 3.5 | 🟠 very high — domain-specific |
| 8 | **synergies** | 69 | 43,310.32 | 13.0 | 🟠 very high — domain-specific |
| 9 | **self-collectedness** | 57 | 38,530.25 | 14.0 | 🟠 very high — domain-specific |
| 10 | **faculty** | 143 | 37,974.99 | 5.5 | 🟠 very high — domain-specific |
| 11 | **āsavas** | 50 | 35,005.55 | 14.5 | 🟠 very high — domain-specific |
| 12 | **thought** | 244 | 32,987.30 | 2.8 | 🟠 very high — domain-specific |
| 13 | **volition** | 83 | 32,060.26 | 8.0 | 🟠 very high — domain-specific |
| 14 | **perception** | 117 | 28,245.86 | 5.0 | 🟠 very high — domain-specific |
| 15 | **incorporeal** | 45 | 22,813.96 | 10.5 | 🟠 very high — domain-specific |
| 16 | **indifference** | 84 | 22,306.99 | 5.5 | 🟠 very high — domain-specific |
| 17 | **consciousness** | 114 | 22,017.29 | 4.0 | 🟠 very high — domain-specific |
| 18 | **zest** | 52 | 21,341.32 | 8.5 | 🟠 very high — domain-specific |
| 19 | **associated** | 105 | 20,279.08 | 4.0 | 🟠 very high — domain-specific |
| 20 | **mindfulness** | 58 | 18,202.89 | 6.5 | 🟠 very high — domain-specific |
| 21 | **feeling** | 149 | 17,985.61 | 2.5 | 🟠 very high — domain-specific |
| 22 | **mind** | 141 | 17,700.74 | 2.6 | 🟠 very high — domain-specific |
| 23 | **mental** | 118 | 17,092.37 | 3.0 | 🟠 very high — domain-specific |
| 24 | **material** | 348 | 16,802.67 | 1.0 | 🟠 very high — domain-specific |
| 25 | **concentration** | 69 | 16,657.81 | 5.0 | 🟠 very high — domain-specific |
| 26 | **wieldiness** | 25 | 15,692.14 | 13.0 | 🟠 very high — domain-specific |
| 27 | **absence** | 79 | 15,257.59 | 4.0 | 🟠 very high — domain-specific |
| 28 | **intuition** | 52 | 13,809.09 | 5.5 | 🟠 very high — domain-specific |
| 29 | **balance** | 77 | 13,012.41 | 3.5 | 🟠 very high — domain-specific |
| 30 | **insight** | 59 | 12,819.27 | 4.5 | 🟠 very high — domain-specific |
| 31 | **faculties** | 48 | 12,746.85 | 5.5 | 🟠 very high — domain-specific |
| 32 | **sustained** | 65 | 12,553.72 | 4.0 | 🟠 very high — domain-specific |
| 33 | **energy** | 71 | 11,998.45 | 3.5 | 🟠 very high — domain-specific |
| 34 | **views** | 80 | 11,588.05 | 3.0 | 🟠 very high — domain-specific |
| 35 | **gladness** | 38 | 11,008.64 | 6.0 | 🟠 very high — domain-specific |
| 36 | **āsava** | 15 | 10,501.67 | 14.5 | 🟠 very high — domain-specific |
| 37 | **sense** | 98 | 10,409.93 | 2.2 | 🟠 very high — domain-specific |
| 38 | **born** | 92 | 10,216.79 | 2.3 | 🟠 very high — domain-specific |
| 39 | **sphere** | 207 | 9,994.69 | 1.0 | 🟡 high — specialist register |
| 40 | **applied** | 63 | 9,733.96 | 3.2 | 🟡 high — specialist register |
| 41 | **ease** | 64 | 9,270.44 | 3.0 | 🟡 high — specialist register |
| 42 | **element** | 192 | 9,270.44 | 1.0 | 🟡 high — specialist register |
| 43 | **life** | 106 | 9,212.50 | 1.8 | 🟡 high — specialist register |
| 44 | **bad** | 117 | 9,038.68 | 1.6 | 🟡 high — specialist register |
| 45 | **bodily** | 182 | 8,787.60 | 1.0 | 🟡 high — specialist register |
| 46 | **covetousness** | 19 | 8,715.18 | 9.5 | 🟡 high — specialist register |
| 47 | **grasp** | 36 | 7,821.93 | 4.5 | 🟡 high — specialist register |
| 48 | **endeavour** | 29 | 7,001.11 | 5.0 | 🟡 high — specialist register |
| 49 | **having** | 136 | 6,566.56 | 1.0 | 🟡 high — specialist register |
| 50 | **ideation** | 15 | 6,518.28 | 9.0 | 🟡 high — specialist register |
| 51 | **skandhas** | 134 | 6,469.99 | 1.0 | 🟡 high — specialist register |
| 52 | **etc** | 129 | 6,228.57 | 1.0 | 🟡 high — specialist register |
| 53 | **object** | 117 | 5,649.17 | 1.0 | 🟡 high — specialist register |
| 54 | **put** | 64 | 5,562.26 | 1.8 | 🟡 high — specialist register |
| 55 | **concomitant** | 12 | 5,504.32 | 9.5 | 🟡 high — specialist register |
| 56 | **serenity** | 19 | 5,504.32 | 6.0 | 🟡 high — specialist register |
| 57 | **faith** | 27 | 5,214.62 | 4.0 | 🟡 high — specialist register |
| 58 | **path** | 43 | 5,190.48 | 2.5 | 🟡 high — specialist register |
| 59 | **answer** | 106 | 5,118.05 | 1.0 | 🟡 high — specialist register |
| 60 | **power** | 51 | 4,924.92 | 2.0 | 🟡 high — specialist register |
| 61 | **body** | 51 | 4,924.92 | 2.0 | 🟡 high — specialist register |
| 62 | **visible** | 99 | 4,780.07 | 1.0 | 🟡 high — specialist register |
| 63 | **moral** | 28 | 4,731.78 | 3.5 | 🟡 high — specialist register |
| 64 | **state** | 39 | 4,707.64 | 2.5 | 🟡 high — specialist register |
| 65 | **spheres** | 97 | 4,683.50 | 1.0 | 🟡 high — specialist register |
| 66 | **nutriment** | 97 | 4,683.50 | 1.0 | 🟡 high — specialist register |
| 67 | **reacting** | 91 | 4,393.80 | 1.0 | 🟡 high — specialist register |
| 68 | **dissociated** | 14 | 4,393.80 | 6.5 | 🟡 high — specialist register |
| 69 | **whatever** | 91 | 4,393.80 | 1.0 | 🟡 high — specialist register |
| 70 | **accompanied** | 90 | 4,345.52 | 1.0 | 🟡 high — specialist register |
| 71 | **right** | 60 | 4,345.52 | 1.5 | 🟡 high — specialist register |
| 72 | **buoyancy** | 12 | 4,345.52 | 7.5 | 🟡 high — specialist register |
| 73 | **aloof** | 86 | 4,152.38 | 1.0 | 🟡 high — specialist register |
| 74 | **intention** | 21 | 4,055.82 | 4.0 | 🟡 high — specialist register |
| 75 | **karma** | 84 | 4,055.82 | 1.0 | 🟡 high — specialist register |
| 76 | **arisen** | 82 | 3,959.25 | 1.0 | 🟡 high — specialist register |
| 77 | **tangible** | 81 | 3,910.97 | 1.0 | 🟡 high — specialist register |
| 78 | **invisible** | 80 | 3,862.68 | 1.0 | 🟡 high — specialist register |
| 79 | **cognition** | 78 | 3,766.11 | 1.0 | 🟡 high — specialist register |
| 80 | **external** | 77 | 3,717.83 | 1.0 | 🟡 high — specialist register |
| 81 | **formless** | 77 | 3,717.83 | 1.0 | 🟡 high — specialist register |
| 82 | **taste** | 77 | 3,717.83 | 1.0 | 🟡 high — specialist register |
| 83 | **pliancy** | 6 | 3,621.26 | 12.5 | 🟡 high — specialist register |
| 84 | **away** | 72 | 3,476.41 | 1.0 | 🟡 high — specialist register |
| 85 | **application** | 20 | 3,379.85 | 3.5 | 🟡 high — specialist register |
| 86 | **vision** | 69 | 3,331.56 | 1.0 | 🟡 high — specialist register |
| 87 | **progress** | 69 | 3,331.56 | 1.0 | 🟡 high — specialist register |
| 88 | **sound** | 68 | 3,283.28 | 1.0 | 🟡 high — specialist register |
| 89 | **rectitude** | 8 | 3,283.28 | 8.5 | 🟡 high — specialist register |
| 90 | **continue** | 68 | 3,283.28 | 1.0 | 🟡 high — specialist register |
| 91 | **knowledge** | 67 | 3,235.00 | 1.0 | 🟡 high — specialist register |
| 92 | **sensuous** | 67 | 3,235.00 | 1.0 | 🟡 high — specialist register |
| 93 | **enters** | 67 | 3,235.00 | 1.0 | 🟡 high — specialist register |
| 94 | **abides** | 67 | 3,235.00 | 1.0 | 🟡 high — specialist register |
| 95 | **opinion** | 67 | 3,235.00 | 1.0 | 🟡 high — specialist register |
| 96 | **way** | 37 | 3,215.68 | 1.8 | 🟡 high — specialist register |
| 97 | **quiet** | 19 | 3,210.85 | 3.5 | 🟡 high — specialist register |
| 98 | **answers** | 66 | 3,186.71 | 1.0 | 🟡 high — specialist register |
| 99 | **under** | 66 | 3,186.71 | 1.0 | 🟡 high — specialist register |
| 100 | **unincluded** | 62 | 2,993.58 | 1.0 | 🟢 medium — moderately distinctive |
| 101 | **higher** | 61 | 2,945.29 | 1.0 | 🟢 medium — moderately distinctive |
| 102 | **ideal** | 60 | 2,897.01 | 1.0 | 🟢 medium — moderately distinctive |
| 103 | **dullness** | 59 | 2,848.73 | 1.0 | 🟢 medium — moderately distinctive |
| 104 | **wrong** | 59 | 2,848.73 | 1.0 | 🟢 medium — moderately distinctive |
| 105 | **grasped** | 58 | 2,800.44 | 1.0 | 🟢 medium — moderately distinctive |
| 106 | **unconditioned** | 58 | 2,800.44 | 1.0 | 🟢 medium — moderately distinctive |
| 107 | **whether** | 58 | 2,800.44 | 1.0 | 🟢 medium — moderately distinctive |
| 108 | **derived** | 56 | 2,703.88 | 1.0 | 🟢 medium — moderately distinctive |
| 109 | **attain** | 56 | 2,703.88 | 1.0 | 🟢 medium — moderately distinctive |
| 110 | **visual** | 56 | 2,703.88 | 1.0 | 🟢 medium — moderately distinctive |
| 111 | **causally** | 55 | 2,655.59 | 1.0 | 🟢 medium — moderately distinctive |
| 112 | **universe** | 55 | 2,655.59 | 1.0 | 🟢 medium — moderately distinctive |
| 113 | **evil** | 55 | 2,655.59 | 1.0 | 🟢 medium — moderately distinctive |
| 114 | **remorse** | 6 | 2,607.31 | 9.0 | 🟢 medium — moderately distinctive |
| 115 | **cultivates** | 54 | 2,607.31 | 1.0 | 🟢 medium — moderately distinctive |
| 116 | **arises** | 54 | 2,607.31 | 1.0 | 🟢 medium — moderately distinctive |
| 117 | **worlds** | 54 | 2,607.31 | 1.0 | 🟢 medium — moderately distinctive |
| 118 | **grasping** | 53 | 2,559.03 | 1.0 | 🟢 medium — moderately distinctive |
| 119 | **shape** | 53 | 2,559.03 | 1.0 | 🟢 medium — moderately distinctive |
| 120 | **phenomena** | 52 | 2,510.74 | 1.0 | 🟢 medium — moderately distinctive |
| 121 | **senses** | 52 | 2,510.74 | 1.0 | 🟢 medium — moderately distinctive |
| 122 | **sight** | 51 | 2,462.46 | 1.0 | 🟢 medium — moderately distinctive |
| 123 | **disconnected** | 51 | 2,462.46 | 1.0 | 🟢 medium — moderately distinctive |
| 124 | **personal** | 51 | 2,462.46 | 1.0 | 🟢 medium — moderately distinctive |
| 125 | **hate** | 49 | 2,365.89 | 1.0 | 🟢 medium — moderately distinctive |
| 126 | **favourable** | 48 | 2,317.61 | 1.0 | 🟢 medium — moderately distinctive |
| 127 | **wrought** | 48 | 2,317.61 | 1.0 | 🟢 medium — moderately distinctive |
| 128 | **words** | 48 | 2,317.61 | 1.0 | 🟢 medium — moderately distinctive |
| 129 | **blame** | 47 | 2,269.33 | 1.0 | 🟢 medium — moderately distinctive |
| 130 | **smell** | 46 | 2,221.04 | 1.0 | 🟢 medium — moderately distinctive |
| 131 | **desires** | 46 | 2,221.04 | 1.0 | 🟢 medium — moderately distinctive |
| 132 | **intelligence** | 13 | 2,196.90 | 3.5 | 🟢 medium — moderately distinctive |
| 133 | **self** | 44 | 2,124.47 | 1.0 | 🟢 medium — moderately distinctive |
| 134 | **immoderation** | 4 | 2,124.47 | 11.0 | 🟢 medium — moderately distinctive |
| 135 | **intimation** | 44 | 2,124.47 | 1.0 | 🟢 medium — moderately distinctive |
| 136 | **end** | 24 | 2,085.85 | 1.8 | 🟢 medium — moderately distinctive |
| 137 | **induced** | 43 | 2,076.19 | 1.0 | 🟢 medium — moderately distinctive |
| 138 | **connexion** | 43 | 2,076.19 | 1.0 | 🟢 medium — moderately distinctive |
| 139 | **paths** | 43 | 2,076.19 | 1.0 | 🟢 medium — moderately distinctive |
| 140 | **arise** | 42 | 2,027.91 | 1.0 | 🟢 medium — moderately distinctive |
| 141 | **ideas** | 41 | 1,979.62 | 1.0 | 🟢 medium — moderately distinctive |
| 142 | **remaining** | 41 | 1,979.62 | 1.0 | 🟢 medium — moderately distinctive |
| 143 | **result** | 41 | 1,979.62 | 1.0 | 🟢 medium — moderately distinctive |
| 144 | **body-sensibility** | 41 | 1,979.62 | 1.0 | 🟢 medium — moderately distinctive |
| 145 | **odour** | 41 | 1,979.62 | 1.0 | 🟢 medium — moderately distinctive |
| 146 | **fetters** | 40 | 1,931.34 | 1.0 | 🟢 medium — moderately distinctive |
| 147 | **rebirth** | 40 | 1,931.34 | 1.0 | 🟢 medium — moderately distinctive |
| 148 | **rapt** | 39 | 1,883.06 | 1.0 | 🟢 medium — moderately distinctive |
| 149 | **meditation** | 39 | 1,883.06 | 1.0 | 🟢 medium — moderately distinctive |
| 150 | **roots** | 38 | 1,834.77 | 1.0 | 🟢 medium — moderately distinctive |
| 151 | **repeat** | 38 | 1,834.77 | 1.0 | 🟢 medium — moderately distinctive |
| 152 | **jhānas** | 37 | 1,786.49 | 1.0 | 🟢 medium — moderately distinctive |
| 153 | **ignorance** | 36 | 1,738.21 | 1.0 | 🟢 medium — moderately distinctive |
| 154 | **suavity** | 3 | 1,738.21 | 12.0 | 🟢 medium — moderately distinctive |
| 155 | **superposing** | 3 | 1,738.21 | 12.0 | 🟢 medium — moderately distinctive |
| 156 | **case** | 36 | 1,738.21 | 1.0 | 🟢 medium — moderately distinctive |
| 157 | **sensual** | 36 | 1,738.21 | 1.0 | 🟢 medium — moderately distinctive |
| 158 | **emptiness** | 35 | 1,689.92 | 1.0 | 🟢 medium — moderately distinctive |
| 159 | **thereto** | 35 | 1,689.92 | 1.0 | 🟢 medium — moderately distinctive |
| 160 | **sluggish** | 35 | 1,689.92 | 1.0 | 🟢 medium — moderately distinctive |
| 161 | **sense-objects** | 35 | 1,689.92 | 1.0 | 🟢 medium — moderately distinctive |
| 162 | **best** | 34 | 1,641.64 | 1.0 | 🟢 medium — moderately distinctive |
| 163 | **kinds** | 34 | 1,641.64 | 1.0 | 🟢 medium — moderately distinctive |
| 164 | **factors** | 33 | 1,593.36 | 1.0 | 🟢 medium — moderately distinctive |
| 165 | **summary** | 33 | 1,593.36 | 1.0 | 🟢 medium — moderately distinctive |
| 166 | **called** | 33 | 1,593.36 | 1.0 | 🟢 medium — moderately distinctive |
| 167 | **composure** | 5 | 1,569.21 | 6.5 | 🟢 medium — moderately distinctive |
| 168 | **thinking** | 32 | 1,545.07 | 1.0 | 🟢 medium — moderately distinctive |
| 169 | **vices** | 32 | 1,545.07 | 1.0 | 🟢 medium — moderately distinctive |
| 170 | **space** | 32 | 1,545.07 | 1.0 | 🟢 medium — moderately distinctive |
| 171 | **basis** | 32 | 1,545.07 | 1.0 | 🟢 medium — moderately distinctive |
| 172 | **depending** | 32 | 1,545.07 | 1.0 | 🟢 medium — moderately distinctive |
| 173 | **going** | 31 | 1,496.79 | 1.0 | 🟢 medium — moderately distinctive |
| 174 | **desire** | 31 | 1,496.79 | 1.0 | 🟢 medium — moderately distinctive |
| 175 | **cognizable** | 31 | 1,496.79 | 1.0 | 🟢 medium — moderately distinctive |
| 176 | **instigation** | 4 | 1,448.51 | 7.5 | 🟢 medium — moderately distinctive |
| 177 | **system** | 30 | 1,448.51 | 1.0 | 🟢 medium — moderately distinctive |
| 178 | **modes** | 30 | 1,448.51 | 1.0 | 🟢 medium — moderately distinctive |
| 179 | **wit** | 30 | 1,448.51 | 1.0 | 🟢 medium — moderately distinctive |
| 180 | **painful** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 181 | **ties** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 182 | **unconscientiousness** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 183 | **vitakko** | 2 | 1,400.22 | 14.5 | 🟢 medium — moderately distinctive |
| 184 | **vicāro** | 2 | 1,400.22 | 14.5 | 🟢 medium — moderately distinctive |
| 185 | **whereto** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 186 | **fetter** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 187 | **themselves** | 29 | 1,400.22 | 1.0 | 🟢 medium — moderately distinctive |
| 188 | **limited** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 189 | **davids** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 190 | **pali** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 191 | **text** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 192 | **society** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 193 | **heavens** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 194 | **disregard** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 195 | **hearing** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 196 | **world** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 197 | **vocal** | 28 | 1,351.94 | 1.0 | 🟢 medium — moderately distinctive |
| 198 | **infinite** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 199 | **dominant** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 200 | **annihilation** | 3 | 1,303.66 | 9.0 | 🟢 medium — moderately distinctive |
| 201 | **greed** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 202 | **fivefold** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 203 | **identical** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 204 | **hindrances** | 27 | 1,303.66 | 1.0 | 🟢 medium — moderately distinctive |
| 205 | **perversion** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 206 | **included** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 207 | **theory** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 208 | **making** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 209 | **stage** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 210 | **group** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 211 | **fluid** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 212 | **exists** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 213 | **relate** | 26 | 1,255.37 | 1.0 | 🟢 medium — moderately distinctive |
| 214 | **influence** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 215 | **plasticity** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 216 | **distraction** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 217 | **respectively** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 218 | **unaimed-at** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 219 | **integration** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 220 | **eye** | 25 | 1,207.09 | 1.0 | 🟢 medium — moderately distinctive |
| 221 | **onward** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 222 | **contumacy** | 2 | 1,158.80 | 12.0 | 🟢 medium — moderately distinctive |
| 223 | **subsistence** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 224 | **ends** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 225 | **fourth** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 226 | **see** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 227 | **relating** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 228 | **above** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 229 | **phenomenon** | 24 | 1,158.80 | 1.0 | 🟢 medium — moderately distinctive |
| 230 | **come** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 231 | **eternalism** | 2 | 1,110.52 | 11.5 | 🟢 medium — moderately distinctive |
| 232 | **representative** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 233 | **obliviousness** | 2 | 1,110.52 | 11.5 | 🟢 medium — moderately distinctive |
| 234 | **type** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 235 | **second** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 236 | **foregoing** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 237 | **opinions** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 238 | **perplexity** | 23 | 1,110.52 | 1.0 | 🟢 medium — moderately distinctive |
| 239 | **together** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 240 | **crookedness** | 2 | 1,062.24 | 11.0 | 🟢 medium — moderately distinctive |
| 241 | **ill** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 242 | **instigated** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 243 | **forth** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 244 | **undoing** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 245 | **described** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 246 | **something** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 247 | **say** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 248 | **root-conditions** | 22 | 1,062.24 | 1.0 | 🟢 medium — moderately distinctive |
| 249 | **lightness** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 250 | **preceding** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 251 | **substituting** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 252 | **fourfold** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 253 | **difficult** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 254 | **conversely** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 255 | **impinge** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 256 | **speculative** | 21 | 1,013.95 | 1.0 | 🟢 medium — moderately distinctive |
| 257 | **latter** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 258 | **sprung** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 259 | **conscientiousness** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 260 | **touch** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 261 | **appropriate** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 262 | **intellection** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 263 | **whereby** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 264 | **taken** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 265 | **impinged** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 266 | **due** | 20 | 965.67 | 1.0 | 🟢 medium — moderately distinctive |
| 267 | **root** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 268 | **belong** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 269 | **fear** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 270 | **lust** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 271 | **phrase** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 272 | **forms** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 273 | **auditory** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 274 | **tastes** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 275 | **impinges** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 276 | **fruits** | 19 | 917.39 | 1.0 | 🟢 medium — moderately distinctive |
| 277 | **present** | 9 | 869.10 | 2.0 | 🟢 medium — moderately distinctive |
| 278 | **wisdom** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 279 | **concerning** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 280 | **easeful** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 281 | **exultation** | 2 | 869.10 | 9.0 | 🟢 medium — moderately distinctive |
| 282 | **causes** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 283 | **third** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 284 | **moreover** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 285 | **shapes** | 18 | 869.10 | 1.0 | 🟢 medium — moderately distinctive |
| 286 | **elements** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 287 | **malice** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 288 | **fortitude** | 2 | 820.82 | 8.5 | 🟢 medium — moderately distinctive |
| 289 | **disinterestedness** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 290 | **questions** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 291 | **passion** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 292 | **aspect** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 293 | **ear** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 294 | **sex** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 295 | **rule** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 296 | **ritual** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 297 | **tie** | 17 | 820.82 | 1.0 | 🟢 medium — moderately distinctive |
| 298 | **set** | 9 | 782.19 | 1.8 | 🟢 medium — moderately distinctive |
| 299 | **vicious** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 300 | **felicity** | 2 | 772.54 | 8.0 | 🟢 medium — moderately distinctive |
| 301 | **powers** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 302 | **made** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 303 | **olfactory** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 304 | **gustatory** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 305 | **consequence** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 306 | **nose** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 307 | **tongue** | 16 | 772.54 | 1.0 | 🟢 medium — moderately distinctive |
| 308 | **results** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 309 | **medium** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 310 | **former** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 311 | **guilt** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 312 | **buddhist** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 313 | **manual** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 314 | **decay** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 315 | **impermanence** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 316 | **sentient** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 317 | **conjunction** | 15 | 724.25 | 1.0 | 🟢 medium — moderately distinctive |
| 318 | **cetanā** | 1 | 700.11 | 14.5 | 🟢 medium — moderately distinctive |
| 319 | **objects** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 320 | **graspings** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 321 | **things** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 322 | **heart** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 323 | **understanding** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 324 | **sammāsati** | 1 | 675.97 | 14.0 | 🟢 medium — moderately distinctive |
| 325 | **without** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 326 | **constituent** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 327 | **psychological** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 328 | **ethics** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 329 | **rys** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 330 | **dhammasaṅgaṇī** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 331 | **compendium** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 332 | **caroline** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 333 | **rhys** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 334 | **litt** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 335 | **published** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 336 | **reprinted** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 337 | **released** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 338 | **creative** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 339 | **commons** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 340 | **attribution-noncommercial** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 341 | **licence** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 342 | **by-nc** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 343 | **statement** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 344 | **http** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 345 | **earth-gazing** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 346 | **question** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 347 | **action** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 348 | **cultivation** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 349 | **organ** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 350 | **appearance** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 351 | **belongs** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 352 | **non-reacting** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 353 | **hindrance** | 14 | 675.97 | 1.0 | 🟢 medium — moderately distinctive |
| 354 | **vipassanā** | 1 | 651.83 | 13.5 | 🟢 medium — moderately distinctive |
| 355 | **fixed** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 356 | **given** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 357 | **beyond** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 358 | **pass** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 359 | **tractableness** | 1 | 627.69 | 13.0 | 🟢 medium — moderately distinctive |
| 360 | **inferior** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 361 | **superlative** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 362 | **efficacy** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 363 | **distress** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 364 | **sounds** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 365 | **odours** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 366 | **woman-faculty** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 367 | **fluidity** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 368 | **gross** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 369 | **itself** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 370 | **excepted** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 371 | **soil** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 372 | **stolidity** | 13 | 627.69 | 1.0 | 🟢 medium — moderately distinctive |
| 373 | **pleasant** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 374 | **belonging** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 375 | **related** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 376 | **supramundane** | 1 | 579.40 | 12.0 | 🟢 medium — moderately distinctive |
| 377 | **properties** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 378 | **conjoined** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 379 | **fitness** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 380 | **truth** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 381 | **felt** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 382 | **wherein** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 383 | **comes** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 384 | **combination** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 385 | **enumerated** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 386 | **speech** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 387 | **conceit** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 388 | **lack** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 389 | **cultivated** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 390 | **pursuit** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 391 | **signless** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 392 | **corresponding** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 393 | **inoperative** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 394 | **remote** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 395 | **near** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 396 | **ten** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 397 | **sort** | 12 | 579.40 | 1.0 | 🟢 medium — moderately distinctive |
| 398 | **past** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 399 | **consecutive** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 400 | **craving** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 401 | **skill** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 402 | **searching** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 403 | **factor** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 404 | **condition** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 405 | **omitting** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 406 | **quick** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 407 | **easy** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 408 | **combinations** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 409 | **perfect** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 410 | **empty** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 411 | **stored** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 412 | **cause** | 5 | 531.12 | 2.2 | 🟢 medium — moderately distinctive |
| 413 | **known** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 414 | **subtle** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 415 | **regards** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 416 | **springing** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 417 | **become** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 418 | **death** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 419 | **afore-named** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 420 | **because** | 11 | 531.12 | 1.0 | 🟢 medium — moderately distinctive |
| 421 | **vitiated** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 422 | **sensation** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 423 | **section** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 424 | **further** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 425 | **sorrow** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 426 | **capable** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 427 | **mastery** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 428 | **investigation** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 429 | **formula** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 430 | **effect** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 431 | **order** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 432 | **triplet** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 433 | **underived** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 434 | **arising** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 435 | **torpor** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 436 | **worry** | 10 | 482.84 | 1.0 | 🔵 low — common in general English |
| 437 | **culture** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 438 | **consequences** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 439 | **purity** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 440 | **joy** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 441 | **grip** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 442 | **exclusive** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 443 | **full** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 444 | **extension** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 445 | **corpse** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 446 | **follow** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 447 | **contained** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 448 | **enlightenment** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 449 | **infected** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 450 | **taking** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 451 | **living** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 452 | **pairs** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 453 | **co-intoxicant** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 454 | **man-faculty** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 455 | **village** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 456 | **against** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 457 | **smells** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 458 | **fruit** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 459 | **kind** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 460 | **united** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 461 | **operative** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 462 | **concomitants** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 463 | **soul** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 464 | **thing** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 465 | **word** | 9 | 434.55 | 1.0 | 🔵 low — common in general English |
| 466 | **offences** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 467 | **attention** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 468 | **holds** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 469 | **solid** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 470 | **doctrine** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 471 | **conscientious** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 472 | **scruple** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 473 | **ought** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 474 | **attaining** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 475 | **know** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 476 | **colour** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 477 | **wholly** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 478 | **gain** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 479 | **path-component** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 480 | **concept** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 481 | **disorder** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 482 | **inclination** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 483 | **towards** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 484 | **distressful** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 485 | **exception** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 486 | **except** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 487 | **category** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 488 | **sapid** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 489 | **caused** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 490 | **groups** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 491 | **springs** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 492 | **individuality** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 493 | **sensuality** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 494 | **speculation** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 495 | **excess** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 496 | **means** | 8 | 386.27 | 1.0 | 🔵 low — common in general English |
| 497 | **happiness** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 498 | **future** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 499 | **perverted** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 500 | **vice** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 501 | **terms** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 502 | **diet** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 503 | **struggle** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 504 | **agitation** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 505 | **pleasurable** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 506 | **research** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 507 | **proficiency** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 508 | **single** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 509 | **purely** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 510 | **thoughts** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 511 | **noble** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 512 | **passing** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 513 | **sixteenfold** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 514 | **part** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 515 | **corporeal** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 516 | **indigo** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 517 | **conscious** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 518 | **love** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 519 | **leading** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 520 | **nineteen** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 521 | **walking** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 522 | **jungle** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 523 | **wilderness** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 524 | **scuffling** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 525 | **tenacity** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 526 | **by-path** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 527 | **road** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 528 | **wrongness** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 529 | **passim** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 530 | **constitutes** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 531 | **attained** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 532 | **impact** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 533 | **next** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 534 | **make** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 535 | **among** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 536 | **eternal** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 537 | **tend** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 538 | **tied** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 539 | **birth** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 540 | **besides** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 541 | **deed** | 7 | 337.98 | 1.0 | 🔵 low — common in general English |
| 542 | **unaccompanied** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 543 | **name** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 544 | **relation** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 545 | **calm** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 546 | **achievement** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 547 | **coming** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 548 | **pleasure** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 549 | **discrimination** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 550 | **search** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 551 | **height** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 552 | **solitude** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 553 | **himself** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 554 | **rūpāni** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 555 | **eightfold** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 556 | **sees** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 557 | **dying** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 558 | **reaction** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 559 | **connected** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 560 | **livelihood** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 561 | **conduct** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 562 | **succession** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 563 | **substituted** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 564 | **sectarianism** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 565 | **doubt** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 566 | **self-state** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 567 | **language** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 568 | **else** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 569 | **beings** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 570 | **apprehended** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 571 | **work** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 572 | **exist** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 573 | **false** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 574 | **wicked** | 6 | 289.70 | 1.0 | 🔵 low — common in general English |
| 575 | **resultant** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 576 | **training** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 577 | **sublime** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 578 | **unfavourable** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 579 | **perversions** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 580 | **conduce** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 581 | **attainments** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 582 | **theoretic** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 583 | **freedom** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 584 | **procedure** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 585 | **reflection** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 586 | **analysis** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 587 | **light** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 588 | **persistence** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 589 | **hatred** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 590 | **viz** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 591 | **unpleasant** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 592 | **working** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 593 | **cattāri** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 594 | **developed** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 595 | **unconscious** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 596 | **aṭṭhakkhattukaṃ** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 597 | **successively** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 598 | **sensory** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 599 | **turning** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 600 | **manifold** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 601 | **unbounded** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 602 | **must** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 603 | **existence** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 604 | **another** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 605 | **characteristics** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 606 | **understood** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 607 | **method** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 608 | **judgment** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 609 | **repugnance** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 610 | **seen** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 611 | **conditions** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 612 | **categories** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 613 | **give** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 614 | **got** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 615 | **life-faculty** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 616 | **nature** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 617 | **feminine** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 618 | **masculine** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 619 | **viscid** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 620 | **triplets** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 621 | **analogous** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 622 | **derivation** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 623 | **excluded** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 624 | **classed** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 625 | **disposition** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 626 | **general** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 627 | **delight** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 628 | **harm** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 629 | **intoxicant** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 630 | **dogmatize** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 631 | **true** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 632 | **therein** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 633 | **certain** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 634 | **unrestrained** | 5 | 241.42 | 1.0 | 🔵 low — common in general English |
| 635 | **cūḷantaradukaṃ** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 636 | **unperverted** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 637 | **piṭṭhidukaṃ** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 638 | **partake** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 639 | **friendship** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 640 | **causal** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 641 | **courtesy** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 642 | **moderation** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 643 | **perceiving** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 644 | **perceived** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 645 | **clear** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 646 | **disposing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 647 | **focussing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 648 | **rejoicing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 649 | **effort** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 650 | **precious** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 651 | **kept** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 652 | **preservation** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 653 | **scruples** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 654 | **hating** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 655 | **calming** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 656 | **tranquillizing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 657 | **tranquillity** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 658 | **portion** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 659 | **recitation** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 660 | **nutriments** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 661 | **main** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 662 | **content** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 663 | **following** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 664 | **omitted** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 665 | **fifth** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 666 | **suppressing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 667 | **high** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 668 | **ones** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 669 | **putting** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 670 | **catasso** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 671 | **paṭipadā** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 672 | **soḷasakkhattukaṃ** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 673 | **sixteen** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 674 | **yellow** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 675 | **seeing** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 676 | **gets** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 677 | **develop** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 678 | **deliverance** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 679 | **conception** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 680 | **sections** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 681 | **idea** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 682 | **feel** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 683 | **nothingness** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 684 | **non-perception** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 685 | **unknown** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 686 | **respect** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 687 | **attributes** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 688 | **addition** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 689 | **methods** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 690 | **toward** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 691 | **passions** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 692 | **inverted** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 693 | **namely** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 694 | **notion** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 695 | **takes** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 696 | **uprising** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 697 | **considered** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 698 | **qualities** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 699 | **root-condition** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 700 | **door** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 701 | **heard** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 702 | **hears** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 703 | **sapids** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 704 | **tactile** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 705 | **female** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 706 | **occupation** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 707 | **deportment** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 708 | **sky** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 709 | **vacuum** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 710 | **rūpassa** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 711 | **femininity** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 712 | **man** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 713 | **spatial** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 714 | **pair** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 715 | **bulk** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 716 | **proximity** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 717 | **non-faculty** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 718 | **sixfold** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 719 | **nine** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 720 | **take** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 721 | **recluses** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 722 | **brahmins** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 723 | **afore-mentioned** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 724 | **conversant** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 725 | **gotten** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 726 | **created** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 727 | **re-created** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 728 | **manifest** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 729 | **supervened** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 730 | **individual** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 731 | **cessation** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 732 | **fondness** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 733 | **fever** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 734 | **finite** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 735 | **shiftiness** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 736 | **theories** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 737 | **envy** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 738 | **meanness** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 739 | **relates** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 740 | **co-āsava** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 741 | **ill-will** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 742 | **mark** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 743 | **entranced** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 744 | **details** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 745 | **restrain** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 746 | **covetous** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 747 | **dejected** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 748 | **flow** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 749 | **dwell** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 750 | **keeps** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 751 | **watch** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 752 | **view** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 753 | **dread** | 4 | 193.13 | 1.0 | 🔵 low — common in general English |
| 754 | **place** | 2 | 173.82 | 1.8 | 🔵 low — common in general English |
| 755 | **quality** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 756 | **hetugocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 757 | **conditioned** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 758 | **mundane** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 759 | **cognized** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 760 | **āsavagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 761 | **saṃyojanagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 762 | **ganthagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 763 | **oghagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 764 | **yogagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 765 | **nīvaraṇagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 766 | **parāmāsagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 767 | **mahantaradukaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 768 | **detached** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 769 | **upādānagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 770 | **kilesagocchakaṃ** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 771 | **foolish** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 772 | **discreet** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 773 | **dark** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 774 | **bright** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 775 | **equivalent** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 776 | **processes** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 777 | **expression** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 778 | **restoration** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 779 | **recovery** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 780 | **soft** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 781 | **patience** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 782 | **amity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 783 | **failure** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 784 | **fallacy** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 785 | **calling** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 786 | **directness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 787 | **purpose** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 788 | **purposefulness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 789 | **fixing** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 790 | **stability** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 791 | **solidity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 792 | **absorbed** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 793 | **steadfastness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 794 | **inception** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 795 | **unfaltering** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 796 | **unflinching** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 797 | **endurance** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 798 | **bearing** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 799 | **opposite** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 800 | **superficiality** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 801 | **discernment** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 802 | **differentiation** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 803 | **erudition** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 804 | **subtlety** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 805 | **criticism** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 806 | **breadth** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 807 | **sagacity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 808 | **sword** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 809 | **glory** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 810 | **splendour** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 811 | **stone** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 812 | **continuance** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 813 | **sluggishness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 814 | **inertia** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 815 | **smoothness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 816 | **rigidity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 817 | **constituents** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 818 | **similar** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 819 | **respecting** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 820 | **follows** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 821 | **seq** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 822 | **seventh** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 823 | **eighth** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 824 | **chapter** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 825 | **dwelling** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 826 | **indifferent** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 827 | **while** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 828 | **repeated** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 829 | **ārammaṇāni** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 830 | **air** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 831 | **red** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 832 | **white** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 833 | **parittāni** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 834 | **stated** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 835 | **substitution** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 836 | **beautiful** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 837 | **ugly** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 838 | **appamāṇāni** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 839 | **manner** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 840 | **soḷasakkhattukāni** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 841 | **pity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 842 | **equanimity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 843 | **passed** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 844 | **believing** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 845 | **awakening** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 846 | **renounce** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 847 | **abstain** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 848 | **refrain** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 849 | **averse** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 850 | **leave** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 851 | **undone** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 852 | **incur** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 853 | **trespass** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 854 | **transgress** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 855 | **destroy** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 856 | **causeway** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 857 | **additional** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 858 | **iii** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 859 | **concepts** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 860 | **arahantship** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 861 | **thoroughly** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 862 | **flood** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 863 | **bias** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 864 | **pain** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 865 | **getting** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 866 | **hostility** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 867 | **abruptness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 868 | **usual** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 869 | **scarifying** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 870 | **excitement** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 871 | **done** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 872 | **vii** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 873 | **viii** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 874 | **science** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 875 | **division** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 876 | **consideration** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 877 | **floods** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 878 | **accumulation** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 879 | **act** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 880 | **ocean** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 881 | **sensibility** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 882 | **like** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 883 | **produces** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 884 | **earthy** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 885 | **hard** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 886 | **cohesiveness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 887 | **masculinity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 888 | **tangibles** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 889 | **source** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 890 | **answered** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 891 | **aspects** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 892 | **exposition** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 893 | **exactly** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 894 | **according** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 895 | **visibility** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 896 | **corruptions** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 897 | **perplexed** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 898 | **assignable** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 899 | **determined** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 900 | **holiness** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 901 | **appertaining** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 902 | **matters** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 903 | **happened** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 904 | **personal-external** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 905 | **languishing** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 906 | **cleaving** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 907 | **longing** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 908 | **consort** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 909 | **māra** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 910 | **rapacity** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 911 | **excited** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 912 | **pleasures** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 913 | **others** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 914 | **want** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 915 | **immoral** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 916 | **alms** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 917 | **sacrifice** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 918 | **offering** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 919 | **deeds** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 920 | **mother** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 921 | **father** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 922 | **reached** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 923 | **highest** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 924 | **realized** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 925 | **alone** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 926 | **bases** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 927 | **range** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 928 | **attainment** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 929 | **old** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 930 | **age** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 931 | **anyone** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 932 | **unguarded** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 933 | **guarded** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 934 | **sets** | 3 | 144.85 | 1.0 | 🔵 low — common in general English |
| 935 | **mātikā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 936 | **neutral** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 937 | **down** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 938 | **base** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 939 | **worth** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 940 | **excellent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 941 | **wrongfulness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 942 | **righteousness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 943 | **entail** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 944 | **bound** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 945 | **reactions** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 946 | **lead** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 947 | **harmful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 948 | **harmless** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 949 | **lightning** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 950 | **thunderbolt** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 951 | **explanations** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 952 | **expressions** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 953 | **dissolution** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 954 | **discretion** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 955 | **law** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 956 | **affirming** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 957 | **negating** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 958 | **upright** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 959 | **loveableness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 960 | **gateways** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 961 | **forgetfulness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 962 | **unintelligence** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 963 | **sign** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 964 | **morals** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 965 | **agitated** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 966 | **discontent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 967 | **kāmāvacarakusalaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 968 | **facility** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 969 | **brought** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 970 | **cittaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 971 | **process** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 972 | **access** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 973 | **continuous** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 974 | **adjusting** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 975 | **mirth** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 976 | **merriment** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 977 | **sukhaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 978 | **cittass** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 979 | **ekaggatā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 980 | **unperturbed** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 981 | **striving** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 982 | **exertion** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 983 | **zeal** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 984 | **ardour** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 985 | **vigour** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 986 | **burden** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 987 | **recollecting** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 988 | **remembering** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 989 | **guide** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 990 | **jīvitindriyaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 991 | **greediness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 992 | **infatuation** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 993 | **infatuated** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 994 | **varying** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 995 | **straightness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 996 | **twist** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 997 | **manāyatanaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 998 | **manoviññāṇadhātu** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 999 | **suññatavāro** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1000 | **list** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1001 | **previous** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1002 | **constituting** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1003 | **omissions** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1004 | **incompatible** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1005 | **substitute** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1006 | **upekkhā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1007 | **reply** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1008 | **sixth** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1009 | **omission** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1010 | **types** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1011 | **rūpāvacarakusalaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1012 | **divisions** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1013 | **self-evolved** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1014 | **free** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1015 | **grows** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1016 | **sure** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1017 | **waning** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1018 | **mindful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1019 | **self-aware** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1020 | **experiences** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1021 | **sense-consciousness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1022 | **whereof** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1023 | **declare** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1024 | **watchful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1025 | **dwelleth** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1026 | **utter** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1027 | **pañcakanayo** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1028 | **sustaining** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1029 | **artifices** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1030 | **aṭṭhakasiṇaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1031 | **water** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1032 | **stations** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1033 | **abhibhāyatanāni** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1034 | **mastery-formula** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1035 | **dve** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1036 | **suvaṇṇa-dubbaṇṇāni** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1037 | **idampi** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1038 | **deliverances** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1039 | **tīṇi** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1040 | **vimokkhāni** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1041 | **divine** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1042 | **brahmavihārajhānāni** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1043 | **discursive** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1044 | **clause** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1045 | **sympathy** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1046 | **foul** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1047 | **cut** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1048 | **pieces** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1049 | **arūpāvacarakusalaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1050 | **suddhikapaṭipadā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1051 | **self-awareness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1052 | **incitement** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1053 | **makes** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1054 | **truths** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1055 | **errors** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1056 | **uncommitted** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1057 | **suññataṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1058 | **appaṇihitaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1059 | **applying** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1060 | **vīsati** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1061 | **mahānayā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1062 | **advance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1063 | **efforts** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1064 | **diminished** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1065 | **strength** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1066 | **entire** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1067 | **residuum** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1068 | **absolutely** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1069 | **entirely** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1070 | **lusting** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1071 | **lustfulness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1072 | **badness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1073 | **penetration** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1074 | **inability** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1075 | **childishness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1076 | **obsession** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1077 | **barrier** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1078 | **dukkhaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1079 | **upset** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1080 | **opposition** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1081 | **churlishness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1082 | **disgust** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1083 | **dubiety** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1084 | **puzzlement** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1085 | **standing** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1086 | **cross-roads** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1087 | **collapse** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1088 | **uncertainty** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1089 | **evasion** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1090 | **hesitation** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1091 | **incapacity** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1092 | **stiffness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1093 | **disquietude** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1094 | **turmoil** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1095 | **twelve** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1096 | **thirteen** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1097 | **schematized** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1098 | **suddhika-suññataṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1099 | **mode** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1100 | **exercise** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1101 | **scheme** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1102 | **systems** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1103 | **perfected** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1104 | **concerned** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1105 | **inclusion** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1106 | **get** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1107 | **derivatives** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1108 | **below** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1109 | **catukkaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1110 | **pañcakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1111 | **chakkaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1112 | **sattakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1113 | **aṭṭhakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1114 | **navakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1115 | **dasakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1116 | **ekādasakaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1117 | **bonds** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1118 | **void** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1119 | **rid** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1120 | **involving** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1121 | **studentship** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1122 | **guidance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1123 | **dual** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1124 | **maintenance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1125 | **lucent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1126 | **field** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1127 | **hither** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1128 | **shore** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1129 | **impingeing** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1130 | **forming** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1131 | **hear** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1132 | **smelt** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1133 | **tasted** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1134 | **touched** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1135 | **touches** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1136 | **principles** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1137 | **short** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1138 | **noise** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1139 | **people** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1140 | **human** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1141 | **bark** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1142 | **leaves** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1143 | **flowers** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1144 | **sour** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1145 | **sweet** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1146 | **male** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1147 | **tension** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1148 | **tense** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1149 | **capacity** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1150 | **changing** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1151 | **easily** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1152 | **rough** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1153 | **upādāniyaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1154 | **reacts-and-impinges** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1155 | **react-or-impinge** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1156 | **indriyaṃ** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1157 | **potentialities** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1158 | **viññatti** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1159 | **relatives** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1160 | **vatthu** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1161 | **descriptions** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1162 | **specific** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1163 | **threefold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1164 | **production** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1165 | **opposites** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1166 | **above-named** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1167 | **potentiality** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1168 | **imagined** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1169 | **flame** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1170 | **heat** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1171 | **hot** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1172 | **sevenfold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1173 | **comprehensible** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1174 | **agreeable** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1175 | **obtainable** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1176 | **disagreeable** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1177 | **ninefold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1178 | **tenfold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1179 | **elevenfold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1180 | **activities** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1181 | **corrupt** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1182 | **baneful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1183 | **average** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1184 | **perceives** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1185 | **comprehends** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1186 | **trained** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1187 | **men** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1188 | **rules** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1189 | **rites** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1190 | **mere** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1191 | **remain** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1192 | **piling** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1193 | **lowest** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1194 | **topmost** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1195 | **acts** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1196 | **immediate** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1197 | **dependent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1198 | **firstly** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1199 | **stages** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1200 | **secondly** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1201 | **cultivating** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1202 | **unborn** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1203 | **dissolved** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1204 | **arrived** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1205 | **self-referable** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1206 | **showing** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1207 | **loving** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1208 | **considerateness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1209 | **causation** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1210 | **compliance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1211 | **affection** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1212 | **appetite** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1213 | **mumbling** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1214 | **hungering** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1215 | **envying** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1216 | **yoke** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1217 | **latent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1218 | **avarice** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1219 | **abhijjhā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1220 | **annoyance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1221 | **doing** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1222 | **someone** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1223 | **benefit** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1224 | **spirit** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1225 | **anger** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1226 | **intermediate** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1227 | **hold** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1228 | **different** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1229 | **won** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1230 | **uncompounded** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1231 | **repulsion** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1232 | **better** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1233 | **jealousy** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1234 | **gifts** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1235 | **hospitality** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1236 | **reverence** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1237 | **mean** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1238 | **aforementioned** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1239 | **kāyagantho** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1240 | **distinguish** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1241 | **indisposition** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1242 | **unwieldiness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1243 | **sleep** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1244 | **lawful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1245 | **unlawful** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1246 | **effects** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1247 | **sense-desires** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1248 | **point** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1249 | **kilesā** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1250 | **term** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1251 | **stand** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1252 | **lower** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1253 | **heaven** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1254 | **devas** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1255 | **inclusive** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1256 | **potential** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1257 | **happily** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1258 | **entrance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1259 | **associates** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1260 | **likeness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1261 | **origins** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1262 | **accordance** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1263 | **norm** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1264 | **said** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1265 | **captiousness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1266 | **regard** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1267 | **deference** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1268 | **frequent** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1269 | **company** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1270 | **associate** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1271 | **persons** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1272 | **resort** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1273 | **devoted** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1274 | **enthusiastic** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1275 | **gentle** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1276 | **feels** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1277 | **recognizes** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1278 | **food** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1279 | **purposes** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1280 | **sport** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1281 | **charm** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1282 | **doors** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1283 | **attains** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1284 | **sickness** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1285 | **struggles** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1286 | **emancipation** | 2 | 96.57 | 1.0 | 🔵 low — common in general English |
| 1287 | **time** | 1 | 77.25 | 1.6 | 🔵 low — common in general English |
| 1288 | **homage** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1289 | **blessed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1290 | **arahant** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1291 | **perfectly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1292 | **enlightened** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1293 | **abhidhammapiṭake** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1294 | **dhammasaṅgaṇīpāḷi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1295 | **tikamātikā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1296 | **building** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1297 | **pulling** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1298 | **adept** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1299 | **dukamātikā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1300 | **immaterial** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1301 | **suttantikadukamātikā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1302 | **resemble** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1303 | **comparable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1304 | **explanation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1305 | **infiniteness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1306 | **finiteness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1307 | **indiscretion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1308 | **unguardedness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1309 | **guardedness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1310 | **computing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1311 | **developing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1312 | **occasions** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1313 | **unfalteringness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1314 | **cittuppādakaṇḍaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1315 | **padabhājanī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1316 | **risen** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1317 | **phasso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1318 | **touching** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1319 | **vedana** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1320 | **saññā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1321 | **pīti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1322 | **transport** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1323 | **experience** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1324 | **saddhindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1325 | **trusting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1326 | **professing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1327 | **confidence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1328 | **assurance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1329 | **viriyindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1330 | **satindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1331 | **samādhindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1332 | **paññindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1333 | **goad** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1334 | **imagination** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1335 | **manindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1336 | **somanassin-driyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1337 | **sammā-diṭṭhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1338 | **sammā-sankappo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1339 | **sammā-vāyāmo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1340 | **sammā-samādhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1341 | **saddhābalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1342 | **viriyabalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1343 | **sati-balaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1344 | **samādhi-balaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1345 | **paññābalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1346 | **hiribalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1347 | **ottappabalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1348 | **alobho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1349 | **greedy** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1350 | **adoso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1351 | **spleen** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1352 | **amoho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1353 | **anabh-ijjhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1354 | **avyāpādo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1355 | **sammādiṭṭhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1356 | **hiri** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1357 | **ottappaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1358 | **repose** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1359 | **kāyappassaddhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1360 | **cittapassaddhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1361 | **kāyalahutā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1362 | **alertness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1363 | **cittalahutā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1364 | **kāyamudutā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1365 | **cittamudutā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1366 | **kāyakammaññatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1367 | **workableness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1368 | **cittakammaññatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1369 | **kayapāguññatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1370 | **competence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1371 | **efficient** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1372 | **cittapāguññatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1373 | **kāyujjukatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1374 | **deflection** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1375 | **cittujjukatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1376 | **sati** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1377 | **sampajaññaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1378 | **samatho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1379 | **paggāho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1380 | **avikkhepo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1381 | **pada-bhājaniyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1382 | **sangahavāraṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1383 | **koṭṭhāsavāraṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1384 | **koṭṭhāsavāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1385 | **āyatanāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1386 | **dhātuyo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1387 | **āhārā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1388 | **indriyāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1389 | **balāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1390 | **hetu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1391 | **dhammāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1392 | **dhammadhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1393 | **phassāharo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1394 | **manosañcetanāhāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1395 | **willing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1396 | **purposiveness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1397 | **cogitation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1398 | **viññāṇāhāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1399 | **pañcangikaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1400 | **jhānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1401 | **pañcangiko** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1402 | **maggo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1403 | **tayohetū** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1404 | **regarded** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1405 | **distinguishable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1406 | **species** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1407 | **dealt** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1408 | **sankhāra-skandha** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1409 | **intuitio** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1410 | **catukkanayo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1411 | **including** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1412 | **course** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1413 | **formulation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1414 | **āramaṇāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1415 | **soḷasakkhat-tukaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1416 | **artifice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1417 | **fire** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1418 | **blue-black** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1419 | **induction** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1420 | **aparampi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1421 | **nīlāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1422 | **expanse** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1423 | **luminousness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1424 | **pītāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1425 | **fair** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1426 | **mettā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1427 | **works** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1428 | **unbiassed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1429 | **adding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1430 | **karūṇā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1431 | **muditā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1432 | **fullness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1433 | **asubha-jhānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1434 | **asubhajhānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1435 | **bloated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1436 | **discoloured** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1437 | **festering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1438 | **cracked** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1439 | **skin** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1440 | **gnawn** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1441 | **mangled** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1442 | **mutilated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1443 | **bloody** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1444 | **infested** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1445 | **worms** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1446 | **skeleton** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1447 | **arūpajhānāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1448 | **arūpajjhānāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1449 | **syā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1450 | **wont** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1451 | **imbued** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1452 | **viññāṇañcāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1453 | **boundless** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1454 | **ākiñcaññāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1455 | **neva-saññā-nāsaññāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1456 | **tebhūmakakusalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1457 | **rises** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1458 | **modified** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1459 | **lokuttarakusalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1460 | **elation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1461 | **component** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1462 | **anaññātaññassāmītindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1463 | **realization** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1464 | **unrealized** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1465 | **uncomprehended** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1466 | **unattained** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1467 | **undiscerned** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1468 | **sammā-vācā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1469 | **sammā-kammanto** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1470 | **sammā-ājīvo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1471 | **unpractised** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1472 | **characterizing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1473 | **awareness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1474 | **items** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1475 | **schemata** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1476 | **suññatamūlakapaṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1477 | **suññata-mūlaka-paṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1478 | **aimless** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1479 | **appaṇihitamūlakapaṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1480 | **appaṇihita-mūlaka-paṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1481 | **adhipati** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1482 | **vehicle** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1483 | **series** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1484 | **mystic** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1485 | **potencies** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1486 | **peace** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1487 | **influences** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1488 | **adhipaṭi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1489 | **dvādasa** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1490 | **akusalāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1491 | **micchāsankappo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1492 | **miccha-diṭṭhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1493 | **ahirikabalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1494 | **anottappabalaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1495 | **co-ordination** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1496 | **comprehend** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1497 | **compare** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1498 | **consider** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1499 | **demonstrate** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1500 | **folly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1501 | **vagueness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1502 | **obfuscation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1503 | **bond** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1504 | **again** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1505 | **twice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1506 | **item** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1507 | **inserted** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1508 | **domanassindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1509 | **disordered** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1510 | **temper** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1511 | **syntheses** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1512 | **vicikicchā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1513 | **hesitating** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1514 | **uddhaccaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1515 | **abyākatavipāko** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1516 | **kusalavipākapañcaviññāṇāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1517 | **kusalavipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1518 | **manodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1519 | **kusalavipākamanodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1520 | **directing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1521 | **self-collected-ness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1522 | **kusala-vipākamanoviññāṇadhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1523 | **kusalavipākamanoviññāṇadhātusomanassasahagatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1524 | **restricted** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1525 | **connotation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1526 | **used** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1527 | **kusalavipākamanoviññāṇadhātuupekkhāsahagatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1528 | **aṭṭha** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1529 | **mahāvipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1530 | **aṭṭhamahāvipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1531 | **rūpāvacaravipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1532 | **formulae** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1533 | **arūpāvacaravipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1534 | **frame** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1535 | **lokuttaravipāka-paṭhamamaggavipākā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1536 | **repeating** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1537 | **suddhikasuññataṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1538 | **suññata-paṭipāda** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1539 | **suññatapaṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1540 | **constitute** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1541 | **suddhika-appaṇihitaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1542 | **suddhikaappaṇihitaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1543 | **appaṇihita-paṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1544 | **appaṇihitapaṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1545 | **turn** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1546 | **exercises** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1547 | **actually** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1548 | **paragraph** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1549 | **chandādhipateyyaṃ-suddhika-paṭipāda** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1550 | **chandādhipateyyasuddhikapaṭipadā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1551 | **chandādhipateyyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1552 | **chandādhipateyyasuddhikasuññatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1553 | **pro-gress** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1554 | **dutiyādimaggavipāko** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1555 | **aññatāvindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1556 | **doctrines** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1557 | **akusalavipākaabyākataṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1558 | **akusalavipākapañcaviññāṇāni** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1559 | **akusalavipākamanodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1560 | **akusalavipākamanoviññāṇadhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1561 | **ahetukakiriyāabyākataṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1562 | **kiriyāmanodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1563 | **remainder** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1564 | **passages** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1565 | **kiriyāmanoviññāṇadhātusomanassasahagatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1566 | **imperturbed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1567 | **kiriyāmanoviññāṇadhātuupekkhāsahagatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1568 | **sahetukakāmāvacarakiriyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1569 | **rūpāvacarakiriyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1570 | **arūpā-vacara-kiriyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1571 | **arūpāvacarakiriyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1572 | **opening** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1573 | **rūpakaṇḍaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1574 | **uddeso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1575 | **finally** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1576 | **ekakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1577 | **sabbaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1578 | **rūpaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1579 | **dukaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1580 | **tikaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1581 | **mātika** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1582 | **table** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1583 | **contents** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1584 | **quantitative** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1585 | **number** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1586 | **uncorrelated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1587 | **dichotomized** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1588 | **singly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1589 | **exclusion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1590 | **afford** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1591 | **affording** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1592 | **inductive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1593 | **classifications** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1594 | **fifthly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1595 | **rūpavibhatti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1596 | **ekakaniddeso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1597 | **dukaniddeso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1598 | **upādābhājanīyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1599 | **endowed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1600 | **property** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1601 | **productive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1602 | **tending** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1603 | **small** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1604 | **account** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1605 | **entailing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1606 | **retribution** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1607 | **unavailing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1608 | **ethical** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1609 | **apparent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1610 | **impermanent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1611 | **subject** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1612 | **positive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1613 | **negative** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1614 | **duvidhena** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1615 | **rūpa-sangaho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1616 | **sights** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1617 | **cakkhāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1618 | **physical** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1619 | **blue** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1620 | **black** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1621 | **crimson** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1622 | **bronze** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1623 | **green-coloured** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1624 | **hue** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1625 | **mango-bud** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1626 | **big** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1627 | **circular** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1628 | **oval** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1629 | **square** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1630 | **hexagonal** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1631 | **octagonal** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1632 | **hekkaidecagonal** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1633 | **low** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1634 | **shady** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1635 | **glowing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1636 | **dim** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1637 | **dull** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1638 | **frosty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1639 | **smoky** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1640 | **dusty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1641 | **disc** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1642 | **moon** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1643 | **sun** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1644 | **stars** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1645 | **mirror** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1646 | **gem** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1647 | **shell** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1648 | **pearl** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1649 | **cat** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1650 | **gold** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1651 | **silver** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1652 | **producing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1653 | **drums** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1654 | **tabors** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1655 | **chank-shells** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1656 | **tom-toms** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1657 | **singing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1658 | **music** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1659 | **clashing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1660 | **concussion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1661 | **substances** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1662 | **wind** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1663 | **sap** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1664 | **verminous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1665 | **putrid** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1666 | **stems** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1667 | **bitter** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1668 | **pungent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1669 | **saline** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1670 | **alkaline** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1671 | **acrid** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1672 | **astringent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1673 | **nice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1674 | **nauseous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1675 | **itthindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1676 | **purisindriyaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1677 | **kāyaviññatti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1678 | **intentness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1679 | **response** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1680 | **advances** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1681 | **recedes** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1682 | **fixes** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1683 | **gaze** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1684 | **glances** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1685 | **around** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1686 | **retracts** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1687 | **arm** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1688 | **stretches** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1689 | **vaciviññatti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1690 | **voice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1691 | **enunciation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1692 | **utterance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1693 | **noises** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1694 | **articulate** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1695 | **expresses** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1696 | **ākāsa-dhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1697 | **lahutā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1698 | **softness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1699 | **non-rigidity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1700 | **serviceableness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1701 | **workable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1702 | **upacayo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1703 | **santati** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1704 | **jaratā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1705 | **ageing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1706 | **decrepitude** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1707 | **hoariness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1708 | **wrinkles** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1709 | **shrinkage** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1710 | **length** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1711 | **days** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1712 | **hypermaturity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1713 | **aniccatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1714 | **destruction** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1715 | **disease** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1716 | **breaking-up** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1717 | **decline** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1718 | **kabaḷinkāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1719 | **āhāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1720 | **boiled** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1721 | **rice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1722 | **gruel** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1723 | **flour** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1724 | **fish** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1725 | **flesh** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1726 | **milk** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1727 | **curds** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1728 | **butter** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1729 | **cheese** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1730 | **tila-oil** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1731 | **cane-syrup** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1732 | **region** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1733 | **eaten** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1734 | **chewed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1735 | **swallowed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1736 | **digested** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1737 | **juice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1738 | **alive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1739 | **upāda** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1740 | **phoṭṭhabbāyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1741 | **lambent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1742 | **calorific** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1743 | **gaseous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1744 | **aerial** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1745 | **smooth** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1746 | **heavy** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1747 | **aqueous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1748 | **āpodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1749 | **viscous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1750 | **upādiṇṇaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1751 | **upādiṇṇ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1752 | **anupādiṇṇ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1753 | **sappaṭighaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1754 | **woman** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1755 | **mahābhūtaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1756 | **citta-samuṭṭhānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1757 | **citta-saha-bhū** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1758 | **citt** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1759 | **ānuparivatti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1760 | **ajjhattikaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1761 | **bāhiraṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1762 | **oḷārikaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1763 | **sukhumaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1764 | **dūre** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1765 | **santike** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1766 | **cakkhusamphassassa** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1767 | **ārammaṇaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1768 | **āyatanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1769 | **dhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1770 | **principle** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1771 | **contradictory** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1772 | **insertion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1773 | **indicated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1774 | **evolution** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1775 | **contradictories** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1776 | **analogously** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1777 | **positives** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1778 | **nutrition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1779 | **triple** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1780 | **tikaniddeso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1781 | **vitality** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1782 | **sex-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1783 | **intension** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1784 | **quoted** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1785 | **presence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1786 | **ending** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1787 | **inquired** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1788 | **definition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1789 | **schema** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1790 | **earth-element** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1791 | **paṭhavī-dhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1792 | **hardness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1793 | **fluid-element** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1794 | **apodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1795 | **heat-element** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1796 | **tejodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1797 | **air-element** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1798 | **vāyodhātu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1799 | **fluctuation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1800 | **inflation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1801 | **vision-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1802 | **hearing-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1803 | **smell-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1804 | **taste-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1805 | **body-faculty** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1806 | **original** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1807 | **vision-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1808 | **hearing-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1809 | **smell-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1810 | **taste-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1811 | **body-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1812 | **shape-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1813 | **sound-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1814 | **odour-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1815 | **sapid-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1816 | **tangible-sphere** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1817 | **eleven** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1818 | **lastly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1819 | **nikkhepakaṇḍaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1820 | **tikanikkhepaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1821 | **involve** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1822 | **yielding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1823 | **ease-yielding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1824 | **ignorant** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1825 | **master** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1826 | **discipline** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1827 | **held** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1828 | **outside** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1829 | **appertain** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1830 | **recluse** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1831 | **emotional** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1832 | **perceptual** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1833 | **active** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1834 | **experienced** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1835 | **thirdly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1836 | **peculiar** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1837 | **named** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1838 | **path-causes** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1839 | **path-governed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1840 | **governor** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1841 | **carried** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1842 | **feelings** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1843 | **perceptions** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1844 | **matured** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1845 | **extinct** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1846 | **changed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1847 | **terminated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1848 | **exterminated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1849 | **issue** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1850 | **individuals** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1851 | **tender** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1852 | **care** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1853 | **forbearance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1854 | **seeking** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1855 | **compassion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1856 | **malignity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1857 | **dukanikkhepaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1858 | **rāgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1859 | **sarāgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1860 | **seducing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1861 | **anunayo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1862 | **anurodho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1863 | **delighting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1864 | **nandī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1865 | **lustful** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1866 | **nandī-rāgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1867 | **cittassasarāgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1868 | **wanting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1869 | **icchā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1870 | **mucchā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1871 | **gulping** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1872 | **devouring** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1873 | **ajjhosānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1874 | **cupidity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1875 | **gedho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1876 | **voracity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1877 | **paligedho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1878 | **saṇgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1879 | **slough** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1880 | **panko** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1881 | **ejā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1882 | **illusion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1883 | **māyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1884 | **genitrix** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1885 | **janikā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1886 | **progenitrix** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1887 | **sañjananī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1888 | **seamstress** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1889 | **sibbanī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1890 | **ensnares** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1891 | **jālinī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1892 | **flowing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1893 | **stream** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1894 | **saritā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1895 | **diffused** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1896 | **visattikā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1897 | **thread** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1898 | **suttaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1899 | **diffusion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1900 | **visatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1901 | **urges** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1902 | **āyūhanī** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1903 | **dutiyā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1904 | **aiming** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1905 | **paniḍhi** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1906 | **leads** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1907 | **bhavanetti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1908 | **forest** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1909 | **vanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1910 | **vanatho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1911 | **intimacy** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1912 | **santhavo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1913 | **sineho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1914 | **apekkhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1915 | **paṭibandhu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1916 | **āsā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1917 | **hoping** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1918 | **āsiṃsanā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1919 | **anticipation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1920 | **āsiṃsitattaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1921 | **rūpāsā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1922 | **wealth** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1923 | **children** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1924 | **jappā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1925 | **muttering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1926 | **murmuring** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1927 | **self-indulgence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1928 | **loluppaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1929 | **self-indulging** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1930 | **intemperateness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1931 | **puñcikatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1932 | **sādukamyatā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1933 | **incestuous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1934 | **adhammarāgo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1935 | **lawless** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1936 | **visamalobho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1937 | **wish** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1938 | **nikanti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1939 | **nikāmanā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1940 | **entreating** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1941 | **patthanā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1942 | **pihanā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1943 | **imploring** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1944 | **sampatthanā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1945 | **indulgence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1946 | **kāmataṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1947 | **bhavataṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1948 | **non-existence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1949 | **vibhava-taṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1950 | **immateriality** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1951 | **dhammataṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1952 | **ogho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1953 | **yogo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1954 | **gantho** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1955 | **upādānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1956 | **obstruction** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1957 | **āvaraṇaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1958 | **nīvaraṇaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1959 | **covering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1960 | **chadanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1961 | **bondage** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1962 | **bandhanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1963 | **depravity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1964 | **upakkileso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1965 | **anusayo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1966 | **pariyuṭṭhānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1967 | **creeper** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1968 | **latā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1969 | **vevicchaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1970 | **dukkhanidānaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1971 | **dukkhappabhavo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1972 | **trap** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1973 | **mārapāso** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1974 | **fish-hook** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1975 | **mārabalisaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1976 | **domain** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1977 | **māravisayo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1978 | **flux** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1979 | **sandataṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1980 | **fishing-net** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1981 | **jalaṃtaṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1982 | **leash** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1983 | **gaddulataṇhā** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1984 | **samuddo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1985 | **dear** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1986 | **conferred** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1987 | **conferring** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1988 | **confer** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1989 | **dislike** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1990 | **groundlessly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1991 | **vexation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1992 | **resentment** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1993 | **ill-temper** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1994 | **irritation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1995 | **indignation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1996 | **antipathy** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1997 | **abhorrence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1998 | **detestation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 1999 | **fuming** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2000 | **wrath** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2001 | **derangement** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2002 | **comprehension** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2003 | **sounding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2004 | **judging** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2005 | **perspicacity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2006 | **unwisdom** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2007 | **stupidity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2008 | **obtuseness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2009 | **obsessed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2010 | **indeterminates** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2011 | **kāmavacarahetū** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2012 | **exclusively** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2013 | **react** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2014 | **supra-mundane** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2015 | **āsava-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2016 | **thirst** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2017 | **yearning** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2018 | **rebirths** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2019 | **includes** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2020 | **saṃyojana-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2021 | **languor** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2022 | **lowly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2023 | **overweening** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2024 | **conceitedness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2025 | **loftiness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2026 | **haughtiness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2027 | **flaunting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2028 | **flag** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2029 | **assumption** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2030 | **self-advertisement** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2031 | **supplement** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2032 | **issāsaṃyojanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2033 | **enviousness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2034 | **mood** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2035 | **worship** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2036 | **accruing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2037 | **maccharisaṃyojanaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2038 | **meannesses** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2039 | **families** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2040 | **reputation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2041 | **grudging** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2042 | **ignobleness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2043 | **niggardliness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2044 | **generosity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2045 | **gantha-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2046 | **vyāpādo** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2047 | **so-called** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2048 | **excepting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2049 | **ogha-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2050 | **yoga-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2051 | **adhering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2052 | **cohering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2053 | **clinging** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2054 | **stickiness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2055 | **stiffening** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2056 | **shrouding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2057 | **enveloping** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2058 | **barricading** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2059 | **within** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2060 | **drowsiness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2061 | **slumbering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2062 | **somnolence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2063 | **fidgeting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2064 | **over-scrupulousness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2065 | **conscience** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2066 | **parāmāsa-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2067 | **contagion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2068 | **ahantara-dukaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2069 | **sense-cognition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2070 | **ideational** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2071 | **intellect** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2072 | **upādāna-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2073 | **attribute** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2074 | **puppet-show** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2075 | **fording-place** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2076 | **specified** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2077 | **kilesa-gocchakaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2078 | **severally** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2079 | **edition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2080 | **rendered** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2081 | **etymologically** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2082 | **fit** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2083 | **stock** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2084 | **ways** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2085 | **nearer** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2086 | **usage** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2087 | **kilesa** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2088 | **earliest** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2089 | **pāli** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2090 | **find** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2091 | **vinaya** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2092 | **dhamma** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2093 | **unregenerate** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2094 | **side** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2095 | **supplementary** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2096 | **congenial** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2097 | **uncongenial** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2098 | **waveless** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2099 | **deep** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2100 | **woe** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2101 | **beneath** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2102 | **parinimittavasavatti** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2103 | **brahma-world** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2104 | **akaniṭṭha** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2105 | **gods** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2106 | **denizens** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2107 | **limit** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2108 | **suttantikadukanikkhepaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2109 | **misconduct** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2110 | **enumeration** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2111 | **designation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2112 | **current** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2113 | **denomination** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2114 | **assigning** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2115 | **interpretation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2116 | **distinctive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2117 | **discourse** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2118 | **non-rebirth** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2119 | **hereafter** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2120 | **ultimate** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2121 | **futurity** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2122 | **rest** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2123 | **ninth** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2124 | **tenth** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2125 | **surly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2126 | **refractious** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2127 | **contumacious** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2128 | **contrariness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2129 | **unbelievers** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2130 | **uneducated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2131 | **mean-spirited** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2132 | **witless** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2133 | **entangled** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2134 | **tractable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2135 | **amenable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2136 | **refraining** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2137 | **contradiction** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2138 | **devotion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2139 | **believers** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2140 | **virtuous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2141 | **educated** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2142 | **generous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2143 | **wise** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2144 | **mixed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2145 | **termed** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2146 | **eighteen** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2147 | **odorous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2148 | **grief** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2149 | **lamentation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2150 | **despair** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2151 | **whole** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2152 | **mass** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2153 | **discerning** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2154 | **uprightness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2155 | **deflexion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2156 | **gentleness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2157 | **lowliness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2158 | **long-suffering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2159 | **rudeness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2160 | **complacency** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2161 | **self-restraint** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2162 | **lovely** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2163 | **insolent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2164 | **scabrous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2165 | **harsh** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2166 | **vituperative** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2167 | **bordering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2168 | **conducive** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2169 | **innocuous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2170 | **affectionate** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2171 | **goes** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2172 | **urbane** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2173 | **acceptable** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2174 | **generally** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2175 | **spoken** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2176 | **polished** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2177 | **friendly** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2178 | **needs** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2179 | **shows** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2180 | **untended** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2181 | **unwatched** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2182 | **carelessness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2183 | **adornment** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2184 | **insatiableness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2185 | **tended** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2186 | **watched** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2187 | **restrained** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2188 | **attractions** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2189 | **suffice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2190 | **sustenance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2191 | **allaying** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2192 | **pangs** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2193 | **hunger** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2194 | **aiding** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2195 | **practice** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2196 | **subdue** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2197 | **mine** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2198 | **blamelessness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2199 | **comfort** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2200 | **unmindfulness** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2201 | **lapse** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2202 | **memory** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2203 | **non-recollection** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2204 | **non-remembrance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2205 | **oblivion** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2206 | **computation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2207 | **pursuing** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2208 | **multiplying** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2209 | **immorality** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2210 | **fallacies** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2211 | **implies** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2212 | **earnest** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2213 | **refers** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2214 | **bhikkhu** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2215 | **brings** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2216 | **firm** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2217 | **confused** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2218 | **frequently** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2219 | **practised** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2220 | **abound** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2221 | **uses** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2222 | **a-going** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2223 | **reaches** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2224 | **forward** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2225 | **dissatisfied** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2226 | **shrinking** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2227 | **thorough** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2228 | **persevering** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2229 | **unresting** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2230 | **performance** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2231 | **stagnation** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2232 | **assiduous** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2233 | **repetition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2234 | **attend** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2235 | **reminiscent** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2236 | **births** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2237 | **decease** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2238 | **renascence** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2239 | **intoxicants** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2240 | **twofold** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2241 | **nirvāna** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2242 | **entitled** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2243 | **deposition** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2244 | **aṭṭhakathākaṇḍaṃ** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2245 | **tikaatthuddhāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2246 | **dukaatthuddhāro** | 1 | 48.28 | 1.0 | ⚪ very low — function / universal word |
| 2247 | **every** | 7 | 40.56 | 0.12 | ⚪ very low — function / universal word |

---

## Observations

### 1. Text-exclusive coinages dominate the top
The highest-scoring terms are overwhelmingly **Rhys Davids coinages** — Victorian English vocabulary pressed into service for Pāli Abhidhamma concepts.
Words like *self-collectedness*, *wieldiness*, *tractableness*, *pliancy* barely exist outside this translation, giving them near-maximum IDF.

### 2. Buddhist technical register
A tight cluster — *skandha*, *jhāna*, *āsava*, *supramundane*, *incorporeal* — forms the Buddhist technical register. These score extremely high because they belong to a specialist domain absent from general English, and they recur in every paragraph.

### 3. The 'falsely familiar' vocabulary problem
Rhys Davids consciously chose ordinary English words — *zest*, *ease*, *synergies*, *contact*, *feeling* — to avoid Pāli transliteration. These occupy a mid-tier TF-IDF band: very frequent here, but their IDF is moderate because they do have a general English presence. They look everyday but carry specialist meaning.

### 4. Repetition as structure inflates TF
The *Dhammasaṅgaṇī* is formally repetitive by design (Buddhist catechism). Every mental factor is defined with the same formula across hundreds of consciousness types. Even moderately rare words (*volition*, *mindfulness*, *concomitant*) achieve unusually high raw frequencies relative to any other English text of equivalent length.

---

*Corpus reference: BNC (100 M words, Leech et al.) · COCA (450 M words, Davies 2008–) · General Service List (West 1953) · Oxford 3000.*  
*Generated 2026-06-02 by `generate_termbase.py`.*