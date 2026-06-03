# Pāli keyword sense clusters (Pāli-only co-occurrence)

- Pāli source  : `1-SOURCES/Text/pi-1.md`
- English used : **none** (Pāli-only pipeline)
- Keyword list : `pi-keywords.txt`
- Pāli blocks  : 1780
- Cluster threshold: Jaccard distance ≤ 0.5
- Pre-cluster filters: pi blocks ≥ 2, pi DF ≤ 0.30, Dice ≥ 0.1, top 10 co-lemmas
- Mapped 500/500 lemmas → 1318 sense clusters

> Each sense cluster is a group of Pāli co-lemmas that tend to appear in the same blocks as the target keyword. Multiple co-lemmas in one cluster ⇒ related usage context. Multiple clusters ⇒ likely polysemy or distinct grammatical roles. Cohesion = average pairwise Jaccard similarity of co-lemma block-sets within the cluster.

---

## Compact form

- **dhamma**: (1) kusala, phassa, avikkhepa, yasmiṃ, jhāna, bhāveti, paṭhama; (2) magga; (3) viññāṇakkhandha; (4) vipāka
- **rūpa**: (1) taṃ; (2) kabaḷīkāra, āhāra; (3) cakkhāyatana; (4) rūpāyatana; (5) yaṃ; (6) bāhira; (7) mahābhūta; (8) upāda; (9) phoṭṭhabbāyatana
- **kusala**: (1) yasmiṃ, avikkhepa, bhāveti, phassa, jhāna, paṭhama, vivicceva, kāma, magga; (2) vipāka
- **phassa**: (1) yasmiṃ, avikkhepa, jhāna, bhāveti, kusala, paṭhama, vivicceva, kāma; (2) magga, rūpūpapattiya
- **avikkhepa**: (1) yasmiṃ, phassa, bhāveti, jhāna, paṭhama, kusala, vivicceva, kāma; (2) rūpūpapattiya, magga
- **jhāna**: (1) bhāveti, yasmiṃ, paṭhama, avikkhepa, phassa, vivicceva, kusala, kāma, magga, rūpūpapattiya
- **viññāṇakkhandha**: (1) vedanākkhandha; (2) rūpāvacara, kāmāvacara, arūpāvacara, kusalākusalābyākata; (3) ṭhapetva; (4) saṅkhārakkhandha, saññākkhandha; (5) dhātu, asaṅkhata
- **magga**: (1) rūpūpapattiya, jhāna, bhāveti, yasmiṃ, avikkhepa, phassa, paṭhama, kusala, vivicceva, kāma
- **bhāveti**: (1) jhāna, yasmiṃ, paṭhama, avikkhepa, vivicceva, kāma, phassa, kusala, rūpūpapattiya; (2) pahāna
- **āhāra**: (1) kabaḷīkāra, taṃ; (2) rūpāyatana, bāhira; (3) atthi, ākāsadhātu, panaññampi; (4) cakkhāyatana; (5) khandha; (6) itthindriya
- **vedanākkhandha**: (1) viññāṇakkhandha; (2) saṅkhārakkhandha, saññākkhandha; (3) ṭhapetva; (4) dhātu, asaṅkhata, rūpāvacara, sabbañca, kāmāvacara, arūpāvacara
- **paṭhama**: (1) bhāveti, vivicceva, kāma, jhāna, yasmiṃ, avikkhepa, phassa, kusala, rūpūpapattiya; (2) dandhābhiñña
- **citta**: (1) manindriya; (2) samādhindriya, samatha, samādhibala; (3) paṭiccasamuppanna, cittassekaggata, aññepi, arūpina; (4) uppanna; (5) ṭhiti
- **vipāka**: (1) bhūmīsu, tīsu, kiriyābyākata, catūsu; (2) kusala; (3) abyākata, pahāna, pattiya, bhūmiya, apacayagāmiṃ
- **kabaḷīkāra**: (1) āhāra, taṃ; (2) rūpāyatana, bāhira; (3) ākāsadhātu, panaññampi, āpodhātu; (4) cakkhāyatana; (5) itthindriya; (6) kāyaviññatti
- **ṭhapetva**: (1) avasesa; (2) viññāṇakkhandha, vedanākkhandha; (3) rūpāvacara, kāmāvacara; (4) saṅkhārakkhandha, saññākkhandha, cittassekaggata; (5) etthuppanna; (6) akusala
- **kāma**: (1) vivicceva, paṭhama, bhāveti, jhāna, yasmiṃ, avikkhepa, phassa, rūpūpapattiya, kusala; (2) dandhābhiñña
- **vivicceva**: (1) kāma, paṭhama, bhāveti, jhāna, yasmiṃ, avikkhepa, rūpūpapattiya, phassa; (2) dandhābhiñña, dukkhapaṭipada
- **tattha**: (1) vuccati, ayaṃ; (2) evarūpa, vipariyāsaggāha, diṭṭhi, diṭṭhigata; (3) pajānana, dhammavicaya, paññā; (4) citta
- **cakkhāyatana**: (1) kāyāyatana, ajjhattika; (2) taṃ; (3) kabaḷīkāra, āhāra; (4) rasāyatana, gandhāyatana, rūpāyatana; (5) phoṭṭhabbāyatana; (6) upāda
- **akusala**: (1) bhūmīsu, tīsu, kiriyābyākata, vipāka, catūsu; (2) pāpaka, samāpattiya; (3) ṭhapetva, avasesa; (4) vattabba
- **vuccati**: (1) tattha, ayaṃ; (2) evarūpa, vipariyāsaggāha, diṭṭhi, diṭṭhigata; (3) pajānana, dhammavicaya, paññā; (4) pubbanta
- **vedana**: (1) sañña, cetana, manindriya, aññepi; (2) vedayita, cetosamphassaja, sāta, cetasika, yaṃ; (3) sukha
- **cattāra**: (1) cattāri, nibbānañca, sāmaññaphala; (2) khandha, dvāyatana, ekaṃ, ekā, dhātuya, dhammadhātu, dhammāyatana
- **rūpāyatana**: (1) bāhira, kabaḷīkāra, āhāra, taṃ; (2) gandhāyatana, rasāyatana, panaññampi, phoṭṭhabbāyatana, saddāyatana, kamma
- **kāmāvacara**: (1) rūpāvacara, arūpāvacara, viññāṇakkhandha, apariyāpanna; (2) kusalākusalābyākata; (3) sāsava, rūpakkhandha; (4) ṭhapetva, avasesa; (5) sabbañca
- **katatta**: (1) kamma; (2) panaññampi, ākāsadhātu, atthi, gandhāyatana; (3) tasseva, abyākata, bhāvitatta, vipāka; (4) āpodhātu
- **apariyāpanna**: (1) dhātu, asaṅkhata; (2) rūpāvacara, kāmāvacara, arūpāvacara; (3) sāmaññaphala, magga, cattāri, cattāra; (4) maggaphala
- **jīvitindriya**: (1) aññepi, arūpina, cittassekaggata, paṭiccasamuppanna, atthi, cetana, vīriyindriya, vicāra, paggāha, samādhindriya
- **rūpāvacara**: (1) arūpāvacara, kāmāvacara, viññāṇakkhandha; (2) kusalākusalābyākata; (3) apariyāpanna, dhātu, vedanākkhandha; (4) sāsava, rūpakkhandha; (5) ṭhapetva
- **rūpūpapattiya**: (1) bhāveti, magga, paṭhama, jhāna, vivicceva, yasmiṃ, kāma; (2) passati, arūpasaññī, abhibhuyya
- **abyākata**: (1) pahāna, tasseva, pattiya, bhūmiya, apacayagāmiṃ, niyyānika, lokuttara, vipāka, bhāvitatta, diṭṭhigata
- **cetana**: (1) cittassekaggata, aññepi, arūpina, paṭiccasamuppanna, jīvitindriya, paggāha, vicāra, vīriyindriya, atthi; (2) sañña
- **diṭṭhigata**: (1) bhūmiya, apacayagāmiṃ, pattiya, niyyānika, lokuttara, pahāna, paṭhama, dandhābhiñña; (2) appaṇihita; (3) suññata
- **saññākkhandha**: (1) saṅkhārakkhandha, vedanākkhandha; (2) aññepi, arūpina, paṭiccasamuppanna, viññāṇakkhandha, cittassekaggata, cetana, ṭhapetva, jīvitindriya
- **saṅkhārakkhandha**: (1) saññākkhandha, vedanākkhandha; (2) aññepi, arūpina, paṭiccasamuppanna, viññāṇakkhandha, cittassekaggata, cetana, ṭhapetva, jīvitindriya
- **paṭiccasamuppanna**: (1) aññepi, arūpina, cittassekaggata, cetana, jīvitindriya, atthi, paggāha, vicāra, samādhindriya, vīriyindriya
- **upāda**: (1) catunna, mahābhūta, pesa, peta, sappaṭigha, anidassana; (2) suñña, pasāda, gāma, tīra
- **pahāna**: (1) bhūmiya, apacayagāmiṃ, pattiya, niyyānika, lokuttara, diṭṭhigata, bhāveti, abyākata, jhāna, yasmiṃ
- **arūpāvacara**: (1) rūpāvacara, kāmāvacara, viññāṇakkhandha; (2) kusalākusalābyākata, avasesa; (3) sāsava, rūpakkhandha; (4) apariyāpanna, dhātu, asaṅkhata
- **bāhira**: (1) rūpāyatana, kabaḷīkāra, āhāra, taṃ; (2) phoṭṭhabbāyatana; (3) ārammaṇa; (4) āpodhātu; (5) saddāyatana; (6) itthindriya; (7) vacīviññatti
- **phoṭṭhabbāyatana**: (1) gandhāyatana, rasāyatana, saddāyatana, rūpāyatana; (2) āpodhātu, ākāsadhātu; (3) panaññampi, kamma, katatta; (4) taṃ
- **arūpina**: (1) aññepi, paṭiccasamuppanna, cittassekaggata, cetana, jīvitindriya, atthi, paggāha, vicāra, samādhindriya, vīriyindriya
- **kamma**: (1) katatta; (2) panaññampi, ākāsadhātu, gandhāyatana, rasāyatana, atthi, rūpāyatana, yaṃ; (3) āpodhātu; (4) phoṭṭhabbāyatana
- **nibbānañca**: (1) rūpañca, catūsu, kiriyābyākata, tīsu, bhūmīsu, vipāka; (2) sāmaññaphala, cattāri, cattāra; (3) vattabba
- **lokuttara**: (1) bhūmiya, apacayagāmiṃ, pattiya, niyyānika, pahāna, diṭṭhigata, paṭhama, dandhābhiñña, dukkhapaṭipada; (2) suññata
- **mahābhūta**: (1) catunna, upāda, pesa, peta, sappaṭigha, anidassana; (2) suñña, pasāda, gāma, tīra
- **asaṅkhata**: (1) dhātu, apariyāpanna; (2) sabbañca, vedanākkhandha, arūpāvacara, rūpāvacara, viññāṇakkhandha, kāmāvacara; (3) maggaphala; (4) kusalākusalābyākata
- **aññepi**: (1) arūpina, paṭiccasamuppanna, cittassekaggata, cetana, jīvitindriya, atthi, paggāha, vicāra, samādhindriya, vīriyindriya
- **dhātu**: (1) asaṅkhata, apariyāpanna; (2) sabbañca, vedanākkhandha, arūpāvacara, rūpāvacara, viññāṇakkhandha, kāmāvacara; (3) maggaphala; (4) kusalākusalābyākata
- **sañña**: (1) vedana, cetana; (2) manindriya, aññepi, rūpārammaṇa, arūpina, cittassekaggata, paṭiccasamuppanna, uppanna; (3) khandha
- **bhūmīsu**: (1) tīsu, kiriyābyākata, vipāka, akusala, kusala; (2) catūsu, rūpañca, nibbānañca; (3) sabbañca; (4) uddhaccasahagata
- **sabbañca**: (1) dhātu, asaṅkhata, arūpāvacara, rūpāvacara, kāmāvacara, vedanākkhandha; (2) avasesa; (3) kiriyābyākata, tīsu, bhūmīsu
- **kāyāyatana**: (1) ajjhattika, cakkhāyatana, taṃ; (2) gandhāyatana, rasāyatana, panaññampi, phoṭṭhabbāyatana; (3) sotāyatana, jivhāyatana, ghānāyatana
- **niyyānika**: (1) bhūmiya, apacayagāmiṃ, pattiya, lokuttara, pahāna, diṭṭhigata, dandhābhiñña, dukkhapaṭipada; (2) suññata; (3) appaṇihita
- **dukkhapaṭipada**: (1) dandhābhiñña, pattiya, bhūmiya, apacayagāmiṃ, niyyānika, paṭhama, lokuttara, vivicceva, kāma, bhāveti
- **dandhābhiñña**: (1) dukkhapaṭipada, pattiya, bhūmiya, apacayagāmiṃ, niyyānika, paṭhama, lokuttara, vivicceva, kāma, bhāveti
- **tīsu**: (1) bhūmīsu, kiriyābyākata, vipāka, akusala, kusala; (2) catūsu, rūpañca, nibbānañca; (3) sabbañca; (4) uddhaccasahagata
- **bhūmiya**: (1) apacayagāmiṃ, pattiya, niyyānika, lokuttara, pahāna, diṭṭhigata, dandhābhiñña, dukkhapaṭipada; (2) suññata; (3) appaṇihita
- **pattiya**: (1) bhūmiya, apacayagāmiṃ, niyyānika, lokuttara, pahāna, diṭṭhigata, dandhābhiñña, dukkhapaṭipada; (2) suññata; (3) appaṇihita
- **apacayagāmiṃ**: (1) bhūmiya, pattiya, niyyānika, lokuttara, pahāna, diṭṭhigata, dandhābhiñña, dukkhapaṭipada; (2) suññata; (3) appaṇihita
- **cittassekaggata**: (1) aññepi, arūpina, paṭiccasamuppanna, cetana, vicāra, jīvitindriya, paggāha, samādhindriya, vitakka, vīriyindriya
- **kiriyābyākata**: (1) tīsu, bhūmīsu, vipāka, akusala, kusala; (2) catūsu, rūpañca, nibbānañca; (3) sabbañca; (4) uddhaccasahagata
- **catuttha**: (1) tatiya, pañcama, dutiya, vūpasama, vitakkavicāra, pahāna, jhāna, bhāveti, yasmiṃ, avikkhepa
- **samādhindriya**: (1) samādhibala, samatha, sammāsamādhi; (2) vīriyindriya, paggāha, cittassekaggata, aññepi, arūpina, paṭiccasamuppanna, saddhindriya
- **sukha**: (1) vedana; (2) somanassindriya; (3) sāta, vedayita, cetosamphassaja, cetasika; (4) sabbasa, catuttha, samatikkamma, arūpūpapattiya
- **manindriya**: (1) manāyatana, hadaya, mānasa, viññāṇa, tajjāmanoviññāṇadhātu, paṇḍara; (2) citta, sañña, aññepi, arūpina
- **sammādiṭṭhi**: (1) paññindriya, pajānana, dhammavicaya, paññā, sampajañña, vipassana, paññābala, paññāpajjota, cinta, paṇḍicca
- **ajjhattika**: (1) kāyāyatana, cakkhāyatana, taṃ; (2) vatthu; (3) jivhāyatana; (4) sotāyatana; (5) ārammaṇa; (6) kāyasamphassa; (7) cakkhusamphassa; (8) cakkhuviññāṇa
- **rasāyatana**: (1) gandhāyatana, saddāyatana, panaññampi, phoṭṭhabbāyatana, rūpāyatana, kamma, atthi; (2) ākāsadhātu, kammaññata, lahuta
- **vīriyindriya**: (1) paggāha, sammāvāyāma, samādhindriya, cittassekaggata, aññepi, arūpina, saddhindriya, paṭiccasamuppanna, cetana; (2) vīriyabala
- **sappaṭigha**: (1) peta, pesa, anidassana, catunna, mahābhūta, upāda, tīra, orima, samudda, dvāra
- **vicāra**: (1) vitakka, cittassekaggata, aññepi, arūpina, paṭiccasamuppanna, cetana, paggāha, jīvitindriya, vīriyindriya, vīriyabala
- **vitakka**: (1) vicāra, cittassekaggata, aññepi, arūpina, paṭiccasamuppanna, cetana, jīvitindriya, vīriyabala, paggāha, vīriyindriya
- **bahiddha**: (1) ajjhatta, arūpasaññī, abhibhuyya, jānāmi, passāmīti, tāni, passati, rūpūpapattiya, appamāṇa, paritta
- **āpodhātu**: (1) ākāsadhātu, panaññampi, kamma, katatta; (2) phoṭṭhabbāyatana; (3) kammaññata, lahuta, muduta, jarata, aniccata
- **panaññampi**: (1) ākāsadhātu, āpodhātu, kammaññata, lahuta, muduta; (2) gandhāyatana, rasāyatana, kamma, atthi, katatta
- **anidassana**: (1) peta, pesa, sappaṭigha, catunna, khetta, attabhāvapariyāpanna, tīra, orima, samudda, dvāra
- **gandhāyatana**: (1) rasāyatana, saddāyatana, panaññampi, phoṭṭhabbāyatana, rūpāyatana, kamma, atthi; (2) ākāsadhātu, kammaññata, lahuta
- **ajjhatta**: (1) bahiddha, arūpasaññī, abhibhuyya, jānāmi, passāmīti, tāni, passati, rūpūpapattiya, appamāṇa, paritta
- **rūpañca**: (1) nibbānañca, catūsu, kiriyābyākata, tīsu, bhūmīsu, vipāka; (2) uddhaccasahagata, vicikicchāsahagata, cittuppāda; (3) vipākata
- **catūsu**: (1) bhūmīsu, kiriyābyākata, tīsu, rūpañca, nibbānañca, vipāka; (2) cittuppāda, vicikicchāsahagata, uddhaccasahagata; (3) akusala
- **samatha**: (1) samādhibala, samādhindriya, sammāsamādhi; (2) avisāhaṭamānasata, avaṭṭhiti, saṇṭhiti, avisāhāra, ṭhiti; (3) micchāsamādhi; (4) vīriyabala
- **dutiya**: (1) tatiya, pañcama, vūpasama, vitakkavicāra, catuttha, paṭhama; (2) pattiya, bhūmiya, apacayagāmiṃ, dandhābhiñña
- **catunna**: (1) peta, pesa, mahābhūta, upāda, anidassana, sappaṭigha; (2) suñña, pasāda, gāma, tīra
- **uppanna**: (1) rūpārammaṇa, panārabbha, dhammārammaṇa; (2) upekkhāsahagata; (3) phoṭṭhabbārammaṇa, manindriya, rasārammaṇa, gandhārammaṇa; (4) somanassasahagata; (5) sasaṅkhāra
- **samādhibala**: (1) samatha, samādhindriya, sammāsamādhi; (2) saṇṭhiti, avisāhāra, avisāhaṭamānasata, avaṭṭhiti, ṭhiti; (3) vīriyabala; (4) micchāsamādhi
- **itthindriya**: (1) purisindriya, ākāsadhātu, jīvitindriya, panaññampi, āpodhātu, gandhāyatana; (2) kabaḷīkāra, āhāra; (3) appaṭigha; (4) upādiṇṇupādāniya
- **passati**: (1) arūpasaññī, abhibhuyya, jānāmi, passāmīti, tāni, ajjhatta, bahiddha, rūpūpapattiya, appamāṇa, paritta
- **avasesa**: (1) kusalākusalābyākata, ṭhapetva, sabbañca, arūpāvacara, rūpāvacara, kāmāvacara; (2) cātipi, vattabba; (3) akusala, kiriyābyākata
- **tatiya**: (1) pañcama, vūpasama, dutiya, vitakkavicāra, catuttha, paṭhama; (2) pattiya, bhūmiya, apacayagāmiṃ, dandhābhiñña
- **ṭhiti**: (1) saṇṭhiti, avisāhāra, avisāhaṭamānasata, avaṭṭhiti, samatha, samādhibala, sammāsamādhi; (2) vattana, yapana, pālana
- **ākāsadhātu**: (1) panaññampi, āpodhātu, gandhāyatana, rasāyatana; (2) kammaññata, lahuta, muduta, jarata, aniccata, vacīviññatti
- **paṇḍara**: (1) hadaya, mānasa, manāyatana, tajjāmanoviññāṇadhātu; (2) khetta, attabhāvapariyāpanna, tīra, orima, samudda, dvāra
- **pesa**: (1) peta, catunna, anidassana, sappaṭigha, khetta, attabhāvapariyāpanna, tīra, orima, samudda, dvāra
- **paritta**: (1) abhibhuyya, jānāmi, passāmīti, tāni, arūpasaññī, passati, ajjhatta, rūpūpapattiya, bahiddha; (2) parittārammaṇa
- **paññindriya**: (1) sammādiṭṭhi, sampajañña, paññābala, vipassana, kosalla, paññāobhāsa, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **arūpasaññī**: (1) abhibhuyya, jānāmi, passāmīti, tāni, passati, ajjhatta, bahiddha, appamāṇa, paritta, rūpūpapattiya
- **hetū**: (1) bala, caturaṅgika, dhātuya, dvāyatana, dhammadhātu, khandha, ekaṃ, dhammāyatana, ekā, aṭṭhindriya
- **appamāṇa**: (1) abhibhuyya, jānāmi, passāmīti, tāni, arūpasaññī, passati, ajjhatta, rūpūpapattiya, bahiddha; (2) appamāṇārammaṇa
- **saddāyatana**: (1) gandhāyatana, rasāyatana, phoṭṭhabbāyatana; (2) kammaññata, lahuta, muduta, panaññampi, jarata, ākāsadhātu, aniccata
- **paggāha**: (1) vīriyindriya, samādhindriya, cittassekaggata, sammāvāyāma, saddhindriya, aññepi, satindriya, arūpina, paṭiccasamuppanna; (2) vīriyabala
- **abhibhuyya**: (1) jānāmi, passāmīti, tāni, arūpasaññī, passati, ajjhatta, bahiddha, appamāṇa, paritta, rūpūpapattiya
- **evarūpa**: (1) vipariyāsaggāha, diṭṭhi, vuccati, tattha; (2) micchāpatha, diṭṭhivisūkāyika, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga
- **jānāmi**: (1) abhibhuyya, passāmīti, tāni, arūpasaññī, passati, ajjhatta, bahiddha, appamāṇa, paritta, rūpūpapattiya
- **passāmīti**: (1) abhibhuyya, jānāmi, tāni, arūpasaññī, passati, ajjhatta, bahiddha, appamāṇa, paritta, rūpūpapattiya
- **tāni**: (1) abhibhuyya, jānāmi, passāmīti, arūpasaññī, passati, ajjhatta, bahiddha, appamāṇa, paritta, rūpūpapattiya
- **sukhapaṭipada**: (1) khippābhiñña, paṭhama, vivicceva, rūpūpapattiya, kāma; (2) dandhābhiñña; (3) appamāṇa, passāmīti, abhibhuyya, jānāmi
- **khippābhiñña**: (1) sukhapaṭipada, paṭhama, vivicceva, rūpūpapattiya, kāma; (2) dukkhapaṭipada; (3) appamāṇa, passāmīti, abhibhuyya, jānāmi
- **vīriyabala**: (1) vīriyindriya, paggāha, samādhibala; (2) micchāvāyāma; (3) thāma, ussāha, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma
- **pathavīkasiṇa**: (1) rūpūpapattiya, bhāveti, magga, vivicceva, paṭhama, kāma, jhāna, yasmiṃ; (2) appamāṇārammaṇa; (3) parittārammaṇa
- **kāyaviññatti**: (1) vacīviññatti, kammaññata, lahuta, muduta, jarata, aniccata, ākāsadhātu, panaññampi, saddāyatana, āpodhātu
- **upekkhāsahagata**: (1) upekkha, upekkhindriya, phoṭṭhabbārammaṇa, cittassekaggata, manindriya; (2) rūpārammaṇa, uppanna, panārabbha, dhammārammaṇa; (3) upacitatta
- **vacīviññatti**: (1) kāyaviññatti, kammaññata, lahuta, muduta, jarata, aniccata, ākāsadhātu, panaññampi, saddāyatana, āpodhātu
- **viññāṇa**: (1) hadaya, mānasa, manāyatana, tajjāmanoviññāṇadhātu, paṇḍara, manindriya, citta, viññāṇakkhandha; (2) saṅkhāra; (3) saṅgahita
- **sammāvāyāma**: (1) vīriyindriya, saddhindriya, paggāha, satindriya, paññindriya, samādhindriya, sammādiṭṭhi, cittassekaggata; (2) vīriyabala; (3) vīriyārambha
- **kusalākusalābyākata**: (1) rūpakkhandha, arūpāvacara, rūpāvacara, sāsava, kāmāvacara, viññāṇakkhandha; (2) avasesa, sabbañca, ṭhapetva, dhātu
- **vedayita**: (1) cetosamphassaja, sāta, cetasika, vedana, yaṃ; (2) nāsāta, adukkhamasukha; (3) sukha; (4) tajjāmanoviññāṇadhātusamphassaja; (5) asāta
- **peta**: (1) pesa, catunna, anidassana, sappaṭigha, khetta, attabhāvapariyāpanna, tīra, orima, samudda, dvāra
- **cittuppāda**: (1) vicikicchāsahagata, uddhaccasahagata, catūsu, tīsu, kiriyābyākata, bhūmīsu; (2) dvīsu, domanassasahagata; (3) domanassasahagatacittuppāda, diṭṭhigatavippayuttalobhasahagatacittuppāda
- **paññā**: (1) pajānana, dhammavicaya, sammādiṭṭhi, bhūrī, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa
- **pañcama**: (1) tatiya, dutiya, vūpasama, vitakkavicāra, catuttha, pattiya, bhūmiya, apacayagāmiṃ, dandhābhiñña, dukkhapaṭipada
- **vitakkavicāra**: (1) vūpasama, tatiya, pañcama, dutiya, catuttha, paṭhama, bhāveti, jhāna, yasmiṃ; (2) rūpūpapattiya
- **lobha**: (1) abhijjha, anottappa, ahirika; (2) tadekaṭṭha, kāyakamma, vacīkamma, taṃsamuṭṭha, manokamma, kilesa; (3) akusalamūla
- **sāsava**: (1) rūpakkhandha, kusalākusalābyākata, arūpāvacara, rūpāvacara, kāmāvacara, viññāṇakkhandha; (2) vippayutta; (3) kusalākusala; (4) avasesa; (5) āsava
- **satindriya**: (1) saddhindriya, sammāvāyāma, paggāha, paññindriya, vīriyindriya, samādhindriya; (2) satibala, sammāsati, apilāpanata, anussati
- **dhammāyatana**: (1) dvāyatana, ekaṃ, dhātuya, dhammadhātu, ekā, khandha, bala, caturaṅgika, aññepi, arūpina
- **tasseva**: (1) bhāvitatta, bhūmiya, apacayagāmiṃ, pattiya, abyākata, pahāna, niyyānika, suññata, appaṇihita, lokuttara
- **cetasika**: (1) cetosamphassaja, vedayita, sāta, vedana, yaṃ; (2) nāsāta, adukkhamasukha; (3) sukha; (4) tajjāmanoviññāṇadhātusamphassaja; (5) somanassindriya
- **dhammavicaya**: (1) pajānana, paññā, sammādiṭṭhi, bhūrī, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa
- **vattabba**: (1) cātipi, avasesa, akusala, ṭhapetva; (2) sāmaññaphala, cattāri; (3) nibbānañca, rūpañca; (4) siya; (5) vipākata
- **khandha**: (1) dvāyatana, dhātuya, ekaṃ, dhammadhātu, ekā, dhammāyatana, bala, caturaṅgika, aññepi, arūpina
- **cattāri**: (1) sāmaññaphala, cattāra, nibbānañca, apariyāpanna, magga; (2) vattabba; (3) pañcindriya, caturaṅgika, bala, dvāyatana
- **pajānana**: (1) dhammavicaya, paññā, sammādiṭṭhi, bhūrī, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa
- **vūpasama**: (1) vitakkavicāra, tatiya, pañcama, dutiya, catuttha, paṭhama, bhāveti, rūpūpapattiya, jhāna, yasmiṃ
- **suññata**: (1) pattiya, bhūmiya, apacayagāmiṃ, niyyānika, lokuttara, bhāvitatta, pahāna, tasseva, diṭṭhigata; (2) appaṇihita
- **dhammadhātu**: (1) dhātuya, dvāyatana, ekā, ekaṃ, khandha, dhammāyatana, bala, caturaṅgika, aññepi, arūpina
- **indriya**: (1) cakkhundriya, kāyindriya; (2) purisindriya; (3) āyatana, dhātuṃ, satipaṭṭha, iddhipāda; (4) evaṃ, rūpasaṅgaha, appaṭigha
- **appaṇihita**: (1) bhūmiya, apacayagāmiṃ, pattiya, niyyānika, lokuttara, bhāvitatta, pahāna, diṭṭhigata, tasseva; (2) animitta
- **sāta**: (1) vedayita, cetosamphassaja, cetasika, vedana, sukha, yaṃ; (2) nāsāta, adukkhamasukha; (3) tajjāmanoviññāṇadhātusamphassaja; (4) somanassindriya
- **cetosamphassaja**: (1) cetasika, vedayita, sāta, vedana, yaṃ; (2) nāsāta, adukkhamasukha; (3) sukha; (4) tajjāmanoviññāṇadhātusamphassaja; (5) somanassindriya
- **ekā**: (1) dvāyatana, ekaṃ, dhammadhātu, dhātuya, khandha, dhammāyatana, caturaṅgika, bala, aññepi, arūpina
- **muduta**: (1) kammaññata, lahuta, jarata, aniccata, ākāsadhātu, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana, āpodhātu
- **purisindriya**: (1) itthindriya, ākāsadhātu, jīvitindriya, panaññampi, āpodhātu, gandhāyatana, rasāyatana, kamma; (2) upādiṇṇupādāniya; (3) upādiṇṇa
- **manāyatana**: (1) hadaya, mānasa, tajjāmanoviññāṇadhātu, viññāṇa, paṇḍara, manindriya, citta, viññāṇakkhandha, yaṃ; (2) dhammāyatana
- **dhātuya**: (1) dhammadhātu, dvāyatana, ekaṃ, ekā, khandha, dhammāyatana, bala, caturaṅgika, aññepi, arūpina
- **vipākata**: (1) kāmāvacarakusalata, kāmāvacarakusala; (2) etthuppanna; (3) rūpāvacaratikacatukkajjhāna; (4) āruppa, upekkhāsahagatacittuppāda; (5) somanassasahagatacittuppāda, pañca; (6) kāmāvacarakiriyata, cittuppāda
- **kilesa**: (1) tadekaṭṭha, taṃsamuṭṭha, manokamma, kāyakamma, vacīkamma, taṃsampayutta, lobha, tīṇi; (2) saṃkiliṭṭha; (3) kilesasampayutta
- **kammaññata**: (1) lahuta, muduta, jarata, aniccata, ākāsadhātu, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana, āpodhātu
- **lahuta**: (1) kammaññata, muduta, jarata, aniccata, ākāsadhātu, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana, āpodhātu
- **ekaṃ**: (1) dvāyatana, ekā, dhātuya, dhammāyatana, dhammadhātu, khandha, caturaṅgika, bala, aññepi, arūpina
- **rūpārammaṇa**: (1) panārabbha, dhammārammaṇa, uppanna; (2) phoṭṭhabbārammaṇa, rasārammaṇa, gandhārammaṇa; (3) upekkhāsahagata, upekkhindriya; (4) sasaṅkhāra; (5) somanassasahagata
- **diṭṭhi**: (1) vipariyāsaggāha, evarūpa; (2) micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha
- **pīti**: (1) paggāha, cittassekaggata, vicāra, vīriyindriya, saddhindriya, samādhindriya, vitakka, aññepi, satindriya; (2) somanassindriya
- **saddhindriya**: (1) satindriya, sammāvāyāma, paggāha, paññindriya, vīriyindriya, samādhindriya; (2) saddhābala, kāyalahuta, kāyapassaddhi, kāyapāguññata
- **bhāvitatta**: (1) tasseva, bhūmiya, apacayagāmiṃ, pattiya, suññata, niyyānika, appaṇihita, lokuttara, pahāna; (2) chandādhipateyya
- **alobha**: (1) anabhijjha, kāyalahuta, cittamuduta, cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyapassaddhi, kāyapāguññata
- **sammāsamādhi**: (1) samādhibala, samatha, avisāhaṭamānasata, avaṭṭhiti, saṇṭhiti, avisāhāra, samādhindriya; (2) sammāsaṅkappa, kāyapassaddhi, kāyapāguññata
- **dvāyatana**: (1) ekaṃ, dhammāyatana, ekā, dhātuya, dhammadhātu, khandha, caturaṅgika, bala, aññepi, arūpina
- **paññābala**: (1) sampajañña, vipassana, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa, bhūrī, sallakkhaṇa
- **vipassana**: (1) sampajañña, paññābala, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa, bhūrī, sallakkhaṇa
- **maggaṅga**: (1) maggapariyāpanna; (2) dhammavicayasambojjhaṅga, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, cinta
- **pasāda**: (1) suñña, gāma, vatthuṃ, tīra, orima, samudda, dvāra, khetta, attabhāvapariyāpanna, catunna
- **suñña**: (1) pasāda, gāma, vatthuṃ, tīra, orima, samudda, dvāra, khetta, attabhāvapariyāpanna, catunna
- **chandādhipateyya**: (1) cittādhipateyya, vīriyādhipateyya, vīmaṃsādhipateyya; (2) bhāvitatta, tasseva, pahāna, bhūmiya, apacayagāmiṃ, pattiya, niyyānika
- **sampajañña**: (1) vipassana, paññābala, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa, bhūrī, sallakkhaṇa
- **taṃsampayutta**: (1) manokamma, kāyakamma, vacīkamma, taṃsamuṭṭha, tadekaṭṭha, kilesa, tīṇi, lobha; (2) viññāṇakkhandha; (3) pahātabbahetū
- **maggapariyāpanna**: (1) maggaṅga; (2) dhammavicayasambojjhaṅga, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, cinta
- **panārabbha**: (1) rūpārammaṇa, dhammārammaṇa, uppanna; (2) phoṭṭhabbārammaṇa, rasārammaṇa, gandhārammaṇa; (3) sasaṅkhāra; (4) upekkhāsahagata, upekkhindriya; (5) somanassasahagata
- **gāma**: (1) suñña, pasāda, catunna, vatthuṃ, tīra, orima, samudda, dvāra, khetta, attabhāvapariyāpanna
- **dassana**: (1) pahātabba; (2) pahātabbahetuka; (3) bhāvana; (4) sīlabbataparāmāsa, tīṇi, sakkāyadiṭṭhi, saṃyojana, vicikiccha; (5) cittuppāda, vicikicchāsahagata
- **parittārammaṇa**: (1) paritta, rūpūpapattiya, abhibhuyya, jānāmi, passāmīti, tāni, arūpasaññī, passati; (2) appamāṇa; (3) pathavīkasiṇa
- **aniccata**: (1) jarata, lahuta, kammaññata, muduta, ākāsadhātu, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana; (2) anupādiṇṇupādāniya
- **tesa**: (1) yapana, pālana, vattana, āyu, jīvita, iriyana, yāpana, arūpīna, ṭhiti; (2) rūpīna
- **rūpakkhandha**: (1) sāsava, kusalākusalābyākata, arūpāvacara, rūpāvacara, kāmāvacara, viññāṇakkhandha; (2) vippayutta; (3) kusalābyākata; (4) avasesa; (5) saṃyojaniya
- **sāmaññaphala**: (1) cattāri, nibbānañca, apariyāpanna, cattāra, magga; (2) vattabba; (3) anārammaṇa, rūpāvacaratikacatukkajjhāna, kiriyāhetukamanoviññāṇadhātu, siya
- **appamāṇārammaṇa**: (1) appamāṇa, rūpūpapattiya, abhibhuyya, jānāmi, passāmīti, tāni, arūpasaññī, passati; (2) paritta; (3) pathavīkasiṇa
- **parāmāsa**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga
- **manoviññāṇadhātu**: (1) dhātuya, dhammadhātu, ekā, khandha; (2) somanassasahagata; (3) aññepi, arūpina, paṭiccasamuppanna; (4) dhammārammaṇa, panārabbha
- **satta**: (1) aṭṭhindriya, bala, caturaṅgika, dvāyatana, ekaṃ, ekā, dhātuya, dhammadhātu, khandha, dhammāyatana
- **bala**: (1) caturaṅgika, khandha, dhātuya, dvāyatana, dhammadhātu, ekaṃ, ekā, dhammāyatana, hetū; (2) aṭṭhindriya
- **etthuppanna**: (1) vipākata, kāmāvacarakusala, kāmāvacarakusalata, somanassasahagatacittuppāda, pañca; (2) domanassasahagatacittuppāda; (3) ṭhapetva, cattāra; (4) cittuppāda; (5) moha
- **uddhaccasahagata**: (1) vicikicchāsahagata, cittuppāda, catūsu, kiriyābyākata, tīsu, bhūmīsu, rūpañca; (2) domanassasahagatacittuppāda; (3) moha; (4) diṭṭhigatavippayuttalobhasahagatacittuppāda
- **vipariyāsaggāha**: (1) diṭṭhi, diṭṭhikantāra, kummagga, micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, micchatta, diṭṭhivipphandita
- **bhāvana**: (1) pahātabbahetuka; (2) pahātabba; (3) dassana; (4) uddhaccasahagata, siya; (5) tadekaṭṭha, kāyakamma, vacīkamma, taṃsamuṭṭha, manokamma
- **upādiṇṇa**: (1) purisindriya, ākāsadhātu, itthindriya, āpodhātu; (2) anupādiṇṇa; (3) kamma, panaññampi, katatta, gandhāyatana, rasāyatana
- **jarata**: (1) aniccata, lahuta, kammaññata, muduta, ākāsadhātu, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana; (2) anupādiṇṇupādāniya
- **upekkha**: (1) upekkhindriya, upekkhāsahagata, rūpārammaṇa, panārabbha, phoṭṭhabbārammaṇa, uppanna, manindriya, dhammārammaṇa, cittassekaggata, vedana
- **dhammārammaṇa**: (1) panārabbha, rūpārammaṇa, uppanna, upekkhāsahagata; (2) sasaṅkhāra; (3) somanassasahagata; (4) rasārammaṇa, gandhārammaṇa, saddārammaṇa, phoṭṭhabbārammaṇa
- **hadaya**: (1) mānasa, tajjāmanoviññāṇadhātu, manāyatana, viññāṇa, paṇḍara, manindriya, citta, viññāṇakkhandha, yaṃ; (2) tajjācakkhuviññāṇadhātu
- **mānasa**: (1) hadaya, tajjāmanoviññāṇadhātu, manāyatana, viññāṇa, paṇḍara, manindriya, citta, viññāṇakkhandha, yaṃ; (2) tajjācakkhuviññāṇadhātu
- **vicikicchāsahagata**: (1) uddhaccasahagata, cittuppāda, catūsu, kiriyābyākata; (2) dvīsu, domanassasahagata; (3) diṭṭhigatavippayuttalobhasahagata; (4) diṭṭhigatasampayuttacittuppāda; (5) diṭṭhigatavippayuttalobhasahagatacittuppāda; (6) domanassasahagatacittuppāda
- **sammāsati**: (1) satibala, satindriya, saraṇata, dhāraṇata, paṭissati, apilāpanata, anussati, asammussanata; (2) sammāsaṅkappa, kāyapassaddhi
- **satibala**: (1) sammāsati, satindriya, saraṇata, dhāraṇata, paṭissati, apilāpanata, anussati, asammussanata; (2) ottappabala, hiribala
- **ārammaṇa**: (1) cakkhusamphassa; (2) kāyasamphassa, ghānasamphassa, jivhāsamphassa, sotasamphassa; (3) cakkhuviññāṇa, cakkhusamphassaja; (4) kāyaviññāṇa, kāyasamphassaja; (5) bāhira
- **appaṭigha**: (1) dhammāyatanapariyāpanna, yañca, anidassana; (2) itthindriya, purisindriya; (3) tika; (4) evaṃ, rūpasaṅgaha, indriya; (5) āpodhātu
- **saṃyojana**: (1) tīṇi, sīlabbataparāmāsa, sakkāyadiṭṭhi, dassana, vicikiccha; (2) saṃyojanasampayutta; (3) saṃyojaniya; (4) avijjāsaṃyojana; (5) pahātabba, imāni
- **sotāyatana**: (1) ghānāyatana, jivhāyatana, kāyāyatana, saddāyatana, gandhāyatana; (2) sotadhātu, sotindriya, sota, sadda; (3) vatthu
- **uppajjanti**: (1) cittacetasika, ārabbha; (2) yattha; (3) lobhasahagata, aṭṭhasu, dvīsu, diṭṭhigatasampayutta, domanassasahagata, uppajjati, sabbākusala
- **avaṭṭhiti**: (1) avisāhaṭamānasata, saṇṭhiti, avisāhāra, ṭhiti, samādhibala, samatha, sammāsamādhi, samādhindriya; (2) samādhisambojjhaṅga; (3) micchāsamādhi
- **avisāhaṭamānasata**: (1) avaṭṭhiti, saṇṭhiti, avisāhāra, ṭhiti, samādhibala, samatha, sammāsamādhi, samādhindriya; (2) samādhisambojjhaṅga; (3) micchāsamādhi
- **avisāhāra**: (1) avisāhaṭamānasata, avaṭṭhiti, saṇṭhiti, ṭhiti, samādhibala, samatha, sammāsamādhi, samādhindriya; (2) samādhisambojjhaṅga; (3) micchāsamādhi
- **saṇṭhiti**: (1) avisāhaṭamānasata, avaṭṭhiti, avisāhāra, ṭhiti, samādhibala, samatha, sammāsamādhi, samādhindriya; (2) samādhisambojjhaṅga; (3) micchāsamādhi
- **anupādiṇṇa**: (1) jarata, aniccata, kammaññata, lahuta, muduta, kamma, vacīviññatti, kāyaviññatti, panaññampi; (2) upādiṇṇa
- **pāpaka**: (1) samāpattiya, akusala; (2) hirīyati, hiriyitabba; (3) ottappati, ottappitabba; (4) ottappa; (5) ghāyitva, saṃvara, anubyañjanaggāhī
- **pahātabba**: (1) dassana; (2) bhāvana; (3) tadekaṭṭha, kāyakamma, vacīkamma, taṃsamuṭṭha, manokamma; (4) tīṇi, sīlabbataparāmāsa, saṃyojana
- **ārabbha**: (1) uppajji, nissa, uppajja, uppajjissati, uppajjati, peta, pesa, catunna; (2) cittacetasika, uppajjanti
- **sampayutta**: (1) dukkha; (2) ṭhapetva; (3) viññāṇakkhandha, vedanākkhandha; (4) adukkhamasukha; (5) hetusampayutta; (6) āsavasampayutta; (7) saṃyojanasampayutta; (8) ganthasampayutta; (9) nīvaraṇasampayutta
- **bhūrī**: (1) kosalla, paññāobhāsa, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **cinta**: (1) paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, paṇḍicca, paññāpajjota, upalakkhaṇa, kosalla
- **kosalla**: (1) paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **maggaphala**: (1) dhātu, asaṅkhata, apariyāpanna, magga; (2) nikkhepakaṇḍa; (3) anāsava; (4) asaṃyojaniya; (5) aganthaniya; (6) anīvaraṇiya; (7) aparāmaṭṭha
- **medha**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **nepuñña**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paccupalakkhaṇa**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **pariṇāyika**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paññāobhāsa**: (1) kosalla, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paññāpajjota**: (1) paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, upalakkhaṇa, kosalla
- **paññāpāsāda**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paññāratana**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paññāsattha**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paññāāloka**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **paṇḍicca**: (1) paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paññāpajjota, upalakkhaṇa, kosalla
- **sallakkhaṇa**: (1) kosalla, paññāobhāsa, bhūrī, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **upalakkhaṇa**: (1) paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, vebhabya, cinta, paṇḍicca, paññāpajjota, kosalla
- **upaparikkha**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, vebhabya, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **vebhabya**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **vatthu**: (1) cakkhusamphassa; (2) kāyasamphassa, ghānasamphassa, jivhāsamphassa, sotasamphassa; (3) cakkhuviññāṇa, cakkhusamphassaja; (4) kāyaviññāṇa; (5) sotāyatana; (6) ajjhattika
- **cakkhundriya**: (1) cakkhu, pasāda, suñña, gāma; (2) kāyindriya, indriya; (3) nayana, netta, cakkhudhātu, cakkhuṃ
- **rūpasaṅgaha**: (1) evaṃ; (2) sotaviññeyya, jivhāviññeyya, kāyaviññeyya, cakkhuviññeyya, ghānaviññeyya, manodhātuviññeyya, manoviññāṇadhātuviññeyya; (3) sabba; (4) appaṭigha
- **uppajjati**: (1) uppajji, nissa, uppajja, uppajjissati, ārabbha; (2) lobhasahagata, aṭṭhasu, diṭṭhigatasampayutta, sabbākusala, dvīsu
- **anottappa**: (1) ahirika, ahirikabala, anottappabala, micchāsaṅkappa, micchāvāyāma, micchāsamādhi, abhijjha, vīriyabala, paggāha, lobha
- **upādiṇṇupādāniya**: (1) purisindriya, kamma, panaññampi, ākāsadhātu, itthindriya, katatta, āpodhātu; (2) gandhāyatana, rasāyatana, kāyāyatana
- **pahātabbahetuka**: (1) dassana; (2) bhāvana; (3) pahātabbahetū, tadekaṭṭha, manokamma, kāyakamma, vacīkamma; (4) moha; (5) sakkāyadiṭṭhi, sīlabbataparāmāsa
- **dukkha**: (1) dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya, paṭipada, pubbantāparanta, idappaccayata, pubbanta, apaccavekkhaṇa, avijjogha; (2) asāta
- **kāya**: (1) phoṭṭhabba; (2) saṇha, lahuka, muduka, pharusa, garuka, kakkhaḷa; (3) gāma, pasāda, suñña
- **upekkhindriya**: (1) upekkha, rūpārammaṇa, panārabbha, phoṭṭhabbārammaṇa, upekkhāsahagata, uppanna; (2) dvāyatana, ekaṃ, ekā, dhātuya
- **kāmāvacarakusala**: (1) kāmāvacarakusalata, vipākata, etthuppanna; (2) somanassasahagatacittuppāda, pañca, rūpāvacaratikacatukkajjhāna, lokuttaratikacatukkajjhāna; (3) upekkhāsahagatacittuppāda, āruppa; (4) ekādasa
- **tīṇi**: (1) vacīkamma, taṃsamuṭṭha, manokamma, kāyakamma, tadekaṭṭha, taṃsampayutta; (2) sīlabbataparāmāsa, saṃyojana, sakkāyadiṭṭhi, vicikiccha
- **animitta**: (1) chandādhipateyyanti; (2) appaṇihita, suññata, bhāvitatta, pattiya, bhūmiya, apacayagāmiṃ, niyyānika, tasseva, lokuttara
- **attabhāvapariyāpanna**: (1) samudda, dvāra, khetta, vatthuṃ, tīra, orima, suñña, pasāda, gāma, peta
- **dvāra**: (1) samudda, khetta, attabhāvapariyāpanna, vatthuṃ, tīra, orima, suñña, pasāda, gāma, peta
- **khetta**: (1) samudda, dvāra, attabhāvapariyāpanna, vatthuṃ, tīra, orima, suñña, pasāda, gāma, peta
- **orima**: (1) dvāra, khetta, attabhāvapariyāpanna, vatthuṃ, tīra, samudda, suñña, pasāda, gāma, peta
- **paṭihañña**: (1) paṭihaññati, paṭihaññissati, paṭihaññi, peta, pesa, anidassana, catunna, sappaṭigha, tīra, orima
- **paṭihaññati**: (1) paṭihaññissati, paṭihañña, paṭihaññi, peta, pesa, anidassana, catunna, sappaṭigha, tīra, orima
- **paṭihaññi**: (1) paṭihaññati, paṭihaññissati, paṭihañña, peta, pesa, anidassana, catunna, sappaṭigha, tīra, orima
- **paṭihaññissati**: (1) paṭihaññati, paṭihañña, paṭihaññi, peta, pesa, anidassana, catunna, sappaṭigha, tīra, orima
- **samudda**: (1) dvāra, khetta, attabhāvapariyāpanna, vatthuṃ, tīra, orima, suñña, pasāda, gāma, peta
- **samāpattiya**: (1) pāpaka, hirīyati, hiriyitabba, akusala; (2) ottappati, ottappitabba; (3) ottappa; (4) ottappabala; (5) hiribala; (6) hirī
- **tajjāmanoviññāṇadhātu**: (1) hadaya, mānasa, manāyatana, viññāṇa, paṇḍara, manindriya, citta, viññāṇakkhandha, yaṃ; (2) ekaṃ
- **tīra**: (1) dvāra, khetta, attabhāvapariyāpanna, vatthuṃ, orima, samudda, suñña, pasāda, gāma, peta
- **vatthuṃ**: (1) samudda, dvāra, khetta, attabhāvapariyāpanna, tīra, orima, suñña, pasāda, gāma, peta
- **gantha**: (1) kāyagantha; (2) ganthasampayutta; (3) ganthaniya; (4) paṇidhi, saddataṇha, gedha, anurodha, dhanāsa, jīvitāsa, jappana
- **nīvaraṇa**: (1) nīvaraṇasampayutta; (2) avijjānīvaraṇa; (3) nīvaraṇiya; (4) paṇidhi, saddataṇha, gedha, anurodha, dhanāsa, jīvitāsa, jappana
- **anupādiṇṇupādāniya**: (1) jarata, aniccata, kammaññata, lahuta, muduta, kamma, vacīviññatti, kāyaviññatti, panaññampi, saddāyatana
- **adukkhamasukha**: (1) nāsāta, sāta, cetosamphassaja, cetasika, vedayita, vedana; (2) upekkhindriya, caturaṅgika; (3) upekkha; (4) tajjāmanoviññāṇadhātusamphassaja
- **vicikiccha**: (1) thambhitatta, manovilekha, vicikicchati, kaṅkhati, satthari, kaṅkhāyitatta, anekaṃsaggāha, kaṅkhāyana, dvedhāpatha, dveḷhaka
- **ahirika**: (1) ahirikabala, anottappabala, anottappa, micchāsaṅkappa, micchāvāyāma, micchāsamādhi, abhijjha, vīriyabala, paggāha; (2) rasārammaṇa
- **jivhāyatana**: (1) ghānāyatana, sotāyatana, kāyāyatana, saddāyatana, gandhāyatana; (2) jivhādhātu, jivhindriya, jivha, gāma, tīra
- **kāyindriya**: (1) jivhindriya, ghānindriya, sotindriya; (2) cakkhundriya, indriya; (3) kāyadhātu, kāya, phoṭṭhabba, gāma, suñña
- **saddhābala**: (1) ottappabala, hiribala, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta, cittalahuta, cittapāguññata, kāyujukata, cittujukata
- **sammāsaṅkappa**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **somanassindriya**: (1) sukha, saddhindriya, satindriya, manindriya, vīriyindriya, paggāha; (2) aṭṭhindriya, caturaṅgika; (3) pīti, somanassasahagata
- **kiriya**: (1) kammavipāka, nākusala, abyākata; (2) diṭṭhadhammasukhavihāra, sabbasa, samatikkamma; (3) kusalākusala, arūpāvacara; (4) manoviññāṇadhātu; (5) abyākatamūla
- **yañca**: (1) dhammāyatanapariyāpanna, appaṭigha, anidassana; (2) kusalākusala, kamma; (3) anidassanaappaṭigha, tika; (4) uppādina; (5) tīsu, bhūmīsu
- **vīriyārambha**: (1) thāma, ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma
- **kāyaviññāṇa**: (1) kāyasamphassaja; (2) sotaviññāṇa, ghānaviññāṇa, jivhāviññāṇa, cakkhuviññāṇa; (3) vatthu; (4) ārammaṇa; (5) phoṭṭhabbārammaṇa; (6) dukkhasahagata; (7) kāyasamphassa
- **sanidassana**: (1) cakkhuṃ; (2) ātapa, mañjiṭṭhaka, soḷasaṃsa, maṇisaṅkhamuttāveḷuriya, ādāsamaṇḍala, vaṭṭa, dhūma, ambaṅkuravaṇṇa, chaḷaṃsa
- **somanassasahagata**: (1) dhammārammaṇa, panārabbha, rūpārammaṇa, uppanna; (2) sasaṅkhāra, ñāṇavippayutta; (3) ñāṇasampayutta; (4) somanassindriya, pīti; (5) manoviññāṇadhātu
- **abyāpāda**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **anabhijjha**: (1) alobha, kāyalahuta, cittamuduta, cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyapassaddhi, kāyapāguññata
- **micchāsamādhi**: (1) ahirikabala, anottappabala, micchāsaṅkappa, micchāvāyāma, ahirika, anottappa, samādhibala, samatha, abhijjha, samādhindriya
- **micchāvāyāma**: (1) ahirikabala, anottappabala, micchāsaṅkappa, ahirika, anottappa, micchāsamādhi, vīriyabala, abhijjha, paggāha, vīriyindriya
- **akusalamūla**: (1) aññāṇa, adassana, avijjālaṅgī, asampajañña, avijja, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjogha, sammoha
- **phusana**: (1) saṃphusana, saṃphusitatta, phassa, ayaṃ
- **saṃphusana**: (1) phusana, saṃphusitatta, phassa, ayaṃ
- **saṃphusitatta**: (1) saṃphusana, phusana, phassa, ayaṃ
- **tajjāmanoviññāṇadhātusamphassaja**: (1) sañcetana, cetayitatta; (2) sañjānitatta, sañjānana; (3) cetosamphassaja, cetasika, vedayita, sāta; (4) nāsāta, adukkhamasukha
- **āsava**: (1) āsavasampayutta; (2) avijjāsava, kāmāsava, diṭṭhāsava, bhavāsava; (3) āsavātipi, cātipi; (4) sāsava; (5) avasesa; (6) vijja
- **cakkhuviññāṇa**: (1) cakkhusamphassaja, sañña; (2) vatthu; (3) ārammaṇa; (4) sotaviññāṇa, ghānaviññāṇa, jivhāviññāṇa, kāyaviññāṇa; (5) cakkhusamphassa, cakkhuṃ
- **diṭṭhisaṃyojana**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga
- **hirī**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **vīriya**: (1) thāma, ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma
- **phoṭṭhabbārammaṇa**: (1) saddārammaṇa, rasārammaṇa, gandhārammaṇa, panārabbha, rūpārammaṇa, dhammārammaṇa, uppanna; (2) upekkhindriya; (3) ahirikabala, anottappabala
- **anikkhittachandata**: (1) anikkhittadhurata, parakkama, vāyāma, thāma, ussāha, uyyāma, dhiti, nikkama, dhurasampaggāha, asithilaparakkamata
- **anikkhittadhurata**: (1) anikkhittachandata, parakkama, vāyāma, thāma, ussāha, uyyāma, dhiti, nikkama, dhurasampaggāha, asithilaparakkamata
- **domanassasahagatacittuppāda**: (1) siya; (2) diṭṭhigatavippayuttalobhasahagatacittuppāda; (3) uddhaccasahagata, cittuppāda, vicikicchāsahagata; (4) diṭṭhigatasampayuttacittuppāda; (5) etthuppanna, moha; (6) lobhasahagatacittuppāda; (7) bhāvana
- **siya**: (1) domanassasahagatacittuppāda, cittuppāda; (2) anārammaṇa, rūpāvacaratikacatukkajjhāna, kiriyāhetukamanoviññāṇadhātu, ākāsānañcāyatana, ākiñcaññāyatana; (3) diṭṭhigatasampayuttacittuppāda; (4) diṭṭhigatavippayuttalobhasahagatacittuppāda; (5) sabba
- **upādāna**: (1) upādānasampayutta; (2) attavādupāda, sīlabbatupāda, kāmupāda, diṭṭhupāda; (3) upādāniya; (4) upādānātipi, cātipi; (5) tāneva; (6) avasesa
- **sabbasa**: (1) samatikkamma, arūpūpapattiya, sukha; (2) viññāṇañcāyatanasaññāsahagata; (3) amanasikāra, nānattasañña, samatikkama, ākāsānañcāyatanasaññāsahagata, paṭighasañña, rūpasañña
- **caturaṅgika**: (1) bala, dvāyatana, ekaṃ, ekā, dhātuya, dhammadhātu, aṭṭhindriya, khandha, dhammāyatana; (2) duvaṅgika
- **hiribala**: (1) ottappabala, kāyalahuta, cittamuduta, cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyapassaddhi, kāyapāguññata
- **ottappabala**: (1) hiribala, kāyalahuta, cittamuduta, cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyapassaddhi, kāyapāguññata
- **kāmāvacarakusalata**: (1) kāmāvacarakusala, vipākata, somanassasahagatacittuppāda, pañca, etthuppanna; (2) upekkhāsahagatacittuppāda, āruppa; (3) rūpāvacaratikacatukkajjhāna, lokuttaratikacatukkajjhāna; (4) lokuttaradukatikajjhāna
- **micchāsaṅkappa**: (1) ahirikabala, anottappabala, micchāvāyāma, ahirika, anottappa, micchāsamādhi, abhijjha, vīriyabala, paggāha, vitakka
- **asithilaparakkamata**: (1) ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, parakkama, vāyāma, thāma, anikkhittadhurata
- **cātipi**: (1) vattabba, avasesa, ṭhapetva; (2) kilesātipi; (3) hetūtipi; (4) āsavātipi; (5) saṃyojanātipi; (6) ganthātipi; (7) nīvaraṇātipi; (8) upādānātipi
- **dhiti**: (1) thāma, ussāha, uyyāma, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **dhurasampaggāha**: (1) ussāha, uyyāma, dhiti, nikkama, ussoḷhī, asithilaparakkamata, parakkama, vāyāma, thāma, anikkhittadhurata
- **kammavipāka**: (1) nākusala, kiriya, abyākata; (2) diṭṭhadhammasukhavihāra, sabbasa, samatikkamma; (3) kusalākusala, arūpāvacara; (4) abyākatamūla; (5) panārabbha
- **kusalamūla**: (1) asārajjitatta, alubbhana, alubbhitatta, asārajjana, asārāga, anabhijjha; (2) abyāpajja, adussitatta, adussana, abyāpāda
- **nikkama**: (1) thāma, ussāha, uyyāma, dhiti, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **nākusala**: (1) kammavipāka, kiriya, abyākata; (2) diṭṭhadhammasukhavihāra, sabbasa, samatikkamma; (3) kusalākusala, arūpāvacara; (4) abyākatamūla; (5) panārabbha
- **parakkama**: (1) ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, vāyāma, thāma, anikkhittadhurata
- **thāma**: (1) ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **ussoḷhī**: (1) thāma, ussāha, uyyāma, dhiti, nikkama, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **ussāha**: (1) thāma, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **uyyāma**: (1) thāma, ussāha, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, vāyāma, anikkhittadhurata
- **vāyāma**: (1) ussāha, uyyāma, dhiti, nikkama, ussoḷhī, dhurasampaggāha, asithilaparakkamata, parakkama, thāma, anikkhittadhurata
- **oḷārika**: (1) phoṭṭhabbāyatana; (2) rasāyatana, gandhāyatana; (3) anupādiṇṇupādāniya, upādiṇṇupādāniya, anupādiṇṇa, upādiṇṇa, sukhuma, dūra; (4) indriya
- **ahirikabala**: (1) anottappabala, micchāsaṅkappa, micchāvāyāma, ahirika, anottappa, micchāsamādhi, abhijjha, vīriyabala, paggāha; (2) rasārammaṇa
- **anottappabala**: (1) ahirikabala, micchāsaṅkappa, micchāvāyāma, ahirika, anottappa, micchāsamādhi, abhijjha, vīriyabala, paggāha; (2) rasārammaṇa
- **nāsāta**: (1) adukkhamasukha, cetosamphassaja, sāta, cetasika, vedayita, vedana; (2) upekkhindriya; (3) upekkha; (4) tajjāmanoviññāṇadhātusamphassaja; (5) caturaṅgika
- **upacitatta**: (1) rūpārammaṇa, upekkhindriya, upekkhāsahagata, uppanna, panārabbha; (2) kamma, abyākata; (3) arūpūpapattiya, sabbasa; (4) phoṭṭhabbārammaṇa
- **vippayutta**: (1) rūpakkhandha, sāsava, kusalākusalābyākata; (2) parāmāsavippayutta; (3) sabbañca; (4) āsavavippayutta; (5) saṃyojanavippayutta; (6) ganthavippayutta; (7) nīvaraṇavippayutta; (8) upādānavippayutta
- **yāpana**: (1) yapana, pālana, vattana, āyu, jīvita, iriyana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **dūra**: (1) itthindriya, purisindriya; (2) āpodhātu, ākāsadhātu, jarata; (3) anupādiṇṇupādāniya, upādiṇṇupādāniya, anupādiṇṇa, upādiṇṇa; (4) indriya
- **sukhuma**: (1) itthindriya, purisindriya; (2) āpodhātu, ākāsadhātu, jarata; (3) anupādiṇṇupādāniya, upādiṇṇupādāniya, anupādiṇṇa, upādiṇṇa; (4) indriya
- **ghānāyatana**: (1) jivhāyatana, sotāyatana, saddāyatana; (2) ghānadhātu, ghānindriya, ghāna, gandha, tīra, orima, samudda
- **phoṭṭhabbadhātu**: (1) pathavīdhātu, pharusa, garuka, saṇha, lahuka, muduka, kakkhaḷa, tejodhātu, vāyodhātu, sukhasamphassa
- **sīlabbataparāmāsa**: (1) sakkāyadiṭṭhi, tīṇi, saṃyojana, vicikiccha; (2) kāyagantha, idaṃsaccābhinivesa; (3) suddhi, sīla, sīlabbata, samaṇabrāhmaṇa
- **micchādiṭṭhi**: (1) sabbāpi, diṭṭhikantāra, kummagga, micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, micchatta, diṭṭhivipphandita
- **abhijjha**: (1) ahirikabala, anottappabala, micchāsaṅkappa, micchāvāyāma, micchāsamādhi, lobha, ahirika, anottappa; (2) sārāga, saddataṇha
- **ottappa**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **sabba**: (1) evaṃ, rūpasaṅgaha, sotaviññeyya, jivhāviññeyya, kāyaviññeyya, cakkhuviññeyya, ghānaviññeyya; (2) kiriyāhetukamanoviññāṇadhātu, anārammaṇa; (3) siya
- **gandhārammaṇa**: (1) rasārammaṇa, saddārammaṇa, phoṭṭhabbārammaṇa, dhammārammaṇa, rūpārammaṇa, panārabbha, ahirikabala, anottappabala, micchāsaṅkappa; (2) ghānaviññāṇa
- **kāyakamma**: (1) manokamma, vacīkamma, taṃsamuṭṭha, tadekaṭṭha, taṃsampayutta, tīṇi, kilesa, lobha; (2) pahātabbahetū; (3) pahātabba
- **manokamma**: (1) kāyakamma, vacīkamma, taṃsamuṭṭha, tadekaṭṭha, taṃsampayutta, tīṇi, kilesa, lobha; (2) pahātabbahetū; (3) pahātabba
- **rasārammaṇa**: (1) gandhārammaṇa, saddārammaṇa, phoṭṭhabbārammaṇa, dhammārammaṇa, rūpārammaṇa, panārabbha, ahirikabala, anottappabala, micchāsaṅkappa; (2) jivhāviññāṇa
- **saddārammaṇa**: (1) rasārammaṇa, gandhārammaṇa, phoṭṭhabbārammaṇa, dhammārammaṇa, rūpārammaṇa, panārabbha, ahirikabala, anottappabala, micchāsaṅkappa; (2) sotaviññāṇa
- **taṃsamuṭṭha**: (1) manokamma, kāyakamma, vacīkamma, tadekaṭṭha, taṃsampayutta, tīṇi, kilesa, lobha; (2) pahātabbahetū; (3) pahātabba
- **vacīkamma**: (1) manokamma, kāyakamma, taṃsamuṭṭha, tadekaṭṭha, taṃsampayutta, tīṇi, kilesa, lobha; (2) pahātabbahetū; (3) pahātabba
- **abhinivesa**: (1) micchāpatha, diṭṭhivisūkāyika, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **cittañca**: (1) avasesañca; (2) acetasika; (3) cittasamuṭṭhāna; (4) cittasahabhuna; (5) cittānuparivattina; (6) cittasaṃsaṭṭhasamuṭṭhāna; (7) cittasaṃsaṭṭhasamuṭṭhānasahabhuna; (8) cittasaṃsaṭṭhasamuṭṭhānānuparivattina; (9) dhātu, asaṅkhata
- **diṭṭhigahana**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **diṭṭhikantāra**: (1) diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, kummagga, micchāpatha, diṭṭhisaṃyojana
- **diṭṭhivipphandita**: (1) diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhikantāra, kummagga, micchāpatha, diṭṭhisaṃyojana
- **diṭṭhivisūkāyika**: (1) micchāpatha, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **gāha**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **iriyana**: (1) yapana, pālana, vattana, āyu, jīvita, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **jīvita**: (1) yapana, pālana, vattana, āyu, iriyana, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **kummagga**: (1) diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, micchāpatha, diṭṭhisaṃyojana
- **micchatta**: (1) diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, diṭṭhivipphandita, diṭṭhikantāra, kummagga, micchāpatha, diṭṭhisaṃyojana
- **micchāpatha**: (1) diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **pālana**: (1) yapana, vattana, āyu, jīvita, iriyana, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **titthāyatana**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga, diṭṭhisaṃyojana
- **vattana**: (1) yapana, pālana, āyu, jīvita, iriyana, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **yapana**: (1) pālana, vattana, āyu, jīvita, iriyana, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **āyu**: (1) yapana, pālana, vattana, jīvita, iriyana, yāpana, arūpīna, tesa, ṭhiti; (2) rūpīna
- **cakkhusamphassa**: (1) vatthu; (2) ārammaṇa; (3) cakkhusamphassaja, cakkhuṃ, cakkhuviññāṇa, nissa, uppajja, uppajji, uppajjissati, cakkhudhātu
- **kāyasamphassa**: (1) ghānasamphassa, jivhāsamphassa, sotasamphassa; (2) vatthu; (3) ārammaṇa; (4) kāyasamphassaja, kāyaviññāṇa, uppajja, uppajji, nissa
- **kāyasamphassaja**: (1) kāyika, asāta, vedayita, dukkha; (2) kāyaviññāṇa, vedana; (3) tajjākāyaviññāṇadhātusamphassaja; (4) kāyasamphassa, uppajji; (5) vatthu
- **rūpadhātu**: (1) vaṇṇanibha, ātapa, mañjiṭṭhaka, soḷasaṃsa, maṇisaṅkhamuttāveḷuriya, ādāsamaṇḍala, vaṭṭa, dhūma, ambaṅkuravaṇṇa, chaḷaṃsa
- **tadekaṭṭha**: (1) manokamma, kāyakamma, vacīkamma, taṃsamuṭṭha, taṃsampayutta, kilesa, tīṇi, lobha; (2) pahātabbahetū; (3) imāni
- **pañca**: (1) somanassasahagatacittuppāda, kāmāvacarakusalata, lokuttaratikacatukkajjhāna, kāmāvacarakusala, rūpāvacaratikacatukkajjhāna; (2) ahetukamanoviññāṇadhātuya, manodhātuya; (3) lokuttaradukatikajjhāna, rūpāvacaradukatikajjhāna, pītiṃ
- **cittakammaññata**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **cittalahuta**: (1) cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **cittamuduta**: (1) cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittalahuta
- **cittapassaddhi**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **cittapāguññata**: (1) cittalahuta, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **cittujukata**: (1) cittalahuta, cittapāguññata, kāyujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **kāyakammaññata**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **kāyalahuta**: (1) cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, cittamuduta, cittalahuta
- **kāyamuduta**: (1) cittalahuta, cittapāguññata, kāyujukata, cittujukata, cittakammaññata, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **kāyapassaddhi**: (1) cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta, cittalahuta
- **kāyapāguññata**: (1) cittapāguññata, kāyujukata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyalahuta, cittamuduta, cittalahuta
- **kāyujukata**: (1) cittalahuta, cittapāguññata, cittujukata, cittakammaññata, kāyamuduta, cittapassaddhi, kāyapassaddhi, kāyapāguññata, kāyalahuta, cittamuduta
- **saṅkhāra**: (1) saṅgahita; (2) viññāṇa; (3) assutava, attata, avinīta, ariyadhamma, rūpavanta, puthujjana, viññāṇavanta, samanupassati
- **cittacetasika**: (1) uppajjanti, ārabbha; (2) karitva, samāpanna, upapanna, diṭṭhadhammasukhavihārissa, ettha, etthāvacara, pariyanta, etasmiṃ
- **sasaṅkhāra**: (1) dhammārammaṇa, panārabbha, rūpārammaṇa, somanassasahagata, uppanna; (2) ñāṇavippayutta; (3) ñāṇasampayutta, upekkhāsahagata; (4) abyākatamūla; (5) diṭṭhigatavippayutta
- **viññatti**: (1) viññāpitatta, kusalacitta, abyākatacitta, viññāpana, akusalacitta, thambhana, samiñjenta, santhambhana, pasārenta, paṭikkamanta
- **cittādhipateyya**: (1) vīriyādhipateyya, vīmaṃsādhipateyya, majjhima, hīna, paṇīta, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) satipaṭṭha
- **vīriyādhipateyya**: (1) cittādhipateyya, vīmaṃsādhipateyya, majjhima, hīna, paṇīta, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) satipaṭṭha
- **vīmaṃsādhipateyya**: (1) cittādhipateyya, vīriyādhipateyya, majjhima, hīna, paṇīta, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) satipaṭṭha
- **samatikkamma**: (1) sabbasa, arūpūpapattiya, sukha; (2) viññāṇañcāyatanasaññāsahagata, ākāsānañcāyatana; (3) ākiñcaññāyatanasaññāsahagata, viññāṇañcāyatana; (4) nevasaññānāsaññāyatanasaññāsahagata, ākiñcaññāyatana; (5) diṭṭhadhammasukhavihāra
- **ghānindriya**: (1) sotindriya, jivhindriya, kāyindriya, purisindriya; (2) ghānadhātu, ghānāyatana, ghāna, gandha, tīra, orima
- **jivhindriya**: (1) ghānindriya, sotindriya, kāyindriya, purisindriya; (2) jivhādhātu, jivha, jivhāyatana, tīra, orima, samudda
- **sotindriya**: (1) ghānindriya, jivhindriya, kāyindriya, purisindriya; (2) sotadhātu, sota, sadda, sotāyatana, tīra, orima
- **anussati**: (1) apilāpanata, saraṇata, dhāraṇata, paṭissati, asammussanata, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **apilāpanata**: (1) anussati, saraṇata, dhāraṇata, paṭissati, asammussanata, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **arūpūpapattiya**: (1) sabbasa, samatikkamma; (2) viññāṇañcāyatanasaññāsahagata; (3) ākiñcaññāyatanasaññāsahagata; (4) amanasikāra, nānattasañña, samatikkama, ākāsānañcāyatanasaññāsahagata, paṭighasañña, rūpasañña
- **dhāraṇata**: (1) apilāpanata, anussati, saraṇata, paṭissati, asammussanata, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **panaññopi**: (1) paṇavasadda, pāṇisadda, gītasadda, manussasadda, nigghosasadda, sammasadda, amanussasadda, udakasadda, saṅkhasadda, vātasadda
- **paṭissati**: (1) apilāpanata, anussati, saraṇata, dhāraṇata, asammussanata, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **pubbanta**: (1) pubbantāparanta, idappaccayata, apariyogāhana, dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya, paṭipada, apaccavekkhaṇa, sammoha, avijjogha
- **saraṇata**: (1) apilāpanata, anussati, dhāraṇata, paṭissati, asammussanata, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **hīna**: (1) paṇīta, majjhima, cittādhipateyya, vīriyādhipateyya, vīmaṃsādhipateyya, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) ñāṇasampayutta
- **majjhima**: (1) hīna, paṇīta, cittādhipateyya, vīriyādhipateyya, vīmaṃsādhipateyya, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) ñāṇasampayutta
- **paṇīta**: (1) hīna, majjhima, cittādhipateyya, vīriyādhipateyya, vīmaṃsādhipateyya, chandādhipateyya; (2) arūpūpapattiya, sabbasa, samatikkamma; (3) ñāṇasampayutta
- **uppajjissati**: (1) uppajji, nissa, uppajja, uppajjati, ārabbha, peta, pesa, samudda, tīra, orima
- **sahetuka**: (1) kāmāvacarakiriyata, vipākata, cittuppāda, etthuppanna; (2) hetū; (3) ahetuka, hetūtipi; (4) aññamañña; (5) abyākatamūla, ñāṇasampayutta
- **ganthaniya**: (1) gantha; (2) aganthaniya, ganthātipi; (3) ganthavippayutta; (4) sāsava, rūpakkhandha; (5) ekavidha, ācayagāmi, nevasekkhanāsekkha, nevavipākanavipākadhammadhamma
- **nīvaraṇiya**: (1) nīvaraṇa; (2) tāneva; (3) anīvaraṇiya, nīvaraṇātipi; (4) nīvaraṇavippayutta; (5) sāsava, rūpakkhandha; (6) ekavidha, ācayagāmi, nevasekkhanāsekkha
- **parāmaṭṭha**: (1) parāmāsa; (2) aparāmaṭṭha; (3) parāmāsavippayutta; (4) sāsava, rūpakkhandha; (5) ekavidha, ācayagāmi, nevasekkhanāsekkha, nevavipākanavipākadhammadhamma, asaṃkiliṭṭhasaṃkilesika
- **saṃkilesika**: (1) asaṃkilesika, kilesātipi; (2) kilesa; (3) kilesavippayutta; (4) sāsava, rūpakkhandha; (5) ekavidha, ācayagāmi, nevasekkhanāsekkha, nevavipākanavipākadhammadhamma
- **saṃyojaniya**: (1) saṃyojana; (2) tāneva; (3) asaṃyojaniya, saṃyojanātipi; (4) saṃyojanavippayutta; (5) sāsava, rūpakkhandha; (6) ekavidha, ācayagāmi, nevasekkhanāsekkha
- **upādāniya**: (1) upādāna; (2) tāneva; (3) anupādāniya, upādānātipi; (4) upādānavippayutta; (5) sāsava, rūpakkhandha; (6) ekavidha, ācayagāmi, nevasekkhanāsekkha
- **cakkhudhātu**: (1) nayana, netta, cakkhuṃ, cakkhu, cakkhundriya, sanidassana, tīra, orima, samudda, dvāra
- **kāyadhātu**: (1) ghānadhātu, sotadhātu, jivhādhātu; (2) phoṭṭhabba, kāyindriya, samudda, dvāra, kāya, tīra, orima
- **sukhasahagata**: (1) sukhabhūmiya; (2) kāmāvacarakusalata, kāmāvacarakusala, upekkhāsahagatacittuppāda, āruppa; (3) pītisahagata; (4) sukhañca; (5) lokuttaratikacatukkajjhāna, somanassasahagatacittuppāda, rūpāvacaratikacatukkajjhāna
- **phoṭṭhabba**: (1) kāya; (2) sukhasamphassa, dukkhasamphassa, lahuka, muduka, pharusa, garuka, saṇha, kakkhaḷa, tejodhātu
- **domanassasahagata**: (1) dvīsu, vicikicchāsahagata, cittuppāda; (2) lobhasahagata, aṭṭhasu, sabbākusala, uppajjati; (3) diṭṭhigatavippayuttalobhasahagata; (4) sasaṅkhārika; (5) paṭighasampayutta
- **cakkhu**: (1) nayana, netta, cakkhuṃ, cakkhudhātu, tīra; (2) suñña, pasāda, cakkhundriya, gāma, catunna
- **āyatana**: (1) satipaṭṭha, iddhipāda, dhātuṃ, sammappadha, sacca, bojjhaṅga, bala; (2) ācaya; (3) vīsati, mahānaya
- **abhiniropana**: (1) appana, saṅkappa, byappana, takka, sammāsaṅkappa, vitakka; (2) micchāsaṅkappa
- **apariyogāhana**: (1) pubbantāparanta, idappaccayata, pubbanta, ananubodha, avijjogha, sammoha, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjāyoga
- **appana**: (1) takka, saṅkappa, byappana, abhiniropana, sammāsaṅkappa, vitakka; (2) micchāsaṅkappa
- **asammussanata**: (1) apilāpanata, anussati, saraṇata, dhāraṇata, paṭissati, satibala, sammāsati, satindriya; (2) satisambojjhaṅga, maggapariyāpanna
- **aṭṭhindriya**: (1) caturaṅgika, satta, bala, dvāyatana, somanassindriya, ekaṃ, ekā, dhātuya, dhammadhātu; (2) duvaṅgika
- **byappana**: (1) appana, saṅkappa, abhiniropana, takka, sammāsaṅkappa, vitakka; (2) micchāsaṅkappa
- **dhammavicayasambojjhaṅga**: (1) kosalla, paññāobhāsa, bhūrī, sallakkhaṇa, paññāpāsāda, upaparikkha, cinta, paṇḍicca, paññāpajjota, upalakkhaṇa
- **idappaccayata**: (1) pubbantāparanta, pubbanta, apariyogāhana, dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya, paṭipada, apaccavekkhaṇa, sammoha, avijjogha
- **kusalākusala**: (1) kammavipāka, nākusala, kiriya; (2) yañca, sāsava; (3) arūpāvacara, rūpāvacara, kāmāvacara; (4) ācayagāmina; (5) uppādina
- **pubbantāparanta**: (1) idappaccayata, pubbanta, apariyogāhana, dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya, paṭipada, apaccavekkhaṇa, sammoha, avijjogha
- **sañjānana**: (1) sañjānitatta, sañña; (2) tajjāmanoviññāṇadhātusamphassaja; (3) tajjācakkhuviññāṇadhātusamphassaja; (4) tajjāmanodhātusamphassaja; (5) tajjākāyaviññāṇadhātusamphassaja
- **sañjānitatta**: (1) sañjānana, sañña; (2) tajjāmanoviññāṇadhātusamphassaja; (3) tajjācakkhuviññāṇadhātusamphassaja; (4) tajjāmanodhātusamphassaja; (5) tajjākāyaviññāṇadhātusamphassaja
- **saṅkappa**: (1) takka, appana, byappana, abhiniropana, sammāsaṅkappa, vitakka; (2) micchāsaṅkappa
- **takka**: (1) appana, saṅkappa, byappana, abhiniropana, sammāsaṅkappa, vitakka; (2) micchāsaṅkappa
- **nissa**: (1) uppajji, uppajja, uppajjissati, uppajjati, ārabbha, peta, pesa, samudda, tīra, orima
- **uppajja**: (1) uppajji, nissa, uppajjissati, uppajjati, ārabbha, peta, pesa, samudda, tīra, orima
- **uppajji**: (1) nissa, uppajja, uppajjissati, uppajjati, ārabbha, peta, pesa, samudda, tīra, orima
- **uddhacca**: (1) bhantatta, vikkhepa, avūpasama; (2) māna, thina, kilesavatthūni; (3) kukkucca, uddhaccakukkuccanīvaraṇa; (4) anottappa, ahirika
- **atta**: (1) cāti; (2) avinīta, ariyadhamma, rūpavanta, puthujjana, viññāṇavanta, samanupassati, sappurisadhamma, assutava, attata
- **gandha**: (1) ghāna; (2) pupphagandha, sāragandha, sugandha, phalagandha, vissagandha, tacagandha, pattagandha, āmakagandha, mūlagandha
- **ghāna**: (1) gandha; (2) pupphagandha, sāragandha, sugandha, phalagandha, vissagandha, tacagandha, pattagandha, āmakagandha, mūlagandha
- **jivha**: (1) rasa; (2) loṇika, kaṭuka, madhura, puppharasa, phalarasa, asādu, lambila, kasāva, pattarasa
- **sadda**: (1) sota; (2) saṅkhasadda, vātasadda, paṇavasadda, pāṇisadda, gītasadda, manussasadda, nigghosasadda, amanussasadda, udakasadda
- **hirīyati**: (1) hiriyitabba, samāpattiya, pāpaka, akusala; (2) hiribala; (3) hirī; (4) ahirika
- **ottappati**: (1) ottappitabba, samāpattiya, pāpaka, akusala; (2) ottappa; (3) ottappabala; (4) anottappa; (5) imāni
- **pītisahagata**: (1) pītiṃ, lokuttaradukatikajjhāna, rūpāvacaradukatikajjhāna, somanassasahagatacittuppāda; (2) pītibhūmiya; (3) kāmāvacarakusalata, kāmāvacarakusala, upekkhāsahagatacittuppāda, āruppa; (4) sukhasahagata
- **kāyika**: (1) vācasika, kāyikavācasika, avītikkama, sīlasaṃvara, sabbopi; (2) kāyasamphassaja, asāta, vedayita, dukkha; (3) tajjākāyaviññāṇadhātusamphassaja
- **sakkāyadiṭṭhi**: (1) sīlabbataparāmāsa; (2) avinīta, ariyadhamma, rūpavanta, puthujjana, viññāṇavanta, samanupassati, sappurisadhamma, assutava, attata
- **manodhātu**: (1) tīṇindriya, dhātuya, dhammadhātu; (2) sotaviññāṇa, ghānaviññāṇa, jivhāviññāṇa; (3) phoṭṭhabbārammaṇa, upekkhindriya, vitakka, vicāra
- **diṭṭhigatasampayutta**: (1) lobhasahagata, aṭṭhasu, sabbākusala, uppajjati, diṭṭhigatavippayuttalobhasahagata, dvīsu, domanassasahagata, cittuppāda, uppajjanti; (2) dhammārammaṇa
- **pañcaṅgika**: (1) bala, dvāyatana, ekaṃ, ekā, dhātuya, dhammadhātu, khandha, dhammāyatana; (2) sammāsamādhi, avisāhaṭamānasata
- **cetayitatta**: (1) sañcetana, tajjāmanoviññāṇadhātusamphassaja, cetana; (2) manosañcetanāhāra; (3) tajjācakkhuviññāṇadhātusamphassaja; (4) tajjāmanodhātusamphassaja; (5) tajjākāyaviññāṇadhātusamphassaja
- **diṭṭhigatasampayuttacittuppāda**: (1) domanassasahagatacittuppāda, siya, diṭṭhigatavippayuttalobhasahagatacittuppāda; (2) vicikicchāsahagata, cittuppāda, dassana; (3) moha, pahātabbahetuka; (4) etthuppanna; (5) aniyata
- **diṭṭhigatavippayuttalobhasahagatacittuppāda**: (1) domanassasahagatacittuppāda, siya; (2) vicikicchāsahagata, uddhaccasahagata, cittuppāda; (3) diṭṭhigatasampayuttacittuppāda; (4) parāmāsavippayutta; (5) moha, etthuppanna; (6) aniyata
- **hiriyitabba**: (1) hirīyati, samāpattiya, pāpaka, akusala; (2) hiribala; (3) hirī; (4) ahirika
- **imāni**: (1) tadekaṭṭha, manokamma, kāyakamma, vacīkamma, taṃsamuṭṭha, pahātabbahetū, suddhīti, tīṇi, sīlabbataparāmāsa, pahātabba
- **kusalahetū**: (1) abyākatahetū; (2) akusalahetū, kāmāvacarahetū; (3) rūpāvacarahetū; (4) arūpāvacarahetū; (5) apariyāpannahetū; (6) ñāṇa, dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya
- **ottappitabba**: (1) ottappati, samāpattiya, pāpaka, akusala; (2) ottappa; (3) ottappabala; (4) anottappa; (5) imāni
- **patiṭṭhāha**: (1) micchāpatha, diṭṭhivisūkāyika, abhinivesa, gāha, diṭṭhigahana, titthāyatana, micchatta, diṭṭhivipphandita, diṭṭhikantāra, kummagga
- **paṭipada**: (1) dukkhanirodhagāminiya, dukkhanirodha, dukkhasamudaya, idappaccayata, pubbantāparanta, apaccavekkhaṇa, pubbanta, avijjogha, sammoha, apaccakkhakamma
- **sañcetana**: (1) cetayitatta, tajjāmanoviññāṇadhātusamphassaja, cetana; (2) manosañcetanāhāra; (3) tajjācakkhuviññāṇadhātusamphassaja; (4) tajjāmanodhātusamphassaja; (5) tajjākāyaviññāṇadhātusamphassaja
- **kilesasampayutta**: (1) kilesavippayutta; (2) kilesa; (3) kilesātipi; (4) māna, thina; (5) asaṃkilesika; (6) akusalacittuppāda, dvādasa; (7) sampayutta; (8) yattha
- **āsavasampayutta**: (1) āsava; (2) āsavavippayutta; (3) āsavātipi; (4) avijjāsava, diṭṭhāsava, bhavāsava, kāmāsava; (5) anāsava; (6) sampayutta; (7) moha
- **ganthasampayutta**: (1) gantha; (2) ganthavippayutta; (3) abhijjhākāyagantha, idaṃsaccābhinivesa; (4) ganthātipi, domanassasahagatacittuppāda, lobhasahagatacittuppāda, aṭṭha; (5) aganthaniya; (6) sampayutta
- **nīvaraṇasampayutta**: (1) nīvaraṇa; (2) nīvaraṇavippayutta; (3) nīvaraṇātipi; (4) uddhaccanīvaraṇa, kukkuccanīvaraṇa, byāpādanīvaraṇa, kāmacchandanīvaraṇa, avijjānīvaraṇa, vicikicchānīvaraṇa, thinamiddhanīvaraṇa
- **saṃyojanasampayutta**: (1) saṃyojanavippayutta; (2) saṃyojana; (3) saṃyojanātipi; (4) macchariyasaṃyojana, vicikicchāsaṃyojana, issāsaṃyojana, bhavarāgasaṃyojana, kāmarāgasaṃyojana, mānasaṃyojana, avijjāsaṃyojana
- **upādānasampayutta**: (1) upādāna; (2) upādānavippayutta; (3) upādānātipi, lobhasahagatacittuppāda, aṭṭha; (4) kāmupāda, diṭṭhupāda, attavādupāda, sīlabbatupāda; (5) anupādāniya
- **ganthavippayutta**: (1) ganthasampayutta; (2) aganthaniya; (3) diṭṭhigatavippayuttalobhasahagata, paṭigha, dvīsu, domanassasahagata; (4) ganthaniya; (5) ganthātipi, lobhasahagatacittuppāda; (6) vippayutta
- **kilesavippayutta**: (1) kilesasampayutta; (2) asaṃkilesika; (3) saṃkilesika, kusalābyākata; (4) vippayutta; (5) kilesātipi
- **nīvaraṇavippayutta**: (1) nīvaraṇasampayutta; (2) anīvaraṇiya; (3) nīvaraṇiya, kusalābyākata; (4) nīvaraṇātipi; (5) vippayutta
- **saṃyojanavippayutta**: (1) saṃyojanasampayutta; (2) asaṃyojaniya; (3) saṃyojaniya; (4) saṃyojanātipi; (5) vippayutta; (6) uddhaccasahagata
- **upādānavippayutta**: (1) upādānasampayutta; (2) anupādāniya, dutiyabhāṇavāra, nikkhepakaṇḍa; (3) diṭṭhigatavippayuttalobhasahagata, domanassasahagatacittuppāda; (4) upādāniya; (5) upādānātipi, lobhasahagatacittuppāda; (6) vippayutta
- **āsavavippayutta**: (1) āsavasampayutta; (2) anāsava, paṭhamabhāṇavāra, nikkhepakaṇḍa; (3) dvīsu, domanassasahagata, vicikicchāsahagata, uddhaccasahagata; (4) āsavātipi; (5) vippayutta
- **aniyata**: (1) micchattaniyata, sammattaniyata; (2) niyata; (3) diṭṭhigatavippayuttalobhasahagatacittuppāda; (4) diṭṭhigatasampayuttacittuppāda, siya; (5) ekavidha, ācayagāmi, nevasekkhanāsekkha, nevavipākanavipākadhammadhamma
- **dvīsu**: (1) domanassasahagata, vicikicchāsahagata, cittuppāda; (2) lobhasahagata, aṭṭhasu, sabbākusala, uppajjati, diṭṭhigatasampayutta; (3) diṭṭhigatavippayuttalobhasahagata; (4) sasaṅkhārika
- **avijja**: (1) aññāṇa, adassana, avijjālaṅgī, ananubodha, avijjogha, sammoha, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjāyoga
- **pathavīdhātu**: (1) kakkhaḷa, tejodhātu, vāyodhātu, saṇha, lahuka, muduka, pharusa, garuka, phoṭṭhabbadhātu, sukhasamphassa
- **arūpīna**: (1) vattana, āyu, jīvita, iriyana, yapana, pālana, yāpana, tīṇindriya, tesa, ṭhiti
- **kusalābyākata**: (1) mahaggata; (2) rūpakkhandha, vippayutta, sāsava; (3) arūpāvacara, rūpāvacara, kāmāvacara; (4) araṇa; (5) asaṃkiliṭṭhasaṃkilesika; (6) asaṃkiliṭṭha
- **rūpāvacaratikacatukkajjhāna**: (1) lokuttaratikacatukkajjhāna, somanassasahagatacittuppāda, kāmāvacarakusalata, vipākata, pañca; (2) anārammaṇa, kiriyāhetukamanoviññāṇadhātu, ākāsānañcāyatana, ākiñcaññāyatana; (3) ñāṇavippayuttacittuppāda
- **samaṇabrāhmaṇa**: (1) sīlabbata, suddhi, sīla, suddhīti; (2) sacchikatva, pita, opapātika, māta, dinna, pavedentīti
- **tīṇindriya**: (1) arūpīna, dvāyatana, yapana, pālana, vattana, āyu, jīvita, iriyana, ekaṃ, yāpana
- **āruppa**: (1) upekkhāsahagatacittuppāda, kāmāvacarakusalata, vipākata, kāmāvacarakusala; (2) aṭṭha, lokuttaradukadukajjhāna, rūpāvacaradukadukajjhāna, ekādasa; (3) lokuttaratikatikajjhāna, rūpāvacaratikatikajjhāna
- **aññāṇa**: (1) adassana, avijjālaṅgī, asampajañña, ananubodha, avijjogha, sammoha, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjāyoga
- **chandādhipateyyanti**: (1) animitta, appaṇihita, suññata, pañcama, tatiya, dutiya, vūpasama, vitakkavicāra, catuttha, bhūmiya
- **hetusampayutta**: (1) hetuvippayutta, hetūtipi; (2) kāmāvacarakiriyata, moha; (3) aññamañña; (4) hetū; (5) sampayutta; (6) yattha
- **cittasamuṭṭha**: (1) cittahetuka, cittaja, kammaññata, lahuta, muduta, saddāyatana, ākāsadhātu, gandhāyatana, āpodhātu; (2) cittasamuṭṭhāna
- **ñāṇavippayutta**: (1) sasaṅkhāra, somanassasahagata, dhammārammaṇa, panārabbha, rūpārammaṇa, uppanna; (2) sattindriya; (3) ñāṇasampayutta, abyākatamūla; (4) alobha
- **saṃkiliṭṭha**: (1) asaṃkiliṭṭha, kilesātipi; (2) kilesa; (3) akusalacittuppāda, dvādasa
- **appaṇihitanti**: (1) suññatanti, animittanti, pañcama, tatiya, dutiya, vūpasama, vitakkavicāra, catuttha, bhūmiya; (2) suddhikapaṭipada
- **suññatanti**: (1) appaṇihitanti, animittanti, pañcama, tatiya, dutiya, vūpasama, vitakkavicāra, catuttha, bhūmiya; (2) suddhikapaṭipada
- **parāmāsavippayutta**: (1) parāmāsasampayutta; (2) aparāmaṭṭha; (3) diṭṭhigatavippayuttalobhasahagatacittuppāda, domanassasahagatacittuppāda, vicikicchāsahagata, uddhaccasahagata; (4) parāmaṭṭha; (5) vippayutta; (6) parāmāsa
- **ñāṇasampayutta**: (1) sasaṅkhāra, somanassasahagata, dhammārammaṇa, panārabbha, rūpārammaṇa, uppanna; (2) ñāṇavippayutta, abyākatamūla; (3) hīna, paṇīta
- **ahetuka**: (1) ahetukamanoviññāṇadhātuya, manodhātuya, tissa, dvepañcaviññāṇa, pañca; (2) sahetuka, hetūtipi; (3) ekavidha, ācayagāmi, nevasekkhanāsekkha
- **ogha**: (1) jīvitāsa, jappana, paṇidhi, rūpataṇha, taṇhājāla, lata, saddataṇha, gedha, anurodha, dhanāsa
- **abyākatahetū**: (1) kusalahetū; (2) apariyāpannahetū; (3) akusalahetū, kāmāvacarahetū; (4) rūpāvacarahetū; (5) arūpāvacarahetū; (6) sabbākusala, kāmāvacarakiriyata; (7) alobha, vipākata
- **anārammaṇa**: (1) kiriyāhetukamanoviññāṇadhātu, rūpāvacaratikacatukkajjhāna, ākāsānañcāyatana, ākiñcaññāyatana, siya, sāmaññaphala; (2) ñāṇavippayuttacittuppāda, ñāṇasampayuttacittuppāda, sabba; (3) ekavidha
- **aññindriya**: (1) kāmarāgabyāpāda, tanubhāva; (2) anavasesappahāna, rūparāgaarūparāgamānauddhaccaavijja; (3) aññātāvindriya; (4) sacchikiriya, diṭṭha; (5) bhāvitatta, lokuttara, tasseva
- **dhammāyatanapariyāpanna**: (1) yañca, appaṭigha, anidassana; (2) anidassanaappaṭigha, tika; (3) ekādasavidha, ekādasaka, mātika; (4) rūpakaṇḍa, niṭṭhita
- **gandhadhātu**: (1) sugandha, phalagandha, vissagandha, tacagandha, pattagandha, duggandha, āmakagandha, mūlagandha, pupphagandha, sāragandha
- **ghānadhātu**: (1) sotadhātu, jivhādhātu, kāyadhātu; (2) ghānindriya, ghānāyatana, ghāna, gandha, tīra, orima, samudda
- **jivhādhātu**: (1) sotadhātu, ghānadhātu, kāyadhātu; (2) jivhindriya, jivha, jivhāyatana, orima, tīra; (3) yāya; (4) rasa
- **moha**: (1) uddhaccasahagata; (2) domanassasahagatacittuppāda, etthuppanna, pahātabbahetuka, siya, diṭṭhigatavippayuttalobhasahagatacittuppāda; (3) vicikicchāsahagata, cittuppāda; (4) kāmāvacarakiriyata; (5) diṭṭhigatasampayuttacittuppāda
- **rasadhātu**: (1) madhura, puppharasa, phalarasa, asādu, lambila, sādu, kasāva, pattarasa, loṇika, kaṭuka
- **saddadhātu**: (1) dhātūna, saṅkhasadda, vātasadda, paṇavasadda, pāṇisadda, gītasadda, manussasadda, nigghosasadda, amanussasadda, udakasadda
- **sotadhātu**: (1) sota, sotindriya, sadda, sotāyatana, tīra, orima, samudda; (2) jivhādhātu, ghānadhātu, kāyadhātu
- **adassana**: (1) avijjālaṅgī, aññāṇa, asampajañña, ananubodha, avijjogha, sammoha, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjāyoga
- **akakkhaḷata**: (1) akathinata, maddavata, muduta; (2) maddava; (3) cittamuduta; (4) kāyamuduta
- **akathinata**: (1) akakkhaḷata, maddavata, muduta; (2) maddava; (3) cittamuduta; (4) kāyamuduta
- **animittanti**: (1) suññatanti, appaṇihitanti, pañcama, tatiya, dutiya, vūpasama, vitakkavicāra, catuttha, bhūmiya; (2) suddhikapaṭipada
- **avijjālaṅgī**: (1) adassana, aññāṇa, asampajañña, ananubodha, avijjogha, sammoha, apaccakkhakamma, anabhisamaya, avijjāpariyuṭṭha, avijjāyoga
- **maddavata**: (1) akathinata, akakkhaḷata, muduta; (2) maddava; (3) cittamuduta; (4) kāyamuduta
- **manovilekha**: (1) thambhitatta, vicikicchati, kaṅkhati, satthari, kaṅkhāyana, saṃsaya, dvedhāpatha, dveḷhaka, kaṅkhāyitatta, anekaṃsaggāha
- **pañcindriya**: (1) tivaṅgika, caturaṅgika, dvāyatana, ekaṃ, ekā, dhātuya, dhammadhātu, khandha, bala, dhammāyatana
- **paṭigha**: (1) anattha, piya, kujjhitatta, jāyati, appiya, paṭighāta, āghāta, amanāpa, carissatīti, kujjhana

---

## Detailed entries

### dhamma

_pi blocks: 961; sense clusters: 4; inflected forms: dhammaṃ, dhamme, dhammehi, dhammesu, dhammo, dhammā, dhammānaṃ_

#### cluster (1) — top co-lemma: **kusala** (cohesion 0.73, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusala | 0.50 | 324 | 324 |
| phassa | 0.44 | 297 | 277 |
| avikkhepa | 0.40 | 264 | 242 |
| yasmiṃ | 0.39 | 230 | 230 |
| jhāna | 0.37 | 223 | 220 |
| bhāveti | 0.34 | 195 | 195 |
| paṭhama | 0.30 | 169 | 169 |

#### cluster (2) — top co-lemma: **magga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| magga | 0.33 | 196 | 193 |

#### cluster (3) — top co-lemma: **viññāṇakkhandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇakkhandha | 0.29 | 209 | 167 |

#### cluster (4) — top co-lemma: **vipāka** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipāka | 0.27 | 156 | 153 |

### rūpa

_pi blocks: 568; sense clusters: 9; inflected forms: rūpamhi, rūpasmiṃ, rūpassa, rūpaṃ, rūpāni_

#### cluster (1) — top co-lemma: **taṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| taṃ | 0.80 | 396 | 388 |

#### cluster (2) — top co-lemma: **kabaḷīkāra** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kabaḷīkāra | 0.40 | 145 | 143 |
| āhāra | 0.38 | 185 | 143 |

#### cluster (3) — top co-lemma: **cakkhāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhāyatana | 0.34 | 129 | 120 |

#### cluster (4) — top co-lemma: **rūpāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāyatana | 0.32 | 116 | 109 |

#### cluster (5) — top co-lemma: **yaṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yaṃ | 0.26 | 237 | 104 |

#### cluster (6) — top co-lemma: **bāhira** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bāhira | 0.26 | 87 | 84 |

#### cluster (7) — top co-lemma: **mahābhūta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| mahābhūta | 0.25 | 85 | 83 |

#### cluster (8) — top co-lemma: **upāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upāda | 0.25 | 93 | 84 |

#### cluster (9) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.25 | 87 | 82 |

### kusala

_pi blocks: 324; sense clusters: 2; inflected forms: kusalassa, kusalaṃ, kusalā, kusalānaṃ_

#### cluster (1) — top co-lemma: **yasmiṃ** (cohesion 0.72, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yasmiṃ | 0.78 | 230 | 215 |
| avikkhepa | 0.75 | 264 | 221 |
| bhāveti | 0.75 | 195 | 195 |
| phassa | 0.74 | 297 | 230 |
| jhāna | 0.74 | 223 | 202 |
| paṭhama | 0.68 | 169 | 168 |
| vivicceva | 0.58 | 132 | 132 |
| kāma | 0.57 | 136 | 132 |
| magga | 0.50 | 196 | 129 |

#### cluster (2) — top co-lemma: **vipāka** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipāka | 0.55 | 156 | 131 |

### phassa

_pi blocks: 297; sense clusters: 2; inflected forms: phassaṃ, phasso_

#### cluster (1) — top co-lemma: **yasmiṃ** (cohesion 0.75, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yasmiṃ | 0.87 | 230 | 230 |
| avikkhepa | 0.86 | 264 | 240 |
| jhāna | 0.80 | 223 | 208 |
| bhāveti | 0.79 | 195 | 195 |
| kusala | 0.74 | 324 | 230 |
| paṭhama | 0.71 | 169 | 166 |
| vivicceva | 0.62 | 132 | 132 |
| kāma | 0.61 | 136 | 132 |

#### cluster (2) — top co-lemma: **magga** (cohesion 0.77, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| magga | 0.54 | 196 | 133 |
| rūpūpapattiya | 0.51 | 102 | 102 |

### avikkhepa

_pi blocks: 264; sense clusters: 2; inflected forms: avikkhepo_

#### cluster (1) — top co-lemma: **yasmiṃ** (cohesion 0.77, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yasmiṃ | 0.88 | 230 | 218 |
| phassa | 0.86 | 297 | 240 |
| bhāveti | 0.85 | 195 | 195 |
| jhāna | 0.83 | 223 | 202 |
| paṭhama | 0.77 | 169 | 166 |
| kusala | 0.75 | 324 | 221 |
| vivicceva | 0.67 | 132 | 132 |
| kāma | 0.66 | 136 | 132 |

#### cluster (2) — top co-lemma: **rūpūpapattiya** (cohesion 0.80, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpūpapattiya | 0.56 | 102 | 102 |
| magga | 0.56 | 196 | 128 |

### jhāna

_pi blocks: 223; sense clusters: 1; inflected forms: jhānassa, jhānaṃ, jhāne_

#### cluster (1) — top co-lemma: **bhāveti** (cohesion 0.71, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāveti | 0.93 | 195 | 195 |
| yasmiṃ | 0.88 | 230 | 199 |
| paṭhama | 0.86 | 169 | 168 |
| avikkhepa | 0.83 | 264 | 202 |
| phassa | 0.80 | 297 | 208 |
| vivicceva | 0.74 | 132 | 132 |
| kusala | 0.74 | 324 | 202 |
| kāma | 0.74 | 136 | 132 |
| magga | 0.65 | 196 | 136 |
| rūpūpapattiya | 0.63 | 102 | 102 |

### viññāṇakkhandha

_pi blocks: 209; sense clusters: 5; inflected forms: viññāṇakkhandhassa, viññāṇakkhandhaṃ, viññāṇakkhandho_

#### cluster (1) — top co-lemma: **vedanākkhandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vedanākkhandha | 0.71 | 178 | 137 |

#### cluster (2) — top co-lemma: **rūpāvacara** (cohesion 0.70, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacara | 0.50 | 102 | 78 |
| kāmāvacara | 0.48 | 115 | 78 |
| arūpāvacara | 0.45 | 88 | 67 |
| kusalākusalābyākata | 0.32 | 41 | 40 |

#### cluster (3) — top co-lemma: **ṭhapetva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.46 | 137 | 80 |

#### cluster (4) — top co-lemma: **saṅkhārakkhandha** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhārakkhandha | 0.37 | 95 | 56 |
| saññākkhandha | 0.37 | 97 | 56 |

#### cluster (5) — top co-lemma: **dhātu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.32 | 81 | 47 |
| asaṅkhata | 0.32 | 84 | 47 |

### magga

_pi blocks: 196; sense clusters: 1; inflected forms: maggaṃ, maggo, maggā_

#### cluster (1) — top co-lemma: **rūpūpapattiya** (cohesion 0.78, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpūpapattiya | 0.68 | 102 | 102 |
| jhāna | 0.65 | 223 | 136 |
| bhāveti | 0.61 | 195 | 120 |
| yasmiṃ | 0.58 | 230 | 124 |
| avikkhepa | 0.56 | 264 | 128 |
| phassa | 0.54 | 297 | 133 |
| paṭhama | 0.52 | 169 | 95 |
| kusala | 0.50 | 324 | 129 |
| vivicceva | 0.48 | 132 | 78 |
| kāma | 0.47 | 136 | 78 |

### bhāveti

_pi blocks: 195; sense clusters: 2; inflected forms: bhāveti_

#### cluster (1) — top co-lemma: **jhāna** (cohesion 0.77, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jhāna | 0.93 | 223 | 195 |
| yasmiṃ | 0.92 | 230 | 195 |
| paṭhama | 0.91 | 169 | 166 |
| avikkhepa | 0.85 | 264 | 195 |
| vivicceva | 0.81 | 132 | 132 |
| kāma | 0.80 | 136 | 132 |
| phassa | 0.79 | 297 | 195 |
| kusala | 0.75 | 324 | 195 |
| rūpūpapattiya | 0.69 | 102 | 102 |

#### cluster (2) — top co-lemma: **pahāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahāna | 0.63 | 92 | 91 |

### āhāra

_pi blocks: 185; sense clusters: 6; inflected forms: āhāraṃ, āhāro, āhārā_

#### cluster (1) — top co-lemma: **kabaḷīkāra** (cohesion 0.97, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kabaḷīkāra | 0.88 | 145 | 145 |
| taṃ | 0.49 | 396 | 142 |

#### cluster (2) — top co-lemma: **rūpāyatana** (cohesion 0.61, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāyatana | 0.43 | 116 | 64 |
| bāhira | 0.38 | 87 | 52 |

#### cluster (3) — top co-lemma: **atthi** (cohesion 0.64, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| atthi | 0.42 | 160 | 73 |
| ākāsadhātu | 0.36 | 46 | 42 |
| panaññampi | 0.34 | 57 | 41 |

#### cluster (4) — top co-lemma: **cakkhāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhāyatana | 0.32 | 129 | 50 |

#### cluster (5) — top co-lemma: **khandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| khandha | 0.31 | 38 | 35 |

#### cluster (6) — top co-lemma: **itthindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.30 | 48 | 35 |

### vedanākkhandha

_pi blocks: 178; sense clusters: 4; inflected forms: vedanākkhandhassa, vedanākkhandhaṃ, vedanākkhandho_

#### cluster (1) — top co-lemma: **viññāṇakkhandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇakkhandha | 0.71 | 209 | 137 |

#### cluster (2) — top co-lemma: **saṅkhārakkhandha** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhārakkhandha | 0.64 | 95 | 87 |
| saññākkhandha | 0.63 | 97 | 87 |

#### cluster (3) — top co-lemma: **ṭhapetva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.42 | 137 | 66 |

#### cluster (4) — top co-lemma: **dhātu** (cohesion 0.66, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.37 | 81 | 48 |
| asaṅkhata | 0.37 | 84 | 48 |
| rūpāvacara | 0.34 | 102 | 47 |
| sabbañca | 0.32 | 79 | 41 |
| kāmāvacara | 0.31 | 115 | 45 |
| arūpāvacara | 0.29 | 88 | 39 |

### paṭhama

_pi blocks: 169; sense clusters: 2; inflected forms: paṭhamaṃ, paṭhamo, paṭhamāya_

#### cluster (1) — top co-lemma: **bhāveti** (cohesion 0.82, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāveti | 0.91 | 195 | 166 |
| vivicceva | 0.88 | 132 | 132 |
| kāma | 0.87 | 136 | 132 |
| jhāna | 0.86 | 223 | 168 |
| yasmiṃ | 0.83 | 230 | 166 |
| avikkhepa | 0.77 | 264 | 166 |
| phassa | 0.71 | 297 | 166 |
| kusala | 0.68 | 324 | 168 |
| rūpūpapattiya | 0.66 | 102 | 89 |

#### cluster (2) — top co-lemma: **dandhābhiñña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dandhābhiñña | 0.63 | 77 | 77 |

### citta

_pi blocks: 161; sense clusters: 5; inflected forms: cittassa, cittaṃ, cittena, cittā_

#### cluster (1) — top co-lemma: **manindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manindriya | 0.52 | 64 | 59 |

#### cluster (2) — top co-lemma: **samādhindriya** (cohesion 0.81, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhindriya | 0.41 | 67 | 47 |
| samatha | 0.40 | 53 | 43 |
| samādhibala | 0.36 | 49 | 38 |

#### cluster (3) — top co-lemma: **paṭiccasamuppanna** (cohesion 0.77, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭiccasamuppanna | 0.38 | 94 | 48 |
| cittassekaggata | 0.37 | 74 | 44 |
| aññepi | 0.36 | 83 | 44 |
| arūpina | 0.36 | 86 | 44 |

#### cluster (4) — top co-lemma: **uppanna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppanna | 0.32 | 49 | 34 |

#### cluster (5) — top co-lemma: **ṭhiti** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhiti | 0.32 | 47 | 33 |

### vipāka

_pi blocks: 156; sense clusters: 3; inflected forms: vipākaṃ, vipākesu, vipāko, vipākā_

#### cluster (1) — top co-lemma: **bhūmīsu** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmīsu | 0.62 | 79 | 73 |
| tīsu | 0.62 | 77 | 72 |
| kiriyābyākata | 0.60 | 73 | 69 |
| catūsu | 0.44 | 54 | 46 |

#### cluster (2) — top co-lemma: **kusala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusala | 0.55 | 324 | 131 |

#### cluster (3) — top co-lemma: **abyākata** (cohesion 0.86, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākata | 0.54 | 98 | 68 |
| pahāna | 0.43 | 92 | 53 |
| pattiya | 0.42 | 75 | 49 |
| bhūmiya | 0.42 | 75 | 49 |
| apacayagāmiṃ | 0.42 | 75 | 49 |

### kabaḷīkāra

_pi blocks: 145; sense clusters: 6; inflected forms: kabaḷīkāro_

#### cluster (1) — top co-lemma: **āhāra** (cohesion 0.97, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āhāra | 0.88 | 185 | 145 |
| taṃ | 0.52 | 396 | 141 |

#### cluster (2) — top co-lemma: **rūpāyatana** (cohesion 0.61, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāyatana | 0.49 | 116 | 64 |
| bāhira | 0.45 | 87 | 52 |

#### cluster (3) — top co-lemma: **ākāsadhātu** (cohesion 0.74, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākāsadhātu | 0.44 | 46 | 42 |
| panaññampi | 0.41 | 57 | 41 |
| āpodhātu | 0.33 | 57 | 33 |

#### cluster (4) — top co-lemma: **cakkhāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhāyatana | 0.36 | 129 | 50 |

#### cluster (5) — top co-lemma: **itthindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.36 | 48 | 35 |

#### cluster (6) — top co-lemma: **kāyaviññatti** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyaviññatti | 0.30 | 42 | 28 |

### ṭhapetva

_pi blocks: 137; sense clusters: 6; inflected forms: ṭhapetvā_

#### cluster (1) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.51 | 47 | 47 |

#### cluster (2) — top co-lemma: **viññāṇakkhandha** (cohesion 0.82, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇakkhandha | 0.46 | 209 | 80 |
| vedanākkhandha | 0.42 | 178 | 66 |

#### cluster (3) — top co-lemma: **rūpāvacara** (cohesion 0.76, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacara | 0.36 | 102 | 43 |
| kāmāvacara | 0.36 | 115 | 45 |

#### cluster (4) — top co-lemma: **saṅkhārakkhandha** (cohesion 0.85, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhārakkhandha | 0.34 | 95 | 40 |
| saññākkhandha | 0.34 | 97 | 40 |
| cittassekaggata | 0.29 | 74 | 31 |

#### cluster (5) — top co-lemma: **etthuppanna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| etthuppanna | 0.33 | 27 | 27 |

#### cluster (6) — top co-lemma: **akusala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusala | 0.31 | 123 | 40 |

### kāma

_pi blocks: 136; sense clusters: 2; inflected forms: kāmehi, kāmesu_

#### cluster (1) — top co-lemma: **vivicceva** (cohesion 0.90, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vivicceva | 0.99 | 132 | 132 |
| paṭhama | 0.87 | 169 | 132 |
| bhāveti | 0.80 | 195 | 132 |
| jhāna | 0.74 | 223 | 132 |
| yasmiṃ | 0.72 | 230 | 132 |
| avikkhepa | 0.66 | 264 | 132 |
| phassa | 0.61 | 297 | 132 |
| rūpūpapattiya | 0.61 | 102 | 72 |
| kusala | 0.57 | 324 | 132 |

#### cluster (2) — top co-lemma: **dandhābhiñña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dandhābhiñña | 0.57 | 77 | 61 |

### vivicceva

_pi blocks: 132; sense clusters: 2; inflected forms: vivicceva_

#### cluster (1) — top co-lemma: **kāma** (cohesion 0.89, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāma | 0.99 | 136 | 132 |
| paṭhama | 0.88 | 169 | 132 |
| bhāveti | 0.81 | 195 | 132 |
| jhāna | 0.74 | 223 | 132 |
| yasmiṃ | 0.73 | 230 | 132 |
| avikkhepa | 0.67 | 264 | 132 |
| rūpūpapattiya | 0.62 | 102 | 72 |
| phassa | 0.62 | 297 | 132 |

#### cluster (2) — top co-lemma: **dandhābhiñña** (cohesion 0.63, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dandhābhiñña | 0.58 | 77 | 61 |
| dukkhapaṭipada | 0.58 | 77 | 61 |

### tattha

_pi blocks: 132; sense clusters: 4; inflected forms: tattha_

#### cluster (1) — top co-lemma: **vuccati** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vuccati | 0.94 | 123 | 120 |
| ayaṃ | 0.37 | 304 | 80 |

#### cluster (2) — top co-lemma: **evarūpa** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evarūpa | 0.50 | 44 | 44 |
| vipariyāsaggāha | 0.31 | 27 | 25 |
| diṭṭhi | 0.30 | 33 | 25 |
| diṭṭhigata | 0.22 | 98 | 25 |

#### cluster (3) — top co-lemma: **pajānana** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pajānana | 0.19 | 38 | 16 |
| dhammavicaya | 0.19 | 38 | 16 |
| paññā | 0.19 | 40 | 16 |

#### cluster (4) — top co-lemma: **citta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| citta | 0.17 | 161 | 25 |

### cakkhāyatana

_pi blocks: 129; sense clusters: 6; inflected forms: cakkhāyatanaṃ_

#### cluster (1) — top co-lemma: **kāyāyatana** (cohesion 0.56, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyāyatana | 0.58 | 78 | 60 |
| ajjhattika | 0.52 | 61 | 49 |

#### cluster (2) — top co-lemma: **taṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| taṃ | 0.45 | 396 | 117 |

#### cluster (3) — top co-lemma: **kabaḷīkāra** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kabaḷīkāra | 0.36 | 145 | 50 |
| āhāra | 0.32 | 185 | 50 |

#### cluster (4) — top co-lemma: **rasāyatana** (cohesion 0.70, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasāyatana | 0.29 | 61 | 28 |
| gandhāyatana | 0.24 | 55 | 22 |
| rūpāyatana | 0.17 | 116 | 21 |

#### cluster (5) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.23 | 87 | 25 |

#### cluster (6) — top co-lemma: **upāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upāda | 0.16 | 93 | 18 |

### akusala

_pi blocks: 123; sense clusters: 4; inflected forms: akusalassa, akusalaṃ, akusalā, akusalānaṃ_

#### cluster (1) — top co-lemma: **bhūmīsu** (cohesion 0.73, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmīsu | 0.45 | 79 | 45 |
| tīsu | 0.44 | 77 | 44 |
| kiriyābyākata | 0.44 | 73 | 43 |
| vipāka | 0.35 | 156 | 49 |
| catūsu | 0.27 | 54 | 24 |

#### cluster (2) — top co-lemma: **pāpaka** (cohesion 0.87, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pāpaka | 0.32 | 23 | 23 |
| samāpattiya | 0.28 | 20 | 20 |

#### cluster (3) — top co-lemma: **ṭhapetva** (cohesion 0.57, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.31 | 137 | 40 |
| avasesa | 0.27 | 47 | 23 |

#### cluster (4) — top co-lemma: **vattabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattabba | 0.25 | 38 | 20 |

### vuccati

_pi blocks: 123; sense clusters: 4; inflected forms: vuccati_

#### cluster (1) — top co-lemma: **tattha** (cohesion 0.65, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tattha | 0.94 | 132 | 120 |
| ayaṃ | 0.39 | 304 | 83 |

#### cluster (2) — top co-lemma: **evarūpa** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evarūpa | 0.53 | 44 | 44 |
| vipariyāsaggāha | 0.33 | 27 | 25 |
| diṭṭhi | 0.32 | 33 | 25 |
| diṭṭhigata | 0.23 | 98 | 25 |

#### cluster (3) — top co-lemma: **pajānana** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pajānana | 0.20 | 38 | 16 |
| dhammavicaya | 0.20 | 38 | 16 |
| paññā | 0.20 | 40 | 16 |

#### cluster (4) — top co-lemma: **pubbanta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pubbanta | 0.18 | 12 | 12 |

### vedana

_pi blocks: 120; sense clusters: 3; inflected forms: vedanaṃ, vedanā, vedanāya_

#### cluster (1) — top co-lemma: **sañña** (cohesion 0.64, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañña | 0.68 | 80 | 68 |
| cetana | 0.51 | 98 | 56 |
| manindriya | 0.36 | 64 | 33 |
| aññepi | 0.35 | 83 | 36 |

#### cluster (2) — top co-lemma: **vedayita** (cohesion 0.72, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vedayita | 0.51 | 41 | 41 |
| cetosamphassaja | 0.45 | 35 | 35 |
| sāta | 0.45 | 35 | 35 |
| cetasika | 0.44 | 38 | 35 |
| yaṃ | 0.41 | 237 | 73 |

#### cluster (3) — top co-lemma: **sukha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukha | 0.43 | 64 | 40 |

### cattāra

_pi blocks: 116; sense clusters: 2; inflected forms: cattāro_

#### cluster (1) — top co-lemma: **cattāri** (cohesion 0.63, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cattāri | 0.43 | 38 | 33 |
| nibbānañca | 0.41 | 86 | 41 |
| sāmaññaphala | 0.39 | 28 | 28 |

#### cluster (2) — top co-lemma: **khandha** (cohesion 0.98, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| khandha | 0.42 | 38 | 32 |
| dvāyatana | 0.41 | 32 | 30 |
| ekaṃ | 0.40 | 34 | 30 |
| ekā | 0.40 | 35 | 30 |
| dhātuya | 0.40 | 35 | 30 |
| dhammadhātu | 0.39 | 37 | 30 |
| dhammāyatana | 0.39 | 39 | 30 |

### rūpāyatana

_pi blocks: 116; sense clusters: 2; inflected forms: rūpāyatanaṃ_

#### cluster (1) — top co-lemma: **bāhira** (cohesion 0.65, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bāhira | 0.53 | 87 | 54 |
| kabaḷīkāra | 0.49 | 145 | 64 |
| āhāra | 0.43 | 185 | 64 |
| taṃ | 0.40 | 396 | 102 |

#### cluster (2) — top co-lemma: **gandhāyatana** (cohesion 0.60, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.51 | 55 | 44 |
| rasāyatana | 0.50 | 61 | 44 |
| panaññampi | 0.44 | 57 | 38 |
| phoṭṭhabbāyatana | 0.42 | 87 | 43 |
| saddāyatana | 0.39 | 44 | 31 |
| kamma | 0.32 | 86 | 32 |

### kāmāvacara

_pi blocks: 115; sense clusters: 5; inflected forms: kāmāvacarassa, kāmāvacaraṃ, kāmāvacare, kāmāvacarā_

#### cluster (1) — top co-lemma: **rūpāvacara** (cohesion 0.69, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacara | 0.78 | 102 | 85 |
| arūpāvacara | 0.72 | 88 | 73 |
| viññāṇakkhandha | 0.48 | 209 | 78 |
| apariyāpanna | 0.47 | 110 | 53 |

#### cluster (2) — top co-lemma: **kusalākusalābyākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.53 | 41 | 41 |

#### cluster (3) — top co-lemma: **sāsava** (cohesion 0.79, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.42 | 39 | 32 |
| rūpakkhandha | 0.38 | 28 | 27 |

#### cluster (4) — top co-lemma: **ṭhapetva** (cohesion 0.58, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.36 | 137 | 45 |
| avasesa | 0.32 | 47 | 26 |

#### cluster (5) — top co-lemma: **sabbañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.33 | 79 | 32 |

### katatta

_pi blocks: 114; sense clusters: 4; inflected forms: katattā_

#### cluster (1) — top co-lemma: **kamma** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kamma | 0.81 | 86 | 81 |

#### cluster (2) — top co-lemma: **panaññampi** (cohesion 0.66, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panaññampi | 0.51 | 57 | 44 |
| ākāsadhātu | 0.40 | 46 | 32 |
| atthi | 0.39 | 160 | 53 |
| gandhāyatana | 0.38 | 55 | 32 |

#### cluster (3) — top co-lemma: **tasseva** (cohesion 0.76, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tasseva | 0.51 | 39 | 39 |
| abyākata | 0.45 | 98 | 48 |
| bhāvitatta | 0.45 | 33 | 33 |
| vipāka | 0.40 | 156 | 54 |

#### cluster (4) — top co-lemma: **āpodhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.37 | 57 | 32 |

### apariyāpanna

_pi blocks: 110; sense clusters: 4; inflected forms: apariyāpannaṃ, apariyāpanne, apariyāpannā_

#### cluster (1) — top co-lemma: **dhātu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.53 | 81 | 51 |
| asaṅkhata | 0.53 | 84 | 51 |

#### cluster (2) — top co-lemma: **rūpāvacara** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacara | 0.53 | 102 | 56 |
| kāmāvacara | 0.47 | 115 | 53 |
| arūpāvacara | 0.42 | 88 | 42 |

#### cluster (3) — top co-lemma: **sāmaññaphala** (cohesion 0.65, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāmaññaphala | 0.39 | 28 | 27 |
| magga | 0.37 | 196 | 57 |
| cattāri | 0.34 | 38 | 25 |
| cattāra | 0.32 | 116 | 36 |

#### cluster (4) — top co-lemma: **maggaphala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maggaphala | 0.33 | 22 | 22 |

### jīvitindriya

_pi blocks: 107; sense clusters: 1; inflected forms: jīvitindriyaṃ_

#### cluster (1) — top co-lemma: **aññepi** (cohesion 0.71, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.69 | 83 | 66 |
| arūpina | 0.68 | 86 | 66 |
| cittassekaggata | 0.67 | 74 | 61 |
| paṭiccasamuppanna | 0.66 | 94 | 66 |
| atthi | 0.64 | 160 | 86 |
| cetana | 0.60 | 98 | 62 |
| vīriyindriya | 0.54 | 61 | 45 |
| vicāra | 0.52 | 59 | 43 |
| paggāha | 0.52 | 44 | 39 |
| samādhindriya | 0.49 | 67 | 43 |

### rūpāvacara

_pi blocks: 102; sense clusters: 5; inflected forms: rūpāvacarassa, rūpāvacaraṃ, rūpāvacare, rūpāvacarā_

#### cluster (1) — top co-lemma: **arūpāvacara** (cohesion 0.82, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpāvacara | 0.80 | 88 | 76 |
| kāmāvacara | 0.78 | 115 | 85 |
| viññāṇakkhandha | 0.50 | 209 | 78 |

#### cluster (2) — top co-lemma: **kusalākusalābyākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.56 | 41 | 40 |

#### cluster (3) — top co-lemma: **apariyāpanna** (cohesion 0.61, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apariyāpanna | 0.53 | 110 | 56 |
| dhātu | 0.34 | 81 | 31 |
| vedanākkhandha | 0.34 | 178 | 47 |

#### cluster (4) — top co-lemma: **sāsava** (cohesion 0.81, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.45 | 39 | 32 |
| rūpakkhandha | 0.40 | 28 | 26 |

#### cluster (5) — top co-lemma: **ṭhapetva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.36 | 137 | 43 |

### rūpūpapattiya

_pi blocks: 102; sense clusters: 2; inflected forms: rūpūpapattiyā_

#### cluster (1) — top co-lemma: **bhāveti** (cohesion 0.85, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāveti | 0.69 | 195 | 102 |
| magga | 0.68 | 196 | 102 |
| paṭhama | 0.66 | 169 | 89 |
| jhāna | 0.63 | 223 | 102 |
| vivicceva | 0.62 | 132 | 72 |
| yasmiṃ | 0.61 | 230 | 102 |
| kāma | 0.61 | 136 | 72 |

#### cluster (2) — top co-lemma: **passati** (cohesion 0.97, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| passati | 0.61 | 48 | 46 |
| arūpasaññī | 0.61 | 45 | 45 |
| abhibhuyya | 0.60 | 44 | 44 |

### abyākata

_pi blocks: 98; sense clusters: 1; inflected forms: abyākataṃ, abyākatā_

#### cluster (1) — top co-lemma: **pahāna** (cohesion 0.79, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahāna | 0.60 | 92 | 57 |
| tasseva | 0.57 | 39 | 39 |
| pattiya | 0.57 | 75 | 49 |
| bhūmiya | 0.57 | 75 | 49 |
| apacayagāmiṃ | 0.57 | 75 | 49 |
| niyyānika | 0.56 | 78 | 49 |
| lokuttara | 0.54 | 85 | 49 |
| vipāka | 0.54 | 156 | 68 |
| bhāvitatta | 0.50 | 33 | 33 |
| diṭṭhigata | 0.49 | 98 | 48 |

### cetana

_pi blocks: 98; sense clusters: 2; inflected forms: cetanaṃ, cetanā, cetanāya_

#### cluster (1) — top co-lemma: **cittassekaggata** (cohesion 0.78, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittassekaggata | 0.71 | 74 | 61 |
| aññepi | 0.71 | 83 | 64 |
| arūpina | 0.70 | 86 | 64 |
| paṭiccasamuppanna | 0.67 | 94 | 64 |
| jīvitindriya | 0.60 | 107 | 62 |
| paggāha | 0.55 | 44 | 39 |
| vicāra | 0.55 | 59 | 43 |
| vīriyindriya | 0.54 | 61 | 43 |
| atthi | 0.53 | 160 | 69 |

#### cluster (2) — top co-lemma: **sañña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañña | 0.63 | 80 | 56 |

### diṭṭhigata

_pi blocks: 98; sense clusters: 3; inflected forms: diṭṭhigataṃ, diṭṭhigatānaṃ_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.91, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 0.82 | 75 | 71 |
| apacayagāmiṃ | 0.82 | 75 | 71 |
| pattiya | 0.82 | 75 | 71 |
| niyyānika | 0.81 | 78 | 71 |
| lokuttara | 0.78 | 85 | 71 |
| pahāna | 0.75 | 92 | 71 |
| paṭhama | 0.53 | 169 | 71 |
| dandhābhiñña | 0.51 | 77 | 45 |

#### cluster (2) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.54 | 36 | 36 |

#### cluster (3) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.53 | 37 | 36 |

### saññākkhandha

_pi blocks: 97; sense clusters: 2; inflected forms: saññākkhandhassa, saññākkhandhaṃ, saññākkhandho_

#### cluster (1) — top co-lemma: **saṅkhārakkhandha** (cohesion 0.93, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhārakkhandha | 0.98 | 95 | 94 |
| vedanākkhandha | 0.63 | 178 | 87 |

#### cluster (2) — top co-lemma: **aññepi** (cohesion 0.80, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.40 | 83 | 36 |
| arūpina | 0.39 | 86 | 36 |
| paṭiccasamuppanna | 0.38 | 94 | 36 |
| viññāṇakkhandha | 0.37 | 209 | 56 |
| cittassekaggata | 0.36 | 74 | 31 |
| cetana | 0.35 | 98 | 34 |
| ṭhapetva | 0.34 | 137 | 40 |
| jīvitindriya | 0.30 | 107 | 31 |

### saṅkhārakkhandha

_pi blocks: 95; sense clusters: 2; inflected forms: saṅkhārakkhandhassa, saṅkhārakkhandho_

#### cluster (1) — top co-lemma: **saññākkhandha** (cohesion 0.93, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saññākkhandha | 0.98 | 97 | 94 |
| vedanākkhandha | 0.64 | 178 | 87 |

#### cluster (2) — top co-lemma: **aññepi** (cohesion 0.80, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.40 | 83 | 36 |
| arūpina | 0.40 | 86 | 36 |
| paṭiccasamuppanna | 0.38 | 94 | 36 |
| viññāṇakkhandha | 0.37 | 209 | 56 |
| cittassekaggata | 0.37 | 74 | 31 |
| cetana | 0.35 | 98 | 34 |
| ṭhapetva | 0.34 | 137 | 40 |
| jīvitindriya | 0.31 | 107 | 31 |

### paṭiccasamuppanna

_pi blocks: 94; sense clusters: 1; inflected forms: paṭiccasamuppannesu, paṭiccasamuppannā_

#### cluster (1) — top co-lemma: **aññepi** (cohesion 0.68, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.94 | 83 | 83 |
| arūpina | 0.92 | 86 | 83 |
| cittassekaggata | 0.73 | 74 | 61 |
| cetana | 0.67 | 98 | 64 |
| jīvitindriya | 0.66 | 107 | 66 |
| atthi | 0.65 | 160 | 83 |
| paggāha | 0.57 | 44 | 39 |
| vicāra | 0.56 | 59 | 43 |
| samādhindriya | 0.56 | 67 | 45 |
| vīriyindriya | 0.55 | 61 | 43 |

### upāda

_pi blocks: 93; sense clusters: 2; inflected forms: upādā, upādānaṃ, upādāya_

#### cluster (1) — top co-lemma: **catunna** (cohesion 0.78, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| catunna | 0.69 | 49 | 49 |
| mahābhūta | 0.64 | 85 | 57 |
| pesa | 0.55 | 45 | 38 |
| peta | 0.54 | 40 | 36 |
| sappaṭigha | 0.53 | 59 | 40 |
| anidassana | 0.50 | 55 | 37 |

#### cluster (2) — top co-lemma: **suñña** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 0.50 | 31 | 31 |
| pasāda | 0.50 | 31 | 31 |
| gāma | 0.48 | 29 | 29 |
| tīra | 0.35 | 20 | 20 |

### pahāna

_pi blocks: 92; sense clusters: 1; inflected forms: pahānā, pahānāya_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.83, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 0.85 | 75 | 71 |
| apacayagāmiṃ | 0.85 | 75 | 71 |
| pattiya | 0.85 | 75 | 71 |
| niyyānika | 0.84 | 78 | 71 |
| lokuttara | 0.80 | 85 | 71 |
| diṭṭhigata | 0.75 | 98 | 71 |
| bhāveti | 0.63 | 195 | 91 |
| abyākata | 0.60 | 98 | 57 |
| jhāna | 0.58 | 223 | 91 |
| yasmiṃ | 0.57 | 230 | 91 |

### arūpāvacara

_pi blocks: 88; sense clusters: 4; inflected forms: arūpāvacarassa, arūpāvacaraṃ, arūpāvacare, arūpāvacarā_

#### cluster (1) — top co-lemma: **rūpāvacara** (cohesion 0.91, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacara | 0.80 | 102 | 76 |
| kāmāvacara | 0.72 | 115 | 73 |
| viññāṇakkhandha | 0.45 | 209 | 67 |

#### cluster (2) — top co-lemma: **kusalākusalābyākata** (cohesion 0.62, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.60 | 41 | 39 |
| avasesa | 0.36 | 47 | 24 |

#### cluster (3) — top co-lemma: **sāsava** (cohesion 0.81, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.50 | 39 | 32 |
| rūpakkhandha | 0.45 | 28 | 26 |

#### cluster (4) — top co-lemma: **apariyāpanna** (cohesion 0.78, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apariyāpanna | 0.42 | 110 | 42 |
| dhātu | 0.36 | 81 | 30 |
| asaṅkhata | 0.35 | 84 | 30 |

### bāhira

_pi blocks: 87; sense clusters: 7; inflected forms: bāhiraṃ, bāhirā_

#### cluster (1) — top co-lemma: **rūpāyatana** (cohesion 0.71, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāyatana | 0.53 | 116 | 54 |
| kabaḷīkāra | 0.45 | 145 | 52 |
| āhāra | 0.38 | 185 | 52 |
| taṃ | 0.35 | 396 | 84 |

#### cluster (2) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.20 | 87 | 17 |

#### cluster (3) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.16 | 24 | 9 |

#### cluster (4) — top co-lemma: **āpodhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.15 | 57 | 11 |

#### cluster (5) — top co-lemma: **saddāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saddāyatana | 0.15 | 44 | 10 |

#### cluster (6) — top co-lemma: **itthindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.15 | 48 | 10 |

#### cluster (7) — top co-lemma: **vacīviññatti** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vacīviññatti | 0.14 | 41 | 9 |

### phoṭṭhabbāyatana

_pi blocks: 87; sense clusters: 4; inflected forms: phoṭṭhabbāyatanaṃ_

#### cluster (1) — top co-lemma: **gandhāyatana** (cohesion 0.72, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.59 | 55 | 42 |
| rasāyatana | 0.57 | 61 | 42 |
| saddāyatana | 0.46 | 44 | 30 |
| rūpāyatana | 0.42 | 116 | 43 |

#### cluster (2) — top co-lemma: **āpodhātu** (cohesion 0.61, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.43 | 57 | 31 |
| ākāsadhātu | 0.29 | 46 | 19 |

#### cluster (3) — top co-lemma: **panaññampi** (cohesion 0.75, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panaññampi | 0.42 | 57 | 30 |
| kamma | 0.37 | 86 | 32 |
| katatta | 0.32 | 114 | 32 |

#### cluster (4) — top co-lemma: **taṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| taṃ | 0.30 | 396 | 73 |

### arūpina

_pi blocks: 86; sense clusters: 1; inflected forms: arūpino_

#### cluster (1) — top co-lemma: **aññepi** (cohesion 0.68, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.98 | 83 | 83 |
| paṭiccasamuppanna | 0.92 | 94 | 83 |
| cittassekaggata | 0.76 | 74 | 61 |
| cetana | 0.70 | 98 | 64 |
| jīvitindriya | 0.68 | 107 | 66 |
| atthi | 0.67 | 160 | 83 |
| paggāha | 0.60 | 44 | 39 |
| vicāra | 0.59 | 59 | 43 |
| samādhindriya | 0.59 | 67 | 45 |
| vīriyindriya | 0.59 | 61 | 43 |

### kamma

_pi blocks: 86; sense clusters: 4; inflected forms: kammassa, kammānaṃ, kammāni_

#### cluster (1) — top co-lemma: **katatta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| katatta | 0.81 | 114 | 81 |

#### cluster (2) — top co-lemma: **panaññampi** (cohesion 0.66, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panaññampi | 0.62 | 57 | 44 |
| ākāsadhātu | 0.48 | 46 | 32 |
| gandhāyatana | 0.45 | 55 | 32 |
| rasāyatana | 0.44 | 61 | 32 |
| atthi | 0.43 | 160 | 53 |
| rūpāyatana | 0.32 | 116 | 32 |
| yaṃ | 0.31 | 237 | 50 |

#### cluster (3) — top co-lemma: **āpodhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.45 | 57 | 32 |

#### cluster (4) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.37 | 87 | 32 |

### nibbānañca

_pi blocks: 86; sense clusters: 3; inflected forms: nibbānañca_

#### cluster (1) — top co-lemma: **rūpañca** (cohesion 0.78, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpañca | 0.77 | 55 | 54 |
| catūsu | 0.47 | 54 | 33 |
| kiriyābyākata | 0.45 | 73 | 36 |
| tīsu | 0.44 | 77 | 36 |
| bhūmīsu | 0.44 | 79 | 36 |
| vipāka | 0.31 | 156 | 38 |

#### cluster (2) — top co-lemma: **sāmaññaphala** (cohesion 0.76, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāmaññaphala | 0.46 | 28 | 26 |
| cattāri | 0.42 | 38 | 26 |
| cattāra | 0.41 | 116 | 41 |

#### cluster (3) — top co-lemma: **vattabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattabba | 0.29 | 38 | 18 |

### lokuttara

_pi blocks: 85; sense clusters: 2; inflected forms: lokuttarassa, lokuttaraṃ, lokuttarā_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.84, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 0.94 | 75 | 75 |
| apacayagāmiṃ | 0.94 | 75 | 75 |
| pattiya | 0.94 | 75 | 75 |
| niyyānika | 0.92 | 78 | 75 |
| pahāna | 0.80 | 92 | 71 |
| diṭṭhigata | 0.78 | 98 | 71 |
| paṭhama | 0.61 | 169 | 77 |
| dandhābhiñña | 0.60 | 77 | 49 |
| dukkhapaṭipada | 0.60 | 77 | 49 |

#### cluster (2) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.61 | 37 | 37 |

### mahābhūta

_pi blocks: 85; sense clusters: 2; inflected forms: mahābhūtaṃ, mahābhūtehi, mahābhūtā, mahābhūtānaṃ_

#### cluster (1) — top co-lemma: **catunna** (cohesion 0.78, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| catunna | 0.73 | 49 | 49 |
| upāda | 0.64 | 93 | 57 |
| pesa | 0.58 | 45 | 38 |
| peta | 0.58 | 40 | 36 |
| sappaṭigha | 0.56 | 59 | 40 |
| anidassana | 0.53 | 55 | 37 |

#### cluster (2) — top co-lemma: **suñña** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 0.53 | 31 | 31 |
| pasāda | 0.53 | 31 | 31 |
| gāma | 0.51 | 29 | 29 |
| tīra | 0.38 | 20 | 20 |

### asaṅkhata

_pi blocks: 84; sense clusters: 4; inflected forms: asaṅkhato, asaṅkhatā_

#### cluster (1) — top co-lemma: **dhātu** (cohesion 0.63, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.98 | 81 | 81 |
| apariyāpanna | 0.53 | 110 | 51 |

#### cluster (2) — top co-lemma: **sabbañca** (cohesion 0.73, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.60 | 79 | 49 |
| vedanākkhandha | 0.37 | 178 | 48 |
| arūpāvacara | 0.35 | 88 | 30 |
| rūpāvacara | 0.33 | 102 | 31 |
| viññāṇakkhandha | 0.32 | 209 | 47 |
| kāmāvacara | 0.31 | 115 | 31 |

#### cluster (3) — top co-lemma: **maggaphala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maggaphala | 0.42 | 22 | 22 |

#### cluster (4) — top co-lemma: **kusalākusalābyākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.27 | 41 | 17 |

### aññepi

_pi blocks: 83; sense clusters: 1; inflected forms: aññepi_

#### cluster (1) — top co-lemma: **arūpina** (cohesion 0.68, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpina | 0.98 | 86 | 83 |
| paṭiccasamuppanna | 0.94 | 94 | 83 |
| cittassekaggata | 0.78 | 74 | 61 |
| cetana | 0.71 | 98 | 64 |
| jīvitindriya | 0.69 | 107 | 66 |
| atthi | 0.68 | 160 | 83 |
| paggāha | 0.61 | 44 | 39 |
| vicāra | 0.61 | 59 | 43 |
| samādhindriya | 0.60 | 67 | 45 |
| vīriyindriya | 0.60 | 61 | 43 |

### dhātu

_pi blocks: 81; sense clusters: 4; inflected forms: dhātu_

#### cluster (1) — top co-lemma: **asaṅkhata** (cohesion 0.63, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṅkhata | 0.98 | 84 | 81 |
| apariyāpanna | 0.53 | 110 | 51 |

#### cluster (2) — top co-lemma: **sabbañca** (cohesion 0.73, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.61 | 79 | 49 |
| vedanākkhandha | 0.37 | 178 | 48 |
| arūpāvacara | 0.36 | 88 | 30 |
| rūpāvacara | 0.34 | 102 | 31 |
| viññāṇakkhandha | 0.32 | 209 | 47 |
| kāmāvacara | 0.32 | 115 | 31 |

#### cluster (3) — top co-lemma: **maggaphala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maggaphala | 0.43 | 22 | 22 |

#### cluster (4) — top co-lemma: **kusalākusalābyākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.28 | 41 | 17 |

### sañña

_pi blocks: 80; sense clusters: 3; inflected forms: saññaṃ, saññā, saññāya_

#### cluster (1) — top co-lemma: **vedana** (cohesion 0.82, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vedana | 0.68 | 120 | 68 |
| cetana | 0.63 | 98 | 56 |

#### cluster (2) — top co-lemma: **manindriya** (cohesion 0.80, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manindriya | 0.46 | 64 | 33 |
| aññepi | 0.40 | 83 | 33 |
| rūpārammaṇa | 0.40 | 34 | 23 |
| arūpina | 0.40 | 86 | 33 |
| cittassekaggata | 0.39 | 74 | 30 |
| paṭiccasamuppanna | 0.38 | 94 | 33 |
| uppanna | 0.37 | 49 | 24 |

#### cluster (3) — top co-lemma: **khandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| khandha | 0.37 | 38 | 22 |

### bhūmīsu

_pi blocks: 79; sense clusters: 4; inflected forms: bhūmīsu_

#### cluster (1) — top co-lemma: **tīsu** (cohesion 0.78, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīsu | 0.97 | 77 | 76 |
| kiriyābyākata | 0.95 | 73 | 72 |
| vipāka | 0.62 | 156 | 73 |
| akusala | 0.45 | 123 | 45 |
| kusala | 0.36 | 324 | 72 |

#### cluster (2) — top co-lemma: **catūsu** (cohesion 0.68, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| catūsu | 0.72 | 54 | 48 |
| rūpañca | 0.45 | 55 | 30 |
| nibbānañca | 0.44 | 86 | 36 |

#### cluster (3) — top co-lemma: **sabbañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.35 | 79 | 28 |

#### cluster (4) — top co-lemma: **uddhaccasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.34 | 27 | 18 |

### sabbañca

_pi blocks: 79; sense clusters: 3; inflected forms: sabbañca_

#### cluster (1) — top co-lemma: **dhātu** (cohesion 0.75, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.61 | 81 | 49 |
| asaṅkhata | 0.60 | 84 | 49 |
| arūpāvacara | 0.35 | 88 | 29 |
| rūpāvacara | 0.33 | 102 | 30 |
| kāmāvacara | 0.33 | 115 | 32 |
| vedanākkhandha | 0.32 | 178 | 41 |

#### cluster (2) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.38 | 47 | 24 |

#### cluster (3) — top co-lemma: **kiriyābyākata** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kiriyābyākata | 0.37 | 73 | 28 |
| tīsu | 0.36 | 77 | 28 |
| bhūmīsu | 0.35 | 79 | 28 |

### kāyāyatana

_pi blocks: 78; sense clusters: 3; inflected forms: kāyāyatanaṃ_

#### cluster (1) — top co-lemma: **ajjhattika** (cohesion 0.64, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ajjhattika | 0.68 | 61 | 47 |
| cakkhāyatana | 0.58 | 129 | 60 |
| taṃ | 0.32 | 396 | 75 |

#### cluster (2) — top co-lemma: **gandhāyatana** (cohesion 0.73, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.35 | 55 | 23 |
| rasāyatana | 0.33 | 61 | 23 |
| panaññampi | 0.22 | 57 | 15 |
| phoṭṭhabbāyatana | 0.22 | 87 | 18 |

#### cluster (3) — top co-lemma: **sotāyatana** (cohesion 0.73, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotāyatana | 0.29 | 24 | 15 |
| jivhāyatana | 0.23 | 19 | 11 |
| ghānāyatana | 0.22 | 14 | 10 |

### niyyānika

_pi blocks: 78; sense clusters: 3; inflected forms: niyyānikaṃ, niyyānikā_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.82, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 0.98 | 75 | 75 |
| apacayagāmiṃ | 0.98 | 75 | 75 |
| pattiya | 0.98 | 75 | 75 |
| lokuttara | 0.92 | 85 | 75 |
| pahāna | 0.84 | 92 | 71 |
| diṭṭhigata | 0.81 | 98 | 71 |
| dandhābhiñña | 0.63 | 77 | 49 |
| dukkhapaṭipada | 0.63 | 77 | 49 |

#### cluster (2) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.64 | 37 | 37 |

#### cluster (3) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.63 | 36 | 36 |

### dukkhapaṭipada

_pi blocks: 77; sense clusters: 1; inflected forms: dukkhapaṭipadaṃ_

#### cluster (1) — top co-lemma: **dandhābhiñña** (cohesion 0.74, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dandhābhiñña | 0.82 | 77 | 63 |
| pattiya | 0.64 | 75 | 49 |
| bhūmiya | 0.64 | 75 | 49 |
| apacayagāmiṃ | 0.64 | 75 | 49 |
| niyyānika | 0.63 | 78 | 49 |
| paṭhama | 0.63 | 169 | 77 |
| lokuttara | 0.60 | 85 | 49 |
| vivicceva | 0.58 | 132 | 61 |
| kāma | 0.57 | 136 | 61 |
| bhāveti | 0.57 | 195 | 77 |

### dandhābhiñña

_pi blocks: 77; sense clusters: 1; inflected forms: dandhābhiññaṃ_

#### cluster (1) — top co-lemma: **dukkhapaṭipada** (cohesion 0.74, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkhapaṭipada | 0.82 | 77 | 63 |
| pattiya | 0.64 | 75 | 49 |
| bhūmiya | 0.64 | 75 | 49 |
| apacayagāmiṃ | 0.64 | 75 | 49 |
| niyyānika | 0.63 | 78 | 49 |
| paṭhama | 0.63 | 169 | 77 |
| lokuttara | 0.60 | 85 | 49 |
| vivicceva | 0.58 | 132 | 61 |
| kāma | 0.57 | 136 | 61 |
| bhāveti | 0.57 | 195 | 77 |

### tīsu

_pi blocks: 77; sense clusters: 4; inflected forms: tīsu_

#### cluster (1) — top co-lemma: **bhūmīsu** (cohesion 0.79, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmīsu | 0.97 | 79 | 76 |
| kiriyābyākata | 0.96 | 73 | 72 |
| vipāka | 0.62 | 156 | 72 |
| akusala | 0.44 | 123 | 44 |
| kusala | 0.35 | 324 | 70 |

#### cluster (2) — top co-lemma: **catūsu** (cohesion 0.71, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| catūsu | 0.69 | 54 | 45 |
| rūpañca | 0.45 | 55 | 30 |
| nibbānañca | 0.44 | 86 | 36 |

#### cluster (3) — top co-lemma: **sabbañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.36 | 79 | 28 |

#### cluster (4) — top co-lemma: **uddhaccasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.35 | 27 | 18 |

### bhūmiya

_pi blocks: 75; sense clusters: 3; inflected forms: bhūmiyā_

#### cluster (1) — top co-lemma: **apacayagāmiṃ** (cohesion 0.82, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apacayagāmiṃ | 1.00 | 75 | 75 |
| pattiya | 1.00 | 75 | 75 |
| niyyānika | 0.98 | 78 | 75 |
| lokuttara | 0.94 | 85 | 75 |
| pahāna | 0.85 | 92 | 71 |
| diṭṭhigata | 0.82 | 98 | 71 |
| dandhābhiñña | 0.64 | 77 | 49 |
| dukkhapaṭipada | 0.64 | 77 | 49 |

#### cluster (2) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.66 | 37 | 37 |

#### cluster (3) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.65 | 36 | 36 |

### pattiya

_pi blocks: 75; sense clusters: 3; inflected forms: pattiyā_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.82, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 1.00 | 75 | 75 |
| apacayagāmiṃ | 1.00 | 75 | 75 |
| niyyānika | 0.98 | 78 | 75 |
| lokuttara | 0.94 | 85 | 75 |
| pahāna | 0.85 | 92 | 71 |
| diṭṭhigata | 0.82 | 98 | 71 |
| dandhābhiñña | 0.64 | 77 | 49 |
| dukkhapaṭipada | 0.64 | 77 | 49 |

#### cluster (2) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.66 | 37 | 37 |

#### cluster (3) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.65 | 36 | 36 |

### apacayagāmiṃ

_pi blocks: 75; sense clusters: 3; inflected forms: apacayagāmiṃ_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.82, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 1.00 | 75 | 75 |
| pattiya | 1.00 | 75 | 75 |
| niyyānika | 0.98 | 78 | 75 |
| lokuttara | 0.94 | 85 | 75 |
| pahāna | 0.85 | 92 | 71 |
| diṭṭhigata | 0.82 | 98 | 71 |
| dandhābhiñña | 0.64 | 77 | 49 |
| dukkhapaṭipada | 0.64 | 77 | 49 |

#### cluster (2) — top co-lemma: **suññata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññata | 0.66 | 37 | 37 |

#### cluster (3) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.65 | 36 | 36 |

### cittassekaggata

_pi blocks: 74; sense clusters: 1; inflected forms: cittassekaggatā_

#### cluster (1) — top co-lemma: **aññepi** (cohesion 0.73, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.78 | 83 | 61 |
| arūpina | 0.76 | 86 | 61 |
| paṭiccasamuppanna | 0.73 | 94 | 61 |
| cetana | 0.71 | 98 | 61 |
| vicāra | 0.68 | 59 | 45 |
| jīvitindriya | 0.67 | 107 | 61 |
| paggāha | 0.66 | 44 | 39 |
| samādhindriya | 0.65 | 67 | 46 |
| vitakka | 0.65 | 59 | 43 |
| vīriyindriya | 0.64 | 61 | 43 |

### kiriyābyākata

_pi blocks: 73; sense clusters: 4; inflected forms: kiriyābyākataṃ, kiriyābyākatesu_

#### cluster (1) — top co-lemma: **tīsu** (cohesion 0.81, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīsu | 0.96 | 77 | 72 |
| bhūmīsu | 0.95 | 79 | 72 |
| vipāka | 0.60 | 156 | 69 |
| akusala | 0.44 | 123 | 43 |
| kusala | 0.35 | 324 | 70 |

#### cluster (2) — top co-lemma: **catūsu** (cohesion 0.71, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| catūsu | 0.69 | 54 | 44 |
| rūpañca | 0.47 | 55 | 30 |
| nibbānañca | 0.45 | 86 | 36 |

#### cluster (3) — top co-lemma: **sabbañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.37 | 79 | 28 |

#### cluster (4) — top co-lemma: **uddhaccasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.36 | 27 | 18 |

### catuttha

_pi blocks: 72; sense clusters: 1; inflected forms: catutthassa, catutthaṃ, catuttho, catutthāya_

#### cluster (1) — top co-lemma: **tatiya** (cohesion 0.67, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tatiya | 0.69 | 47 | 41 |
| pañcama | 0.68 | 40 | 38 |
| dutiya | 0.67 | 51 | 41 |
| vūpasama | 0.62 | 38 | 34 |
| vitakkavicāra | 0.61 | 40 | 34 |
| pahāna | 0.50 | 92 | 41 |
| jhāna | 0.47 | 223 | 70 |
| bhāveti | 0.46 | 195 | 62 |
| yasmiṃ | 0.42 | 230 | 63 |
| avikkhepa | 0.38 | 264 | 64 |

### samādhindriya

_pi blocks: 67; sense clusters: 2; inflected forms: samādhindriyaṃ_

#### cluster (1) — top co-lemma: **samādhibala** (cohesion 0.72, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhibala | 0.81 | 49 | 47 |
| samatha | 0.78 | 53 | 47 |
| sammāsamādhi | 0.55 | 32 | 27 |

#### cluster (2) — top co-lemma: **vīriyindriya** (cohesion 0.78, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyindriya | 0.67 | 61 | 43 |
| paggāha | 0.67 | 44 | 37 |
| cittassekaggata | 0.65 | 74 | 46 |
| aññepi | 0.60 | 83 | 45 |
| arūpina | 0.59 | 86 | 45 |
| paṭiccasamuppanna | 0.56 | 94 | 45 |
| saddhindriya | 0.54 | 33 | 27 |

### sukha

_pi blocks: 64; sense clusters: 4; inflected forms: sukhassa, sukhaṃ, sukhā, sukhāya_

#### cluster (1) — top co-lemma: **vedana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vedana | 0.43 | 120 | 40 |

#### cluster (2) — top co-lemma: **somanassindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.41 | 19 | 17 |

#### cluster (3) — top co-lemma: **sāta** (cohesion 0.90, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāta | 0.40 | 35 | 20 |
| vedayita | 0.38 | 41 | 20 |
| cetosamphassaja | 0.34 | 35 | 17 |
| cetasika | 0.33 | 38 | 17 |

#### cluster (4) — top co-lemma: **sabbasa** (cohesion 0.65, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbasa | 0.40 | 16 | 16 |
| catuttha | 0.32 | 72 | 22 |
| samatikkamma | 0.32 | 12 | 12 |
| arūpūpapattiya | 0.32 | 12 | 12 |

### manindriya

_pi blocks: 64; sense clusters: 2; inflected forms: manindriyaṃ_

#### cluster (1) — top co-lemma: **manāyatana** (cohesion 0.89, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manāyatana | 0.59 | 35 | 29 |
| hadaya | 0.58 | 26 | 26 |
| mānasa | 0.58 | 26 | 26 |
| viññāṇa | 0.50 | 41 | 26 |
| tajjāmanoviññāṇadhātu | 0.48 | 20 | 20 |
| paṇḍara | 0.47 | 46 | 26 |

#### cluster (2) — top co-lemma: **citta** (cohesion 0.78, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| citta | 0.52 | 161 | 59 |
| sañña | 0.46 | 80 | 33 |
| aññepi | 0.45 | 83 | 33 |
| arūpina | 0.44 | 86 | 33 |

### sammādiṭṭhi

_pi blocks: 62; sense clusters: 1; inflected forms: sammādiṭṭhi_

#### cluster (1) — top co-lemma: **paññindriya** (cohesion 0.67, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññindriya | 0.80 | 45 | 43 |
| pajānana | 0.76 | 38 | 38 |
| dhammavicaya | 0.76 | 38 | 38 |
| paññā | 0.75 | 40 | 38 |
| sampajañña | 0.65 | 30 | 30 |
| vipassana | 0.65 | 31 | 30 |
| paññābala | 0.62 | 31 | 29 |
| paññāpajjota | 0.52 | 22 | 22 |
| cinta | 0.52 | 22 | 22 |
| paṇḍicca | 0.52 | 22 | 22 |

### ajjhattika

_pi blocks: 61; sense clusters: 8; inflected forms: ajjhattikaṃ, ajjhattikā_

#### cluster (1) — top co-lemma: **kāyāyatana** (cohesion 0.76, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyāyatana | 0.68 | 78 | 47 |
| cakkhāyatana | 0.52 | 129 | 49 |
| taṃ | 0.25 | 396 | 58 |

#### cluster (2) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.22 | 21 | 9 |

#### cluster (3) — top co-lemma: **jivhāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhāyatana | 0.15 | 19 | 6 |

#### cluster (4) — top co-lemma: **sotāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotāyatana | 0.14 | 24 | 6 |

#### cluster (5) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.12 | 24 | 5 |

#### cluster (6) — top co-lemma: **kāyasamphassa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassa | 0.11 | 13 | 4 |

#### cluster (7) — top co-lemma: **cakkhusamphassa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassa | 0.11 | 13 | 4 |

#### cluster (8) — top co-lemma: **cakkhuviññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhuviññāṇa | 0.10 | 17 | 4 |

### rasāyatana

_pi blocks: 61; sense clusters: 2; inflected forms: rasāyatanaṃ_

#### cluster (1) — top co-lemma: **gandhāyatana** (cohesion 0.65, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.88 | 55 | 51 |
| saddāyatana | 0.67 | 44 | 35 |
| panaññampi | 0.64 | 57 | 38 |
| phoṭṭhabbāyatana | 0.57 | 87 | 42 |
| rūpāyatana | 0.50 | 116 | 44 |
| kamma | 0.44 | 86 | 32 |
| atthi | 0.39 | 160 | 43 |

#### cluster (2) — top co-lemma: **ākāsadhātu** (cohesion 0.76, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākāsadhātu | 0.52 | 46 | 28 |
| kammaññata | 0.38 | 34 | 18 |
| lahuta | 0.38 | 34 | 18 |

### vīriyindriya

_pi blocks: 61; sense clusters: 2; inflected forms: vīriyindriyaṃ_

#### cluster (1) — top co-lemma: **paggāha** (cohesion 0.76, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paggāha | 0.80 | 44 | 42 |
| sammāvāyāma | 0.71 | 41 | 36 |
| samādhindriya | 0.67 | 67 | 43 |
| cittassekaggata | 0.64 | 74 | 43 |
| aññepi | 0.60 | 83 | 43 |
| arūpina | 0.59 | 86 | 43 |
| saddhindriya | 0.57 | 33 | 27 |
| paṭiccasamuppanna | 0.55 | 94 | 43 |
| cetana | 0.54 | 98 | 43 |

#### cluster (2) — top co-lemma: **vīriyabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyabala | 0.79 | 43 | 41 |

### sappaṭigha

_pi blocks: 59; sense clusters: 1; inflected forms: sappaṭighamhi, sappaṭighaṃ, sappaṭighena, sappaṭigho, sappaṭighā, sappaṭighāya_

#### cluster (1) — top co-lemma: **peta** (cohesion 0.70, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| peta | 0.79 | 40 | 39 |
| pesa | 0.75 | 45 | 39 |
| anidassana | 0.70 | 55 | 40 |
| catunna | 0.67 | 49 | 36 |
| mahābhūta | 0.56 | 85 | 40 |
| upāda | 0.53 | 93 | 40 |
| tīra | 0.51 | 20 | 20 |
| orima | 0.51 | 20 | 20 |
| samudda | 0.51 | 20 | 20 |
| dvāra | 0.51 | 20 | 20 |

### vicāra

_pi blocks: 59; sense clusters: 1; inflected forms: vicāraṃ, vicāro_

#### cluster (1) — top co-lemma: **vitakka** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vitakka | 0.75 | 59 | 44 |
| cittassekaggata | 0.68 | 74 | 45 |
| aññepi | 0.61 | 83 | 43 |
| arūpina | 0.59 | 86 | 43 |
| paṭiccasamuppanna | 0.56 | 94 | 43 |
| cetana | 0.55 | 98 | 43 |
| paggāha | 0.52 | 44 | 27 |
| jīvitindriya | 0.52 | 107 | 43 |
| vīriyindriya | 0.52 | 61 | 31 |
| vīriyabala | 0.49 | 43 | 25 |

### vitakka

_pi blocks: 59; sense clusters: 1; inflected forms: vitakkaṃ, vitakko_

#### cluster (1) — top co-lemma: **vicāra** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicāra | 0.75 | 59 | 44 |
| cittassekaggata | 0.65 | 74 | 43 |
| aññepi | 0.58 | 83 | 41 |
| arūpina | 0.57 | 86 | 41 |
| paṭiccasamuppanna | 0.54 | 94 | 41 |
| cetana | 0.52 | 98 | 41 |
| jīvitindriya | 0.49 | 107 | 41 |
| vīriyabala | 0.49 | 43 | 25 |
| paggāha | 0.49 | 44 | 25 |
| vīriyindriya | 0.48 | 61 | 29 |

### bahiddha

_pi blocks: 59; sense clusters: 1; inflected forms: bahiddhā_

#### cluster (1) — top co-lemma: **ajjhatta** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ajjhatta | 0.91 | 55 | 52 |
| arūpasaññī | 0.87 | 45 | 45 |
| abhibhuyya | 0.85 | 44 | 44 |
| jānāmi | 0.85 | 44 | 44 |
| passāmīti | 0.85 | 44 | 44 |
| tāni | 0.85 | 44 | 44 |
| passati | 0.84 | 48 | 45 |
| rūpūpapattiya | 0.56 | 102 | 45 |
| appamāṇa | 0.54 | 44 | 28 |
| paritta | 0.54 | 45 | 28 |

### āpodhātu

_pi blocks: 57; sense clusters: 3; inflected forms: āpodhātu_

#### cluster (1) — top co-lemma: **ākāsadhātu** (cohesion 0.74, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākāsadhātu | 0.60 | 46 | 31 |
| panaññampi | 0.53 | 57 | 30 |
| kamma | 0.45 | 86 | 32 |
| katatta | 0.37 | 114 | 32 |

#### cluster (2) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.43 | 87 | 31 |

#### cluster (3) — top co-lemma: **kammaññata** (cohesion 0.87, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammaññata | 0.42 | 34 | 19 |
| lahuta | 0.42 | 34 | 19 |
| muduta | 0.41 | 35 | 19 |
| jarata | 0.36 | 26 | 15 |
| aniccata | 0.35 | 28 | 15 |

### panaññampi

_pi blocks: 57; sense clusters: 2; inflected forms: panaññampi_

#### cluster (1) — top co-lemma: **ākāsadhātu** (cohesion 0.71, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākāsadhātu | 0.74 | 46 | 38 |
| āpodhātu | 0.53 | 57 | 30 |
| kammaññata | 0.48 | 34 | 22 |
| lahuta | 0.48 | 34 | 22 |
| muduta | 0.48 | 35 | 22 |

#### cluster (2) — top co-lemma: **gandhāyatana** (cohesion 0.74, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.68 | 55 | 38 |
| rasāyatana | 0.64 | 61 | 38 |
| kamma | 0.62 | 86 | 44 |
| atthi | 0.53 | 160 | 57 |
| katatta | 0.51 | 114 | 44 |

### anidassana

_pi blocks: 55; sense clusters: 1; inflected forms: anidassanamhi, anidassanaṃ, anidassanena, anidassano, anidassanā, anidassanāya_

#### cluster (1) — top co-lemma: **peta** (cohesion 0.74, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| peta | 0.80 | 40 | 38 |
| pesa | 0.76 | 45 | 38 |
| sappaṭigha | 0.70 | 59 | 40 |
| catunna | 0.67 | 49 | 35 |
| khetta | 0.53 | 20 | 20 |
| attabhāvapariyāpanna | 0.53 | 20 | 20 |
| tīra | 0.53 | 20 | 20 |
| orima | 0.53 | 20 | 20 |
| samudda | 0.53 | 20 | 20 |
| dvāra | 0.53 | 20 | 20 |

### gandhāyatana

_pi blocks: 55; sense clusters: 2; inflected forms: gandhāyatanaṃ_

#### cluster (1) — top co-lemma: **rasāyatana** (cohesion 0.65, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasāyatana | 0.88 | 61 | 51 |
| saddāyatana | 0.71 | 44 | 35 |
| panaññampi | 0.68 | 57 | 38 |
| phoṭṭhabbāyatana | 0.59 | 87 | 42 |
| rūpāyatana | 0.51 | 116 | 44 |
| kamma | 0.45 | 86 | 32 |
| atthi | 0.40 | 160 | 43 |

#### cluster (2) — top co-lemma: **ākāsadhātu** (cohesion 0.76, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākāsadhātu | 0.55 | 46 | 28 |
| kammaññata | 0.40 | 34 | 18 |
| lahuta | 0.40 | 34 | 18 |

### ajjhatta

_pi blocks: 55; sense clusters: 1; inflected forms: ajjhattaṃ, ajjhatte, ajjhattā_

#### cluster (1) — top co-lemma: **bahiddha** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bahiddha | 0.91 | 59 | 52 |
| arūpasaññī | 0.90 | 45 | 45 |
| abhibhuyya | 0.89 | 44 | 44 |
| jānāmi | 0.89 | 44 | 44 |
| passāmīti | 0.89 | 44 | 44 |
| tāni | 0.89 | 44 | 44 |
| passati | 0.87 | 48 | 45 |
| rūpūpapattiya | 0.59 | 102 | 46 |
| appamāṇa | 0.57 | 44 | 28 |
| paritta | 0.56 | 45 | 28 |

### rūpañca

_pi blocks: 55; sense clusters: 3; inflected forms: rūpañca_

#### cluster (1) — top co-lemma: **nibbānañca** (cohesion 0.80, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nibbānañca | 0.77 | 86 | 54 |
| catūsu | 0.51 | 54 | 28 |
| kiriyābyākata | 0.47 | 73 | 30 |
| tīsu | 0.45 | 77 | 30 |
| bhūmīsu | 0.45 | 79 | 30 |
| vipāka | 0.31 | 156 | 33 |

#### cluster (2) — top co-lemma: **uddhaccasahagata** (cohesion 0.65, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.32 | 27 | 13 |
| vicikicchāsahagata | 0.30 | 26 | 12 |
| cittuppāda | 0.25 | 40 | 12 |

#### cluster (3) — top co-lemma: **vipākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipākata | 0.29 | 34 | 13 |

### catūsu

_pi blocks: 54; sense clusters: 3; inflected forms: catūsu_

#### cluster (1) — top co-lemma: **bhūmīsu** (cohesion 0.79, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmīsu | 0.72 | 79 | 48 |
| kiriyābyākata | 0.69 | 73 | 44 |
| tīsu | 0.69 | 77 | 45 |
| rūpañca | 0.51 | 55 | 28 |
| nibbānañca | 0.47 | 86 | 33 |
| vipāka | 0.44 | 156 | 46 |

#### cluster (2) — top co-lemma: **cittuppāda** (cohesion 0.61, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittuppāda | 0.51 | 40 | 24 |
| vicikicchāsahagata | 0.40 | 26 | 16 |
| uddhaccasahagata | 0.37 | 27 | 15 |

#### cluster (3) — top co-lemma: **akusala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusala | 0.27 | 123 | 24 |

### samatha

_pi blocks: 53; sense clusters: 4; inflected forms: samathaṃ, samatho_

#### cluster (1) — top co-lemma: **samādhibala** (cohesion 0.71, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhibala | 0.92 | 49 | 47 |
| samādhindriya | 0.78 | 67 | 47 |
| sammāsamādhi | 0.66 | 32 | 28 |

#### cluster (2) — top co-lemma: **avisāhaṭamānasata** (cohesion 0.98, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avisāhaṭamānasata | 0.62 | 24 | 24 |
| avaṭṭhiti | 0.62 | 24 | 24 |
| saṇṭhiti | 0.62 | 24 | 24 |
| avisāhāra | 0.62 | 24 | 24 |
| ṭhiti | 0.50 | 47 | 25 |

#### cluster (3) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.51 | 18 | 18 |

#### cluster (4) — top co-lemma: **vīriyabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyabala | 0.48 | 43 | 23 |

### dutiya

_pi blocks: 51; sense clusters: 2; inflected forms: dutiyaṃ, dutiyā, dutiyāya_

#### cluster (1) — top co-lemma: **tatiya** (cohesion 0.86, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tatiya | 0.84 | 47 | 41 |
| pañcama | 0.84 | 40 | 38 |
| vūpasama | 0.81 | 38 | 36 |
| vitakkavicāra | 0.79 | 40 | 36 |
| catuttha | 0.67 | 72 | 41 |
| paṭhama | 0.38 | 169 | 42 |

#### cluster (2) — top co-lemma: **pattiya** (cohesion 0.80, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pattiya | 0.38 | 75 | 24 |
| bhūmiya | 0.38 | 75 | 24 |
| apacayagāmiṃ | 0.38 | 75 | 24 |
| dandhābhiñña | 0.38 | 77 | 24 |

### catunna

_pi blocks: 49; sense clusters: 2; inflected forms: catunnaṃ_

#### cluster (1) — top co-lemma: **peta** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| peta | 0.81 | 40 | 36 |
| pesa | 0.81 | 45 | 38 |
| mahābhūta | 0.73 | 85 | 49 |
| upāda | 0.69 | 93 | 49 |
| anidassana | 0.67 | 55 | 35 |
| sappaṭigha | 0.67 | 59 | 36 |

#### cluster (2) — top co-lemma: **suñña** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 0.78 | 31 | 31 |
| pasāda | 0.78 | 31 | 31 |
| gāma | 0.74 | 29 | 29 |
| tīra | 0.58 | 20 | 20 |

### uppanna

_pi blocks: 49; sense clusters: 5; inflected forms: uppannaṃ, uppanno, uppannā, uppannānaṃ_

#### cluster (1) — top co-lemma: **rūpārammaṇa** (cohesion 0.87, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpārammaṇa | 0.77 | 34 | 32 |
| panārabbha | 0.76 | 30 | 30 |
| dhammārammaṇa | 0.69 | 26 | 26 |

#### cluster (2) — top co-lemma: **upekkhāsahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagata | 0.51 | 41 | 23 |

#### cluster (3) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 0.73, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.45 | 17 | 15 |
| manindriya | 0.39 | 64 | 22 |
| rasārammaṇa | 0.38 | 14 | 12 |
| gandhārammaṇa | 0.38 | 14 | 12 |

#### cluster (4) — top co-lemma: **somanassasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagata | 0.42 | 18 | 14 |

#### cluster (5) — top co-lemma: **sasaṅkhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.39 | 12 | 12 |

### samādhibala

_pi blocks: 49; sense clusters: 4; inflected forms: samādhibalaṃ_

#### cluster (1) — top co-lemma: **samatha** (cohesion 0.72, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samatha | 0.92 | 53 | 47 |
| samādhindriya | 0.81 | 67 | 47 |
| sammāsamādhi | 0.67 | 32 | 27 |

#### cluster (2) — top co-lemma: **saṇṭhiti** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṇṭhiti | 0.66 | 24 | 24 |
| avisāhāra | 0.66 | 24 | 24 |
| avisāhaṭamānasata | 0.66 | 24 | 24 |
| avaṭṭhiti | 0.66 | 24 | 24 |
| ṭhiti | 0.50 | 47 | 24 |

#### cluster (3) — top co-lemma: **vīriyabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyabala | 0.54 | 43 | 25 |

#### cluster (4) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.54 | 18 | 18 |

### itthindriya

_pi blocks: 48; sense clusters: 4; inflected forms: itthindriyaṃ_

#### cluster (1) — top co-lemma: **purisindriya** (cohesion 0.65, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| purisindriya | 0.70 | 35 | 29 |
| ākāsadhātu | 0.43 | 46 | 20 |
| jīvitindriya | 0.37 | 107 | 29 |
| panaññampi | 0.34 | 57 | 18 |
| āpodhātu | 0.29 | 57 | 15 |
| gandhāyatana | 0.27 | 55 | 14 |

#### cluster (2) — top co-lemma: **kabaḷīkāra** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kabaḷīkāra | 0.36 | 145 | 35 |
| āhāra | 0.30 | 185 | 35 |

#### cluster (3) — top co-lemma: **appaṭigha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṭigha | 0.28 | 24 | 10 |

#### cluster (4) — top co-lemma: **upādiṇṇupādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādiṇṇupādāniya | 0.26 | 20 | 9 |

### passati

_pi blocks: 48; sense clusters: 1; inflected forms: passati_

#### cluster (1) — top co-lemma: **arūpasaññī** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpasaññī | 0.97 | 45 | 45 |
| abhibhuyya | 0.96 | 44 | 44 |
| jānāmi | 0.96 | 44 | 44 |
| passāmīti | 0.96 | 44 | 44 |
| tāni | 0.96 | 44 | 44 |
| ajjhatta | 0.87 | 55 | 45 |
| bahiddha | 0.84 | 59 | 45 |
| rūpūpapattiya | 0.61 | 102 | 46 |
| appamāṇa | 0.61 | 44 | 28 |
| paritta | 0.60 | 45 | 28 |

### avasesa

_pi blocks: 47; sense clusters: 3; inflected forms: avasesaṃ, avasesā_

#### cluster (1) — top co-lemma: **kusalākusalābyākata** (cohesion 0.70, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusalābyākata | 0.55 | 41 | 24 |
| ṭhapetva | 0.51 | 137 | 47 |
| sabbañca | 0.38 | 79 | 24 |
| arūpāvacara | 0.36 | 88 | 24 |
| rūpāvacara | 0.32 | 102 | 24 |
| kāmāvacara | 0.32 | 115 | 26 |

#### cluster (2) — top co-lemma: **cātipi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cātipi | 0.38 | 16 | 12 |
| vattabba | 0.28 | 38 | 12 |

#### cluster (3) — top co-lemma: **akusala** (cohesion 0.70, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusala | 0.27 | 123 | 23 |
| kiriyābyākata | 0.27 | 73 | 16 |

### tatiya

_pi blocks: 47; sense clusters: 2; inflected forms: tatiyaṃ, tatiyāya_

#### cluster (1) — top co-lemma: **pañcama** (cohesion 0.86, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pañcama | 0.87 | 40 | 38 |
| vūpasama | 0.85 | 38 | 36 |
| dutiya | 0.84 | 51 | 41 |
| vitakkavicāra | 0.83 | 40 | 36 |
| catuttha | 0.69 | 72 | 41 |
| paṭhama | 0.39 | 169 | 42 |

#### cluster (2) — top co-lemma: **pattiya** (cohesion 0.80, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pattiya | 0.39 | 75 | 24 |
| bhūmiya | 0.39 | 75 | 24 |
| apacayagāmiṃ | 0.39 | 75 | 24 |
| dandhābhiñña | 0.39 | 77 | 24 |

### ṭhiti

_pi blocks: 47; sense clusters: 2; inflected forms: ṭhiti_

#### cluster (1) — top co-lemma: **saṇṭhiti** (cohesion 0.88, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṇṭhiti | 0.68 | 24 | 24 |
| avisāhāra | 0.68 | 24 | 24 |
| avisāhaṭamānasata | 0.68 | 24 | 24 |
| avaṭṭhiti | 0.68 | 24 | 24 |
| samatha | 0.50 | 53 | 25 |
| samādhibala | 0.50 | 49 | 24 |
| sammāsamādhi | 0.48 | 32 | 19 |

#### cluster (2) — top co-lemma: **vattana** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattana | 0.46 | 14 | 14 |
| yapana | 0.46 | 14 | 14 |
| pālana | 0.46 | 14 | 14 |

### ākāsadhātu

_pi blocks: 46; sense clusters: 2; inflected forms: ākāsadhātu_

#### cluster (1) — top co-lemma: **panaññampi** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panaññampi | 0.74 | 57 | 38 |
| āpodhātu | 0.60 | 57 | 31 |
| gandhāyatana | 0.55 | 55 | 28 |
| rasāyatana | 0.52 | 61 | 28 |

#### cluster (2) — top co-lemma: **kammaññata** (cohesion 0.88, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammaññata | 0.60 | 34 | 24 |
| lahuta | 0.60 | 34 | 24 |
| muduta | 0.59 | 35 | 24 |
| jarata | 0.56 | 26 | 20 |
| aniccata | 0.54 | 28 | 20 |
| vacīviññatti | 0.51 | 41 | 22 |

### paṇḍara

_pi blocks: 46; sense clusters: 2; inflected forms: paṇḍaraṃ_

#### cluster (1) — top co-lemma: **hadaya** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hadaya | 0.72 | 26 | 26 |
| mānasa | 0.72 | 26 | 26 |
| manāyatana | 0.64 | 35 | 26 |
| tajjāmanoviññāṇadhātu | 0.61 | 20 | 20 |

#### cluster (2) — top co-lemma: **khetta** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| khetta | 0.61 | 20 | 20 |
| attabhāvapariyāpanna | 0.61 | 20 | 20 |
| tīra | 0.61 | 20 | 20 |
| orima | 0.61 | 20 | 20 |
| samudda | 0.61 | 20 | 20 |
| dvāra | 0.61 | 20 | 20 |

### pesa

_pi blocks: 45; sense clusters: 1; inflected forms: pesā_

#### cluster (1) — top co-lemma: **peta** (cohesion 0.73, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| peta | 0.94 | 40 | 40 |
| catunna | 0.81 | 49 | 38 |
| anidassana | 0.76 | 55 | 38 |
| sappaṭigha | 0.75 | 59 | 39 |
| khetta | 0.62 | 20 | 20 |
| attabhāvapariyāpanna | 0.62 | 20 | 20 |
| tīra | 0.62 | 20 | 20 |
| orima | 0.62 | 20 | 20 |
| samudda | 0.62 | 20 | 20 |
| dvāra | 0.62 | 20 | 20 |

### paritta

_pi blocks: 45; sense clusters: 2; inflected forms: parittaṃ, paritte, parittā, parittāni_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.93, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 0.63 | 44 | 28 |
| jānāmi | 0.63 | 44 | 28 |
| passāmīti | 0.63 | 44 | 28 |
| tāni | 0.63 | 44 | 28 |
| arūpasaññī | 0.62 | 45 | 28 |
| passati | 0.60 | 48 | 28 |
| ajjhatta | 0.56 | 55 | 28 |
| rūpūpapattiya | 0.54 | 102 | 40 |
| bahiddha | 0.54 | 59 | 28 |

#### cluster (2) — top co-lemma: **parittārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parittārammaṇa | 0.55 | 28 | 20 |

### paññindriya

_pi blocks: 45; sense clusters: 1; inflected forms: paññindriyaṃ_

#### cluster (1) — top co-lemma: **sammādiṭṭhi** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sammādiṭṭhi | 0.80 | 62 | 43 |
| sampajañña | 0.77 | 30 | 29 |
| paññābala | 0.76 | 31 | 29 |
| vipassana | 0.76 | 31 | 29 |
| kosalla | 0.66 | 22 | 22 |
| paññāobhāsa | 0.66 | 22 | 22 |
| cinta | 0.66 | 22 | 22 |
| paṇḍicca | 0.66 | 22 | 22 |
| paññāpajjota | 0.66 | 22 | 22 |
| upalakkhaṇa | 0.66 | 22 | 22 |

### arūpasaññī

_pi blocks: 45; sense clusters: 1; inflected forms: arūpasaññī_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.85, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 0.99 | 44 | 44 |
| jānāmi | 0.99 | 44 | 44 |
| passāmīti | 0.99 | 44 | 44 |
| tāni | 0.99 | 44 | 44 |
| passati | 0.97 | 48 | 45 |
| ajjhatta | 0.90 | 55 | 45 |
| bahiddha | 0.87 | 59 | 45 |
| appamāṇa | 0.63 | 44 | 28 |
| paritta | 0.62 | 45 | 28 |
| rūpūpapattiya | 0.61 | 102 | 45 |

### hetū

_pi blocks: 44; sense clusters: 1; inflected forms: hetū_

#### cluster (1) — top co-lemma: **bala** (cohesion 0.85, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bala | 0.51 | 27 | 18 |
| caturaṅgika | 0.47 | 16 | 14 |
| dhātuya | 0.46 | 35 | 18 |
| dvāyatana | 0.45 | 32 | 17 |
| dhammadhātu | 0.44 | 37 | 18 |
| khandha | 0.44 | 38 | 18 |
| ekaṃ | 0.44 | 34 | 17 |
| dhammāyatana | 0.43 | 39 | 18 |
| ekā | 0.43 | 35 | 17 |
| aṭṭhindriya | 0.33 | 11 | 9 |

### appamāṇa

_pi blocks: 44; sense clusters: 2; inflected forms: appamāṇaṃ, appamāṇe, appamāṇā, appamāṇāni_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.93, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 0.64 | 44 | 28 |
| jānāmi | 0.64 | 44 | 28 |
| passāmīti | 0.64 | 44 | 28 |
| tāni | 0.64 | 44 | 28 |
| arūpasaññī | 0.63 | 45 | 28 |
| passati | 0.61 | 48 | 28 |
| ajjhatta | 0.57 | 55 | 28 |
| rūpūpapattiya | 0.55 | 102 | 40 |
| bahiddha | 0.54 | 59 | 28 |

#### cluster (2) — top co-lemma: **appamāṇārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇārammaṇa | 0.56 | 27 | 20 |

### saddāyatana

_pi blocks: 44; sense clusters: 2; inflected forms: saddāyatanaṃ_

#### cluster (1) — top co-lemma: **gandhāyatana** (cohesion 0.90, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.71 | 55 | 35 |
| rasāyatana | 0.67 | 61 | 35 |
| phoṭṭhabbāyatana | 0.46 | 87 | 30 |

#### cluster (2) — top co-lemma: **kammaññata** (cohesion 0.80, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammaññata | 0.46 | 34 | 18 |
| lahuta | 0.46 | 34 | 18 |
| muduta | 0.46 | 35 | 18 |
| panaññampi | 0.44 | 57 | 22 |
| jarata | 0.40 | 26 | 14 |
| ākāsadhātu | 0.40 | 46 | 18 |
| aniccata | 0.39 | 28 | 14 |

### paggāha

_pi blocks: 44; sense clusters: 2; inflected forms: paggāho_

#### cluster (1) — top co-lemma: **vīriyindriya** (cohesion 0.79, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyindriya | 0.80 | 61 | 42 |
| samādhindriya | 0.67 | 67 | 37 |
| cittassekaggata | 0.66 | 74 | 39 |
| sammāvāyāma | 0.66 | 41 | 28 |
| saddhindriya | 0.65 | 33 | 25 |
| aññepi | 0.61 | 83 | 39 |
| satindriya | 0.60 | 39 | 25 |
| arūpina | 0.60 | 86 | 39 |
| paṭiccasamuppanna | 0.57 | 94 | 39 |

#### cluster (2) — top co-lemma: **vīriyabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyabala | 0.64 | 43 | 28 |

### abhibhuyya

_pi blocks: 44; sense clusters: 1; inflected forms: abhibhuyya_

#### cluster (1) — top co-lemma: **jānāmi** (cohesion 0.86, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jānāmi | 1.00 | 44 | 44 |
| passāmīti | 1.00 | 44 | 44 |
| tāni | 1.00 | 44 | 44 |
| arūpasaññī | 0.99 | 45 | 44 |
| passati | 0.96 | 48 | 44 |
| ajjhatta | 0.89 | 55 | 44 |
| bahiddha | 0.85 | 59 | 44 |
| appamāṇa | 0.64 | 44 | 28 |
| paritta | 0.63 | 45 | 28 |
| rūpūpapattiya | 0.60 | 102 | 44 |

### evarūpa

_pi blocks: 44; sense clusters: 2; inflected forms: evarūpaṃ, evarūpo, evarūpā_

#### cluster (1) — top co-lemma: **vipariyāsaggāha** (cohesion 0.68, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipariyāsaggāha | 0.65 | 27 | 23 |
| diṭṭhi | 0.60 | 33 | 23 |
| vuccati | 0.53 | 123 | 44 |
| tattha | 0.50 | 132 | 44 |

#### cluster (2) — top co-lemma: **micchāpatha** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 0.41 | 14 | 12 |
| diṭṭhivisūkāyika | 0.41 | 14 | 12 |
| micchatta | 0.41 | 14 | 12 |
| diṭṭhivipphandita | 0.41 | 14 | 12 |
| diṭṭhikantāra | 0.41 | 14 | 12 |
| kummagga | 0.41 | 14 | 12 |

### jānāmi

_pi blocks: 44; sense clusters: 1; inflected forms: jānāmi_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.86, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 1.00 | 44 | 44 |
| passāmīti | 1.00 | 44 | 44 |
| tāni | 1.00 | 44 | 44 |
| arūpasaññī | 0.99 | 45 | 44 |
| passati | 0.96 | 48 | 44 |
| ajjhatta | 0.89 | 55 | 44 |
| bahiddha | 0.85 | 59 | 44 |
| appamāṇa | 0.64 | 44 | 28 |
| paritta | 0.63 | 45 | 28 |
| rūpūpapattiya | 0.60 | 102 | 44 |

### passāmīti

_pi blocks: 44; sense clusters: 1; inflected forms: passāmīti_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.86, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 1.00 | 44 | 44 |
| jānāmi | 1.00 | 44 | 44 |
| tāni | 1.00 | 44 | 44 |
| arūpasaññī | 0.99 | 45 | 44 |
| passati | 0.96 | 48 | 44 |
| ajjhatta | 0.89 | 55 | 44 |
| bahiddha | 0.85 | 59 | 44 |
| appamāṇa | 0.64 | 44 | 28 |
| paritta | 0.63 | 45 | 28 |
| rūpūpapattiya | 0.60 | 102 | 44 |

### tāni

_pi blocks: 44; sense clusters: 1; inflected forms: tāni_

#### cluster (1) — top co-lemma: **abhibhuyya** (cohesion 0.86, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhibhuyya | 1.00 | 44 | 44 |
| jānāmi | 1.00 | 44 | 44 |
| passāmīti | 1.00 | 44 | 44 |
| arūpasaññī | 0.99 | 45 | 44 |
| passati | 0.96 | 48 | 44 |
| ajjhatta | 0.89 | 55 | 44 |
| bahiddha | 0.85 | 59 | 44 |
| appamāṇa | 0.64 | 44 | 28 |
| paritta | 0.63 | 45 | 28 |
| rūpūpapattiya | 0.60 | 102 | 44 |

### sukhapaṭipada

_pi blocks: 43; sense clusters: 3; inflected forms: sukhapaṭipadaṃ_

#### cluster (1) — top co-lemma: **khippābhiñña** (cohesion 0.64, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| khippābhiñña | 0.67 | 43 | 29 |
| paṭhama | 0.41 | 169 | 43 |
| vivicceva | 0.39 | 132 | 34 |
| rūpūpapattiya | 0.39 | 102 | 28 |
| kāma | 0.38 | 136 | 34 |

#### cluster (2) — top co-lemma: **dandhābhiñña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dandhābhiñña | 0.48 | 77 | 29 |

#### cluster (3) — top co-lemma: **appamāṇa** (cohesion 0.76, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇa | 0.37 | 44 | 16 |
| passāmīti | 0.37 | 44 | 16 |
| abhibhuyya | 0.37 | 44 | 16 |
| jānāmi | 0.37 | 44 | 16 |

### khippābhiñña

_pi blocks: 43; sense clusters: 3; inflected forms: khippābhiññaṃ_

#### cluster (1) — top co-lemma: **sukhapaṭipada** (cohesion 0.64, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukhapaṭipada | 0.67 | 43 | 29 |
| paṭhama | 0.41 | 169 | 43 |
| vivicceva | 0.39 | 132 | 34 |
| rūpūpapattiya | 0.39 | 102 | 28 |
| kāma | 0.38 | 136 | 34 |

#### cluster (2) — top co-lemma: **dukkhapaṭipada** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkhapaṭipada | 0.48 | 77 | 29 |

#### cluster (3) — top co-lemma: **appamāṇa** (cohesion 0.76, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇa | 0.37 | 44 | 16 |
| passāmīti | 0.37 | 44 | 16 |
| abhibhuyya | 0.37 | 44 | 16 |
| jānāmi | 0.37 | 44 | 16 |

### vīriyabala

_pi blocks: 43; sense clusters: 3; inflected forms: vīriyabalaṃ_

#### cluster (1) — top co-lemma: **vīriyindriya** (cohesion 0.66, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyindriya | 0.79 | 61 | 41 |
| paggāha | 0.64 | 44 | 28 |
| samādhibala | 0.54 | 49 | 25 |

#### cluster (2) — top co-lemma: **micchāvāyāma** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāvāyāma | 0.59 | 18 | 18 |

#### cluster (3) — top co-lemma: **thāma** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 0.54 | 16 | 16 |
| ussāha | 0.54 | 16 | 16 |
| dhurasampaggāha | 0.54 | 16 | 16 |
| asithilaparakkamata | 0.54 | 16 | 16 |
| parakkama | 0.54 | 16 | 16 |
| vāyāma | 0.54 | 16 | 16 |

### pathavīkasiṇa

_pi blocks: 42; sense clusters: 3; inflected forms: pathavīkasiṇaṃ_

#### cluster (1) — top co-lemma: **rūpūpapattiya** (cohesion 0.83, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpūpapattiya | 0.56 | 102 | 40 |
| bhāveti | 0.35 | 195 | 42 |
| magga | 0.34 | 196 | 40 |
| vivicceva | 0.33 | 132 | 29 |
| paṭhama | 0.33 | 169 | 35 |
| kāma | 0.33 | 136 | 29 |
| jhāna | 0.32 | 223 | 42 |
| yasmiṃ | 0.31 | 230 | 42 |

#### cluster (2) — top co-lemma: **appamāṇārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇārammaṇa | 0.35 | 27 | 12 |

#### cluster (3) — top co-lemma: **parittārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parittārammaṇa | 0.34 | 28 | 12 |

### kāyaviññatti

_pi blocks: 42; sense clusters: 1; inflected forms: kāyaviññatti_

#### cluster (1) — top co-lemma: **vacīviññatti** (cohesion 0.75, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vacīviññatti | 0.84 | 41 | 35 |
| kammaññata | 0.58 | 34 | 22 |
| lahuta | 0.58 | 34 | 22 |
| muduta | 0.57 | 35 | 22 |
| jarata | 0.53 | 26 | 18 |
| aniccata | 0.51 | 28 | 18 |
| ākāsadhātu | 0.50 | 46 | 22 |
| panaññampi | 0.40 | 57 | 20 |
| saddāyatana | 0.37 | 44 | 16 |
| āpodhātu | 0.34 | 57 | 17 |

### upekkhāsahagata

_pi blocks: 41; sense clusters: 3; inflected forms: upekkhāsahagataṃ, upekkhāsahagatā_

#### cluster (1) — top co-lemma: **upekkha** (cohesion 0.66, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkha | 0.57 | 26 | 19 |
| upekkhindriya | 0.43 | 20 | 13 |
| phoṭṭhabbārammaṇa | 0.34 | 17 | 10 |
| cittassekaggata | 0.30 | 74 | 17 |
| manindriya | 0.29 | 64 | 15 |

#### cluster (2) — top co-lemma: **rūpārammaṇa** (cohesion 0.77, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpārammaṇa | 0.53 | 34 | 20 |
| uppanna | 0.51 | 49 | 23 |
| panārabbha | 0.51 | 30 | 18 |
| dhammārammaṇa | 0.42 | 26 | 14 |

#### cluster (3) — top co-lemma: **upacitatta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upacitatta | 0.29 | 15 | 8 |

### vacīviññatti

_pi blocks: 41; sense clusters: 1; inflected forms: vacīviññatti_

#### cluster (1) — top co-lemma: **kāyaviññatti** (cohesion 0.75, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyaviññatti | 0.84 | 42 | 35 |
| kammaññata | 0.59 | 34 | 22 |
| lahuta | 0.59 | 34 | 22 |
| muduta | 0.58 | 35 | 22 |
| jarata | 0.54 | 26 | 18 |
| aniccata | 0.52 | 28 | 18 |
| ākāsadhātu | 0.51 | 46 | 22 |
| panaññampi | 0.41 | 57 | 20 |
| saddāyatana | 0.38 | 44 | 16 |
| āpodhātu | 0.35 | 57 | 17 |

### viññāṇa

_pi blocks: 41; sense clusters: 3; inflected forms: viññāṇasmiṃ, viññāṇaṃ, viññāṇehi_

#### cluster (1) — top co-lemma: **hadaya** (cohesion 0.94, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hadaya | 0.78 | 26 | 26 |
| mānasa | 0.78 | 26 | 26 |
| manāyatana | 0.68 | 35 | 26 |
| tajjāmanoviññāṇadhātu | 0.66 | 20 | 20 |
| paṇḍara | 0.60 | 46 | 26 |
| manindriya | 0.50 | 64 | 26 |
| citta | 0.26 | 161 | 26 |
| viññāṇakkhandha | 0.21 | 209 | 26 |

#### cluster (2) — top co-lemma: **saṅkhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhāra | 0.48 | 13 | 13 |

#### cluster (3) — top co-lemma: **saṅgahita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅgahita | 0.22 | 5 | 5 |

### sammāvāyāma

_pi blocks: 41; sense clusters: 3; inflected forms: sammāvāyāmo_

#### cluster (1) — top co-lemma: **vīriyindriya** (cohesion 0.82, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyindriya | 0.71 | 61 | 36 |
| saddhindriya | 0.68 | 33 | 25 |
| paggāha | 0.66 | 44 | 28 |
| satindriya | 0.62 | 39 | 25 |
| paññindriya | 0.49 | 45 | 21 |
| samādhindriya | 0.46 | 67 | 25 |
| sammādiṭṭhi | 0.45 | 62 | 23 |
| cittassekaggata | 0.43 | 74 | 25 |

#### cluster (2) — top co-lemma: **vīriyabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyabala | 0.52 | 43 | 22 |

#### cluster (3) — top co-lemma: **vīriyārambha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyārambha | 0.47 | 19 | 14 |

### kusalākusalābyākata

_pi blocks: 41; sense clusters: 2; inflected forms: kusalākusalābyākatā_

#### cluster (1) — top co-lemma: **rūpakkhandha** (cohesion 0.75, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpakkhandha | 0.67 | 28 | 23 |
| arūpāvacara | 0.60 | 88 | 39 |
| rūpāvacara | 0.56 | 102 | 40 |
| sāsava | 0.55 | 39 | 22 |
| kāmāvacara | 0.53 | 115 | 41 |
| viññāṇakkhandha | 0.32 | 209 | 40 |

#### cluster (2) — top co-lemma: **avasesa** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.55 | 47 | 24 |
| sabbañca | 0.28 | 79 | 17 |
| ṭhapetva | 0.28 | 137 | 25 |
| dhātu | 0.28 | 81 | 17 |

### vedayita

_pi blocks: 41; sense clusters: 5; inflected forms: vedayitaṃ_

#### cluster (1) — top co-lemma: **cetosamphassaja** (cohesion 0.88, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cetosamphassaja | 0.92 | 35 | 35 |
| sāta | 0.92 | 35 | 35 |
| cetasika | 0.89 | 38 | 35 |
| vedana | 0.51 | 120 | 41 |
| yaṃ | 0.29 | 237 | 41 |

#### cluster (2) — top co-lemma: **nāsāta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.54 | 15 | 15 |
| adukkhamasukha | 0.50 | 19 | 15 |

#### cluster (3) — top co-lemma: **sukha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukha | 0.38 | 64 | 20 |

#### cluster (4) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.27 | 18 | 8 |

#### cluster (5) — top co-lemma: **asāta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asāta | 0.26 | 6 | 6 |

### peta

_pi blocks: 40; sense clusters: 1; inflected forms: petaṃ_

#### cluster (1) — top co-lemma: **pesa** (cohesion 0.74, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pesa | 0.94 | 45 | 40 |
| catunna | 0.81 | 49 | 36 |
| anidassana | 0.80 | 55 | 38 |
| sappaṭigha | 0.79 | 59 | 39 |
| khetta | 0.67 | 20 | 20 |
| attabhāvapariyāpanna | 0.67 | 20 | 20 |
| tīra | 0.67 | 20 | 20 |
| orima | 0.67 | 20 | 20 |
| samudda | 0.67 | 20 | 20 |
| dvāra | 0.67 | 20 | 20 |

### cittuppāda

_pi blocks: 40; sense clusters: 3; inflected forms: cittuppāde, cittuppādesu, cittuppādo, cittuppādā_

#### cluster (1) — top co-lemma: **vicikicchāsahagata** (cohesion 0.66, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicikicchāsahagata | 0.67 | 26 | 22 |
| uddhaccasahagata | 0.60 | 27 | 20 |
| catūsu | 0.51 | 54 | 24 |
| tīsu | 0.34 | 77 | 20 |
| kiriyābyākata | 0.34 | 73 | 19 |
| bhūmīsu | 0.34 | 79 | 20 |

#### cluster (2) — top co-lemma: **dvīsu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvīsu | 0.37 | 9 | 9 |
| domanassasahagata | 0.35 | 11 | 9 |

#### cluster (3) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.35 | 17 | 10 |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.32 | 10 | 8 |

### paññā

_pi blocks: 40; sense clusters: 1; inflected forms: paññā_

#### cluster (1) — top co-lemma: **pajānana** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pajānana | 0.97 | 38 | 38 |
| dhammavicaya | 0.97 | 38 | 38 |
| sammādiṭṭhi | 0.75 | 62 | 38 |
| bhūrī | 0.71 | 22 | 22 |
| cinta | 0.71 | 22 | 22 |
| paṇḍicca | 0.71 | 22 | 22 |
| paññāpajjota | 0.71 | 22 | 22 |
| upalakkhaṇa | 0.71 | 22 | 22 |
| kosalla | 0.71 | 22 | 22 |
| paññāobhāsa | 0.71 | 22 | 22 |

### pañcama

_pi blocks: 40; sense clusters: 1; inflected forms: pañcamaṃ_

#### cluster (1) — top co-lemma: **tatiya** (cohesion 0.65, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tatiya | 0.87 | 47 | 38 |
| dutiya | 0.84 | 51 | 38 |
| vūpasama | 0.82 | 38 | 32 |
| vitakkavicāra | 0.80 | 40 | 32 |
| catuttha | 0.68 | 72 | 38 |
| pattiya | 0.38 | 75 | 22 |
| bhūmiya | 0.38 | 75 | 22 |
| apacayagāmiṃ | 0.38 | 75 | 22 |
| dandhābhiñña | 0.38 | 77 | 22 |
| dukkhapaṭipada | 0.38 | 77 | 22 |

### vitakkavicāra

_pi blocks: 40; sense clusters: 2; inflected forms: vitakkavicāre, vitakkavicārānaṃ_

#### cluster (1) — top co-lemma: **vūpasama** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vūpasama | 0.97 | 38 | 38 |
| tatiya | 0.83 | 47 | 36 |
| pañcama | 0.80 | 40 | 32 |
| dutiya | 0.79 | 51 | 36 |
| catuttha | 0.61 | 72 | 34 |
| paṭhama | 0.33 | 169 | 35 |
| bhāveti | 0.32 | 195 | 38 |
| jhāna | 0.30 | 223 | 39 |
| yasmiṃ | 0.28 | 230 | 38 |

#### cluster (2) — top co-lemma: **rūpūpapattiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpūpapattiya | 0.30 | 102 | 21 |

### lobha

_pi blocks: 39; sense clusters: 3; inflected forms: lobhaṃ, lobhena, lobho_

#### cluster (1) — top co-lemma: **abhijjha** (cohesion 0.65, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhijjha | 0.49 | 14 | 13 |
| anottappa | 0.37 | 20 | 11 |
| ahirika | 0.34 | 19 | 10 |

#### cluster (2) — top co-lemma: **tadekaṭṭha** (cohesion 0.93, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tadekaṭṭha | 0.42 | 13 | 11 |
| kāyakamma | 0.42 | 14 | 11 |
| vacīkamma | 0.42 | 14 | 11 |
| taṃsamuṭṭha | 0.42 | 14 | 11 |
| manokamma | 0.42 | 14 | 11 |
| kilesa | 0.38 | 34 | 14 |

#### cluster (3) — top co-lemma: **akusalamūla** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusalamūla | 0.35 | 18 | 10 |

### sāsava

_pi blocks: 39; sense clusters: 5; inflected forms: sāsavaṃ, sāsavā_

#### cluster (1) — top co-lemma: **rūpakkhandha** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpakkhandha | 0.78 | 28 | 26 |
| kusalākusalābyākata | 0.55 | 41 | 22 |
| arūpāvacara | 0.50 | 88 | 32 |
| rūpāvacara | 0.45 | 102 | 32 |
| kāmāvacara | 0.42 | 115 | 32 |
| viññāṇakkhandha | 0.25 | 209 | 31 |

#### cluster (2) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.26 | 15 | 7 |

#### cluster (3) — top co-lemma: **kusalākusala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusala | 0.20 | 11 | 5 |

#### cluster (4) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.19 | 47 | 8 |

#### cluster (5) — top co-lemma: **āsava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsava | 0.18 | 17 | 5 |

### satindriya

_pi blocks: 39; sense clusters: 2; inflected forms: satindriyaṃ_

#### cluster (1) — top co-lemma: **saddhindriya** (cohesion 0.91, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saddhindriya | 0.75 | 33 | 27 |
| sammāvāyāma | 0.62 | 41 | 25 |
| paggāha | 0.60 | 44 | 25 |
| paññindriya | 0.55 | 45 | 23 |
| vīriyindriya | 0.54 | 61 | 27 |
| samādhindriya | 0.51 | 67 | 27 |

#### cluster (2) — top co-lemma: **satibala** (cohesion 0.68, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satibala | 0.72 | 25 | 23 |
| sammāsati | 0.72 | 25 | 23 |
| apilāpanata | 0.47 | 12 | 12 |
| anussati | 0.47 | 12 | 12 |

### dhammāyatana

_pi blocks: 39; sense clusters: 1; inflected forms: dhammāyatanaṃ_

#### cluster (1) — top co-lemma: **dvāyatana** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāyatana | 0.90 | 32 | 32 |
| ekaṃ | 0.85 | 34 | 31 |
| dhātuya | 0.84 | 35 | 31 |
| dhammadhātu | 0.82 | 37 | 31 |
| ekā | 0.81 | 35 | 30 |
| khandha | 0.81 | 38 | 31 |
| bala | 0.61 | 27 | 20 |
| caturaṅgika | 0.58 | 16 | 16 |
| aññepi | 0.51 | 83 | 31 |
| arūpina | 0.50 | 86 | 31 |

### tasseva

_pi blocks: 39; sense clusters: 1; inflected forms: tasseva_

#### cluster (1) — top co-lemma: **bhāvitatta** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvitatta | 0.92 | 33 | 33 |
| bhūmiya | 0.58 | 75 | 33 |
| apacayagāmiṃ | 0.58 | 75 | 33 |
| pattiya | 0.58 | 75 | 33 |
| abyākata | 0.57 | 98 | 39 |
| pahāna | 0.56 | 92 | 37 |
| niyyānika | 0.56 | 78 | 33 |
| suññata | 0.55 | 37 | 21 |
| appaṇihita | 0.53 | 36 | 20 |
| lokuttara | 0.53 | 85 | 33 |

### cetasika

_pi blocks: 38; sense clusters: 5; inflected forms: cetasikaṃ, cetasikā_

#### cluster (1) — top co-lemma: **cetosamphassaja** (cohesion 0.97, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cetosamphassaja | 0.96 | 35 | 35 |
| vedayita | 0.89 | 41 | 35 |
| sāta | 0.88 | 35 | 32 |
| vedana | 0.44 | 120 | 35 |
| yaṃ | 0.25 | 237 | 35 |

#### cluster (2) — top co-lemma: **nāsāta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.57 | 15 | 15 |
| adukkhamasukha | 0.53 | 19 | 15 |

#### cluster (3) — top co-lemma: **sukha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukha | 0.33 | 64 | 17 |

#### cluster (4) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.29 | 18 | 8 |

#### cluster (5) — top co-lemma: **somanassindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.18 | 19 | 5 |

### dhammavicaya

_pi blocks: 38; sense clusters: 1; inflected forms: dhammavicayo_

#### cluster (1) — top co-lemma: **pajānana** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pajānana | 1.00 | 38 | 38 |
| paññā | 0.97 | 40 | 38 |
| sammādiṭṭhi | 0.76 | 62 | 38 |
| bhūrī | 0.73 | 22 | 22 |
| cinta | 0.73 | 22 | 22 |
| paṇḍicca | 0.73 | 22 | 22 |
| paññāpajjota | 0.73 | 22 | 22 |
| upalakkhaṇa | 0.73 | 22 | 22 |
| kosalla | 0.73 | 22 | 22 |
| paññāobhāsa | 0.73 | 22 | 22 |

### vattabba

_pi blocks: 38; sense clusters: 5; inflected forms: vattabbaṃ, vattabbo, vattabbā_

#### cluster (1) — top co-lemma: **cātipi** (cohesion 0.68, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cātipi | 0.59 | 16 | 16 |
| avasesa | 0.28 | 47 | 12 |
| akusala | 0.25 | 123 | 20 |
| ṭhapetva | 0.23 | 137 | 20 |

#### cluster (2) — top co-lemma: **sāmaññaphala** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāmaññaphala | 0.33 | 28 | 11 |
| cattāri | 0.29 | 38 | 11 |

#### cluster (3) — top co-lemma: **nibbānañca** (cohesion 0.61, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nibbānañca | 0.29 | 86 | 18 |
| rūpañca | 0.24 | 55 | 11 |

#### cluster (4) — top co-lemma: **siya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| siya | 0.26 | 16 | 7 |

#### cluster (5) — top co-lemma: **vipākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipākata | 0.25 | 34 | 9 |

### khandha

_pi blocks: 38; sense clusters: 1; inflected forms: khandhaṃ, khandhā_

#### cluster (1) — top co-lemma: **dvāyatana** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāyatana | 0.86 | 32 | 30 |
| dhātuya | 0.85 | 35 | 31 |
| ekaṃ | 0.83 | 34 | 30 |
| dhammadhātu | 0.83 | 37 | 31 |
| ekā | 0.82 | 35 | 30 |
| dhammāyatana | 0.81 | 39 | 31 |
| bala | 0.74 | 27 | 24 |
| caturaṅgika | 0.59 | 16 | 16 |
| aññepi | 0.51 | 83 | 31 |
| arūpina | 0.50 | 86 | 31 |

### cattāri

_pi blocks: 38; sense clusters: 3; inflected forms: cattāri_

#### cluster (1) — top co-lemma: **sāmaññaphala** (cohesion 0.82, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāmaññaphala | 0.79 | 28 | 26 |
| cattāra | 0.43 | 116 | 33 |
| nibbānañca | 0.42 | 86 | 26 |
| apariyāpanna | 0.34 | 110 | 25 |
| magga | 0.30 | 196 | 35 |

#### cluster (2) — top co-lemma: **vattabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattabba | 0.29 | 38 | 11 |

#### cluster (3) — top co-lemma: **pañcindriya** (cohesion 0.86, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pañcindriya | 0.26 | 8 | 6 |
| caturaṅgika | 0.22 | 16 | 6 |
| bala | 0.22 | 27 | 7 |
| dvāyatana | 0.20 | 32 | 7 |

### pajānana

_pi blocks: 38; sense clusters: 1; inflected forms: pajānanā_

#### cluster (1) — top co-lemma: **dhammavicaya** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammavicaya | 1.00 | 38 | 38 |
| paññā | 0.97 | 40 | 38 |
| sammādiṭṭhi | 0.76 | 62 | 38 |
| bhūrī | 0.73 | 22 | 22 |
| cinta | 0.73 | 22 | 22 |
| paṇḍicca | 0.73 | 22 | 22 |
| paññāpajjota | 0.73 | 22 | 22 |
| upalakkhaṇa | 0.73 | 22 | 22 |
| kosalla | 0.73 | 22 | 22 |
| paññāobhāsa | 0.73 | 22 | 22 |

### vūpasama

_pi blocks: 38; sense clusters: 1; inflected forms: vūpasamā_

#### cluster (1) — top co-lemma: **vitakkavicāra** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vitakkavicāra | 0.97 | 40 | 38 |
| tatiya | 0.85 | 47 | 36 |
| pañcama | 0.82 | 40 | 32 |
| dutiya | 0.81 | 51 | 36 |
| catuttha | 0.62 | 72 | 34 |
| paṭhama | 0.33 | 169 | 34 |
| bhāveti | 0.33 | 195 | 38 |
| rūpūpapattiya | 0.30 | 102 | 21 |
| jhāna | 0.29 | 223 | 38 |
| yasmiṃ | 0.28 | 230 | 38 |

### suññata

_pi blocks: 37; sense clusters: 2; inflected forms: suññataṃ_

#### cluster (1) — top co-lemma: **pattiya** (cohesion 0.82, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pattiya | 0.66 | 75 | 37 |
| bhūmiya | 0.66 | 75 | 37 |
| apacayagāmiṃ | 0.66 | 75 | 37 |
| niyyānika | 0.64 | 78 | 37 |
| lokuttara | 0.61 | 85 | 37 |
| bhāvitatta | 0.60 | 33 | 21 |
| pahāna | 0.56 | 92 | 36 |
| tasseva | 0.55 | 39 | 21 |
| diṭṭhigata | 0.53 | 98 | 36 |

#### cluster (2) — top co-lemma: **appaṇihita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.49 | 36 | 18 |

### dhammadhātu

_pi blocks: 37; sense clusters: 1; inflected forms: dhammadhātu_

#### cluster (1) — top co-lemma: **dhātuya** (cohesion 0.79, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātuya | 0.97 | 35 | 35 |
| dvāyatana | 0.87 | 32 | 30 |
| ekā | 0.86 | 35 | 31 |
| ekaṃ | 0.85 | 34 | 30 |
| khandha | 0.83 | 38 | 31 |
| dhammāyatana | 0.82 | 39 | 31 |
| bala | 0.62 | 27 | 20 |
| caturaṅgika | 0.60 | 16 | 16 |
| aññepi | 0.55 | 83 | 33 |
| arūpina | 0.54 | 86 | 33 |

### indriya

_pi blocks: 36; sense clusters: 4; inflected forms: indriyaṃ, indriyānaṃ, indriyāni_

#### cluster (1) — top co-lemma: **cakkhundriya** (cohesion 0.80, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhundriya | 0.35 | 21 | 10 |
| kāyindriya | 0.29 | 19 | 8 |

#### cluster (2) — top co-lemma: **purisindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| purisindriya | 0.23 | 35 | 8 |

#### cluster (3) — top co-lemma: **āyatana** (cohesion 0.90, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āyatana | 0.21 | 11 | 5 |
| dhātuṃ | 0.20 | 4 | 4 |
| satipaṭṭha | 0.20 | 4 | 4 |
| iddhipāda | 0.20 | 4 | 4 |

#### cluster (4) — top co-lemma: **evaṃ** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evaṃ | 0.21 | 21 | 6 |
| rūpasaṅgaha | 0.21 | 21 | 6 |
| appaṭigha | 0.20 | 24 | 6 |

### appaṇihita

_pi blocks: 36; sense clusters: 2; inflected forms: appaṇihitaṃ_

#### cluster (1) — top co-lemma: **bhūmiya** (cohesion 0.83, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhūmiya | 0.65 | 75 | 36 |
| apacayagāmiṃ | 0.65 | 75 | 36 |
| pattiya | 0.65 | 75 | 36 |
| niyyānika | 0.63 | 78 | 36 |
| lokuttara | 0.60 | 85 | 36 |
| bhāvitatta | 0.58 | 33 | 20 |
| pahāna | 0.56 | 92 | 36 |
| diṭṭhigata | 0.54 | 98 | 36 |
| tasseva | 0.53 | 39 | 20 |

#### cluster (2) — top co-lemma: **animitta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| animitta | 0.50 | 20 | 14 |

### sāta

_pi blocks: 35; sense clusters: 4; inflected forms: sātaṃ, sātā_

#### cluster (1) — top co-lemma: **vedayita** (cohesion 0.81, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vedayita | 0.92 | 41 | 35 |
| cetosamphassaja | 0.91 | 35 | 32 |
| cetasika | 0.88 | 38 | 32 |
| vedana | 0.45 | 120 | 35 |
| sukha | 0.40 | 64 | 20 |
| yaṃ | 0.26 | 237 | 35 |

#### cluster (2) — top co-lemma: **nāsāta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.60 | 15 | 15 |
| adukkhamasukha | 0.56 | 19 | 15 |

#### cluster (3) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.26 | 18 | 7 |

#### cluster (4) — top co-lemma: **somanassindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.19 | 19 | 5 |

### cetosamphassaja

_pi blocks: 35; sense clusters: 5; inflected forms: cetosamphassajaṃ, cetosamphassajā_

#### cluster (1) — top co-lemma: **cetasika** (cohesion 0.97, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cetasika | 0.96 | 38 | 35 |
| vedayita | 0.92 | 41 | 35 |
| sāta | 0.91 | 35 | 32 |
| vedana | 0.45 | 120 | 35 |
| yaṃ | 0.26 | 237 | 35 |

#### cluster (2) — top co-lemma: **nāsāta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.60 | 15 | 15 |
| adukkhamasukha | 0.56 | 19 | 15 |

#### cluster (3) — top co-lemma: **sukha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukha | 0.34 | 64 | 17 |

#### cluster (4) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.30 | 18 | 8 |

#### cluster (5) — top co-lemma: **somanassindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.19 | 19 | 5 |

### ekā

_pi blocks: 35; sense clusters: 1; inflected forms: ekā_

#### cluster (1) — top co-lemma: **dvāyatana** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāyatana | 0.90 | 32 | 30 |
| ekaṃ | 0.87 | 34 | 30 |
| dhammadhātu | 0.86 | 37 | 31 |
| dhātuya | 0.86 | 35 | 30 |
| khandha | 0.82 | 38 | 30 |
| dhammāyatana | 0.81 | 39 | 30 |
| caturaṅgika | 0.63 | 16 | 16 |
| bala | 0.61 | 27 | 19 |
| aññepi | 0.53 | 83 | 31 |
| arūpina | 0.51 | 86 | 31 |

### muduta

_pi blocks: 35; sense clusters: 1; inflected forms: mudutā_

#### cluster (1) — top co-lemma: **kammaññata** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammaññata | 0.70 | 34 | 24 |
| lahuta | 0.70 | 34 | 24 |
| jarata | 0.66 | 26 | 20 |
| aniccata | 0.63 | 28 | 20 |
| ākāsadhātu | 0.59 | 46 | 24 |
| vacīviññatti | 0.58 | 41 | 22 |
| kāyaviññatti | 0.57 | 42 | 22 |
| panaññampi | 0.48 | 57 | 22 |
| saddāyatana | 0.46 | 44 | 18 |
| āpodhātu | 0.41 | 57 | 19 |

### purisindriya

_pi blocks: 35; sense clusters: 3; inflected forms: purisindriyaṃ_

#### cluster (1) — top co-lemma: **itthindriya** (cohesion 0.64, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.70 | 48 | 29 |
| ākāsadhātu | 0.49 | 46 | 20 |
| jīvitindriya | 0.41 | 107 | 29 |
| panaññampi | 0.39 | 57 | 18 |
| āpodhātu | 0.33 | 57 | 15 |
| gandhāyatana | 0.31 | 55 | 14 |
| rasāyatana | 0.29 | 61 | 14 |
| kamma | 0.26 | 86 | 16 |

#### cluster (2) — top co-lemma: **upādiṇṇupādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādiṇṇupādāniya | 0.33 | 20 | 9 |

#### cluster (3) — top co-lemma: **upādiṇṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādiṇṇa | 0.30 | 26 | 9 |

### manāyatana

_pi blocks: 35; sense clusters: 2; inflected forms: manāyatanaṃ_

#### cluster (1) — top co-lemma: **hadaya** (cohesion 0.90, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hadaya | 0.85 | 26 | 26 |
| mānasa | 0.85 | 26 | 26 |
| tajjāmanoviññāṇadhātu | 0.73 | 20 | 20 |
| viññāṇa | 0.68 | 41 | 26 |
| paṇḍara | 0.64 | 46 | 26 |
| manindriya | 0.59 | 64 | 29 |
| citta | 0.30 | 161 | 29 |
| viññāṇakkhandha | 0.24 | 209 | 29 |
| yaṃ | 0.19 | 237 | 26 |

#### cluster (2) — top co-lemma: **dhammāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammāyatana | 0.16 | 39 | 6 |

### dhātuya

_pi blocks: 35; sense clusters: 1; inflected forms: dhātuyo_

#### cluster (1) — top co-lemma: **dhammadhātu** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammadhātu | 0.97 | 37 | 35 |
| dvāyatana | 0.90 | 32 | 30 |
| ekaṃ | 0.87 | 34 | 30 |
| ekā | 0.86 | 35 | 30 |
| khandha | 0.85 | 38 | 31 |
| dhammāyatana | 0.84 | 39 | 31 |
| bala | 0.65 | 27 | 20 |
| caturaṅgika | 0.63 | 16 | 16 |
| aññepi | 0.53 | 83 | 31 |
| arūpina | 0.51 | 86 | 31 |

### vipākata

_pi blocks: 34; sense clusters: 6; inflected forms: vipākato_

#### cluster (1) — top co-lemma: **kāmāvacarakusalata** (cohesion 0.65, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakusalata | 0.64 | 16 | 16 |
| kāmāvacarakusala | 0.63 | 20 | 17 |

#### cluster (2) — top co-lemma: **etthuppanna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| etthuppanna | 0.52 | 27 | 16 |

#### cluster (3) — top co-lemma: **rūpāvacaratikacatukkajjhāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacaratikacatukkajjhāna | 0.42 | 9 | 9 |

#### cluster (4) — top co-lemma: **āruppa** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āruppa | 0.42 | 9 | 9 |
| upekkhāsahagatacittuppāda | 0.30 | 6 | 6 |

#### cluster (5) — top co-lemma: **somanassasahagatacittuppāda** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagatacittuppāda | 0.34 | 7 | 7 |
| pañca | 0.30 | 13 | 7 |

#### cluster (6) — top co-lemma: **kāmāvacarakiriyata** (cohesion 0.55, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakiriyata | 0.30 | 6 | 6 |
| cittuppāda | 0.30 | 40 | 11 |

### kilesa

_pi blocks: 34; sense clusters: 3; inflected forms: kilesā_

#### cluster (1) — top co-lemma: **tadekaṭṭha** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tadekaṭṭha | 0.55 | 13 | 13 |
| taṃsamuṭṭha | 0.54 | 14 | 13 |
| manokamma | 0.54 | 14 | 13 |
| kāyakamma | 0.54 | 14 | 13 |
| vacīkamma | 0.54 | 14 | 13 |
| taṃsampayutta | 0.41 | 30 | 13 |
| lobha | 0.38 | 39 | 14 |
| tīṇi | 0.33 | 20 | 9 |

#### cluster (2) — top co-lemma: **saṃkiliṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃkiliṭṭha | 0.29 | 8 | 6 |

#### cluster (3) — top co-lemma: **kilesasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesasampayutta | 0.23 | 9 | 5 |

### kammaññata

_pi blocks: 34; sense clusters: 1; inflected forms: kammaññatā_

#### cluster (1) — top co-lemma: **lahuta** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lahuta | 0.71 | 34 | 24 |
| muduta | 0.70 | 35 | 24 |
| jarata | 0.67 | 26 | 20 |
| aniccata | 0.65 | 28 | 20 |
| ākāsadhātu | 0.60 | 46 | 24 |
| vacīviññatti | 0.59 | 41 | 22 |
| kāyaviññatti | 0.58 | 42 | 22 |
| panaññampi | 0.48 | 57 | 22 |
| saddāyatana | 0.46 | 44 | 18 |
| āpodhātu | 0.42 | 57 | 19 |

### lahuta

_pi blocks: 34; sense clusters: 1; inflected forms: lahutā_

#### cluster (1) — top co-lemma: **kammaññata** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammaññata | 0.71 | 34 | 24 |
| muduta | 0.70 | 35 | 24 |
| jarata | 0.67 | 26 | 20 |
| aniccata | 0.65 | 28 | 20 |
| ākāsadhātu | 0.60 | 46 | 24 |
| vacīviññatti | 0.59 | 41 | 22 |
| kāyaviññatti | 0.58 | 42 | 22 |
| panaññampi | 0.48 | 57 | 22 |
| saddāyatana | 0.46 | 44 | 18 |
| āpodhātu | 0.42 | 57 | 19 |

### ekaṃ

_pi blocks: 34; sense clusters: 1; inflected forms: ekaṃ_

#### cluster (1) — top co-lemma: **dvāyatana** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāyatana | 0.91 | 32 | 30 |
| ekā | 0.87 | 35 | 30 |
| dhātuya | 0.87 | 35 | 30 |
| dhammāyatana | 0.85 | 39 | 31 |
| dhammadhātu | 0.85 | 37 | 30 |
| khandha | 0.83 | 38 | 30 |
| caturaṅgika | 0.64 | 16 | 16 |
| bala | 0.62 | 27 | 19 |
| aññepi | 0.51 | 83 | 30 |
| arūpina | 0.50 | 86 | 30 |

### rūpārammaṇa

_pi blocks: 34; sense clusters: 5; inflected forms: rūpārammaṇaṃ, rūpārammaṇo, rūpārammaṇā_

#### cluster (1) — top co-lemma: **panārabbha** (cohesion 0.87, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panārabbha | 0.94 | 30 | 30 |
| dhammārammaṇa | 0.87 | 26 | 26 |
| uppanna | 0.77 | 49 | 32 |

#### cluster (2) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 0.86, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.55 | 17 | 14 |
| rasārammaṇa | 0.46 | 14 | 11 |
| gandhārammaṇa | 0.46 | 14 | 11 |

#### cluster (3) — top co-lemma: **upekkhāsahagata** (cohesion 0.65, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagata | 0.53 | 41 | 20 |
| upekkhindriya | 0.48 | 20 | 13 |

#### cluster (4) — top co-lemma: **sasaṅkhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.48 | 12 | 11 |

#### cluster (5) — top co-lemma: **somanassasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagata | 0.46 | 18 | 12 |

### diṭṭhi

_pi blocks: 33; sense clusters: 2; inflected forms: diṭṭhi_

#### cluster (1) — top co-lemma: **vipariyāsaggāha** (cohesion 0.85, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipariyāsaggāha | 0.90 | 27 | 27 |
| evarūpa | 0.60 | 44 | 23 |

#### cluster (2) — top co-lemma: **micchatta** (cohesion 1.00, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchatta | 0.60 | 14 | 14 |
| diṭṭhivipphandita | 0.60 | 14 | 14 |
| diṭṭhikantāra | 0.60 | 14 | 14 |
| kummagga | 0.60 | 14 | 14 |
| micchāpatha | 0.60 | 14 | 14 |
| diṭṭhivisūkāyika | 0.60 | 14 | 14 |
| abhinivesa | 0.60 | 14 | 14 |
| gāha | 0.60 | 14 | 14 |

### pīti

_pi blocks: 33; sense clusters: 2; inflected forms: pīti_

#### cluster (1) — top co-lemma: **paggāha** (cohesion 0.70, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paggāha | 0.44 | 44 | 17 |
| cittassekaggata | 0.43 | 74 | 23 |
| vicāra | 0.41 | 59 | 19 |
| vīriyindriya | 0.40 | 61 | 19 |
| saddhindriya | 0.39 | 33 | 13 |
| samādhindriya | 0.38 | 67 | 19 |
| vitakka | 0.37 | 59 | 17 |
| aññepi | 0.36 | 83 | 21 |
| satindriya | 0.36 | 39 | 13 |

#### cluster (2) — top co-lemma: **somanassindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.38 | 19 | 10 |

### saddhindriya

_pi blocks: 33; sense clusters: 2; inflected forms: saddhindriyaṃ_

#### cluster (1) — top co-lemma: **satindriya** (cohesion 0.91, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satindriya | 0.75 | 39 | 27 |
| sammāvāyāma | 0.68 | 41 | 25 |
| paggāha | 0.65 | 44 | 25 |
| paññindriya | 0.59 | 45 | 23 |
| vīriyindriya | 0.57 | 61 | 27 |
| samādhindriya | 0.54 | 67 | 27 |

#### cluster (2) — top co-lemma: **saddhābala** (cohesion 0.82, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saddhābala | 0.65 | 19 | 17 |
| kāyalahuta | 0.48 | 13 | 11 |
| kāyapassaddhi | 0.48 | 13 | 11 |
| kāyapāguññata | 0.48 | 13 | 11 |

### bhāvitatta

_pi blocks: 33; sense clusters: 2; inflected forms: bhāvitattā_

#### cluster (1) — top co-lemma: **tasseva** (cohesion 0.83, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tasseva | 0.92 | 39 | 33 |
| bhūmiya | 0.61 | 75 | 33 |
| apacayagāmiṃ | 0.61 | 75 | 33 |
| pattiya | 0.61 | 75 | 33 |
| suññata | 0.60 | 37 | 21 |
| niyyānika | 0.59 | 78 | 33 |
| appaṇihita | 0.58 | 36 | 20 |
| lokuttara | 0.56 | 85 | 33 |
| pahāna | 0.51 | 92 | 32 |

#### cluster (2) — top co-lemma: **chandādhipateyya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| chandādhipateyya | 0.51 | 30 | 16 |

### alobha

_pi blocks: 32; sense clusters: 1; inflected forms: alobho_

#### cluster (1) — top co-lemma: **anabhijjha** (cohesion 0.92, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anabhijjha | 0.72 | 18 | 18 |
| kāyalahuta | 0.49 | 13 | 11 |
| cittamuduta | 0.49 | 13 | 11 |
| cittalahuta | 0.49 | 13 | 11 |
| cittapāguññata | 0.49 | 13 | 11 |
| kāyujukata | 0.49 | 13 | 11 |
| cittujukata | 0.49 | 13 | 11 |
| cittakammaññata | 0.49 | 13 | 11 |
| kāyapassaddhi | 0.49 | 13 | 11 |
| kāyapāguññata | 0.49 | 13 | 11 |

### sammāsamādhi

_pi blocks: 32; sense clusters: 2; inflected forms: sammāsamādhi_

#### cluster (1) — top co-lemma: **samādhibala** (cohesion 0.76, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhibala | 0.67 | 49 | 27 |
| samatha | 0.66 | 53 | 28 |
| avisāhaṭamānasata | 0.57 | 24 | 16 |
| avaṭṭhiti | 0.57 | 24 | 16 |
| saṇṭhiti | 0.57 | 24 | 16 |
| avisāhāra | 0.57 | 24 | 16 |
| samādhindriya | 0.55 | 67 | 27 |

#### cluster (2) — top co-lemma: **sammāsaṅkappa** (cohesion 0.90, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sammāsaṅkappa | 0.51 | 19 | 13 |
| kāyapassaddhi | 0.49 | 13 | 11 |
| kāyapāguññata | 0.49 | 13 | 11 |

### dvāyatana

_pi blocks: 32; sense clusters: 1; inflected forms: dvāyatanāni_

#### cluster (1) — top co-lemma: **ekaṃ** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekaṃ | 0.91 | 34 | 30 |
| dhammāyatana | 0.90 | 39 | 32 |
| ekā | 0.90 | 35 | 30 |
| dhātuya | 0.90 | 35 | 30 |
| dhammadhātu | 0.87 | 37 | 30 |
| khandha | 0.86 | 38 | 30 |
| caturaṅgika | 0.67 | 16 | 16 |
| bala | 0.64 | 27 | 19 |
| aññepi | 0.52 | 83 | 30 |
| arūpina | 0.51 | 86 | 30 |

### paññābala

_pi blocks: 31; sense clusters: 1; inflected forms: paññābalaṃ_

#### cluster (1) — top co-lemma: **sampajañña** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampajañña | 0.95 | 30 | 29 |
| vipassana | 0.94 | 31 | 29 |
| cinta | 0.83 | 22 | 22 |
| paṇḍicca | 0.83 | 22 | 22 |
| paññāpajjota | 0.83 | 22 | 22 |
| upalakkhaṇa | 0.83 | 22 | 22 |
| kosalla | 0.83 | 22 | 22 |
| paññāobhāsa | 0.83 | 22 | 22 |
| bhūrī | 0.83 | 22 | 22 |
| sallakkhaṇa | 0.83 | 22 | 22 |

### vipassana

_pi blocks: 31; sense clusters: 1; inflected forms: vipassanā_

#### cluster (1) — top co-lemma: **sampajañña** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampajañña | 0.95 | 30 | 29 |
| paññābala | 0.94 | 31 | 29 |
| cinta | 0.83 | 22 | 22 |
| paṇḍicca | 0.83 | 22 | 22 |
| paññāpajjota | 0.83 | 22 | 22 |
| upalakkhaṇa | 0.83 | 22 | 22 |
| kosalla | 0.83 | 22 | 22 |
| paññāobhāsa | 0.83 | 22 | 22 |
| bhūrī | 0.83 | 22 | 22 |
| sallakkhaṇa | 0.83 | 22 | 22 |

### maggaṅga

_pi blocks: 31; sense clusters: 2; inflected forms: maggaṅgaṃ, maggaṅgāni_

#### cluster (1) — top co-lemma: **maggapariyāpanna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maggapariyāpanna | 0.98 | 30 | 30 |

#### cluster (2) — top co-lemma: **dhammavicayasambojjhaṅga** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammavicayasambojjhaṅga | 0.52 | 11 | 11 |
| paṇḍicca | 0.42 | 22 | 11 |
| paññāpajjota | 0.42 | 22 | 11 |
| upalakkhaṇa | 0.42 | 22 | 11 |
| kosalla | 0.42 | 22 | 11 |
| paññāobhāsa | 0.42 | 22 | 11 |
| bhūrī | 0.42 | 22 | 11 |
| sallakkhaṇa | 0.42 | 22 | 11 |
| cinta | 0.42 | 22 | 11 |

### pasāda

_pi blocks: 31; sense clusters: 1; inflected forms: pasādo_

#### cluster (1) — top co-lemma: **suñña** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 1.00 | 31 | 31 |
| gāma | 0.97 | 29 | 29 |
| vatthuṃ | 0.78 | 20 | 20 |
| tīra | 0.78 | 20 | 20 |
| orima | 0.78 | 20 | 20 |
| samudda | 0.78 | 20 | 20 |
| dvāra | 0.78 | 20 | 20 |
| khetta | 0.78 | 20 | 20 |
| attabhāvapariyāpanna | 0.78 | 20 | 20 |
| catunna | 0.78 | 49 | 31 |

### suñña

_pi blocks: 31; sense clusters: 1; inflected forms: suñño_

#### cluster (1) — top co-lemma: **pasāda** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pasāda | 1.00 | 31 | 31 |
| gāma | 0.97 | 29 | 29 |
| vatthuṃ | 0.78 | 20 | 20 |
| tīra | 0.78 | 20 | 20 |
| orima | 0.78 | 20 | 20 |
| samudda | 0.78 | 20 | 20 |
| dvāra | 0.78 | 20 | 20 |
| khetta | 0.78 | 20 | 20 |
| attabhāvapariyāpanna | 0.78 | 20 | 20 |
| catunna | 0.78 | 49 | 31 |

### chandādhipateyya

_pi blocks: 30; sense clusters: 2; inflected forms: chandādhipateyyaṃ_

#### cluster (1) — top co-lemma: **cittādhipateyya** (cohesion 0.94, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittādhipateyya | 0.57 | 12 | 12 |
| vīriyādhipateyya | 0.57 | 12 | 12 |
| vīmaṃsādhipateyya | 0.52 | 12 | 11 |

#### cluster (2) — top co-lemma: **bhāvitatta** (cohesion 0.83, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvitatta | 0.51 | 33 | 16 |
| tasseva | 0.46 | 39 | 16 |
| pahāna | 0.43 | 92 | 26 |
| bhūmiya | 0.42 | 75 | 22 |
| apacayagāmiṃ | 0.42 | 75 | 22 |
| pattiya | 0.42 | 75 | 22 |
| niyyānika | 0.41 | 78 | 22 |

### sampajañña

_pi blocks: 30; sense clusters: 1; inflected forms: sampajaññaṃ_

#### cluster (1) — top co-lemma: **vipassana** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipassana | 0.95 | 31 | 29 |
| paññābala | 0.95 | 31 | 29 |
| cinta | 0.85 | 22 | 22 |
| paṇḍicca | 0.85 | 22 | 22 |
| paññāpajjota | 0.85 | 22 | 22 |
| upalakkhaṇa | 0.85 | 22 | 22 |
| kosalla | 0.85 | 22 | 22 |
| paññāobhāsa | 0.85 | 22 | 22 |
| bhūrī | 0.85 | 22 | 22 |
| sallakkhaṇa | 0.85 | 22 | 22 |

### taṃsampayutta

_pi blocks: 30; sense clusters: 3; inflected forms: taṃsampayutto_

#### cluster (1) — top co-lemma: **manokamma** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manokamma | 0.64 | 14 | 14 |
| kāyakamma | 0.64 | 14 | 14 |
| vacīkamma | 0.64 | 14 | 14 |
| taṃsamuṭṭha | 0.64 | 14 | 14 |
| tadekaṭṭha | 0.60 | 13 | 13 |
| kilesa | 0.41 | 34 | 13 |
| tīṇi | 0.40 | 20 | 10 |
| lobha | 0.32 | 39 | 11 |

#### cluster (2) — top co-lemma: **viññāṇakkhandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇakkhandha | 0.25 | 209 | 30 |

#### cluster (3) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.24 | 4 | 4 |

### maggapariyāpanna

_pi blocks: 30; sense clusters: 2; inflected forms: maggapariyāpannaṃ_

#### cluster (1) — top co-lemma: **maggaṅga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maggaṅga | 0.98 | 31 | 30 |

#### cluster (2) — top co-lemma: **dhammavicayasambojjhaṅga** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammavicayasambojjhaṅga | 0.54 | 11 | 11 |
| paṇḍicca | 0.42 | 22 | 11 |
| paññāpajjota | 0.42 | 22 | 11 |
| upalakkhaṇa | 0.42 | 22 | 11 |
| kosalla | 0.42 | 22 | 11 |
| paññāobhāsa | 0.42 | 22 | 11 |
| bhūrī | 0.42 | 22 | 11 |
| sallakkhaṇa | 0.42 | 22 | 11 |
| cinta | 0.42 | 22 | 11 |

### panārabbha

_pi blocks: 30; sense clusters: 5; inflected forms: panārabbha_

#### cluster (1) — top co-lemma: **rūpārammaṇa** (cohesion 0.91, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpārammaṇa | 0.94 | 34 | 30 |
| dhammārammaṇa | 0.93 | 26 | 26 |
| uppanna | 0.76 | 49 | 30 |

#### cluster (2) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 0.85, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.55 | 17 | 13 |
| rasārammaṇa | 0.45 | 14 | 10 |
| gandhārammaṇa | 0.45 | 14 | 10 |

#### cluster (3) — top co-lemma: **sasaṅkhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.52 | 12 | 11 |

#### cluster (4) — top co-lemma: **upekkhāsahagata** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagata | 0.51 | 41 | 18 |
| upekkhindriya | 0.48 | 20 | 12 |

#### cluster (5) — top co-lemma: **somanassasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagata | 0.50 | 18 | 12 |

### gāma

_pi blocks: 29; sense clusters: 1; inflected forms: gāmo_

#### cluster (1) — top co-lemma: **suñña** (cohesion 0.82, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 0.97 | 31 | 29 |
| pasāda | 0.97 | 31 | 29 |
| catunna | 0.74 | 49 | 29 |
| vatthuṃ | 0.73 | 20 | 18 |
| tīra | 0.73 | 20 | 18 |
| orima | 0.73 | 20 | 18 |
| samudda | 0.73 | 20 | 18 |
| dvāra | 0.73 | 20 | 18 |
| khetta | 0.73 | 20 | 18 |
| attabhāvapariyāpanna | 0.73 | 20 | 18 |

### dassana

_pi blocks: 28; sense clusters: 5; inflected forms: dassanena_

#### cluster (1) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.64 | 22 | 16 |

#### cluster (2) — top co-lemma: **pahātabbahetuka** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetuka | 0.58 | 20 | 14 |

#### cluster (3) — top co-lemma: **bhāvana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvana | 0.37 | 26 | 10 |

#### cluster (4) — top co-lemma: **sīlabbataparāmāsa** (cohesion 0.85, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sīlabbataparāmāsa | 0.33 | 14 | 7 |
| tīṇi | 0.33 | 20 | 8 |
| sakkāyadiṭṭhi | 0.32 | 10 | 6 |
| saṃyojana | 0.31 | 24 | 8 |
| vicikiccha | 0.26 | 19 | 6 |

#### cluster (5) — top co-lemma: **cittuppāda** (cohesion 0.56, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittuppāda | 0.24 | 40 | 8 |
| vicikicchāsahagata | 0.22 | 26 | 6 |

### parittārammaṇa

_pi blocks: 28; sense clusters: 3; inflected forms: parittārammaṇaṃ, parittārammaṇā_

#### cluster (1) — top co-lemma: **paritta** (cohesion 0.80, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paritta | 0.55 | 45 | 20 |
| rūpūpapattiya | 0.37 | 102 | 24 |
| abhibhuyya | 0.33 | 44 | 12 |
| jānāmi | 0.33 | 44 | 12 |
| passāmīti | 0.33 | 44 | 12 |
| tāni | 0.33 | 44 | 12 |
| arūpasaññī | 0.33 | 45 | 12 |
| passati | 0.32 | 48 | 12 |

#### cluster (2) — top co-lemma: **appamāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇa | 0.39 | 44 | 14 |

#### cluster (3) — top co-lemma: **pathavīkasiṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pathavīkasiṇa | 0.34 | 42 | 12 |

### aniccata

_pi blocks: 28; sense clusters: 2; inflected forms: aniccatā_

#### cluster (1) — top co-lemma: **jarata** (cohesion 0.87, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jarata | 0.74 | 26 | 20 |
| lahuta | 0.65 | 34 | 20 |
| kammaññata | 0.65 | 34 | 20 |
| muduta | 0.63 | 35 | 20 |
| ākāsadhātu | 0.54 | 46 | 20 |
| vacīviññatti | 0.52 | 41 | 18 |
| kāyaviññatti | 0.51 | 42 | 18 |
| panaññampi | 0.42 | 57 | 18 |
| saddāyatana | 0.39 | 44 | 14 |

#### cluster (2) — top co-lemma: **anupādiṇṇupādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇupādāniya | 0.38 | 19 | 9 |

### tesa

_pi blocks: 28; sense clusters: 2; inflected forms: tesaṃ_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 0.67 | 14 | 14 |
| pālana | 0.67 | 14 | 14 |
| vattana | 0.67 | 14 | 14 |
| āyu | 0.67 | 14 | 14 |
| jīvita | 0.67 | 14 | 14 |
| iriyana | 0.67 | 14 | 14 |
| yāpana | 0.65 | 15 | 14 |
| arūpīna | 0.49 | 9 | 9 |
| ṭhiti | 0.37 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.30 | 5 | 5 |

### rūpakkhandha

_pi blocks: 28; sense clusters: 5; inflected forms: rūpakkhandho_

#### cluster (1) — top co-lemma: **sāsava** (cohesion 0.92, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.78 | 39 | 26 |
| kusalākusalābyākata | 0.67 | 41 | 23 |
| arūpāvacara | 0.45 | 88 | 26 |
| rūpāvacara | 0.40 | 102 | 26 |
| kāmāvacara | 0.38 | 115 | 27 |
| viññāṇakkhandha | 0.24 | 209 | 28 |

#### cluster (2) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.33 | 15 | 7 |

#### cluster (3) — top co-lemma: **kusalābyākata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalābyākata | 0.22 | 9 | 4 |

#### cluster (4) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.19 | 47 | 7 |

#### cluster (5) — top co-lemma: **saṃyojaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojaniya | 0.15 | 11 | 3 |

### sāmaññaphala

_pi blocks: 28; sense clusters: 3; inflected forms: sāmaññaphalāni_

#### cluster (1) — top co-lemma: **cattāri** (cohesion 0.94, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cattāri | 0.79 | 38 | 26 |
| nibbānañca | 0.46 | 86 | 26 |
| apariyāpanna | 0.39 | 110 | 27 |
| cattāra | 0.39 | 116 | 28 |
| magga | 0.24 | 196 | 27 |

#### cluster (2) — top co-lemma: **vattabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattabba | 0.33 | 38 | 11 |

#### cluster (3) — top co-lemma: **anārammaṇa** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anārammaṇa | 0.22 | 8 | 4 |
| rūpāvacaratikacatukkajjhāna | 0.22 | 9 | 4 |
| kiriyāhetukamanoviññāṇadhātu | 0.19 | 4 | 3 |
| siya | 0.18 | 16 | 4 |

### appamāṇārammaṇa

_pi blocks: 27; sense clusters: 3; inflected forms: appamāṇārammaṇaṃ, appamāṇārammaṇā_

#### cluster (1) — top co-lemma: **appamāṇa** (cohesion 0.80, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appamāṇa | 0.56 | 44 | 20 |
| rūpūpapattiya | 0.37 | 102 | 24 |
| abhibhuyya | 0.34 | 44 | 12 |
| jānāmi | 0.34 | 44 | 12 |
| passāmīti | 0.34 | 44 | 12 |
| tāni | 0.34 | 44 | 12 |
| arūpasaññī | 0.33 | 45 | 12 |
| passati | 0.32 | 48 | 12 |

#### cluster (2) — top co-lemma: **paritta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paritta | 0.39 | 45 | 14 |

#### cluster (3) — top co-lemma: **pathavīkasiṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pathavīkasiṇa | 0.35 | 42 | 12 |

### parāmāsa

_pi blocks: 27; sense clusters: 1; inflected forms: parāmāsaṃ, parāmāso, parāmāsā_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 0.68 | 14 | 14 |
| diṭṭhivisūkāyika | 0.68 | 14 | 14 |
| abhinivesa | 0.68 | 14 | 14 |
| gāha | 0.68 | 14 | 14 |
| diṭṭhigahana | 0.68 | 14 | 14 |
| titthāyatana | 0.68 | 14 | 14 |
| micchatta | 0.68 | 14 | 14 |
| diṭṭhivipphandita | 0.68 | 14 | 14 |
| diṭṭhikantāra | 0.68 | 14 | 14 |
| kummagga | 0.68 | 14 | 14 |

### manoviññāṇadhātu

_pi blocks: 27; sense clusters: 4; inflected forms: manoviññāṇadhātu_

#### cluster (1) — top co-lemma: **dhātuya** (cohesion 0.73, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātuya | 0.35 | 35 | 11 |
| dhammadhātu | 0.34 | 37 | 11 |
| ekā | 0.26 | 35 | 8 |
| khandha | 0.25 | 38 | 8 |

#### cluster (2) — top co-lemma: **somanassasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagata | 0.31 | 18 | 7 |

#### cluster (3) — top co-lemma: **aññepi** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññepi | 0.29 | 83 | 16 |
| arūpina | 0.28 | 86 | 16 |
| paṭiccasamuppanna | 0.26 | 94 | 16 |

#### cluster (4) — top co-lemma: **dhammārammaṇa** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammārammaṇa | 0.26 | 26 | 7 |
| panārabbha | 0.25 | 30 | 7 |

### satta

_pi blocks: 27; sense clusters: 1; inflected forms: satta, sattā, sattānaṃ_

#### cluster (1) — top co-lemma: **aṭṭhindriya** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aṭṭhindriya | 0.47 | 11 | 9 |
| bala | 0.44 | 27 | 12 |
| caturaṅgika | 0.37 | 16 | 8 |
| dvāyatana | 0.34 | 32 | 10 |
| ekaṃ | 0.33 | 34 | 10 |
| ekā | 0.32 | 35 | 10 |
| dhātuya | 0.32 | 35 | 10 |
| dhammadhātu | 0.31 | 37 | 10 |
| khandha | 0.31 | 38 | 10 |
| dhammāyatana | 0.30 | 39 | 10 |

### bala

_pi blocks: 27; sense clusters: 2; inflected forms: balaṃ, balāni_

#### cluster (1) — top co-lemma: **caturaṅgika** (cohesion 0.88, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| caturaṅgika | 0.74 | 16 | 16 |
| khandha | 0.74 | 38 | 24 |
| dhātuya | 0.65 | 35 | 20 |
| dvāyatana | 0.64 | 32 | 19 |
| dhammadhātu | 0.62 | 37 | 20 |
| ekaṃ | 0.62 | 34 | 19 |
| ekā | 0.61 | 35 | 19 |
| dhammāyatana | 0.61 | 39 | 20 |
| hetū | 0.51 | 44 | 18 |

#### cluster (2) — top co-lemma: **aṭṭhindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aṭṭhindriya | 0.47 | 11 | 9 |

### etthuppanna

_pi blocks: 27; sense clusters: 5; inflected forms: etthuppannaṃ, etthuppanne_

#### cluster (1) — top co-lemma: **vipākata** (cohesion 0.61, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vipākata | 0.52 | 34 | 16 |
| kāmāvacarakusala | 0.51 | 20 | 12 |
| kāmāvacarakusalata | 0.42 | 16 | 9 |
| somanassasahagatacittuppāda | 0.35 | 7 | 6 |
| pañca | 0.30 | 13 | 6 |

#### cluster (2) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.36 | 17 | 8 |

#### cluster (3) — top co-lemma: **ṭhapetva** (cohesion 0.59, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.33 | 137 | 27 |
| cattāra | 0.22 | 116 | 16 |

#### cluster (4) — top co-lemma: **cittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittuppāda | 0.30 | 40 | 10 |

#### cluster (5) — top co-lemma: **moha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.29 | 8 | 5 |

### uddhaccasahagata

_pi blocks: 27; sense clusters: 4; inflected forms: uddhaccasahagataṃ, uddhaccasahagatesu, uddhaccasahagato_

#### cluster (1) — top co-lemma: **vicikicchāsahagata** (cohesion 0.69, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicikicchāsahagata | 0.72 | 26 | 19 |
| cittuppāda | 0.60 | 40 | 20 |
| catūsu | 0.37 | 54 | 15 |
| kiriyābyākata | 0.36 | 73 | 18 |
| tīsu | 0.35 | 77 | 18 |
| bhūmīsu | 0.34 | 79 | 18 |
| rūpañca | 0.32 | 55 | 13 |

#### cluster (2) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.41 | 17 | 9 |

#### cluster (3) — top co-lemma: **moha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.34 | 8 | 6 |

#### cluster (4) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.32 | 10 | 6 |

### vipariyāsaggāha

_pi blocks: 27; sense clusters: 1; inflected forms: vipariyāsaggāho_

#### cluster (1) — top co-lemma: **diṭṭhi** (cohesion 0.90, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhi | 0.90 | 33 | 27 |
| diṭṭhikantāra | 0.68 | 14 | 14 |
| kummagga | 0.68 | 14 | 14 |
| micchāpatha | 0.68 | 14 | 14 |
| diṭṭhivisūkāyika | 0.68 | 14 | 14 |
| abhinivesa | 0.68 | 14 | 14 |
| gāha | 0.68 | 14 | 14 |
| diṭṭhigahana | 0.68 | 14 | 14 |
| micchatta | 0.68 | 14 | 14 |
| diṭṭhivipphandita | 0.68 | 14 | 14 |

### bhāvana

_pi blocks: 26; sense clusters: 5; inflected forms: bhāvanā, bhāvanāya_

#### cluster (1) — top co-lemma: **pahātabbahetuka** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetuka | 0.48 | 20 | 11 |

#### cluster (2) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.46 | 22 | 11 |

#### cluster (3) — top co-lemma: **dassana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dassana | 0.37 | 28 | 10 |

#### cluster (4) — top co-lemma: **uddhaccasahagata** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.23 | 27 | 6 |
| siya | 0.19 | 16 | 4 |

#### cluster (5) — top co-lemma: **tadekaṭṭha** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tadekaṭṭha | 0.21 | 13 | 4 |
| kāyakamma | 0.20 | 14 | 4 |
| vacīkamma | 0.20 | 14 | 4 |
| taṃsamuṭṭha | 0.20 | 14 | 4 |
| manokamma | 0.20 | 14 | 4 |

### upādiṇṇa

_pi blocks: 26; sense clusters: 3; inflected forms: upādiṇṇaṃ, upādiṇṇā_

#### cluster (1) — top co-lemma: **purisindriya** (cohesion 0.79, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| purisindriya | 0.30 | 35 | 9 |
| ākāsadhātu | 0.25 | 46 | 9 |
| itthindriya | 0.24 | 48 | 9 |
| āpodhātu | 0.24 | 57 | 10 |

#### cluster (2) — top co-lemma: **anupādiṇṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇa | 0.29 | 23 | 7 |

#### cluster (3) — top co-lemma: **kamma** (cohesion 0.66, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kamma | 0.29 | 86 | 16 |
| panaññampi | 0.27 | 57 | 11 |
| katatta | 0.23 | 114 | 16 |
| gandhāyatana | 0.22 | 55 | 9 |
| rasāyatana | 0.21 | 61 | 9 |

### jarata

_pi blocks: 26; sense clusters: 2; inflected forms: jaratā_

#### cluster (1) — top co-lemma: **aniccata** (cohesion 0.87, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aniccata | 0.74 | 28 | 20 |
| lahuta | 0.67 | 34 | 20 |
| kammaññata | 0.67 | 34 | 20 |
| muduta | 0.66 | 35 | 20 |
| ākāsadhātu | 0.56 | 46 | 20 |
| vacīviññatti | 0.54 | 41 | 18 |
| kāyaviññatti | 0.53 | 42 | 18 |
| panaññampi | 0.43 | 57 | 18 |
| saddāyatana | 0.40 | 44 | 14 |

#### cluster (2) — top co-lemma: **anupādiṇṇupādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇupādāniya | 0.40 | 19 | 9 |

### upekkha

_pi blocks: 26; sense clusters: 1; inflected forms: upekkhaṃ, upekkhā_

#### cluster (1) — top co-lemma: **upekkhindriya** (cohesion 0.69, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhindriya | 0.65 | 20 | 15 |
| upekkhāsahagata | 0.57 | 41 | 19 |
| rūpārammaṇa | 0.43 | 34 | 13 |
| panārabbha | 0.43 | 30 | 12 |
| phoṭṭhabbārammaṇa | 0.37 | 17 | 8 |
| uppanna | 0.35 | 49 | 13 |
| manindriya | 0.33 | 64 | 15 |
| dhammārammaṇa | 0.31 | 26 | 8 |
| cittassekaggata | 0.30 | 74 | 15 |
| vedana | 0.29 | 120 | 21 |

### dhammārammaṇa

_pi blocks: 26; sense clusters: 4; inflected forms: dhammārammaṇaṃ, dhammārammaṇā_

#### cluster (1) — top co-lemma: **panārabbha** (cohesion 0.77, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panārabbha | 0.93 | 30 | 26 |
| rūpārammaṇa | 0.87 | 34 | 26 |
| uppanna | 0.69 | 49 | 26 |
| upekkhāsahagata | 0.42 | 41 | 14 |

#### cluster (2) — top co-lemma: **sasaṅkhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.58 | 12 | 11 |

#### cluster (3) — top co-lemma: **somanassasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagata | 0.55 | 18 | 12 |

#### cluster (4) — top co-lemma: **rasārammaṇa** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.50 | 14 | 10 |
| gandhārammaṇa | 0.50 | 14 | 10 |
| saddārammaṇa | 0.50 | 14 | 10 |
| phoṭṭhabbārammaṇa | 0.47 | 17 | 10 |

### hadaya

_pi blocks: 26; sense clusters: 2; inflected forms: hadayaṃ_

#### cluster (1) — top co-lemma: **mānasa** (cohesion 0.95, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| mānasa | 1.00 | 26 | 26 |
| tajjāmanoviññāṇadhātu | 0.87 | 20 | 20 |
| manāyatana | 0.85 | 35 | 26 |
| viññāṇa | 0.78 | 41 | 26 |
| paṇḍara | 0.72 | 46 | 26 |
| manindriya | 0.58 | 64 | 26 |
| citta | 0.28 | 161 | 26 |
| viññāṇakkhandha | 0.22 | 209 | 26 |
| yaṃ | 0.20 | 237 | 26 |

#### cluster (2) — top co-lemma: **tajjācakkhuviññāṇadhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātu | 0.14 | 2 | 2 |

### mānasa

_pi blocks: 26; sense clusters: 2; inflected forms: mānasaṃ_

#### cluster (1) — top co-lemma: **hadaya** (cohesion 0.95, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hadaya | 1.00 | 26 | 26 |
| tajjāmanoviññāṇadhātu | 0.87 | 20 | 20 |
| manāyatana | 0.85 | 35 | 26 |
| viññāṇa | 0.78 | 41 | 26 |
| paṇḍara | 0.72 | 46 | 26 |
| manindriya | 0.58 | 64 | 26 |
| citta | 0.28 | 161 | 26 |
| viññāṇakkhandha | 0.22 | 209 | 26 |
| yaṃ | 0.20 | 237 | 26 |

#### cluster (2) — top co-lemma: **tajjācakkhuviññāṇadhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātu | 0.14 | 2 | 2 |

### vicikicchāsahagata

_pi blocks: 26; sense clusters: 6; inflected forms: vicikicchāsahagataṃ, vicikicchāsahagatesu, vicikicchāsahagato_

#### cluster (1) — top co-lemma: **uddhaccasahagata** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.72 | 27 | 19 |
| cittuppāda | 0.67 | 40 | 22 |
| catūsu | 0.40 | 54 | 16 |
| kiriyābyākata | 0.32 | 73 | 16 |

#### cluster (2) — top co-lemma: **dvīsu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvīsu | 0.40 | 9 | 7 |
| domanassasahagata | 0.38 | 11 | 7 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagata | 0.36 | 7 | 6 |

#### cluster (4) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.33 | 10 | 6 |

#### cluster (5) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.33 | 10 | 6 |

#### cluster (6) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.33 | 17 | 7 |

### sammāsati

_pi blocks: 25; sense clusters: 2; inflected forms: sammāsati_

#### cluster (1) — top co-lemma: **satibala** (cohesion 0.78, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satibala | 0.92 | 25 | 23 |
| satindriya | 0.72 | 39 | 23 |
| saraṇata | 0.65 | 12 | 12 |
| dhāraṇata | 0.65 | 12 | 12 |
| paṭissati | 0.65 | 12 | 12 |
| apilāpanata | 0.65 | 12 | 12 |
| anussati | 0.65 | 12 | 12 |
| asammussanata | 0.61 | 11 | 11 |

#### cluster (2) — top co-lemma: **sammāsaṅkappa** (cohesion 0.85, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sammāsaṅkappa | 0.59 | 19 | 13 |
| kāyapassaddhi | 0.58 | 13 | 11 |

### satibala

_pi blocks: 25; sense clusters: 2; inflected forms: satibalaṃ_

#### cluster (1) — top co-lemma: **sammāsati** (cohesion 0.78, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sammāsati | 0.92 | 25 | 23 |
| satindriya | 0.72 | 39 | 23 |
| saraṇata | 0.65 | 12 | 12 |
| dhāraṇata | 0.65 | 12 | 12 |
| paṭissati | 0.65 | 12 | 12 |
| apilāpanata | 0.65 | 12 | 12 |
| anussati | 0.65 | 12 | 12 |
| asammussanata | 0.61 | 11 | 11 |

#### cluster (2) — top co-lemma: **ottappabala** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.63 | 16 | 13 |
| hiribala | 0.63 | 16 | 13 |

### ārammaṇa

_pi blocks: 24; sense clusters: 5; inflected forms: ārammaṇaṃ, ārammaṇāni_

#### cluster (1) — top co-lemma: **cakkhusamphassa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassa | 0.32 | 13 | 6 |

#### cluster (2) — top co-lemma: **kāyasamphassa** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassa | 0.32 | 13 | 6 |
| ghānasamphassa | 0.19 | 7 | 3 |
| jivhāsamphassa | 0.19 | 7 | 3 |
| sotasamphassa | 0.19 | 7 | 3 |

#### cluster (3) — top co-lemma: **cakkhuviññāṇa** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhuviññāṇa | 0.29 | 17 | 6 |
| cakkhusamphassaja | 0.19 | 7 | 3 |

#### cluster (4) — top co-lemma: **kāyaviññāṇa** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyaviññāṇa | 0.29 | 18 | 6 |
| kāyasamphassaja | 0.16 | 13 | 3 |

#### cluster (5) — top co-lemma: **bāhira** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bāhira | 0.16 | 87 | 9 |

### appaṭigha

_pi blocks: 24; sense clusters: 5; inflected forms: appaṭighaṃ, appaṭighā_

#### cluster (1) — top co-lemma: **dhammāyatanapariyāpanna** (cohesion 0.77, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammāyatanapariyāpanna | 0.44 | 8 | 7 |
| yañca | 0.28 | 19 | 6 |
| anidassana | 0.23 | 55 | 9 |

#### cluster (2) — top co-lemma: **itthindriya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.28 | 48 | 10 |
| purisindriya | 0.17 | 35 | 5 |

#### cluster (3) — top co-lemma: **tika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tika | 0.22 | 3 | 3 |

#### cluster (4) — top co-lemma: **evaṃ** (cohesion 0.71, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evaṃ | 0.22 | 21 | 5 |
| rūpasaṅgaha | 0.22 | 21 | 5 |
| indriya | 0.20 | 36 | 6 |

#### cluster (5) — top co-lemma: **āpodhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.17 | 57 | 7 |

### saṃyojana

_pi blocks: 24; sense clusters: 5; inflected forms: saṃyojane, saṃyojanā, saṃyojanāni_

#### cluster (1) — top co-lemma: **tīṇi** (cohesion 0.81, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīṇi | 0.41 | 20 | 9 |
| sīlabbataparāmāsa | 0.37 | 14 | 7 |
| sakkāyadiṭṭhi | 0.35 | 10 | 6 |
| dassana | 0.31 | 28 | 8 |
| vicikiccha | 0.28 | 19 | 6 |

#### cluster (2) — top co-lemma: **saṃyojanasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanasampayutta | 0.30 | 9 | 5 |

#### cluster (3) — top co-lemma: **saṃyojaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojaniya | 0.29 | 11 | 5 |

#### cluster (4) — top co-lemma: **avijjāsaṃyojana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avijjāsaṃyojana | 0.29 | 4 | 4 |

#### cluster (5) — top co-lemma: **pahātabba** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.26 | 22 | 6 |
| imāni | 0.24 | 10 | 4 |

### sotāyatana

_pi blocks: 24; sense clusters: 3; inflected forms: sotāyatanaṃ_

#### cluster (1) — top co-lemma: **ghānāyatana** (cohesion 0.72, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānāyatana | 0.53 | 14 | 10 |
| jivhāyatana | 0.47 | 19 | 10 |
| kāyāyatana | 0.29 | 78 | 15 |
| saddāyatana | 0.21 | 44 | 7 |
| gandhāyatana | 0.20 | 55 | 8 |

#### cluster (2) — top co-lemma: **sotadhātu** (cohesion 0.87, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotadhātu | 0.31 | 8 | 5 |
| sotindriya | 0.28 | 12 | 5 |
| sota | 0.27 | 6 | 4 |
| sadda | 0.24 | 10 | 4 |

#### cluster (3) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.22 | 21 | 5 |

### uppajjanti

_pi blocks: 24; sense clusters: 3; inflected forms: uppajjanti_

#### cluster (1) — top co-lemma: **cittacetasika** (cohesion 0.91, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittacetasika | 0.59 | 13 | 11 |
| ārabbha | 0.43 | 22 | 10 |

#### cluster (2) — top co-lemma: **yattha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yattha | 0.50 | 8 | 8 |

#### cluster (3) — top co-lemma: **lobhasahagata** (cohesion 0.77, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagata | 0.32 | 7 | 5 |
| aṭṭhasu | 0.32 | 7 | 5 |
| dvīsu | 0.24 | 9 | 4 |
| diṭṭhigatasampayutta | 0.24 | 10 | 4 |
| domanassasahagata | 0.23 | 11 | 4 |
| uppajjati | 0.23 | 20 | 5 |
| sabbākusala | 0.21 | 5 | 3 |

### avaṭṭhiti

_pi blocks: 24; sense clusters: 3; inflected forms: avaṭṭhiti_

#### cluster (1) — top co-lemma: **avisāhaṭamānasata** (cohesion 0.92, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avisāhaṭamānasata | 1.00 | 24 | 24 |
| saṇṭhiti | 1.00 | 24 | 24 |
| avisāhāra | 1.00 | 24 | 24 |
| ṭhiti | 0.68 | 47 | 24 |
| samādhibala | 0.66 | 49 | 24 |
| samatha | 0.62 | 53 | 24 |
| sammāsamādhi | 0.57 | 32 | 16 |
| samādhindriya | 0.53 | 67 | 24 |

#### cluster (2) — top co-lemma: **samādhisambojjhaṅga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhisambojjhaṅga | 0.40 | 6 | 6 |

#### cluster (3) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.29 | 18 | 6 |

### avisāhaṭamānasata

_pi blocks: 24; sense clusters: 3; inflected forms: avisāhaṭamānasatā_

#### cluster (1) — top co-lemma: **avaṭṭhiti** (cohesion 0.92, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avaṭṭhiti | 1.00 | 24 | 24 |
| saṇṭhiti | 1.00 | 24 | 24 |
| avisāhāra | 1.00 | 24 | 24 |
| ṭhiti | 0.68 | 47 | 24 |
| samādhibala | 0.66 | 49 | 24 |
| samatha | 0.62 | 53 | 24 |
| sammāsamādhi | 0.57 | 32 | 16 |
| samādhindriya | 0.53 | 67 | 24 |

#### cluster (2) — top co-lemma: **samādhisambojjhaṅga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhisambojjhaṅga | 0.40 | 6 | 6 |

#### cluster (3) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.29 | 18 | 6 |

### avisāhāra

_pi blocks: 24; sense clusters: 3; inflected forms: avisāhāro_

#### cluster (1) — top co-lemma: **avisāhaṭamānasata** (cohesion 0.92, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avisāhaṭamānasata | 1.00 | 24 | 24 |
| avaṭṭhiti | 1.00 | 24 | 24 |
| saṇṭhiti | 1.00 | 24 | 24 |
| ṭhiti | 0.68 | 47 | 24 |
| samādhibala | 0.66 | 49 | 24 |
| samatha | 0.62 | 53 | 24 |
| sammāsamādhi | 0.57 | 32 | 16 |
| samādhindriya | 0.53 | 67 | 24 |

#### cluster (2) — top co-lemma: **samādhisambojjhaṅga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhisambojjhaṅga | 0.40 | 6 | 6 |

#### cluster (3) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.29 | 18 | 6 |

### saṇṭhiti

_pi blocks: 24; sense clusters: 3; inflected forms: saṇṭhiti_

#### cluster (1) — top co-lemma: **avisāhaṭamānasata** (cohesion 0.92, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avisāhaṭamānasata | 1.00 | 24 | 24 |
| avaṭṭhiti | 1.00 | 24 | 24 |
| avisāhāra | 1.00 | 24 | 24 |
| ṭhiti | 0.68 | 47 | 24 |
| samādhibala | 0.66 | 49 | 24 |
| samatha | 0.62 | 53 | 24 |
| sammāsamādhi | 0.57 | 32 | 16 |
| samādhindriya | 0.53 | 67 | 24 |

#### cluster (2) — top co-lemma: **samādhisambojjhaṅga** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samādhisambojjhaṅga | 0.40 | 6 | 6 |

#### cluster (3) — top co-lemma: **micchāsamādhi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsamādhi | 0.29 | 18 | 6 |

### anupādiṇṇa

_pi blocks: 23; sense clusters: 2; inflected forms: anupādiṇṇaṃ, anupādiṇṇā_

#### cluster (1) — top co-lemma: **jarata** (cohesion 0.82, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jarata | 0.37 | 26 | 9 |
| aniccata | 0.35 | 28 | 9 |
| kammaññata | 0.32 | 34 | 9 |
| lahuta | 0.32 | 34 | 9 |
| muduta | 0.31 | 35 | 9 |
| kamma | 0.29 | 86 | 16 |
| vacīviññatti | 0.28 | 41 | 9 |
| kāyaviññatti | 0.28 | 42 | 9 |
| panaññampi | 0.28 | 57 | 11 |

#### cluster (2) — top co-lemma: **upādiṇṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādiṇṇa | 0.29 | 26 | 7 |

### pāpaka

_pi blocks: 23; sense clusters: 5; inflected forms: pāpakā, pāpakānaṃ_

#### cluster (1) — top co-lemma: **samāpattiya** (cohesion 0.87, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samāpattiya | 0.93 | 20 | 20 |
| akusala | 0.32 | 123 | 23 |

#### cluster (2) — top co-lemma: **hirīyati** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hirīyati | 0.61 | 10 | 10 |
| hiriyitabba | 0.61 | 10 | 10 |

#### cluster (3) — top co-lemma: **ottappati** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappati | 0.61 | 10 | 10 |
| ottappitabba | 0.61 | 10 | 10 |

#### cluster (4) — top co-lemma: **ottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappa | 0.16 | 14 | 3 |

#### cluster (5) — top co-lemma: **ghāyitva** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghāyitva | 0.16 | 2 | 2 |
| saṃvara | 0.16 | 2 | 2 |
| anubyañjanaggāhī | 0.16 | 2 | 2 |

### pahātabba

_pi blocks: 22; sense clusters: 4; inflected forms: pahātabbaṃ, pahātabbā_

#### cluster (1) — top co-lemma: **dassana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dassana | 0.64 | 28 | 16 |

#### cluster (2) — top co-lemma: **bhāvana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvana | 0.46 | 26 | 11 |

#### cluster (3) — top co-lemma: **tadekaṭṭha** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tadekaṭṭha | 0.34 | 13 | 6 |
| kāyakamma | 0.33 | 14 | 6 |
| vacīkamma | 0.33 | 14 | 6 |
| taṃsamuṭṭha | 0.33 | 14 | 6 |
| manokamma | 0.33 | 14 | 6 |

#### cluster (4) — top co-lemma: **tīṇi** (cohesion 0.89, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīṇi | 0.29 | 20 | 6 |
| sīlabbataparāmāsa | 0.28 | 14 | 5 |
| saṃyojana | 0.26 | 24 | 6 |

### ārabbha

_pi blocks: 22; sense clusters: 2; inflected forms: ārabbha_

#### cluster (1) — top co-lemma: **uppajji** (cohesion 0.93, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajji | 0.62 | 10 | 10 |
| nissa | 0.62 | 10 | 10 |
| uppajja | 0.62 | 10 | 10 |
| uppajjissati | 0.61 | 11 | 10 |
| uppajjati | 0.57 | 20 | 12 |
| peta | 0.32 | 40 | 10 |
| pesa | 0.30 | 45 | 10 |
| catunna | 0.25 | 49 | 9 |

#### cluster (2) — top co-lemma: **cittacetasika** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittacetasika | 0.57 | 13 | 10 |
| uppajjanti | 0.43 | 24 | 10 |

### sampayutta

_pi blocks: 22; sense clusters: 9; inflected forms: sampayuttā_

#### cluster (1) — top co-lemma: **dukkha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkha | 0.19 | 20 | 4 |

#### cluster (2) — top co-lemma: **ṭhapetva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ṭhapetva | 0.16 | 137 | 13 |

#### cluster (3) — top co-lemma: **viññāṇakkhandha** (cohesion 0.83, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇakkhandha | 0.16 | 209 | 18 |
| vedanākkhandha | 0.15 | 178 | 15 |

#### cluster (4) — top co-lemma: **adukkhamasukha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| adukkhamasukha | 0.15 | 19 | 3 |

#### cluster (5) — top co-lemma: **hetusampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hetusampayutta | 0.13 | 8 | 2 |

#### cluster (6) — top co-lemma: **āsavasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavasampayutta | 0.13 | 9 | 2 |

#### cluster (7) — top co-lemma: **saṃyojanasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanasampayutta | 0.13 | 9 | 2 |

#### cluster (8) — top co-lemma: **ganthasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthasampayutta | 0.13 | 9 | 2 |

#### cluster (9) — top co-lemma: **nīvaraṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇasampayutta | 0.13 | 9 | 2 |

### bhūrī

_pi blocks: 22; sense clusters: 1; inflected forms: bhūrī_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### cinta

_pi blocks: 22; sense clusters: 1; inflected forms: cintā_

#### cluster (1) — top co-lemma: **paññāobhāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |
| kosalla | 1.00 | 22 | 22 |

### kosalla

_pi blocks: 22; sense clusters: 1; inflected forms: kosallaṃ_

#### cluster (1) — top co-lemma: **paññāobhāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### maggaphala

_pi blocks: 22; sense clusters: 7; inflected forms: maggaphalāni_

#### cluster (1) — top co-lemma: **dhātu** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.43 | 81 | 22 |
| asaṅkhata | 0.42 | 84 | 22 |
| apariyāpanna | 0.33 | 110 | 22 |
| magga | 0.20 | 196 | 22 |

#### cluster (2) — top co-lemma: **nikkhepakaṇḍa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nikkhepakaṇḍa | 0.16 | 3 | 2 |

#### cluster (3) — top co-lemma: **anāsava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anāsava | 0.14 | 6 | 2 |

#### cluster (4) — top co-lemma: **asaṃyojaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃyojaniya | 0.14 | 6 | 2 |

#### cluster (5) — top co-lemma: **aganthaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aganthaniya | 0.14 | 6 | 2 |

#### cluster (6) — top co-lemma: **anīvaraṇiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anīvaraṇiya | 0.14 | 6 | 2 |

#### cluster (7) — top co-lemma: **aparāmaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aparāmaṭṭha | 0.14 | 6 | 2 |

### medha

_pi blocks: 22; sense clusters: 1; inflected forms: medhā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### nepuñña

_pi blocks: 22; sense clusters: 1; inflected forms: nepuññaṃ_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paccupalakkhaṇa

_pi blocks: 22; sense clusters: 1; inflected forms: paccupalakkhaṇā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### pariṇāyika

_pi blocks: 22; sense clusters: 1; inflected forms: pariṇāyikā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paññāobhāsa

_pi blocks: 22; sense clusters: 1; inflected forms: paññāobhāso_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paññāpajjota

_pi blocks: 22; sense clusters: 1; inflected forms: paññāpajjoto_

#### cluster (1) — top co-lemma: **paññāobhāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |
| kosalla | 1.00 | 22 | 22 |

### paññāpāsāda

_pi blocks: 22; sense clusters: 1; inflected forms: paññāpāsādo_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paññāratana

_pi blocks: 22; sense clusters: 1; inflected forms: paññāratanaṃ_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paññāsattha

_pi blocks: 22; sense clusters: 1; inflected forms: paññāsatthaṃ_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paññāāloka

_pi blocks: 22; sense clusters: 1; inflected forms: paññāāloko_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### paṇḍicca

_pi blocks: 22; sense clusters: 1; inflected forms: paṇḍiccaṃ_

#### cluster (1) — top co-lemma: **paññāobhāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |
| kosalla | 1.00 | 22 | 22 |

### sallakkhaṇa

_pi blocks: 22; sense clusters: 1; inflected forms: sallakkhaṇā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### upalakkhaṇa

_pi blocks: 22; sense clusters: 1; inflected forms: upalakkhaṇā_

#### cluster (1) — top co-lemma: **paññāobhāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| kosalla | 1.00 | 22 | 22 |

### upaparikkha

_pi blocks: 22; sense clusters: 1; inflected forms: upaparikkhā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| vebhabya | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### vebhabya

_pi blocks: 22; sense clusters: 1; inflected forms: vebhabyā_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 1.00 | 22 | 22 |
| paññāobhāsa | 1.00 | 22 | 22 |
| bhūrī | 1.00 | 22 | 22 |
| sallakkhaṇa | 1.00 | 22 | 22 |
| paññāpāsāda | 1.00 | 22 | 22 |
| upaparikkha | 1.00 | 22 | 22 |
| cinta | 1.00 | 22 | 22 |
| paṇḍicca | 1.00 | 22 | 22 |
| paññāpajjota | 1.00 | 22 | 22 |
| upalakkhaṇa | 1.00 | 22 | 22 |

### vatthu

_pi blocks: 21; sense clusters: 6; inflected forms: vatthu_

#### cluster (1) — top co-lemma: **cakkhusamphassa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassa | 0.35 | 13 | 6 |

#### cluster (2) — top co-lemma: **kāyasamphassa** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassa | 0.35 | 13 | 6 |
| ghānasamphassa | 0.21 | 7 | 3 |
| jivhāsamphassa | 0.21 | 7 | 3 |
| sotasamphassa | 0.21 | 7 | 3 |

#### cluster (3) — top co-lemma: **cakkhuviññāṇa** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhuviññāṇa | 0.32 | 17 | 6 |
| cakkhusamphassaja | 0.21 | 7 | 3 |

#### cluster (4) — top co-lemma: **kāyaviññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyaviññāṇa | 0.31 | 18 | 6 |

#### cluster (5) — top co-lemma: **sotāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotāyatana | 0.22 | 24 | 5 |

#### cluster (6) — top co-lemma: **ajjhattika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ajjhattika | 0.22 | 61 | 9 |

### cakkhundriya

_pi blocks: 21; sense clusters: 3; inflected forms: cakkhundriyaṃ, cakkhundriye_

#### cluster (1) — top co-lemma: **cakkhu** (cohesion 0.94, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhu | 0.50 | 11 | 8 |
| pasāda | 0.31 | 31 | 8 |
| suñña | 0.31 | 31 | 8 |
| gāma | 0.28 | 29 | 7 |

#### cluster (2) — top co-lemma: **kāyindriya** (cohesion 0.80, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyindriya | 0.40 | 19 | 8 |
| indriya | 0.35 | 36 | 10 |

#### cluster (3) — top co-lemma: **nayana** (cohesion 0.90, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nayana | 0.32 | 4 | 4 |
| netta | 0.32 | 4 | 4 |
| cakkhudhātu | 0.31 | 11 | 5 |
| cakkhuṃ | 0.30 | 6 | 4 |

### rūpasaṅgaha

_pi blocks: 21; sense clusters: 4; inflected forms: rūpasaṅgaho_

#### cluster (1) — top co-lemma: **evaṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evaṃ | 1.00 | 21 | 21 |

#### cluster (2) — top co-lemma: **sotaviññeyya** (cohesion 0.84, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotaviññeyya | 0.43 | 7 | 6 |
| jivhāviññeyya | 0.43 | 7 | 6 |
| kāyaviññeyya | 0.43 | 7 | 6 |
| cakkhuviññeyya | 0.43 | 7 | 6 |
| ghānaviññeyya | 0.43 | 7 | 6 |
| manodhātuviññeyya | 0.32 | 4 | 4 |
| manoviññāṇadhātuviññeyya | 0.32 | 4 | 4 |

#### cluster (3) — top co-lemma: **sabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabba | 0.34 | 14 | 6 |

#### cluster (4) — top co-lemma: **appaṭigha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṭigha | 0.22 | 24 | 5 |

### uppajjati

_pi blocks: 20; sense clusters: 2; inflected forms: uppajjati_

#### cluster (1) — top co-lemma: **uppajji** (cohesion 0.93, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajji | 0.67 | 10 | 10 |
| nissa | 0.67 | 10 | 10 |
| uppajja | 0.67 | 10 | 10 |
| uppajjissati | 0.65 | 11 | 10 |
| ārabbha | 0.57 | 22 | 12 |

#### cluster (2) — top co-lemma: **lobhasahagata** (cohesion 0.65, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagata | 0.52 | 7 | 7 |
| aṭṭhasu | 0.52 | 7 | 7 |
| diṭṭhigatasampayutta | 0.40 | 10 | 6 |
| sabbākusala | 0.40 | 5 | 5 |
| dvīsu | 0.34 | 9 | 5 |

### anottappa

_pi blocks: 20; sense clusters: 1; inflected forms: anottappaṃ, anottappena_

#### cluster (1) — top co-lemma: **ahirika** (cohesion 0.79, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirika | 0.82 | 19 | 16 |
| ahirikabala | 0.80 | 15 | 14 |
| anottappabala | 0.80 | 15 | 14 |
| micchāsaṅkappa | 0.78 | 16 | 14 |
| micchāvāyāma | 0.74 | 18 | 14 |
| micchāsamādhi | 0.63 | 18 | 12 |
| abhijjha | 0.47 | 14 | 8 |
| vīriyabala | 0.44 | 43 | 14 |
| paggāha | 0.44 | 44 | 14 |
| lobha | 0.37 | 39 | 11 |

### upādiṇṇupādāniya

_pi blocks: 20; sense clusters: 2; inflected forms: upādiṇṇupādāniyaṃ, upādiṇṇupādāniyā_

#### cluster (1) — top co-lemma: **purisindriya** (cohesion 0.64, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| purisindriya | 0.33 | 35 | 9 |
| kamma | 0.30 | 86 | 16 |
| panaññampi | 0.29 | 57 | 11 |
| ākāsadhātu | 0.27 | 46 | 9 |
| itthindriya | 0.26 | 48 | 9 |
| katatta | 0.24 | 114 | 16 |
| āpodhātu | 0.23 | 57 | 9 |

#### cluster (2) — top co-lemma: **gandhāyatana** (cohesion 0.87, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhāyatana | 0.24 | 55 | 9 |
| rasāyatana | 0.22 | 61 | 9 |
| kāyāyatana | 0.18 | 78 | 9 |

### pahātabbahetuka

_pi blocks: 20; sense clusters: 5; inflected forms: pahātabbahetukaṃ, pahātabbahetukā_

#### cluster (1) — top co-lemma: **dassana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dassana | 0.58 | 28 | 14 |

#### cluster (2) — top co-lemma: **bhāvana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvana | 0.48 | 26 | 11 |

#### cluster (3) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.33 | 4 | 4 |
| tadekaṭṭha | 0.24 | 13 | 4 |
| manokamma | 0.24 | 14 | 4 |
| kāyakamma | 0.24 | 14 | 4 |
| vacīkamma | 0.24 | 14 | 4 |

#### cluster (4) — top co-lemma: **moha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.29 | 8 | 4 |

#### cluster (5) — top co-lemma: **sakkāyadiṭṭhi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sakkāyadiṭṭhi | 0.27 | 10 | 4 |
| sīlabbataparāmāsa | 0.24 | 14 | 4 |

### dukkha

_pi blocks: 20; sense clusters: 2; inflected forms: dukkhassa, dukkhaṃ, dukkhe, dukkhā, dukkhāya_

#### cluster (1) — top co-lemma: **dukkhanirodhagāminiya** (cohesion 0.89, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkhanirodhagāminiya | 0.52 | 7 | 7 |
| dukkhanirodha | 0.52 | 7 | 7 |
| dukkhasamudaya | 0.52 | 7 | 7 |
| paṭipada | 0.47 | 10 | 7 |
| pubbantāparanta | 0.45 | 11 | 7 |
| idappaccayata | 0.45 | 11 | 7 |
| pubbanta | 0.44 | 12 | 7 |
| apaccavekkhaṇa | 0.40 | 5 | 5 |
| avijjogha | 0.38 | 6 | 5 |

#### cluster (2) — top co-lemma: **asāta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asāta | 0.46 | 6 | 6 |

### kāya

_pi blocks: 20; sense clusters: 3; inflected forms: kāyamhi, kāyassa, kāyaṃ, kāyena, kāyo_

#### cluster (1) — top co-lemma: **phoṭṭhabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabba | 0.65 | 11 | 10 |

#### cluster (2) — top co-lemma: **saṇha** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṇha | 0.33 | 4 | 4 |
| lahuka | 0.33 | 4 | 4 |
| muduka | 0.33 | 4 | 4 |
| pharusa | 0.33 | 4 | 4 |
| garuka | 0.33 | 4 | 4 |
| kakkhaḷa | 0.32 | 5 | 4 |

#### cluster (3) — top co-lemma: **gāma** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gāma | 0.33 | 29 | 8 |
| pasāda | 0.31 | 31 | 8 |
| suñña | 0.31 | 31 | 8 |

### upekkhindriya

_pi blocks: 20; sense clusters: 2; inflected forms: upekkhindriyaṃ_

#### cluster (1) — top co-lemma: **upekkha** (cohesion 0.81, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkha | 0.65 | 26 | 15 |
| rūpārammaṇa | 0.48 | 34 | 13 |
| panārabbha | 0.48 | 30 | 12 |
| phoṭṭhabbārammaṇa | 0.43 | 17 | 8 |
| upekkhāsahagata | 0.43 | 41 | 13 |
| uppanna | 0.38 | 49 | 13 |

#### cluster (2) — top co-lemma: **dvāyatana** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāyatana | 0.38 | 32 | 10 |
| ekaṃ | 0.37 | 34 | 10 |
| ekā | 0.36 | 35 | 10 |
| dhātuya | 0.36 | 35 | 10 |

### kāmāvacarakusala

_pi blocks: 20; sense clusters: 4; inflected forms: kāmāvacarakusalassa, kāmāvacarakusalaṃ_

#### cluster (1) — top co-lemma: **kāmāvacarakusalata** (cohesion 0.68, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakusalata | 0.72 | 16 | 13 |
| vipākata | 0.63 | 34 | 17 |
| etthuppanna | 0.51 | 27 | 12 |

#### cluster (2) — top co-lemma: **somanassasahagatacittuppāda** (cohesion 0.66, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagatacittuppāda | 0.52 | 7 | 7 |
| pañca | 0.42 | 13 | 7 |
| rūpāvacaratikacatukkajjhāna | 0.34 | 9 | 5 |
| lokuttaratikacatukkajjhāna | 0.32 | 5 | 4 |

#### cluster (3) — top co-lemma: **upekkhāsahagatacittuppāda** (cohesion 0.83, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagatacittuppāda | 0.46 | 6 | 6 |
| āruppa | 0.34 | 9 | 5 |

#### cluster (4) — top co-lemma: **ekādasa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekādasa | 0.40 | 5 | 5 |

### tīṇi

_pi blocks: 20; sense clusters: 2; inflected forms: tīṇi_

#### cluster (1) — top co-lemma: **vacīkamma** (cohesion 0.97, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vacīkamma | 0.59 | 14 | 10 |
| taṃsamuṭṭha | 0.59 | 14 | 10 |
| manokamma | 0.59 | 14 | 10 |
| kāyakamma | 0.59 | 14 | 10 |
| tadekaṭṭha | 0.55 | 13 | 9 |
| taṃsampayutta | 0.40 | 30 | 10 |

#### cluster (2) — top co-lemma: **sīlabbataparāmāsa** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sīlabbataparāmāsa | 0.41 | 14 | 7 |
| saṃyojana | 0.41 | 24 | 9 |
| sakkāyadiṭṭhi | 0.40 | 10 | 6 |
| vicikiccha | 0.36 | 19 | 7 |

### animitta

_pi blocks: 20; sense clusters: 2; inflected forms: animittaṃ_

#### cluster (1) — top co-lemma: **chandādhipateyyanti** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| chandādhipateyyanti | 0.57 | 8 | 8 |

#### cluster (2) — top co-lemma: **appaṇihita** (cohesion 0.72, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihita | 0.50 | 36 | 14 |
| suññata | 0.49 | 37 | 14 |
| bhāvitatta | 0.45 | 33 | 12 |
| pattiya | 0.42 | 75 | 20 |
| bhūmiya | 0.42 | 75 | 20 |
| apacayagāmiṃ | 0.42 | 75 | 20 |
| niyyānika | 0.41 | 78 | 20 |
| tasseva | 0.41 | 39 | 12 |
| lokuttara | 0.38 | 85 | 20 |

### attabhāvapariyāpanna

_pi blocks: 20; sense clusters: 1; inflected forms: attabhāvapariyāpanno_

#### cluster (1) — top co-lemma: **samudda** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samudda | 1.00 | 20 | 20 |
| dvāra | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### dvāra

_pi blocks: 20; sense clusters: 1; inflected forms: dvārā_

#### cluster (1) — top co-lemma: **samudda** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samudda | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### khetta

_pi blocks: 20; sense clusters: 1; inflected forms: khettaṃ_

#### cluster (1) — top co-lemma: **samudda** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samudda | 1.00 | 20 | 20 |
| dvāra | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### orima

_pi blocks: 20; sense clusters: 1; inflected forms: orimaṃ_

#### cluster (1) — top co-lemma: **dvāra** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāra | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| samudda | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### paṭihañña

_pi blocks: 20; sense clusters: 1; inflected forms: paṭihaññe_

#### cluster (1) — top co-lemma: **paṭihaññati** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭihaññati | 1.00 | 20 | 20 |
| paṭihaññissati | 1.00 | 20 | 20 |
| paṭihaññi | 1.00 | 20 | 20 |
| peta | 0.67 | 40 | 20 |
| pesa | 0.62 | 45 | 20 |
| anidassana | 0.53 | 55 | 20 |
| catunna | 0.52 | 49 | 18 |
| sappaṭigha | 0.51 | 59 | 20 |
| tīra | 0.50 | 20 | 10 |
| orima | 0.50 | 20 | 10 |

### paṭihaññati

_pi blocks: 20; sense clusters: 1; inflected forms: paṭihaññati_

#### cluster (1) — top co-lemma: **paṭihaññissati** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭihaññissati | 1.00 | 20 | 20 |
| paṭihañña | 1.00 | 20 | 20 |
| paṭihaññi | 1.00 | 20 | 20 |
| peta | 0.67 | 40 | 20 |
| pesa | 0.62 | 45 | 20 |
| anidassana | 0.53 | 55 | 20 |
| catunna | 0.52 | 49 | 18 |
| sappaṭigha | 0.51 | 59 | 20 |
| tīra | 0.50 | 20 | 10 |
| orima | 0.50 | 20 | 10 |

### paṭihaññi

_pi blocks: 20; sense clusters: 1; inflected forms: paṭihaññi_

#### cluster (1) — top co-lemma: **paṭihaññati** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭihaññati | 1.00 | 20 | 20 |
| paṭihaññissati | 1.00 | 20 | 20 |
| paṭihañña | 1.00 | 20 | 20 |
| peta | 0.67 | 40 | 20 |
| pesa | 0.62 | 45 | 20 |
| anidassana | 0.53 | 55 | 20 |
| catunna | 0.52 | 49 | 18 |
| sappaṭigha | 0.51 | 59 | 20 |
| tīra | 0.50 | 20 | 10 |
| orima | 0.50 | 20 | 10 |

### paṭihaññissati

_pi blocks: 20; sense clusters: 1; inflected forms: paṭihaññissati_

#### cluster (1) — top co-lemma: **paṭihaññati** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭihaññati | 1.00 | 20 | 20 |
| paṭihañña | 1.00 | 20 | 20 |
| paṭihaññi | 1.00 | 20 | 20 |
| peta | 0.67 | 40 | 20 |
| pesa | 0.62 | 45 | 20 |
| anidassana | 0.53 | 55 | 20 |
| catunna | 0.52 | 49 | 18 |
| sappaṭigha | 0.51 | 59 | 20 |
| tīra | 0.50 | 20 | 10 |
| orima | 0.50 | 20 | 10 |

### samudda

_pi blocks: 20; sense clusters: 1; inflected forms: samuddo_

#### cluster (1) — top co-lemma: **dvāra** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāra | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### samāpattiya

_pi blocks: 20; sense clusters: 6; inflected forms: samāpattiyā_

#### cluster (1) — top co-lemma: **pāpaka** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pāpaka | 0.93 | 23 | 20 |
| hirīyati | 0.67 | 10 | 10 |
| hiriyitabba | 0.67 | 10 | 10 |
| akusala | 0.28 | 123 | 20 |

#### cluster (2) — top co-lemma: **ottappati** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappati | 0.67 | 10 | 10 |
| ottappitabba | 0.67 | 10 | 10 |

#### cluster (3) — top co-lemma: **ottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappa | 0.18 | 14 | 3 |

#### cluster (4) — top co-lemma: **ottappabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.17 | 16 | 3 |

#### cluster (5) — top co-lemma: **hiribala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hiribala | 0.17 | 16 | 3 |

#### cluster (6) — top co-lemma: **hirī** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hirī | 0.16 | 17 | 3 |

### tajjāmanoviññāṇadhātu

_pi blocks: 20; sense clusters: 2; inflected forms: tajjāmanoviññāṇadhātu_

#### cluster (1) — top co-lemma: **hadaya** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hadaya | 0.87 | 26 | 20 |
| mānasa | 0.87 | 26 | 20 |
| manāyatana | 0.73 | 35 | 20 |
| viññāṇa | 0.66 | 41 | 20 |
| paṇḍara | 0.61 | 46 | 20 |
| manindriya | 0.48 | 64 | 20 |
| citta | 0.22 | 161 | 20 |
| viññāṇakkhandha | 0.17 | 209 | 20 |
| yaṃ | 0.16 | 237 | 20 |

#### cluster (2) — top co-lemma: **ekaṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekaṃ | 0.11 | 34 | 3 |

### tīra

_pi blocks: 20; sense clusters: 1; inflected forms: tīraṃ_

#### cluster (1) — top co-lemma: **dvāra** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvāra | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| vatthuṃ | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| samudda | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### vatthuṃ

_pi blocks: 20; sense clusters: 1; inflected forms: vatthuṃ_

#### cluster (1) — top co-lemma: **samudda** (cohesion 0.98, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samudda | 1.00 | 20 | 20 |
| dvāra | 1.00 | 20 | 20 |
| khetta | 1.00 | 20 | 20 |
| attabhāvapariyāpanna | 1.00 | 20 | 20 |
| tīra | 1.00 | 20 | 20 |
| orima | 1.00 | 20 | 20 |
| suñña | 0.78 | 31 | 20 |
| pasāda | 0.78 | 31 | 20 |
| gāma | 0.73 | 29 | 18 |
| peta | 0.67 | 40 | 20 |

### gantha

_pi blocks: 19; sense clusters: 4; inflected forms: ganthe, gantho, ganthā_

#### cluster (1) — top co-lemma: **kāyagantha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyagantha | 0.38 | 7 | 5 |

#### cluster (2) — top co-lemma: **ganthasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthasampayutta | 0.36 | 9 | 5 |

#### cluster (3) — top co-lemma: **ganthaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthaniya | 0.33 | 11 | 5 |

#### cluster (4) — top co-lemma: **paṇidhi** (cohesion 1.00, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṇidhi | 0.27 | 3 | 3 |
| saddataṇha | 0.27 | 3 | 3 |
| gedha | 0.27 | 3 | 3 |
| anurodha | 0.27 | 3 | 3 |
| dhanāsa | 0.27 | 3 | 3 |
| jīvitāsa | 0.27 | 3 | 3 |
| jappana | 0.27 | 3 | 3 |

### nīvaraṇa

_pi blocks: 19; sense clusters: 4; inflected forms: nīvaraṇaṃ, nīvaraṇe, nīvaraṇā, nīvaraṇāni_

#### cluster (1) — top co-lemma: **nīvaraṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇasampayutta | 0.36 | 9 | 5 |

#### cluster (2) — top co-lemma: **avijjānīvaraṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avijjānīvaraṇa | 0.35 | 4 | 4 |

#### cluster (3) — top co-lemma: **nīvaraṇiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇiya | 0.33 | 11 | 5 |

#### cluster (4) — top co-lemma: **paṇidhi** (cohesion 1.00, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṇidhi | 0.27 | 3 | 3 |
| saddataṇha | 0.27 | 3 | 3 |
| gedha | 0.27 | 3 | 3 |
| anurodha | 0.27 | 3 | 3 |
| dhanāsa | 0.27 | 3 | 3 |
| jīvitāsa | 0.27 | 3 | 3 |
| jappana | 0.27 | 3 | 3 |

### anupādiṇṇupādāniya

_pi blocks: 19; sense clusters: 1; inflected forms: anupādiṇṇupādāniyaṃ, anupādiṇṇupādāniyā_

#### cluster (1) — top co-lemma: **jarata** (cohesion 0.76, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jarata | 0.40 | 26 | 9 |
| aniccata | 0.38 | 28 | 9 |
| kammaññata | 0.34 | 34 | 9 |
| lahuta | 0.34 | 34 | 9 |
| muduta | 0.33 | 35 | 9 |
| kamma | 0.30 | 86 | 16 |
| vacīviññatti | 0.30 | 41 | 9 |
| kāyaviññatti | 0.30 | 42 | 9 |
| panaññampi | 0.29 | 57 | 11 |
| saddāyatana | 0.29 | 44 | 9 |

### adukkhamasukha

_pi blocks: 19; sense clusters: 4; inflected forms: adukkhamasukhaṃ, adukkhamasukhā, adukkhamasukhāya_

#### cluster (1) — top co-lemma: **nāsāta** (cohesion 0.93, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.88 | 15 | 15 |
| sāta | 0.56 | 35 | 15 |
| cetosamphassaja | 0.56 | 35 | 15 |
| cetasika | 0.53 | 38 | 15 |
| vedayita | 0.50 | 41 | 15 |
| vedana | 0.27 | 120 | 19 |

#### cluster (2) — top co-lemma: **upekkhindriya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhindriya | 0.31 | 20 | 6 |
| caturaṅgika | 0.17 | 16 | 3 |

#### cluster (3) — top co-lemma: **upekkha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkha | 0.27 | 26 | 6 |

#### cluster (4) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.16 | 18 | 3 |

### vicikiccha

_pi blocks: 19; sense clusters: 1; inflected forms: vicikicchā, vicikicchāya_

#### cluster (1) — top co-lemma: **thambhitatta** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thambhitatta | 0.52 | 8 | 7 |
| manovilekha | 0.52 | 8 | 7 |
| vicikicchati | 0.48 | 6 | 6 |
| kaṅkhati | 0.48 | 6 | 6 |
| satthari | 0.48 | 6 | 6 |
| kaṅkhāyitatta | 0.42 | 5 | 5 |
| anekaṃsaggāha | 0.42 | 5 | 5 |
| kaṅkhāyana | 0.42 | 5 | 5 |
| dvedhāpatha | 0.42 | 5 | 5 |
| dveḷhaka | 0.42 | 5 | 5 |

### ahirika

_pi blocks: 19; sense clusters: 2; inflected forms: ahirikaṃ_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.85, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.82 | 15 | 14 |
| anottappabala | 0.82 | 15 | 14 |
| anottappa | 0.82 | 20 | 16 |
| micchāsaṅkappa | 0.80 | 16 | 14 |
| micchāvāyāma | 0.76 | 18 | 14 |
| micchāsamādhi | 0.65 | 18 | 12 |
| abhijjha | 0.48 | 14 | 8 |
| vīriyabala | 0.45 | 43 | 14 |
| paggāha | 0.44 | 44 | 14 |

#### cluster (2) — top co-lemma: **rasārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.36 | 14 | 6 |

### jivhāyatana

_pi blocks: 19; sense clusters: 2; inflected forms: jivhāyatanaṃ_

#### cluster (1) — top co-lemma: **ghānāyatana** (cohesion 0.81, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānāyatana | 0.61 | 14 | 10 |
| sotāyatana | 0.47 | 24 | 10 |
| kāyāyatana | 0.23 | 78 | 11 |
| saddāyatana | 0.22 | 44 | 7 |
| gandhāyatana | 0.22 | 55 | 8 |

#### cluster (2) — top co-lemma: **jivhādhātu** (cohesion 0.81, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhādhātu | 0.37 | 8 | 5 |
| jivhindriya | 0.32 | 12 | 5 |
| jivha | 0.28 | 10 | 4 |
| gāma | 0.21 | 29 | 5 |
| tīra | 0.21 | 20 | 4 |

### kāyindriya

_pi blocks: 19; sense clusters: 3; inflected forms: kāyindriyaṃ_

#### cluster (1) — top co-lemma: **jivhindriya** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhindriya | 0.52 | 12 | 8 |
| ghānindriya | 0.52 | 12 | 8 |
| sotindriya | 0.52 | 12 | 8 |

#### cluster (2) — top co-lemma: **cakkhundriya** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhundriya | 0.40 | 21 | 8 |
| indriya | 0.29 | 36 | 8 |

#### cluster (3) — top co-lemma: **kāyadhātu** (cohesion 0.75, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyadhātu | 0.33 | 11 | 5 |
| kāya | 0.31 | 20 | 6 |
| phoṭṭhabba | 0.27 | 11 | 4 |
| gāma | 0.25 | 29 | 6 |
| suñña | 0.24 | 31 | 6 |

### saddhābala

_pi blocks: 19; sense clusters: 1; inflected forms: saddhābalaṃ_

#### cluster (1) — top co-lemma: **ottappabala** (cohesion 0.95, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.74 | 16 | 13 |
| hiribala | 0.74 | 16 | 13 |
| kāyapassaddhi | 0.69 | 13 | 11 |
| kāyapāguññata | 0.69 | 13 | 11 |
| kāyalahuta | 0.69 | 13 | 11 |
| cittamuduta | 0.69 | 13 | 11 |
| cittalahuta | 0.69 | 13 | 11 |
| cittapāguññata | 0.69 | 13 | 11 |
| kāyujukata | 0.69 | 13 | 11 |
| cittujukata | 0.69 | 13 | 11 |

### sammāsaṅkappa

_pi blocks: 19; sense clusters: 1; inflected forms: sammāsaṅkappo_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.69 | 13 | 11 |
| cittapāguññata | 0.69 | 13 | 11 |
| kāyujukata | 0.69 | 13 | 11 |
| cittujukata | 0.69 | 13 | 11 |
| cittakammaññata | 0.69 | 13 | 11 |
| kāyamuduta | 0.69 | 13 | 11 |
| kāyapassaddhi | 0.69 | 13 | 11 |
| kāyapāguññata | 0.69 | 13 | 11 |
| kāyalahuta | 0.69 | 13 | 11 |
| cittamuduta | 0.69 | 13 | 11 |

### somanassindriya

_pi blocks: 19; sense clusters: 3; inflected forms: somanassindriyaṃ_

#### cluster (1) — top co-lemma: **sukha** (cohesion 0.69, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukha | 0.41 | 64 | 17 |
| saddhindriya | 0.38 | 33 | 10 |
| satindriya | 0.34 | 39 | 10 |
| manindriya | 0.34 | 64 | 14 |
| vīriyindriya | 0.33 | 61 | 13 |
| paggāha | 0.32 | 44 | 10 |

#### cluster (2) — top co-lemma: **aṭṭhindriya** (cohesion 0.71, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aṭṭhindriya | 0.40 | 11 | 6 |
| caturaṅgika | 0.34 | 16 | 6 |

#### cluster (3) — top co-lemma: **pīti** (cohesion 0.60, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pīti | 0.38 | 33 | 10 |
| somanassasahagata | 0.32 | 18 | 6 |

### kiriya

_pi blocks: 19; sense clusters: 5; inflected forms: kiriyaṃ, kiriyā_

#### cluster (1) — top co-lemma: **kammavipāka** (cohesion 0.75, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammavipāka | 0.91 | 16 | 16 |
| nākusala | 0.91 | 16 | 16 |
| abyākata | 0.26 | 98 | 15 |

#### cluster (2) — top co-lemma: **diṭṭhadhammasukhavihāra** (cohesion 0.64, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhadhammasukhavihāra | 0.48 | 6 | 6 |
| sabbasa | 0.23 | 16 | 4 |
| samatikkamma | 0.19 | 12 | 3 |

#### cluster (3) — top co-lemma: **kusalākusala** (cohesion 0.56, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusala | 0.33 | 11 | 5 |
| arūpāvacara | 0.17 | 88 | 9 |

#### cluster (4) — top co-lemma: **manoviññāṇadhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manoviññāṇadhātu | 0.22 | 27 | 5 |

#### cluster (5) — top co-lemma: **abyākatamūla** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatamūla | 0.18 | 3 | 2 |

### yañca

_pi blocks: 19; sense clusters: 5; inflected forms: yañca_

#### cluster (1) — top co-lemma: **dhammāyatanapariyāpanna** (cohesion 0.90, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammāyatanapariyāpanna | 0.52 | 8 | 7 |
| appaṭigha | 0.28 | 24 | 6 |
| anidassana | 0.16 | 55 | 6 |

#### cluster (2) — top co-lemma: **kusalākusala** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusala | 0.33 | 11 | 5 |
| kamma | 0.19 | 86 | 10 |

#### cluster (3) — top co-lemma: **anidassanaappaṭigha** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anidassanaappaṭigha | 0.26 | 4 | 3 |
| tika | 0.18 | 3 | 2 |

#### cluster (4) — top co-lemma: **uppādina** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppādina | 0.18 | 3 | 2 |

#### cluster (5) — top co-lemma: **tīsu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīsu | 0.17 | 77 | 8 |
| bhūmīsu | 0.16 | 79 | 8 |

### vīriyārambha

_pi blocks: 19; sense clusters: 1; inflected forms: vīriyārambho_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 0.91 | 16 | 16 |
| ussāha | 0.91 | 16 | 16 |
| uyyāma | 0.91 | 16 | 16 |
| dhiti | 0.91 | 16 | 16 |
| nikkama | 0.91 | 16 | 16 |
| ussoḷhī | 0.91 | 16 | 16 |
| dhurasampaggāha | 0.91 | 16 | 16 |
| asithilaparakkamata | 0.91 | 16 | 16 |
| parakkama | 0.91 | 16 | 16 |
| vāyāma | 0.91 | 16 | 16 |

### kāyaviññāṇa

_pi blocks: 18; sense clusters: 7; inflected forms: kāyaviññāṇassa, kāyaviññāṇaṃ_

#### cluster (1) — top co-lemma: **kāyasamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassaja | 0.45 | 13 | 7 |

#### cluster (2) — top co-lemma: **sotaviññāṇa** (cohesion 0.80, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotaviññāṇa | 0.33 | 6 | 4 |
| ghānaviññāṇa | 0.33 | 6 | 4 |
| jivhāviññāṇa | 0.33 | 6 | 4 |
| cakkhuviññāṇa | 0.23 | 17 | 4 |

#### cluster (3) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.31 | 21 | 6 |

#### cluster (4) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.29 | 24 | 6 |

#### cluster (5) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.23 | 17 | 4 |

#### cluster (6) — top co-lemma: **dukkhasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkhasahagata | 0.20 | 2 | 2 |

#### cluster (7) — top co-lemma: **kāyasamphassa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassa | 0.19 | 13 | 3 |

### sanidassana

_pi blocks: 18; sense clusters: 2; inflected forms: sanidassanamhi, sanidassanaṃ, sanidassanā_

#### cluster (1) — top co-lemma: **cakkhuṃ** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhuṃ | 0.42 | 6 | 5 |

#### cluster (2) — top co-lemma: **ātapa** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ātapa | 0.36 | 4 | 4 |
| mañjiṭṭhaka | 0.36 | 4 | 4 |
| soḷasaṃsa | 0.36 | 4 | 4 |
| maṇisaṅkhamuttāveḷuriya | 0.36 | 4 | 4 |
| ādāsamaṇḍala | 0.36 | 4 | 4 |
| vaṭṭa | 0.36 | 4 | 4 |
| dhūma | 0.36 | 4 | 4 |
| ambaṅkuravaṇṇa | 0.36 | 4 | 4 |
| chaḷaṃsa | 0.36 | 4 | 4 |

### somanassasahagata

_pi blocks: 18; sense clusters: 5; inflected forms: somanassasahagataṃ, somanassasahagatā_

#### cluster (1) — top co-lemma: **dhammārammaṇa** (cohesion 0.93, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammārammaṇa | 0.55 | 26 | 12 |
| panārabbha | 0.50 | 30 | 12 |
| rūpārammaṇa | 0.46 | 34 | 12 |
| uppanna | 0.42 | 49 | 14 |

#### cluster (2) — top co-lemma: **sasaṅkhāra** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.47 | 12 | 7 |
| ñāṇavippayutta | 0.38 | 8 | 5 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.46 | 8 | 6 |

#### cluster (4) — top co-lemma: **somanassindriya** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassindriya | 0.32 | 19 | 6 |
| pīti | 0.31 | 33 | 8 |

#### cluster (5) — top co-lemma: **manoviññāṇadhātu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manoviññāṇadhātu | 0.31 | 27 | 7 |

### abyāpāda

_pi blocks: 18; sense clusters: 1; inflected forms: abyāpādo_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.71 | 13 | 11 |
| cittapāguññata | 0.71 | 13 | 11 |
| kāyujukata | 0.71 | 13 | 11 |
| cittujukata | 0.71 | 13 | 11 |
| cittakammaññata | 0.71 | 13 | 11 |
| kāyamuduta | 0.71 | 13 | 11 |
| kāyapassaddhi | 0.71 | 13 | 11 |
| kāyapāguññata | 0.71 | 13 | 11 |
| kāyalahuta | 0.71 | 13 | 11 |
| cittamuduta | 0.71 | 13 | 11 |

### anabhijjha

_pi blocks: 18; sense clusters: 1; inflected forms: anabhijjhā_

#### cluster (1) — top co-lemma: **alobha** (cohesion 0.92, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| alobha | 0.72 | 32 | 18 |
| kāyalahuta | 0.71 | 13 | 11 |
| cittamuduta | 0.71 | 13 | 11 |
| cittalahuta | 0.71 | 13 | 11 |
| cittapāguññata | 0.71 | 13 | 11 |
| kāyujukata | 0.71 | 13 | 11 |
| cittujukata | 0.71 | 13 | 11 |
| cittakammaññata | 0.71 | 13 | 11 |
| kāyapassaddhi | 0.71 | 13 | 11 |
| kāyapāguññata | 0.71 | 13 | 11 |

### micchāsamādhi

_pi blocks: 18; sense clusters: 1; inflected forms: micchāsamādhi_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.79, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.73 | 15 | 12 |
| anottappabala | 0.73 | 15 | 12 |
| micchāsaṅkappa | 0.71 | 16 | 12 |
| micchāvāyāma | 0.67 | 18 | 12 |
| ahirika | 0.65 | 19 | 12 |
| anottappa | 0.63 | 20 | 12 |
| samādhibala | 0.54 | 49 | 18 |
| samatha | 0.51 | 53 | 18 |
| abhijjha | 0.50 | 14 | 8 |
| samādhindriya | 0.42 | 67 | 18 |

### micchāvāyāma

_pi blocks: 18; sense clusters: 1; inflected forms: micchāvāyāmo_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.85 | 15 | 14 |
| anottappabala | 0.85 | 15 | 14 |
| micchāsaṅkappa | 0.82 | 16 | 14 |
| ahirika | 0.76 | 19 | 14 |
| anottappa | 0.74 | 20 | 14 |
| micchāsamādhi | 0.67 | 18 | 12 |
| vīriyabala | 0.59 | 43 | 18 |
| abhijjha | 0.50 | 14 | 8 |
| paggāha | 0.48 | 44 | 15 |
| vīriyindriya | 0.46 | 61 | 18 |

### akusalamūla

_pi blocks: 18; sense clusters: 1; inflected forms: akusalamūlaṃ, akusalamūlāni_

#### cluster (1) — top co-lemma: **aññāṇa** (cohesion 0.86, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññāṇa | 0.62 | 8 | 8 |
| adassana | 0.62 | 8 | 8 |
| avijjālaṅgī | 0.62 | 8 | 8 |
| asampajañña | 0.56 | 7 | 7 |
| avijja | 0.52 | 9 | 7 |
| apaccakkhakamma | 0.50 | 6 | 6 |
| anabhisamaya | 0.50 | 6 | 6 |
| avijjāpariyuṭṭha | 0.50 | 6 | 6 |
| avijjogha | 0.50 | 6 | 6 |
| sammoha | 0.50 | 6 | 6 |

### phusana

_pi blocks: 18; sense clusters: 1; inflected forms: phusanā_

#### cluster (1) — top co-lemma: **saṃphusana** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃphusana | 1.00 | 18 | 18 |
| saṃphusitatta | 1.00 | 18 | 18 |
| phassa | 0.11 | 297 | 18 |
| ayaṃ | 0.11 | 304 | 18 |

### saṃphusana

_pi blocks: 18; sense clusters: 1; inflected forms: saṃphusanā_

#### cluster (1) — top co-lemma: **phusana** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phusana | 1.00 | 18 | 18 |
| saṃphusitatta | 1.00 | 18 | 18 |
| phassa | 0.11 | 297 | 18 |
| ayaṃ | 0.11 | 304 | 18 |

### saṃphusitatta

_pi blocks: 18; sense clusters: 1; inflected forms: saṃphusitattaṃ_

#### cluster (1) — top co-lemma: **saṃphusana** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃphusana | 1.00 | 18 | 18 |
| phusana | 1.00 | 18 | 18 |
| phassa | 0.11 | 297 | 18 |
| ayaṃ | 0.11 | 304 | 18 |

### tajjāmanoviññāṇadhātusamphassaja

_pi blocks: 18; sense clusters: 4; inflected forms: tajjāmanoviññāṇadhātusamphassajaṃ, tajjāmanoviññāṇadhātusamphassajā_

#### cluster (1) — top co-lemma: **sañcetana** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañcetana | 0.36 | 10 | 5 |
| cetayitatta | 0.36 | 10 | 5 |

#### cluster (2) — top co-lemma: **sañjānitatta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañjānitatta | 0.34 | 11 | 5 |
| sañjānana | 0.34 | 11 | 5 |

#### cluster (3) — top co-lemma: **cetosamphassaja** (cohesion 0.94, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cetosamphassaja | 0.30 | 35 | 8 |
| cetasika | 0.29 | 38 | 8 |
| vedayita | 0.27 | 41 | 8 |
| sāta | 0.26 | 35 | 7 |

#### cluster (4) — top co-lemma: **nāsāta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nāsāta | 0.18 | 15 | 3 |
| adukkhamasukha | 0.16 | 19 | 3 |

### āsava

_pi blocks: 17; sense clusters: 6; inflected forms: āsave, āsavo, āsavā, āsavānaṃ_

#### cluster (1) — top co-lemma: **āsavasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavasampayutta | 0.38 | 9 | 5 |

#### cluster (2) — top co-lemma: **avijjāsava** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avijjāsava | 0.38 | 4 | 4 |
| kāmāsava | 0.29 | 4 | 3 |
| diṭṭhāsava | 0.29 | 4 | 3 |
| bhavāsava | 0.29 | 4 | 3 |

#### cluster (3) — top co-lemma: **āsavātipi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavātipi | 0.21 | 2 | 2 |
| cātipi | 0.12 | 16 | 2 |

#### cluster (4) — top co-lemma: **sāsava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.18 | 39 | 5 |

#### cluster (5) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.16 | 47 | 5 |

#### cluster (6) — top co-lemma: **vijja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vijja | 0.10 | 3 | 1 |

### cakkhuviññāṇa

_pi blocks: 17; sense clusters: 5; inflected forms: cakkhuviññāṇassa, cakkhuviññāṇaṃ_

#### cluster (1) — top co-lemma: **cakkhusamphassaja** (cohesion 0.78, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassaja | 0.58 | 7 | 7 |
| sañña | 0.19 | 80 | 9 |

#### cluster (2) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.32 | 21 | 6 |

#### cluster (3) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.29 | 24 | 6 |

#### cluster (4) — top co-lemma: **sotaviññāṇa** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotaviññāṇa | 0.26 | 6 | 3 |
| ghānaviññāṇa | 0.26 | 6 | 3 |
| jivhāviññāṇa | 0.26 | 6 | 3 |
| kāyaviññāṇa | 0.23 | 18 | 4 |

#### cluster (5) — top co-lemma: **cakkhusamphassa** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassa | 0.20 | 13 | 3 |
| cakkhuṃ | 0.17 | 6 | 2 |

### diṭṭhisaṃyojana

_pi blocks: 17; sense clusters: 1; inflected forms: diṭṭhisaṃyojanaṃ, diṭṭhisaṃyojanena_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 0.90 | 14 | 14 |
| diṭṭhivisūkāyika | 0.90 | 14 | 14 |
| abhinivesa | 0.90 | 14 | 14 |
| gāha | 0.90 | 14 | 14 |
| diṭṭhigahana | 0.90 | 14 | 14 |
| titthāyatana | 0.90 | 14 | 14 |
| micchatta | 0.90 | 14 | 14 |
| diṭṭhivipphandita | 0.90 | 14 | 14 |
| diṭṭhikantāra | 0.90 | 14 | 14 |
| kummagga | 0.90 | 14 | 14 |

### hirī

_pi blocks: 17; sense clusters: 1; inflected forms: hirī_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.73 | 13 | 11 |
| cittapāguññata | 0.73 | 13 | 11 |
| kāyujukata | 0.73 | 13 | 11 |
| cittujukata | 0.73 | 13 | 11 |
| cittakammaññata | 0.73 | 13 | 11 |
| kāyamuduta | 0.73 | 13 | 11 |
| kāyapassaddhi | 0.73 | 13 | 11 |
| kāyapāguññata | 0.73 | 13 | 11 |
| kāyalahuta | 0.73 | 13 | 11 |
| cittamuduta | 0.73 | 13 | 11 |

### vīriya

_pi blocks: 17; sense clusters: 1; inflected forms: vīriyaṃ_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 0.97 | 16 | 16 |
| ussāha | 0.97 | 16 | 16 |
| uyyāma | 0.97 | 16 | 16 |
| dhiti | 0.97 | 16 | 16 |
| nikkama | 0.97 | 16 | 16 |
| ussoḷhī | 0.97 | 16 | 16 |
| dhurasampaggāha | 0.97 | 16 | 16 |
| asithilaparakkamata | 0.97 | 16 | 16 |
| parakkama | 0.97 | 16 | 16 |
| vāyāma | 0.97 | 16 | 16 |

### phoṭṭhabbārammaṇa

_pi blocks: 17; sense clusters: 3; inflected forms: phoṭṭhabbārammaṇaṃ, phoṭṭhabbārammaṇo, phoṭṭhabbārammaṇā_

#### cluster (1) — top co-lemma: **saddārammaṇa** (cohesion 0.81, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saddārammaṇa | 0.77 | 14 | 12 |
| rasārammaṇa | 0.77 | 14 | 12 |
| gandhārammaṇa | 0.77 | 14 | 12 |
| panārabbha | 0.55 | 30 | 13 |
| rūpārammaṇa | 0.55 | 34 | 14 |
| dhammārammaṇa | 0.47 | 26 | 10 |
| uppanna | 0.45 | 49 | 15 |

#### cluster (2) — top co-lemma: **upekkhindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhindriya | 0.43 | 20 | 8 |

#### cluster (3) — top co-lemma: **ahirikabala** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.38 | 15 | 6 |
| anottappabala | 0.38 | 15 | 6 |

### anikkhittachandata

_pi blocks: 17; sense clusters: 1; inflected forms: anikkhittachandatā_

#### cluster (1) — top co-lemma: **anikkhittadhurata** (cohesion 0.99, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anikkhittadhurata | 1.00 | 17 | 17 |
| parakkama | 0.97 | 16 | 16 |
| vāyāma | 0.97 | 16 | 16 |
| thāma | 0.97 | 16 | 16 |
| ussāha | 0.97 | 16 | 16 |
| uyyāma | 0.97 | 16 | 16 |
| dhiti | 0.97 | 16 | 16 |
| nikkama | 0.97 | 16 | 16 |
| dhurasampaggāha | 0.97 | 16 | 16 |
| asithilaparakkamata | 0.97 | 16 | 16 |

### anikkhittadhurata

_pi blocks: 17; sense clusters: 1; inflected forms: anikkhittadhuratā_

#### cluster (1) — top co-lemma: **anikkhittachandata** (cohesion 0.99, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anikkhittachandata | 1.00 | 17 | 17 |
| parakkama | 0.97 | 16 | 16 |
| vāyāma | 0.97 | 16 | 16 |
| thāma | 0.97 | 16 | 16 |
| ussāha | 0.97 | 16 | 16 |
| uyyāma | 0.97 | 16 | 16 |
| dhiti | 0.97 | 16 | 16 |
| nikkama | 0.97 | 16 | 16 |
| dhurasampaggāha | 0.97 | 16 | 16 |
| asithilaparakkamata | 0.97 | 16 | 16 |

### domanassasahagatacittuppāda

_pi blocks: 17; sense clusters: 7; inflected forms: domanassasahagatacittuppādā_

#### cluster (1) — top co-lemma: **siya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| siya | 0.55 | 16 | 9 |

#### cluster (2) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.52 | 10 | 7 |

#### cluster (3) — top co-lemma: **uddhaccasahagata** (cohesion 0.58, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.41 | 27 | 9 |
| cittuppāda | 0.35 | 40 | 10 |
| vicikicchāsahagata | 0.33 | 26 | 7 |

#### cluster (4) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.37 | 10 | 5 |

#### cluster (5) — top co-lemma: **etthuppanna** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| etthuppanna | 0.36 | 27 | 8 |
| moha | 0.32 | 8 | 4 |

#### cluster (6) — top co-lemma: **lobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagatacittuppāda | 0.29 | 4 | 3 |

#### cluster (7) — top co-lemma: **bhāvana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvana | 0.19 | 26 | 4 |

### siya

_pi blocks: 16; sense clusters: 5; inflected forms: siyā_

#### cluster (1) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 0.55, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.55 | 17 | 9 |
| cittuppāda | 0.29 | 40 | 8 |

#### cluster (2) — top co-lemma: **anārammaṇa** (cohesion 0.75, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anārammaṇa | 0.33 | 8 | 4 |
| rūpāvacaratikacatukkajjhāna | 0.32 | 9 | 4 |
| kiriyāhetukamanoviññāṇadhātu | 0.30 | 4 | 3 |
| ākāsānañcāyatana | 0.26 | 7 | 3 |
| ākiñcaññāyatana | 0.26 | 7 | 3 |

#### cluster (3) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.31 | 10 | 4 |

#### cluster (4) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.31 | 10 | 4 |

#### cluster (5) — top co-lemma: **sabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabba | 0.27 | 14 | 4 |

### upādāna

_pi blocks: 16; sense clusters: 6; inflected forms: upādāne, upādānā, upādānāni_

#### cluster (1) — top co-lemma: **upādānasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānasampayutta | 0.40 | 9 | 5 |

#### cluster (2) — top co-lemma: **attavādupāda** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| attavādupāda | 0.40 | 4 | 4 |
| sīlabbatupāda | 0.30 | 4 | 3 |
| kāmupāda | 0.30 | 4 | 3 |
| diṭṭhupāda | 0.30 | 4 | 3 |

#### cluster (3) — top co-lemma: **upādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādāniya | 0.37 | 11 | 5 |

#### cluster (4) — top co-lemma: **upādānātipi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānātipi | 0.22 | 2 | 2 |
| cātipi | 0.12 | 16 | 2 |

#### cluster (5) — top co-lemma: **tāneva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tāneva | 0.18 | 6 | 2 |

#### cluster (6) — top co-lemma: **avasesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesa | 0.13 | 47 | 4 |

### sabbasa

_pi blocks: 16; sense clusters: 3; inflected forms: sabbaso_

#### cluster (1) — top co-lemma: **samatikkamma** (cohesion 0.70, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| samatikkamma | 0.86 | 12 | 12 |
| arūpūpapattiya | 0.86 | 12 | 12 |
| sukha | 0.40 | 64 | 16 |

#### cluster (2) — top co-lemma: **viññāṇañcāyatanasaññāsahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇañcāyatanasaññāsahagata | 0.40 | 4 | 4 |

#### cluster (3) — top co-lemma: **amanasikāra** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| amanasikāra | 0.40 | 4 | 4 |
| nānattasañña | 0.40 | 4 | 4 |
| samatikkama | 0.40 | 4 | 4 |
| ākāsānañcāyatanasaññāsahagata | 0.40 | 4 | 4 |
| paṭighasañña | 0.40 | 4 | 4 |
| rūpasañña | 0.40 | 4 | 4 |

### caturaṅgika

_pi blocks: 16; sense clusters: 2; inflected forms: caturaṅgikaṃ, caturaṅgiko_

#### cluster (1) — top co-lemma: **bala** (cohesion 0.89, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bala | 0.74 | 27 | 16 |
| dvāyatana | 0.67 | 32 | 16 |
| ekaṃ | 0.64 | 34 | 16 |
| ekā | 0.63 | 35 | 16 |
| dhātuya | 0.63 | 35 | 16 |
| dhammadhātu | 0.60 | 37 | 16 |
| aṭṭhindriya | 0.59 | 11 | 8 |
| khandha | 0.59 | 38 | 16 |
| dhammāyatana | 0.58 | 39 | 16 |

#### cluster (2) — top co-lemma: **duvaṅgika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| duvaṅgika | 0.48 | 5 | 5 |

### hiribala

_pi blocks: 16; sense clusters: 1; inflected forms: hiribalaṃ_

#### cluster (1) — top co-lemma: **ottappabala** (cohesion 0.97, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.81 | 16 | 13 |
| kāyalahuta | 0.76 | 13 | 11 |
| cittamuduta | 0.76 | 13 | 11 |
| cittalahuta | 0.76 | 13 | 11 |
| cittapāguññata | 0.76 | 13 | 11 |
| kāyujukata | 0.76 | 13 | 11 |
| cittujukata | 0.76 | 13 | 11 |
| cittakammaññata | 0.76 | 13 | 11 |
| kāyapassaddhi | 0.76 | 13 | 11 |
| kāyapāguññata | 0.76 | 13 | 11 |

### ottappabala

_pi blocks: 16; sense clusters: 1; inflected forms: ottappabalaṃ_

#### cluster (1) — top co-lemma: **hiribala** (cohesion 0.97, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hiribala | 0.81 | 16 | 13 |
| kāyalahuta | 0.76 | 13 | 11 |
| cittamuduta | 0.76 | 13 | 11 |
| cittalahuta | 0.76 | 13 | 11 |
| cittapāguññata | 0.76 | 13 | 11 |
| kāyujukata | 0.76 | 13 | 11 |
| cittujukata | 0.76 | 13 | 11 |
| cittakammaññata | 0.76 | 13 | 11 |
| kāyapassaddhi | 0.76 | 13 | 11 |
| kāyapāguññata | 0.76 | 13 | 11 |

### kāmāvacarakusalata

_pi blocks: 16; sense clusters: 4; inflected forms: kāmāvacarakusalato_

#### cluster (1) — top co-lemma: **kāmāvacarakusala** (cohesion 0.62, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakusala | 0.72 | 20 | 13 |
| vipākata | 0.64 | 34 | 16 |
| somanassasahagatacittuppāda | 0.61 | 7 | 7 |
| pañca | 0.48 | 13 | 7 |
| etthuppanna | 0.42 | 27 | 9 |

#### cluster (2) — top co-lemma: **upekkhāsahagatacittuppāda** (cohesion 0.71, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagatacittuppāda | 0.55 | 6 | 6 |
| āruppa | 0.48 | 9 | 6 |

#### cluster (3) — top co-lemma: **rūpāvacaratikacatukkajjhāna** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacaratikacatukkajjhāna | 0.48 | 9 | 6 |
| lokuttaratikacatukkajjhāna | 0.38 | 5 | 4 |

#### cluster (4) — top co-lemma: **lokuttaradukatikajjhāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lokuttaradukatikajjhāna | 0.32 | 3 | 3 |

### micchāsaṅkappa

_pi blocks: 16; sense clusters: 1; inflected forms: micchāsaṅkappo_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.87, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.90 | 15 | 14 |
| anottappabala | 0.90 | 15 | 14 |
| micchāvāyāma | 0.82 | 18 | 14 |
| ahirika | 0.80 | 19 | 14 |
| anottappa | 0.78 | 20 | 14 |
| micchāsamādhi | 0.71 | 18 | 12 |
| abhijjha | 0.53 | 14 | 8 |
| vīriyabala | 0.47 | 43 | 14 |
| paggāha | 0.47 | 44 | 14 |
| vitakka | 0.43 | 59 | 16 |

### asithilaparakkamata

_pi blocks: 16; sense clusters: 1; inflected forms: asithilaparakkamatā_

#### cluster (1) — top co-lemma: **ussāha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| thāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### cātipi

_pi blocks: 16; sense clusters: 8; inflected forms: cātipi_

#### cluster (1) — top co-lemma: **vattabba** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattabba | 0.59 | 38 | 16 |
| avasesa | 0.38 | 47 | 12 |
| ṭhapetva | 0.21 | 137 | 16 |

#### cluster (2) — top co-lemma: **kilesātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesātipi | 0.32 | 3 | 3 |

#### cluster (3) — top co-lemma: **hetūtipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hetūtipi | 0.22 | 2 | 2 |

#### cluster (4) — top co-lemma: **āsavātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavātipi | 0.22 | 2 | 2 |

#### cluster (5) — top co-lemma: **saṃyojanātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanātipi | 0.22 | 2 | 2 |

#### cluster (6) — top co-lemma: **ganthātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthātipi | 0.22 | 2 | 2 |

#### cluster (7) — top co-lemma: **nīvaraṇātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇātipi | 0.22 | 2 | 2 |

#### cluster (8) — top co-lemma: **upādānātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānātipi | 0.22 | 2 | 2 |

### dhiti

_pi blocks: 16; sense clusters: 1; inflected forms: dhiti_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 1.00 | 16 | 16 |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### dhurasampaggāha

_pi blocks: 16; sense clusters: 1; inflected forms: dhurasampaggāho_

#### cluster (1) — top co-lemma: **ussāha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| thāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### kammavipāka

_pi blocks: 16; sense clusters: 5; inflected forms: kammavipākaṃ, kammavipākā_

#### cluster (1) — top co-lemma: **nākusala** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nākusala | 1.00 | 16 | 16 |
| kiriya | 0.91 | 19 | 16 |
| abyākata | 0.21 | 98 | 12 |

#### cluster (2) — top co-lemma: **diṭṭhadhammasukhavihāra** (cohesion 0.64, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhadhammasukhavihāra | 0.55 | 6 | 6 |
| sabbasa | 0.25 | 16 | 4 |
| samatikkamma | 0.21 | 12 | 3 |

#### cluster (3) — top co-lemma: **kusalākusala** (cohesion 0.56, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusala | 0.37 | 11 | 5 |
| arūpāvacara | 0.17 | 88 | 9 |

#### cluster (4) — top co-lemma: **abyākatamūla** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatamūla | 0.21 | 3 | 2 |

#### cluster (5) — top co-lemma: **panārabbha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panārabbha | 0.17 | 30 | 4 |

### kusalamūla

_pi blocks: 16; sense clusters: 2; inflected forms: kusalamūlaṃ, kusalamūlāni_

#### cluster (1) — top co-lemma: **asārajjitatta** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asārajjitatta | 0.61 | 7 | 7 |
| alubbhana | 0.61 | 7 | 7 |
| alubbhitatta | 0.61 | 7 | 7 |
| asārajjana | 0.61 | 7 | 7 |
| asārāga | 0.61 | 7 | 7 |
| anabhijjha | 0.41 | 18 | 7 |

#### cluster (2) — top co-lemma: **abyāpajja** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyāpajja | 0.61 | 7 | 7 |
| adussitatta | 0.61 | 7 | 7 |
| adussana | 0.61 | 7 | 7 |
| abyāpāda | 0.41 | 18 | 7 |

### nikkama

_pi blocks: 16; sense clusters: 1; inflected forms: nikkamo_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 1.00 | 16 | 16 |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### nākusala

_pi blocks: 16; sense clusters: 5; inflected forms: nākusalaṃ, nākusalā_

#### cluster (1) — top co-lemma: **kammavipāka** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammavipāka | 1.00 | 16 | 16 |
| kiriya | 0.91 | 19 | 16 |
| abyākata | 0.21 | 98 | 12 |

#### cluster (2) — top co-lemma: **diṭṭhadhammasukhavihāra** (cohesion 0.64, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhadhammasukhavihāra | 0.55 | 6 | 6 |
| sabbasa | 0.25 | 16 | 4 |
| samatikkamma | 0.21 | 12 | 3 |

#### cluster (3) — top co-lemma: **kusalākusala** (cohesion 0.56, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalākusala | 0.37 | 11 | 5 |
| arūpāvacara | 0.17 | 88 | 9 |

#### cluster (4) — top co-lemma: **abyākatamūla** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatamūla | 0.21 | 3 | 2 |

#### cluster (5) — top co-lemma: **panārabbha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| panārabbha | 0.17 | 30 | 4 |

### parakkama

_pi blocks: 16; sense clusters: 1; inflected forms: parakkamo_

#### cluster (1) — top co-lemma: **ussāha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| thāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### thāma

_pi blocks: 16; sense clusters: 1; inflected forms: thāmo_

#### cluster (1) — top co-lemma: **ussāha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### ussoḷhī

_pi blocks: 16; sense clusters: 1; inflected forms: ussoḷhī_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 1.00 | 16 | 16 |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### ussāha

_pi blocks: 16; sense clusters: 1; inflected forms: ussāho_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### uyyāma

_pi blocks: 16; sense clusters: 1; inflected forms: uyyāmo_

#### cluster (1) — top co-lemma: **thāma** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thāma | 1.00 | 16 | 16 |
| ussāha | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| vāyāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### vāyāma

_pi blocks: 16; sense clusters: 1; inflected forms: vāyāmo_

#### cluster (1) — top co-lemma: **ussāha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ussāha | 1.00 | 16 | 16 |
| uyyāma | 1.00 | 16 | 16 |
| dhiti | 1.00 | 16 | 16 |
| nikkama | 1.00 | 16 | 16 |
| ussoḷhī | 1.00 | 16 | 16 |
| dhurasampaggāha | 1.00 | 16 | 16 |
| asithilaparakkamata | 1.00 | 16 | 16 |
| parakkama | 1.00 | 16 | 16 |
| thāma | 1.00 | 16 | 16 |
| anikkhittadhurata | 0.97 | 17 | 16 |

### oḷārika

_pi blocks: 15; sense clusters: 4; inflected forms: oḷārikaṃ_

#### cluster (1) — top co-lemma: **phoṭṭhabbāyatana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbāyatana | 0.20 | 87 | 10 |

#### cluster (2) — top co-lemma: **rasāyatana** (cohesion 0.71, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasāyatana | 0.18 | 61 | 7 |
| gandhāyatana | 0.14 | 55 | 5 |

#### cluster (3) — top co-lemma: **anupādiṇṇupādāniya** (cohesion 0.62, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇupādāniya | 0.18 | 19 | 3 |
| upādiṇṇupādāniya | 0.17 | 20 | 3 |
| anupādiṇṇa | 0.16 | 23 | 3 |
| upādiṇṇa | 0.15 | 26 | 3 |
| sukhuma | 0.14 | 14 | 2 |
| dūra | 0.14 | 14 | 2 |

#### cluster (4) — top co-lemma: **indriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| indriya | 0.16 | 36 | 4 |

### ahirikabala

_pi blocks: 15; sense clusters: 2; inflected forms: ahirikabalaṃ_

#### cluster (1) — top co-lemma: **anottappabala** (cohesion 0.88, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anottappabala | 0.93 | 15 | 14 |
| micchāsaṅkappa | 0.90 | 16 | 14 |
| micchāvāyāma | 0.85 | 18 | 14 |
| ahirika | 0.82 | 19 | 14 |
| anottappa | 0.80 | 20 | 14 |
| micchāsamādhi | 0.73 | 18 | 12 |
| abhijjha | 0.55 | 14 | 8 |
| vīriyabala | 0.48 | 43 | 14 |
| paggāha | 0.47 | 44 | 14 |

#### cluster (2) — top co-lemma: **rasārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.41 | 14 | 6 |

### anottappabala

_pi blocks: 15; sense clusters: 2; inflected forms: anottappabalaṃ_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.88, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.93 | 15 | 14 |
| micchāsaṅkappa | 0.90 | 16 | 14 |
| micchāvāyāma | 0.85 | 18 | 14 |
| ahirika | 0.82 | 19 | 14 |
| anottappa | 0.80 | 20 | 14 |
| micchāsamādhi | 0.73 | 18 | 12 |
| abhijjha | 0.55 | 14 | 8 |
| vīriyabala | 0.48 | 43 | 14 |
| paggāha | 0.47 | 44 | 14 |

#### cluster (2) — top co-lemma: **rasārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.41 | 14 | 6 |

### nāsāta

_pi blocks: 15; sense clusters: 5; inflected forms: nāsātaṃ_

#### cluster (1) — top co-lemma: **adukkhamasukha** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| adukkhamasukha | 0.88 | 19 | 15 |
| cetosamphassaja | 0.60 | 35 | 15 |
| sāta | 0.60 | 35 | 15 |
| cetasika | 0.57 | 38 | 15 |
| vedayita | 0.54 | 41 | 15 |
| vedana | 0.22 | 120 | 15 |

#### cluster (2) — top co-lemma: **upekkhindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhindriya | 0.29 | 20 | 5 |

#### cluster (3) — top co-lemma: **upekkha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkha | 0.24 | 26 | 5 |

#### cluster (4) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.18 | 18 | 3 |

#### cluster (5) — top co-lemma: **caturaṅgika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| caturaṅgika | 0.13 | 16 | 2 |

### upacitatta

_pi blocks: 15; sense clusters: 4; inflected forms: upacitattā_

#### cluster (1) — top co-lemma: **rūpārammaṇa** (cohesion 0.69, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpārammaṇa | 0.33 | 34 | 8 |
| upekkhindriya | 0.29 | 20 | 5 |
| upekkhāsahagata | 0.29 | 41 | 8 |
| uppanna | 0.28 | 49 | 9 |
| panārabbha | 0.27 | 30 | 6 |

#### cluster (2) — top co-lemma: **kamma** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kamma | 0.30 | 86 | 15 |
| abyākata | 0.27 | 98 | 15 |

#### cluster (3) — top co-lemma: **arūpūpapattiya** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.30 | 12 | 4 |
| sabbasa | 0.26 | 16 | 4 |

#### cluster (4) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.25 | 17 | 4 |

### vippayutta

_pi blocks: 15; sense clusters: 8; inflected forms: vippayuttā_

#### cluster (1) — top co-lemma: **rūpakkhandha** (cohesion 0.81, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpakkhandha | 0.33 | 28 | 7 |
| sāsava | 0.26 | 39 | 7 |
| kusalākusalābyākata | 0.18 | 41 | 5 |

#### cluster (2) — top co-lemma: **parāmāsavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsavippayutta | 0.17 | 8 | 2 |

#### cluster (3) — top co-lemma: **sabbañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbañca | 0.17 | 79 | 8 |

#### cluster (4) — top co-lemma: **āsavavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavavippayutta | 0.17 | 9 | 2 |

#### cluster (5) — top co-lemma: **saṃyojanavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanavippayutta | 0.17 | 9 | 2 |

#### cluster (6) — top co-lemma: **ganthavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthavippayutta | 0.17 | 9 | 2 |

#### cluster (7) — top co-lemma: **nīvaraṇavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇavippayutta | 0.17 | 9 | 2 |

#### cluster (8) — top co-lemma: **upādānavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānavippayutta | 0.17 | 9 | 2 |

### yāpana

_pi blocks: 15; sense clusters: 2; inflected forms: yāpanā, yāpanāya_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 0.97 | 14 | 14 |
| pālana | 0.97 | 14 | 14 |
| vattana | 0.97 | 14 | 14 |
| āyu | 0.97 | 14 | 14 |
| jīvita | 0.97 | 14 | 14 |
| iriyana | 0.97 | 14 | 14 |
| arūpīna | 0.75 | 9 | 9 |
| tesa | 0.65 | 28 | 14 |
| ṭhiti | 0.45 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.50 | 5 | 5 |

### dūra

_pi blocks: 14; sense clusters: 4; inflected forms: dūre_

#### cluster (1) — top co-lemma: **itthindriya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.26 | 48 | 8 |
| purisindriya | 0.16 | 35 | 4 |

#### cluster (2) — top co-lemma: **āpodhātu** (cohesion 0.58, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.20 | 57 | 7 |
| ākāsadhātu | 0.17 | 46 | 5 |
| jarata | 0.15 | 26 | 3 |

#### cluster (3) — top co-lemma: **anupādiṇṇupādāniya** (cohesion 0.50, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇupādāniya | 0.18 | 19 | 3 |
| upādiṇṇupādāniya | 0.18 | 20 | 3 |
| anupādiṇṇa | 0.16 | 23 | 3 |
| upādiṇṇa | 0.15 | 26 | 3 |

#### cluster (4) — top co-lemma: **indriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| indriya | 0.16 | 36 | 4 |

### sukhuma

_pi blocks: 14; sense clusters: 4; inflected forms: sukhumaṃ_

#### cluster (1) — top co-lemma: **itthindriya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| itthindriya | 0.26 | 48 | 8 |
| purisindriya | 0.16 | 35 | 4 |

#### cluster (2) — top co-lemma: **āpodhātu** (cohesion 0.58, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āpodhātu | 0.20 | 57 | 7 |
| ākāsadhātu | 0.17 | 46 | 5 |
| jarata | 0.15 | 26 | 3 |

#### cluster (3) — top co-lemma: **anupādiṇṇupādāniya** (cohesion 0.50, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādiṇṇupādāniya | 0.18 | 19 | 3 |
| upādiṇṇupādāniya | 0.18 | 20 | 3 |
| anupādiṇṇa | 0.16 | 23 | 3 |
| upādiṇṇa | 0.15 | 26 | 3 |

#### cluster (4) — top co-lemma: **indriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| indriya | 0.16 | 36 | 4 |

### ghānāyatana

_pi blocks: 14; sense clusters: 2; inflected forms: ghānāyatanaṃ_

#### cluster (1) — top co-lemma: **jivhāyatana** (cohesion 0.80, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhāyatana | 0.61 | 19 | 10 |
| sotāyatana | 0.53 | 24 | 10 |
| saddāyatana | 0.24 | 44 | 7 |

#### cluster (2) — top co-lemma: **ghānadhātu** (cohesion 0.90, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānadhātu | 0.45 | 8 | 5 |
| ghānindriya | 0.38 | 12 | 5 |
| ghāna | 0.33 | 10 | 4 |
| gandha | 0.33 | 10 | 4 |
| tīra | 0.24 | 20 | 4 |
| orima | 0.24 | 20 | 4 |
| samudda | 0.24 | 20 | 4 |

### phoṭṭhabbadhātu

_pi blocks: 14; sense clusters: 1; inflected forms: phoṭṭhabbadhātu_

#### cluster (1) — top co-lemma: **pathavīdhātu** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pathavīdhātu | 0.61 | 9 | 7 |
| pharusa | 0.44 | 4 | 4 |
| garuka | 0.44 | 4 | 4 |
| saṇha | 0.44 | 4 | 4 |
| lahuka | 0.44 | 4 | 4 |
| muduka | 0.44 | 4 | 4 |
| kakkhaḷa | 0.42 | 5 | 4 |
| tejodhātu | 0.40 | 6 | 4 |
| vāyodhātu | 0.40 | 6 | 4 |
| sukhasamphassa | 0.40 | 6 | 4 |

### sīlabbataparāmāsa

_pi blocks: 14; sense clusters: 3; inflected forms: sīlabbataparāmāsaṃ, sīlabbataparāmāsena, sīlabbataparāmāso_

#### cluster (1) — top co-lemma: **sakkāyadiṭṭhi** (cohesion 0.90, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sakkāyadiṭṭhi | 0.50 | 10 | 6 |
| tīṇi | 0.41 | 20 | 7 |
| saṃyojana | 0.37 | 24 | 7 |
| vicikiccha | 0.36 | 19 | 6 |

#### cluster (2) — top co-lemma: **kāyagantha** (cohesion 0.60, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyagantha | 0.48 | 7 | 5 |
| idaṃsaccābhinivesa | 0.35 | 3 | 3 |

#### cluster (3) — top co-lemma: **suddhi** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suddhi | 0.40 | 6 | 4 |
| sīla | 0.40 | 6 | 4 |
| sīlabbata | 0.40 | 6 | 4 |
| samaṇabrāhmaṇa | 0.35 | 9 | 4 |

### micchādiṭṭhi

_pi blocks: 14; sense clusters: 1; inflected forms: micchādiṭṭhi_

#### cluster (1) — top co-lemma: **sabbāpi** (cohesion 0.93, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbāpi | 0.64 | 8 | 7 |
| diṭṭhikantāra | 0.57 | 14 | 8 |
| kummagga | 0.57 | 14 | 8 |
| micchāpatha | 0.57 | 14 | 8 |
| diṭṭhivisūkāyika | 0.57 | 14 | 8 |
| abhinivesa | 0.57 | 14 | 8 |
| gāha | 0.57 | 14 | 8 |
| diṭṭhigahana | 0.57 | 14 | 8 |
| micchatta | 0.57 | 14 | 8 |
| diṭṭhivipphandita | 0.57 | 14 | 8 |

### abhijjha

_pi blocks: 14; sense clusters: 2; inflected forms: abhijjhā_

#### cluster (1) — top co-lemma: **ahirikabala** (cohesion 0.90, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirikabala | 0.55 | 15 | 8 |
| anottappabala | 0.55 | 15 | 8 |
| micchāsaṅkappa | 0.53 | 16 | 8 |
| micchāvāyāma | 0.50 | 18 | 8 |
| micchāsamādhi | 0.50 | 18 | 8 |
| lobha | 0.49 | 39 | 13 |
| ahirika | 0.48 | 19 | 8 |
| anottappa | 0.47 | 20 | 8 |

#### cluster (2) — top co-lemma: **sārāga** (cohesion 0.60, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sārāga | 0.53 | 5 | 5 |
| saddataṇha | 0.35 | 3 | 3 |

### ottappa

_pi blocks: 14; sense clusters: 1; inflected forms: ottappaṃ_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.81 | 13 | 11 |
| cittapāguññata | 0.81 | 13 | 11 |
| kāyujukata | 0.81 | 13 | 11 |
| cittujukata | 0.81 | 13 | 11 |
| cittakammaññata | 0.81 | 13 | 11 |
| kāyamuduta | 0.81 | 13 | 11 |
| kāyapassaddhi | 0.81 | 13 | 11 |
| kāyapāguññata | 0.81 | 13 | 11 |
| kāyalahuta | 0.81 | 13 | 11 |
| cittamuduta | 0.81 | 13 | 11 |

### sabba

_pi blocks: 14; sense clusters: 3; inflected forms: sabbaṃ, sabbe, sabbo_

#### cluster (1) — top co-lemma: **evaṃ** (cohesion 0.76, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| evaṃ | 0.34 | 21 | 6 |
| rūpasaṅgaha | 0.34 | 21 | 6 |
| sotaviññeyya | 0.29 | 7 | 3 |
| jivhāviññeyya | 0.29 | 7 | 3 |
| kāyaviññeyya | 0.29 | 7 | 3 |
| cakkhuviññeyya | 0.29 | 7 | 3 |
| ghānaviññeyya | 0.29 | 7 | 3 |

#### cluster (2) — top co-lemma: **kiriyāhetukamanoviññāṇadhātu** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kiriyāhetukamanoviññāṇadhātu | 0.33 | 4 | 3 |
| anārammaṇa | 0.27 | 8 | 3 |

#### cluster (3) — top co-lemma: **siya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| siya | 0.27 | 16 | 4 |

### gandhārammaṇa

_pi blocks: 14; sense clusters: 2; inflected forms: gandhārammaṇaṃ, gandhārammaṇo, gandhārammaṇā_

#### cluster (1) — top co-lemma: **rasārammaṇa** (cohesion 0.73, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.86 | 14 | 12 |
| saddārammaṇa | 0.86 | 14 | 12 |
| phoṭṭhabbārammaṇa | 0.77 | 17 | 12 |
| dhammārammaṇa | 0.50 | 26 | 10 |
| rūpārammaṇa | 0.46 | 34 | 11 |
| panārabbha | 0.45 | 30 | 10 |
| ahirikabala | 0.41 | 15 | 6 |
| anottappabala | 0.41 | 15 | 6 |
| micchāsaṅkappa | 0.40 | 16 | 6 |

#### cluster (2) — top co-lemma: **ghānaviññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānaviññāṇa | 0.40 | 6 | 4 |

### kāyakamma

_pi blocks: 14; sense clusters: 3; inflected forms: kāyakammaṃ_

#### cluster (1) — top co-lemma: **manokamma** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manokamma | 1.00 | 14 | 14 |
| vacīkamma | 1.00 | 14 | 14 |
| taṃsamuṭṭha | 1.00 | 14 | 14 |
| tadekaṭṭha | 0.96 | 13 | 13 |
| taṃsampayutta | 0.64 | 30 | 14 |
| tīṇi | 0.59 | 20 | 10 |
| kilesa | 0.54 | 34 | 13 |
| lobha | 0.42 | 39 | 11 |

#### cluster (2) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.44 | 4 | 4 |

#### cluster (3) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.33 | 22 | 6 |

### manokamma

_pi blocks: 14; sense clusters: 3; inflected forms: manokammaṃ_

#### cluster (1) — top co-lemma: **kāyakamma** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyakamma | 1.00 | 14 | 14 |
| vacīkamma | 1.00 | 14 | 14 |
| taṃsamuṭṭha | 1.00 | 14 | 14 |
| tadekaṭṭha | 0.96 | 13 | 13 |
| taṃsampayutta | 0.64 | 30 | 14 |
| tīṇi | 0.59 | 20 | 10 |
| kilesa | 0.54 | 34 | 13 |
| lobha | 0.42 | 39 | 11 |

#### cluster (2) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.44 | 4 | 4 |

#### cluster (3) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.33 | 22 | 6 |

### rasārammaṇa

_pi blocks: 14; sense clusters: 2; inflected forms: rasārammaṇaṃ, rasārammaṇo, rasārammaṇā_

#### cluster (1) — top co-lemma: **gandhārammaṇa** (cohesion 0.73, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandhārammaṇa | 0.86 | 14 | 12 |
| saddārammaṇa | 0.86 | 14 | 12 |
| phoṭṭhabbārammaṇa | 0.77 | 17 | 12 |
| dhammārammaṇa | 0.50 | 26 | 10 |
| rūpārammaṇa | 0.46 | 34 | 11 |
| panārabbha | 0.45 | 30 | 10 |
| ahirikabala | 0.41 | 15 | 6 |
| anottappabala | 0.41 | 15 | 6 |
| micchāsaṅkappa | 0.40 | 16 | 6 |

#### cluster (2) — top co-lemma: **jivhāviññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhāviññāṇa | 0.40 | 6 | 4 |

### saddārammaṇa

_pi blocks: 14; sense clusters: 2; inflected forms: saddārammaṇaṃ, saddārammaṇo, saddārammaṇā_

#### cluster (1) — top co-lemma: **rasārammaṇa** (cohesion 0.73, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasārammaṇa | 0.86 | 14 | 12 |
| gandhārammaṇa | 0.86 | 14 | 12 |
| phoṭṭhabbārammaṇa | 0.77 | 17 | 12 |
| dhammārammaṇa | 0.50 | 26 | 10 |
| rūpārammaṇa | 0.46 | 34 | 11 |
| panārabbha | 0.45 | 30 | 10 |
| ahirikabala | 0.41 | 15 | 6 |
| anottappabala | 0.41 | 15 | 6 |
| micchāsaṅkappa | 0.40 | 16 | 6 |

#### cluster (2) — top co-lemma: **sotaviññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotaviññāṇa | 0.40 | 6 | 4 |

### taṃsamuṭṭha

_pi blocks: 14; sense clusters: 3; inflected forms: taṃsamuṭṭhānaṃ_

#### cluster (1) — top co-lemma: **manokamma** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manokamma | 1.00 | 14 | 14 |
| kāyakamma | 1.00 | 14 | 14 |
| vacīkamma | 1.00 | 14 | 14 |
| tadekaṭṭha | 0.96 | 13 | 13 |
| taṃsampayutta | 0.64 | 30 | 14 |
| tīṇi | 0.59 | 20 | 10 |
| kilesa | 0.54 | 34 | 13 |
| lobha | 0.42 | 39 | 11 |

#### cluster (2) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.44 | 4 | 4 |

#### cluster (3) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.33 | 22 | 6 |

### vacīkamma

_pi blocks: 14; sense clusters: 3; inflected forms: vacīkammaṃ_

#### cluster (1) — top co-lemma: **manokamma** (cohesion 0.85, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manokamma | 1.00 | 14 | 14 |
| kāyakamma | 1.00 | 14 | 14 |
| taṃsamuṭṭha | 1.00 | 14 | 14 |
| tadekaṭṭha | 0.96 | 13 | 13 |
| taṃsampayutta | 0.64 | 30 | 14 |
| tīṇi | 0.59 | 20 | 10 |
| kilesa | 0.54 | 34 | 13 |
| lobha | 0.42 | 39 | 11 |

#### cluster (2) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.44 | 4 | 4 |

#### cluster (3) — top co-lemma: **pahātabba** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabba | 0.33 | 22 | 6 |

### abhinivesa

_pi blocks: 14; sense clusters: 1; inflected forms: abhiniveso_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### cittañca

_pi blocks: 14; sense clusters: 9; inflected forms: cittañca_

#### cluster (1) — top co-lemma: **avasesañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avasesañca | 0.60 | 6 | 6 |

#### cluster (2) — top co-lemma: **acetasika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| acetasika | 0.22 | 4 | 2 |

#### cluster (3) — top co-lemma: **cittasamuṭṭhāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasamuṭṭhāna | 0.21 | 5 | 2 |

#### cluster (4) — top co-lemma: **cittasahabhuna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasahabhuna | 0.21 | 5 | 2 |

#### cluster (5) — top co-lemma: **cittānuparivattina** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittānuparivattina | 0.21 | 5 | 2 |

#### cluster (6) — top co-lemma: **cittasaṃsaṭṭhasamuṭṭhāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasaṃsaṭṭhasamuṭṭhāna | 0.21 | 5 | 2 |

#### cluster (7) — top co-lemma: **cittasaṃsaṭṭhasamuṭṭhānasahabhuna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasaṃsaṭṭhasamuṭṭhānasahabhuna | 0.21 | 5 | 2 |

#### cluster (8) — top co-lemma: **cittasaṃsaṭṭhasamuṭṭhānānuparivattina** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasaṃsaṭṭhasamuṭṭhānānuparivattina | 0.21 | 5 | 2 |

#### cluster (9) — top co-lemma: **dhātu** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātu | 0.15 | 81 | 7 |
| asaṅkhata | 0.14 | 84 | 7 |

### diṭṭhigahana

_pi blocks: 14; sense clusters: 1; inflected forms: diṭṭhigahanaṃ_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### diṭṭhikantāra

_pi blocks: 14; sense clusters: 1; inflected forms: diṭṭhikantāro_

#### cluster (1) — top co-lemma: **diṭṭhivisūkāyika** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### diṭṭhivipphandita

_pi blocks: 14; sense clusters: 1; inflected forms: diṭṭhivipphanditaṃ_

#### cluster (1) — top co-lemma: **diṭṭhivisūkāyika** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### diṭṭhivisūkāyika

_pi blocks: 14; sense clusters: 1; inflected forms: diṭṭhivisūkāyikaṃ_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### gāha

_pi blocks: 14; sense clusters: 1; inflected forms: gāho_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### iriyana

_pi blocks: 14; sense clusters: 2; inflected forms: iriyanā_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 1.00 | 14 | 14 |
| pālana | 1.00 | 14 | 14 |
| vattana | 1.00 | 14 | 14 |
| āyu | 1.00 | 14 | 14 |
| jīvita | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### jīvita

_pi blocks: 14; sense clusters: 2; inflected forms: jīvitaṃ_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 1.00 | 14 | 14 |
| pālana | 1.00 | 14 | 14 |
| vattana | 1.00 | 14 | 14 |
| āyu | 1.00 | 14 | 14 |
| iriyana | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### kummagga

_pi blocks: 14; sense clusters: 1; inflected forms: kummaggo_

#### cluster (1) — top co-lemma: **diṭṭhivisūkāyika** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### micchatta

_pi blocks: 14; sense clusters: 1; inflected forms: micchattaṃ_

#### cluster (1) — top co-lemma: **diṭṭhivisūkāyika** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### micchāpatha

_pi blocks: 14; sense clusters: 1; inflected forms: micchāpatho_

#### cluster (1) — top co-lemma: **diṭṭhivisūkāyika** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| titthāyatana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### pālana

_pi blocks: 14; sense clusters: 2; inflected forms: pālanā_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 1.00 | 14 | 14 |
| vattana | 1.00 | 14 | 14 |
| āyu | 1.00 | 14 | 14 |
| jīvita | 1.00 | 14 | 14 |
| iriyana | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### titthāyatana

_pi blocks: 14; sense clusters: 1; inflected forms: titthāyatanaṃ_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 1.00 | 14 | 14 |
| diṭṭhivisūkāyika | 1.00 | 14 | 14 |
| abhinivesa | 1.00 | 14 | 14 |
| gāha | 1.00 | 14 | 14 |
| diṭṭhigahana | 1.00 | 14 | 14 |
| micchatta | 1.00 | 14 | 14 |
| diṭṭhivipphandita | 1.00 | 14 | 14 |
| diṭṭhikantāra | 1.00 | 14 | 14 |
| kummagga | 1.00 | 14 | 14 |
| diṭṭhisaṃyojana | 0.90 | 17 | 14 |

### vattana

_pi blocks: 14; sense clusters: 2; inflected forms: vattanā_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 1.00 | 14 | 14 |
| pālana | 1.00 | 14 | 14 |
| āyu | 1.00 | 14 | 14 |
| jīvita | 1.00 | 14 | 14 |
| iriyana | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### yapana

_pi blocks: 14; sense clusters: 2; inflected forms: yapanā_

#### cluster (1) — top co-lemma: **pālana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pālana | 1.00 | 14 | 14 |
| vattana | 1.00 | 14 | 14 |
| āyu | 1.00 | 14 | 14 |
| jīvita | 1.00 | 14 | 14 |
| iriyana | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### āyu

_pi blocks: 14; sense clusters: 2; inflected forms: āyu_

#### cluster (1) — top co-lemma: **yapana** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yapana | 1.00 | 14 | 14 |
| pālana | 1.00 | 14 | 14 |
| vattana | 1.00 | 14 | 14 |
| jīvita | 1.00 | 14 | 14 |
| iriyana | 1.00 | 14 | 14 |
| yāpana | 0.97 | 15 | 14 |
| arūpīna | 0.78 | 9 | 9 |
| tesa | 0.67 | 28 | 14 |
| ṭhiti | 0.46 | 47 | 14 |

#### cluster (2) — top co-lemma: **rūpīna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpīna | 0.53 | 5 | 5 |

### cakkhusamphassa

_pi blocks: 13; sense clusters: 3; inflected forms: cakkhusamphassassa, cakkhusamphasso_

#### cluster (1) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.35 | 21 | 6 |

#### cluster (2) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.32 | 24 | 6 |

#### cluster (3) — top co-lemma: **cakkhusamphassaja** (cohesion 0.74, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cakkhusamphassaja | 0.30 | 7 | 3 |
| cakkhuṃ | 0.21 | 6 | 2 |
| cakkhuviññāṇa | 0.20 | 17 | 3 |
| nissa | 0.17 | 10 | 2 |
| uppajja | 0.17 | 10 | 2 |
| uppajji | 0.17 | 10 | 2 |
| uppajjissati | 0.17 | 11 | 2 |
| cakkhudhātu | 0.17 | 11 | 2 |

### kāyasamphassa

_pi blocks: 13; sense clusters: 4; inflected forms: kāyasamphassassa, kāyasamphasso_

#### cluster (1) — top co-lemma: **ghānasamphassa** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānasamphassa | 0.50 | 7 | 5 |
| jivhāsamphassa | 0.50 | 7 | 5 |
| sotasamphassa | 0.50 | 7 | 5 |

#### cluster (2) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.35 | 21 | 6 |

#### cluster (3) — top co-lemma: **ārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ārammaṇa | 0.32 | 24 | 6 |

#### cluster (4) — top co-lemma: **kāyasamphassaja** (cohesion 0.80, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassaja | 0.23 | 13 | 3 |
| kāyaviññāṇa | 0.19 | 18 | 3 |
| uppajja | 0.17 | 10 | 2 |
| uppajji | 0.17 | 10 | 2 |
| nissa | 0.17 | 10 | 2 |

### kāyasamphassaja

_pi blocks: 13; sense clusters: 5; inflected forms: kāyasamphassajaṃ, kāyasamphassajā, kāyasamphassajāya_

#### cluster (1) — top co-lemma: **kāyika** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyika | 0.52 | 10 | 6 |
| asāta | 0.32 | 6 | 3 |
| vedayita | 0.22 | 41 | 6 |
| dukkha | 0.18 | 20 | 3 |

#### cluster (2) — top co-lemma: **kāyaviññāṇa** (cohesion 0.54, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyaviññāṇa | 0.45 | 18 | 7 |
| vedana | 0.20 | 120 | 13 |

#### cluster (3) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.24 | 4 | 2 |

#### cluster (4) — top co-lemma: **kāyasamphassa** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassa | 0.23 | 13 | 3 |
| uppajji | 0.17 | 10 | 2 |

#### cluster (5) — top co-lemma: **vatthu** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vatthu | 0.18 | 21 | 3 |

### rūpadhātu

_pi blocks: 13; sense clusters: 1; inflected forms: rūpadhātu_

#### cluster (1) — top co-lemma: **vaṇṇanibha** (cohesion 0.93, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vaṇṇanibha | 0.63 | 6 | 6 |
| ātapa | 0.47 | 4 | 4 |
| mañjiṭṭhaka | 0.47 | 4 | 4 |
| soḷasaṃsa | 0.47 | 4 | 4 |
| maṇisaṅkhamuttāveḷuriya | 0.47 | 4 | 4 |
| ādāsamaṇḍala | 0.47 | 4 | 4 |
| vaṭṭa | 0.47 | 4 | 4 |
| dhūma | 0.47 | 4 | 4 |
| ambaṅkuravaṇṇa | 0.47 | 4 | 4 |
| chaḷaṃsa | 0.47 | 4 | 4 |

### tadekaṭṭha

_pi blocks: 13; sense clusters: 3; inflected forms: tadekaṭṭho, tadekaṭṭhā_

#### cluster (1) — top co-lemma: **manokamma** (cohesion 0.88, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manokamma | 0.96 | 14 | 13 |
| kāyakamma | 0.96 | 14 | 13 |
| vacīkamma | 0.96 | 14 | 13 |
| taṃsamuṭṭha | 0.96 | 14 | 13 |
| taṃsampayutta | 0.60 | 30 | 13 |
| kilesa | 0.55 | 34 | 13 |
| tīṇi | 0.55 | 20 | 9 |
| lobha | 0.42 | 39 | 11 |

#### cluster (2) — top co-lemma: **pahātabbahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pahātabbahetū | 0.47 | 4 | 4 |

#### cluster (3) — top co-lemma: **imāni** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| imāni | 0.35 | 10 | 4 |

### pañca

_pi blocks: 13; sense clusters: 3; inflected forms: pañca_

#### cluster (1) — top co-lemma: **somanassasahagatacittuppāda** (cohesion 0.74, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| somanassasahagatacittuppāda | 0.70 | 7 | 7 |
| kāmāvacarakusalata | 0.48 | 16 | 7 |
| lokuttaratikacatukkajjhāna | 0.44 | 5 | 4 |
| kāmāvacarakusala | 0.42 | 20 | 7 |
| rūpāvacaratikacatukkajjhāna | 0.36 | 9 | 4 |

#### cluster (2) — top co-lemma: **ahetukamanoviññāṇadhātuya** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahetukamanoviññāṇadhātuya | 0.38 | 3 | 3 |
| manodhātuya | 0.35 | 4 | 3 |

#### cluster (3) — top co-lemma: **lokuttaradukatikajjhāna** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lokuttaradukatikajjhāna | 0.38 | 3 | 3 |
| rūpāvacaradukatikajjhāna | 0.38 | 3 | 3 |
| pītiṃ | 0.32 | 6 | 3 |

### cittakammaññata

_pi blocks: 13; sense clusters: 1; inflected forms: cittakammaññatā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### cittalahuta

_pi blocks: 13; sense clusters: 1; inflected forms: cittalahutā_

#### cluster (1) — top co-lemma: **cittapāguññata** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### cittamuduta

_pi blocks: 13; sense clusters: 1; inflected forms: cittamudutā_

#### cluster (1) — top co-lemma: **cittapāguññata** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittalahuta | 0.85 | 13 | 11 |

### cittapassaddhi

_pi blocks: 13; sense clusters: 1; inflected forms: cittapassaddhi_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### cittapāguññata

_pi blocks: 13; sense clusters: 1; inflected forms: cittapāguññatā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### cittujukata

_pi blocks: 13; sense clusters: 1; inflected forms: cittujukatā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### kāyakammaññata

_pi blocks: 13; sense clusters: 1; inflected forms: kāyakammaññatā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### kāyalahuta

_pi blocks: 13; sense clusters: 1; inflected forms: kāyalahutā_

#### cluster (1) — top co-lemma: **cittapāguññata** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |
| cittalahuta | 0.85 | 13 | 11 |

### kāyamuduta

_pi blocks: 13; sense clusters: 1; inflected forms: kāyamudutā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### kāyapassaddhi

_pi blocks: 13; sense clusters: 1; inflected forms: kāyapassaddhi_

#### cluster (1) — top co-lemma: **cittapāguññata** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |
| cittalahuta | 0.85 | 13 | 11 |

### kāyapāguññata

_pi blocks: 13; sense clusters: 1; inflected forms: kāyapāguññatā_

#### cluster (1) — top co-lemma: **cittapāguññata** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittapāguññata | 0.85 | 13 | 11 |
| kāyujukata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |
| cittalahuta | 0.85 | 13 | 11 |

### kāyujukata

_pi blocks: 13; sense clusters: 1; inflected forms: kāyujukatā_

#### cluster (1) — top co-lemma: **cittalahuta** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittalahuta | 0.85 | 13 | 11 |
| cittapāguññata | 0.85 | 13 | 11 |
| cittujukata | 0.85 | 13 | 11 |
| cittakammaññata | 0.85 | 13 | 11 |
| kāyamuduta | 0.85 | 13 | 11 |
| cittapassaddhi | 0.85 | 13 | 11 |
| kāyapassaddhi | 0.85 | 13 | 11 |
| kāyapāguññata | 0.85 | 13 | 11 |
| kāyalahuta | 0.85 | 13 | 11 |
| cittamuduta | 0.85 | 13 | 11 |

### saṅkhāra

_pi blocks: 13; sense clusters: 3; inflected forms: saṅkhāre, saṅkhāresu, saṅkhārā_

#### cluster (1) — top co-lemma: **saṅgahita** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅgahita | 0.56 | 5 | 5 |

#### cluster (2) — top co-lemma: **viññāṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇa | 0.48 | 41 | 13 |

#### cluster (3) — top co-lemma: **assutava** (cohesion 1.00, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| assutava | 0.47 | 4 | 4 |
| attata | 0.47 | 4 | 4 |
| avinīta | 0.47 | 4 | 4 |
| ariyadhamma | 0.47 | 4 | 4 |
| rūpavanta | 0.47 | 4 | 4 |
| puthujjana | 0.47 | 4 | 4 |
| viññāṇavanta | 0.47 | 4 | 4 |
| samanupassati | 0.47 | 4 | 4 |

### cittacetasika

_pi blocks: 13; sense clusters: 2; inflected forms: cittacetasikā_

#### cluster (1) — top co-lemma: **uppajjanti** (cohesion 0.91, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajjanti | 0.59 | 24 | 11 |
| ārabbha | 0.57 | 22 | 10 |

#### cluster (2) — top co-lemma: **karitva** (cohesion 0.92, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| karitva | 0.35 | 4 | 3 |
| samāpanna | 0.27 | 2 | 2 |
| upapanna | 0.27 | 2 | 2 |
| diṭṭhadhammasukhavihārissa | 0.27 | 2 | 2 |
| ettha | 0.25 | 3 | 2 |
| etthāvacara | 0.25 | 3 | 2 |
| pariyanta | 0.25 | 3 | 2 |
| etasmiṃ | 0.25 | 3 | 2 |

### sasaṅkhāra

_pi blocks: 12; sense clusters: 5; inflected forms: sasaṅkhārena_

#### cluster (1) — top co-lemma: **dhammārammaṇa** (cohesion 0.78, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammārammaṇa | 0.58 | 26 | 11 |
| panārabbha | 0.52 | 30 | 11 |
| rūpārammaṇa | 0.48 | 34 | 11 |
| somanassasahagata | 0.47 | 18 | 7 |
| uppanna | 0.39 | 49 | 12 |

#### cluster (2) — top co-lemma: **ñāṇavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇavippayutta | 0.50 | 8 | 5 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.50 | 8 | 5 |
| upekkhāsahagata | 0.26 | 41 | 7 |

#### cluster (4) — top co-lemma: **abyākatamūla** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatamūla | 0.27 | 3 | 2 |

#### cluster (5) — top co-lemma: **diṭṭhigatavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayutta | 0.22 | 6 | 2 |

### viññatti

_pi blocks: 12; sense clusters: 1; inflected forms: viññatti_

#### cluster (1) — top co-lemma: **viññāpitatta** (cohesion 0.72, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāpitatta | 0.67 | 6 | 6 |
| kusalacitta | 0.67 | 6 | 6 |
| abyākatacitta | 0.67 | 6 | 6 |
| viññāpana | 0.67 | 6 | 6 |
| akusalacitta | 0.63 | 7 | 6 |
| thambhana | 0.40 | 3 | 3 |
| samiñjenta | 0.40 | 3 | 3 |
| santhambhana | 0.40 | 3 | 3 |
| pasārenta | 0.40 | 3 | 3 |
| paṭikkamanta | 0.40 | 3 | 3 |

### cittādhipateyya

_pi blocks: 12; sense clusters: 3; inflected forms: cittādhipateyyaṃ_

#### cluster (1) — top co-lemma: **vīriyādhipateyya** (cohesion 0.77, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīriyādhipateyya | 1.00 | 12 | 12 |
| vīmaṃsādhipateyya | 0.92 | 12 | 11 |
| majjhima | 0.70 | 11 | 8 |
| hīna | 0.70 | 11 | 8 |
| paṇīta | 0.70 | 11 | 8 |
| chandādhipateyya | 0.57 | 30 | 12 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.33 | 12 | 4 |
| sabbasa | 0.29 | 16 | 4 |
| samatikkamma | 0.25 | 12 | 3 |

#### cluster (3) — top co-lemma: **satipaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satipaṭṭha | 0.25 | 4 | 2 |

### vīriyādhipateyya

_pi blocks: 12; sense clusters: 3; inflected forms: vīriyādhipateyyaṃ_

#### cluster (1) — top co-lemma: **cittādhipateyya** (cohesion 0.77, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittādhipateyya | 1.00 | 12 | 12 |
| vīmaṃsādhipateyya | 0.92 | 12 | 11 |
| majjhima | 0.70 | 11 | 8 |
| hīna | 0.70 | 11 | 8 |
| paṇīta | 0.70 | 11 | 8 |
| chandādhipateyya | 0.57 | 30 | 12 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.33 | 12 | 4 |
| sabbasa | 0.29 | 16 | 4 |
| samatikkamma | 0.25 | 12 | 3 |

#### cluster (3) — top co-lemma: **satipaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satipaṭṭha | 0.25 | 4 | 2 |

### vīmaṃsādhipateyya

_pi blocks: 12; sense clusters: 3; inflected forms: vīmaṃsādhipateyyaṃ_

#### cluster (1) — top co-lemma: **cittādhipateyya** (cohesion 0.78, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittādhipateyya | 0.92 | 12 | 11 |
| vīriyādhipateyya | 0.92 | 12 | 11 |
| majjhima | 0.61 | 11 | 7 |
| hīna | 0.61 | 11 | 7 |
| paṇīta | 0.61 | 11 | 7 |
| chandādhipateyya | 0.52 | 30 | 11 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.33 | 12 | 4 |
| sabbasa | 0.29 | 16 | 4 |
| samatikkamma | 0.25 | 12 | 3 |

#### cluster (3) — top co-lemma: **satipaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satipaṭṭha | 0.25 | 4 | 2 |

### samatikkamma

_pi blocks: 12; sense clusters: 5; inflected forms: samatikkamma_

#### cluster (1) — top co-lemma: **sabbasa** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbasa | 0.86 | 16 | 12 |
| arūpūpapattiya | 0.75 | 12 | 9 |
| sukha | 0.32 | 64 | 12 |

#### cluster (2) — top co-lemma: **viññāṇañcāyatanasaññāsahagata** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇañcāyatanasaññāsahagata | 0.50 | 4 | 4 |
| ākāsānañcāyatana | 0.42 | 7 | 4 |

#### cluster (3) — top co-lemma: **ākiñcaññāyatanasaññāsahagata** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākiñcaññāyatanasaññāsahagata | 0.50 | 4 | 4 |
| viññāṇañcāyatana | 0.42 | 7 | 4 |

#### cluster (4) — top co-lemma: **nevasaññānāsaññāyatanasaññāsahagata** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nevasaññānāsaññāyatanasaññāsahagata | 0.50 | 4 | 4 |
| ākiñcaññāyatana | 0.42 | 7 | 4 |

#### cluster (5) — top co-lemma: **diṭṭhadhammasukhavihāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhadhammasukhavihāra | 0.33 | 6 | 3 |

### ghānindriya

_pi blocks: 12; sense clusters: 2; inflected forms: ghānindriyaṃ_

#### cluster (1) — top co-lemma: **sotindriya** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotindriya | 0.67 | 12 | 8 |
| jivhindriya | 0.67 | 12 | 8 |
| kāyindriya | 0.52 | 19 | 8 |
| purisindriya | 0.26 | 35 | 6 |

#### cluster (2) — top co-lemma: **ghānadhātu** (cohesion 0.89, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānadhātu | 0.50 | 8 | 5 |
| ghānāyatana | 0.38 | 14 | 5 |
| ghāna | 0.36 | 10 | 4 |
| gandha | 0.36 | 10 | 4 |
| tīra | 0.25 | 20 | 4 |
| orima | 0.25 | 20 | 4 |

### jivhindriya

_pi blocks: 12; sense clusters: 2; inflected forms: jivhindriyaṃ_

#### cluster (1) — top co-lemma: **ghānindriya** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānindriya | 0.67 | 12 | 8 |
| sotindriya | 0.67 | 12 | 8 |
| kāyindriya | 0.52 | 19 | 8 |
| purisindriya | 0.26 | 35 | 6 |

#### cluster (2) — top co-lemma: **jivhādhātu** (cohesion 0.89, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhādhātu | 0.50 | 8 | 5 |
| jivha | 0.36 | 10 | 4 |
| jivhāyatana | 0.32 | 19 | 5 |
| tīra | 0.25 | 20 | 4 |
| orima | 0.25 | 20 | 4 |
| samudda | 0.25 | 20 | 4 |

### sotindriya

_pi blocks: 12; sense clusters: 2; inflected forms: sotindriyaṃ_

#### cluster (1) — top co-lemma: **ghānindriya** (cohesion 0.88, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānindriya | 0.67 | 12 | 8 |
| jivhindriya | 0.67 | 12 | 8 |
| kāyindriya | 0.52 | 19 | 8 |
| purisindriya | 0.26 | 35 | 6 |

#### cluster (2) — top co-lemma: **sotadhātu** (cohesion 0.89, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotadhātu | 0.50 | 8 | 5 |
| sota | 0.44 | 6 | 4 |
| sadda | 0.36 | 10 | 4 |
| sotāyatana | 0.28 | 24 | 5 |
| tīra | 0.25 | 20 | 4 |
| orima | 0.25 | 20 | 4 |

### anussati

_pi blocks: 12; sense clusters: 2; inflected forms: anussati_

#### cluster (1) — top co-lemma: **apilāpanata** (cohesion 0.98, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apilāpanata | 1.00 | 12 | 12 |
| saraṇata | 1.00 | 12 | 12 |
| dhāraṇata | 1.00 | 12 | 12 |
| paṭissati | 1.00 | 12 | 12 |
| asammussanata | 0.96 | 11 | 11 |
| satibala | 0.65 | 25 | 12 |
| sammāsati | 0.65 | 25 | 12 |
| satindriya | 0.47 | 39 | 12 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.50 | 4 | 4 |
| maggapariyāpanna | 0.19 | 30 | 4 |

### apilāpanata

_pi blocks: 12; sense clusters: 2; inflected forms: apilāpanatā_

#### cluster (1) — top co-lemma: **anussati** (cohesion 0.98, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anussati | 1.00 | 12 | 12 |
| saraṇata | 1.00 | 12 | 12 |
| dhāraṇata | 1.00 | 12 | 12 |
| paṭissati | 1.00 | 12 | 12 |
| asammussanata | 0.96 | 11 | 11 |
| satibala | 0.65 | 25 | 12 |
| sammāsati | 0.65 | 25 | 12 |
| satindriya | 0.47 | 39 | 12 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.50 | 4 | 4 |
| maggapariyāpanna | 0.19 | 30 | 4 |

### arūpūpapattiya

_pi blocks: 12; sense clusters: 4; inflected forms: arūpūpapattiyā_

#### cluster (1) — top co-lemma: **sabbasa** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbasa | 0.86 | 16 | 12 |
| samatikkamma | 0.75 | 12 | 9 |

#### cluster (2) — top co-lemma: **viññāṇañcāyatanasaññāsahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| viññāṇañcāyatanasaññāsahagata | 0.38 | 4 | 3 |

#### cluster (3) — top co-lemma: **ākiñcaññāyatanasaññāsahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ākiñcaññāyatanasaññāsahagata | 0.38 | 4 | 3 |

#### cluster (4) — top co-lemma: **amanasikāra** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| amanasikāra | 0.38 | 4 | 3 |
| nānattasañña | 0.38 | 4 | 3 |
| samatikkama | 0.38 | 4 | 3 |
| ākāsānañcāyatanasaññāsahagata | 0.38 | 4 | 3 |
| paṭighasañña | 0.38 | 4 | 3 |
| rūpasañña | 0.38 | 4 | 3 |

### dhāraṇata

_pi blocks: 12; sense clusters: 2; inflected forms: dhāraṇatā_

#### cluster (1) — top co-lemma: **apilāpanata** (cohesion 0.98, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apilāpanata | 1.00 | 12 | 12 |
| anussati | 1.00 | 12 | 12 |
| saraṇata | 1.00 | 12 | 12 |
| paṭissati | 1.00 | 12 | 12 |
| asammussanata | 0.96 | 11 | 11 |
| satibala | 0.65 | 25 | 12 |
| sammāsati | 0.65 | 25 | 12 |
| satindriya | 0.47 | 39 | 12 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.50 | 4 | 4 |
| maggapariyāpanna | 0.19 | 30 | 4 |

### panaññopi

_pi blocks: 12; sense clusters: 1; inflected forms: panaññopi_

#### cluster (1) — top co-lemma: **paṇavasadda** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṇavasadda | 0.50 | 4 | 4 |
| pāṇisadda | 0.50 | 4 | 4 |
| gītasadda | 0.50 | 4 | 4 |
| manussasadda | 0.50 | 4 | 4 |
| nigghosasadda | 0.50 | 4 | 4 |
| sammasadda | 0.50 | 4 | 4 |
| amanussasadda | 0.50 | 4 | 4 |
| udakasadda | 0.50 | 4 | 4 |
| saṅkhasadda | 0.50 | 4 | 4 |
| vātasadda | 0.50 | 4 | 4 |

### paṭissati

_pi blocks: 12; sense clusters: 2; inflected forms: paṭissati_

#### cluster (1) — top co-lemma: **apilāpanata** (cohesion 0.98, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apilāpanata | 1.00 | 12 | 12 |
| anussati | 1.00 | 12 | 12 |
| saraṇata | 1.00 | 12 | 12 |
| dhāraṇata | 1.00 | 12 | 12 |
| asammussanata | 0.96 | 11 | 11 |
| satibala | 0.65 | 25 | 12 |
| sammāsati | 0.65 | 25 | 12 |
| satindriya | 0.47 | 39 | 12 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.50 | 4 | 4 |
| maggapariyāpanna | 0.19 | 30 | 4 |

### pubbanta

_pi blocks: 12; sense clusters: 1; inflected forms: pubbantaṃ, pubbante_

#### cluster (1) — top co-lemma: **pubbantāparanta** (cohesion 0.70, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pubbantāparanta | 0.96 | 11 | 11 |
| idappaccayata | 0.96 | 11 | 11 |
| apariyogāhana | 0.78 | 11 | 9 |
| dukkhanirodhagāminiya | 0.74 | 7 | 7 |
| dukkhanirodha | 0.74 | 7 | 7 |
| dukkhasamudaya | 0.74 | 7 | 7 |
| paṭipada | 0.64 | 10 | 7 |
| apaccavekkhaṇa | 0.59 | 5 | 5 |
| sammoha | 0.56 | 6 | 5 |
| avijjogha | 0.56 | 6 | 5 |

### saraṇata

_pi blocks: 12; sense clusters: 2; inflected forms: saraṇatā_

#### cluster (1) — top co-lemma: **apilāpanata** (cohesion 0.98, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apilāpanata | 1.00 | 12 | 12 |
| anussati | 1.00 | 12 | 12 |
| dhāraṇata | 1.00 | 12 | 12 |
| paṭissati | 1.00 | 12 | 12 |
| asammussanata | 0.96 | 11 | 11 |
| satibala | 0.65 | 25 | 12 |
| sammāsati | 0.65 | 25 | 12 |
| satindriya | 0.47 | 39 | 12 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.50 | 4 | 4 |
| maggapariyāpanna | 0.19 | 30 | 4 |

### hīna

_pi blocks: 11; sense clusters: 3; inflected forms: hīnaṃ, hīnā_

#### cluster (1) — top co-lemma: **paṇīta** (cohesion 0.90, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṇīta | 0.82 | 11 | 9 |
| majjhima | 0.82 | 11 | 9 |
| cittādhipateyya | 0.70 | 12 | 8 |
| vīriyādhipateyya | 0.70 | 12 | 8 |
| vīmaṃsādhipateyya | 0.61 | 12 | 7 |
| chandādhipateyya | 0.39 | 30 | 8 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.35 | 12 | 4 |
| sabbasa | 0.30 | 16 | 4 |
| samatikkamma | 0.26 | 12 | 3 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.21 | 8 | 2 |

### majjhima

_pi blocks: 11; sense clusters: 3; inflected forms: majjhimaṃ, majjhimā_

#### cluster (1) — top co-lemma: **hīna** (cohesion 0.90, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hīna | 0.82 | 11 | 9 |
| paṇīta | 0.82 | 11 | 9 |
| cittādhipateyya | 0.70 | 12 | 8 |
| vīriyādhipateyya | 0.70 | 12 | 8 |
| vīmaṃsādhipateyya | 0.61 | 12 | 7 |
| chandādhipateyya | 0.39 | 30 | 8 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.35 | 12 | 4 |
| sabbasa | 0.30 | 16 | 4 |
| samatikkamma | 0.26 | 12 | 3 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.21 | 8 | 2 |

### paṇīta

_pi blocks: 11; sense clusters: 3; inflected forms: paṇītaṃ, paṇītā_

#### cluster (1) — top co-lemma: **hīna** (cohesion 0.90, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hīna | 0.82 | 11 | 9 |
| majjhima | 0.82 | 11 | 9 |
| cittādhipateyya | 0.70 | 12 | 8 |
| vīriyādhipateyya | 0.70 | 12 | 8 |
| vīmaṃsādhipateyya | 0.61 | 12 | 7 |
| chandādhipateyya | 0.39 | 30 | 8 |

#### cluster (2) — top co-lemma: **arūpūpapattiya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpūpapattiya | 0.35 | 12 | 4 |
| sabbasa | 0.30 | 16 | 4 |
| samatikkamma | 0.26 | 12 | 3 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.21 | 8 | 2 |

### uppajjissati

_pi blocks: 11; sense clusters: 1; inflected forms: uppajjissati_

#### cluster (1) — top co-lemma: **uppajji** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajji | 0.95 | 10 | 10 |
| nissa | 0.95 | 10 | 10 |
| uppajja | 0.95 | 10 | 10 |
| uppajjati | 0.65 | 20 | 10 |
| ārabbha | 0.61 | 22 | 10 |
| peta | 0.39 | 40 | 10 |
| pesa | 0.36 | 45 | 10 |
| samudda | 0.32 | 20 | 5 |
| tīra | 0.32 | 20 | 5 |
| orima | 0.32 | 20 | 5 |

### sahetuka

_pi blocks: 11; sense clusters: 5; inflected forms: sahetukā_

#### cluster (1) — top co-lemma: **kāmāvacarakiriyata** (cohesion 0.83, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakiriyata | 0.35 | 6 | 3 |
| vipākata | 0.13 | 34 | 3 |
| cittuppāda | 0.12 | 40 | 3 |
| etthuppanna | 0.11 | 27 | 2 |

#### cluster (2) — top co-lemma: **hetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hetū | 0.25 | 44 | 7 |

#### cluster (3) — top co-lemma: **ahetuka** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahetuka | 0.21 | 8 | 2 |
| hetūtipi | 0.15 | 2 | 1 |

#### cluster (4) — top co-lemma: **aññamañña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññamañña | 0.15 | 2 | 1 |

#### cluster (5) — top co-lemma: **abyākatamūla** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatamūla | 0.14 | 3 | 1 |
| ñāṇasampayutta | 0.11 | 8 | 1 |

### ganthaniya

_pi blocks: 11; sense clusters: 5; inflected forms: ganthaniyaṃ, ganthaniyā_

#### cluster (1) — top co-lemma: **gantha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gantha | 0.33 | 19 | 5 |

#### cluster (2) — top co-lemma: **aganthaniya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aganthaniya | 0.24 | 6 | 2 |
| ganthātipi | 0.15 | 2 | 1 |

#### cluster (3) — top co-lemma: **ganthavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthavippayutta | 0.20 | 9 | 2 |

#### cluster (4) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (5) — top co-lemma: **ekavidha** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |
| nevavipākanavipākadhammadhamma | 0.13 | 4 | 1 |

### nīvaraṇiya

_pi blocks: 11; sense clusters: 6; inflected forms: nīvaraṇiyaṃ, nīvaraṇiyā_

#### cluster (1) — top co-lemma: **nīvaraṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇa | 0.33 | 19 | 5 |

#### cluster (2) — top co-lemma: **tāneva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tāneva | 0.24 | 6 | 2 |

#### cluster (3) — top co-lemma: **anīvaraṇiya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anīvaraṇiya | 0.24 | 6 | 2 |
| nīvaraṇātipi | 0.15 | 2 | 1 |

#### cluster (4) — top co-lemma: **nīvaraṇavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇavippayutta | 0.20 | 9 | 2 |

#### cluster (5) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (6) — top co-lemma: **ekavidha** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |

### parāmaṭṭha

_pi blocks: 11; sense clusters: 5; inflected forms: parāmaṭṭhaṃ, parāmaṭṭho, parāmaṭṭhā_

#### cluster (1) — top co-lemma: **parāmāsa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsa | 0.26 | 27 | 5 |

#### cluster (2) — top co-lemma: **aparāmaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aparāmaṭṭha | 0.24 | 6 | 2 |

#### cluster (3) — top co-lemma: **parāmāsavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsavippayutta | 0.21 | 8 | 2 |

#### cluster (4) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (5) — top co-lemma: **ekavidha** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |
| nevavipākanavipākadhammadhamma | 0.13 | 4 | 1 |
| asaṃkiliṭṭhasaṃkilesika | 0.13 | 4 | 1 |

### saṃkilesika

_pi blocks: 11; sense clusters: 5; inflected forms: saṃkilesikaṃ, saṃkilesikā_

#### cluster (1) — top co-lemma: **asaṃkilesika** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkilesika | 0.24 | 6 | 2 |
| kilesātipi | 0.14 | 3 | 1 |

#### cluster (2) — top co-lemma: **kilesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesa | 0.22 | 34 | 5 |

#### cluster (3) — top co-lemma: **kilesavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesavippayutta | 0.20 | 9 | 2 |

#### cluster (4) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (5) — top co-lemma: **ekavidha** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |
| nevavipākanavipākadhammadhamma | 0.13 | 4 | 1 |

### saṃyojaniya

_pi blocks: 11; sense clusters: 6; inflected forms: saṃyojaniyaṃ, saṃyojaniyā_

#### cluster (1) — top co-lemma: **saṃyojana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojana | 0.29 | 24 | 5 |

#### cluster (2) — top co-lemma: **tāneva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tāneva | 0.24 | 6 | 2 |

#### cluster (3) — top co-lemma: **asaṃyojaniya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃyojaniya | 0.24 | 6 | 2 |
| saṃyojanātipi | 0.15 | 2 | 1 |

#### cluster (4) — top co-lemma: **saṃyojanavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanavippayutta | 0.20 | 9 | 2 |

#### cluster (5) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (6) — top co-lemma: **ekavidha** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |

### upādāniya

_pi blocks: 11; sense clusters: 6; inflected forms: upādāniyaṃ, upādāniyā_

#### cluster (1) — top co-lemma: **upādāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādāna | 0.37 | 16 | 5 |

#### cluster (2) — top co-lemma: **tāneva** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tāneva | 0.24 | 6 | 2 |

#### cluster (3) — top co-lemma: **anupādāniya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādāniya | 0.24 | 6 | 2 |
| upādānātipi | 0.15 | 2 | 1 |

#### cluster (4) — top co-lemma: **upādānavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānavippayutta | 0.20 | 9 | 2 |

#### cluster (5) — top co-lemma: **sāsava** (cohesion 0.75, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sāsava | 0.16 | 39 | 4 |
| rūpakkhandha | 0.15 | 28 | 3 |

#### cluster (6) — top co-lemma: **ekavidha** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.15 | 2 | 1 |
| ācayagāmi | 0.14 | 3 | 1 |
| nevasekkhanāsekkha | 0.13 | 4 | 1 |

### cakkhudhātu

_pi blocks: 11; sense clusters: 1; inflected forms: cakkhudhātu_

#### cluster (1) — top co-lemma: **nayana** (cohesion 0.89, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nayana | 0.53 | 4 | 4 |
| netta | 0.53 | 4 | 4 |
| cakkhuṃ | 0.47 | 6 | 4 |
| cakkhu | 0.36 | 11 | 4 |
| cakkhundriya | 0.31 | 21 | 5 |
| sanidassana | 0.28 | 18 | 4 |
| tīra | 0.26 | 20 | 4 |
| orima | 0.26 | 20 | 4 |
| samudda | 0.26 | 20 | 4 |
| dvāra | 0.26 | 20 | 4 |

### kāyadhātu

_pi blocks: 11; sense clusters: 2; inflected forms: kāyadhātu_

#### cluster (1) — top co-lemma: **ghānadhātu** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānadhātu | 0.42 | 8 | 4 |
| sotadhātu | 0.42 | 8 | 4 |
| jivhādhātu | 0.42 | 8 | 4 |

#### cluster (2) — top co-lemma: **phoṭṭhabba** (cohesion 0.94, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabba | 0.36 | 11 | 4 |
| kāyindriya | 0.33 | 19 | 5 |
| samudda | 0.26 | 20 | 4 |
| dvāra | 0.26 | 20 | 4 |
| kāya | 0.26 | 20 | 4 |
| tīra | 0.26 | 20 | 4 |
| orima | 0.26 | 20 | 4 |

### sukhasahagata

_pi blocks: 11; sense clusters: 5; inflected forms: sukhasahagataṃ, sukhasahagatā_

#### cluster (1) — top co-lemma: **sukhabhūmiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukhabhūmiya | 0.40 | 4 | 3 |

#### cluster (2) — top co-lemma: **kāmāvacarakusalata** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakusalata | 0.30 | 16 | 4 |
| kāmāvacarakusala | 0.26 | 20 | 4 |
| upekkhāsahagatacittuppāda | 0.24 | 6 | 2 |
| āruppa | 0.20 | 9 | 2 |

#### cluster (3) — top co-lemma: **pītisahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pītisahagata | 0.29 | 10 | 3 |

#### cluster (4) — top co-lemma: **sukhañca** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukhañca | 0.29 | 3 | 2 |

#### cluster (5) — top co-lemma: **lokuttaratikacatukkajjhāna** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lokuttaratikacatukkajjhāna | 0.25 | 5 | 2 |
| somanassasahagatacittuppāda | 0.22 | 7 | 2 |
| rūpāvacaratikacatukkajjhāna | 0.20 | 9 | 2 |

### phoṭṭhabba

_pi blocks: 11; sense clusters: 2; inflected forms: phoṭṭhabbamhi, phoṭṭhabbaṃ, phoṭṭhabbo_

#### cluster (1) — top co-lemma: **kāya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāya | 0.65 | 20 | 10 |

#### cluster (2) — top co-lemma: **sukhasamphassa** (cohesion 0.92, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukhasamphassa | 0.59 | 6 | 5 |
| dukkhasamphassa | 0.59 | 6 | 5 |
| lahuka | 0.53 | 4 | 4 |
| muduka | 0.53 | 4 | 4 |
| pharusa | 0.53 | 4 | 4 |
| garuka | 0.53 | 4 | 4 |
| saṇha | 0.53 | 4 | 4 |
| kakkhaḷa | 0.50 | 5 | 4 |
| tejodhātu | 0.47 | 6 | 4 |

### domanassasahagata

_pi blocks: 11; sense clusters: 5; inflected forms: domanassasahagataṃ, domanassasahagatesu_

#### cluster (1) — top co-lemma: **dvīsu** (cohesion 0.85, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvīsu | 0.90 | 9 | 9 |
| vicikicchāsahagata | 0.38 | 26 | 7 |
| cittuppāda | 0.35 | 40 | 9 |

#### cluster (2) — top co-lemma: **lobhasahagata** (cohesion 0.90, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagata | 0.56 | 7 | 5 |
| aṭṭhasu | 0.56 | 7 | 5 |
| sabbākusala | 0.50 | 5 | 4 |
| uppajjati | 0.32 | 20 | 5 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagata | 0.44 | 7 | 4 |

#### cluster (4) — top co-lemma: **sasaṅkhārika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhārika | 0.31 | 2 | 2 |

#### cluster (5) — top co-lemma: **paṭighasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| paṭighasampayutta | 0.31 | 2 | 2 |

### cakkhu

_pi blocks: 11; sense clusters: 2; inflected forms: cakkhu_

#### cluster (1) — top co-lemma: **nayana** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nayana | 0.53 | 4 | 4 |
| netta | 0.53 | 4 | 4 |
| cakkhuṃ | 0.47 | 6 | 4 |
| cakkhudhātu | 0.36 | 11 | 4 |
| tīra | 0.26 | 20 | 4 |

#### cluster (2) — top co-lemma: **suñña** (cohesion 0.85, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suñña | 0.52 | 31 | 11 |
| pasāda | 0.52 | 31 | 11 |
| cakkhundriya | 0.50 | 21 | 8 |
| gāma | 0.50 | 29 | 10 |
| catunna | 0.37 | 49 | 11 |

### āyatana

_pi blocks: 11; sense clusters: 3; inflected forms: āyatanaṃ, āyatanā, āyatanānaṃ, āyatanāni_

#### cluster (1) — top co-lemma: **satipaṭṭha** (cohesion 0.94, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satipaṭṭha | 0.53 | 4 | 4 |
| iddhipāda | 0.53 | 4 | 4 |
| dhātuṃ | 0.53 | 4 | 4 |
| sammappadha | 0.53 | 4 | 4 |
| sacca | 0.50 | 5 | 4 |
| bojjhaṅga | 0.50 | 5 | 4 |
| bala | 0.26 | 27 | 5 |

#### cluster (2) — top co-lemma: **ācaya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ācaya | 0.43 | 3 | 3 |

#### cluster (3) — top co-lemma: **vīsati** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vīsati | 0.31 | 2 | 2 |
| mahānaya | 0.31 | 2 | 2 |

### abhiniropana

_pi blocks: 11; sense clusters: 2; inflected forms: abhiniropanā_

#### cluster (1) — top co-lemma: **appana** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appana | 1.00 | 11 | 11 |
| saṅkappa | 1.00 | 11 | 11 |
| byappana | 1.00 | 11 | 11 |
| takka | 1.00 | 11 | 11 |
| sammāsaṅkappa | 0.40 | 19 | 6 |
| vitakka | 0.31 | 59 | 11 |

#### cluster (2) — top co-lemma: **micchāsaṅkappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsaṅkappa | 0.15 | 16 | 2 |

### apariyogāhana

_pi blocks: 11; sense clusters: 1; inflected forms: apariyogāhanā_

#### cluster (1) — top co-lemma: **pubbantāparanta** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pubbantāparanta | 0.82 | 11 | 9 |
| idappaccayata | 0.82 | 11 | 9 |
| pubbanta | 0.78 | 12 | 9 |
| ananubodha | 0.71 | 6 | 6 |
| avijjogha | 0.71 | 6 | 6 |
| sammoha | 0.71 | 6 | 6 |
| apaccakkhakamma | 0.71 | 6 | 6 |
| anabhisamaya | 0.71 | 6 | 6 |
| avijjāpariyuṭṭha | 0.71 | 6 | 6 |
| avijjāyoga | 0.71 | 6 | 6 |

### appana

_pi blocks: 11; sense clusters: 2; inflected forms: appanā_

#### cluster (1) — top co-lemma: **takka** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| takka | 1.00 | 11 | 11 |
| saṅkappa | 1.00 | 11 | 11 |
| byappana | 1.00 | 11 | 11 |
| abhiniropana | 1.00 | 11 | 11 |
| sammāsaṅkappa | 0.40 | 19 | 6 |
| vitakka | 0.31 | 59 | 11 |

#### cluster (2) — top co-lemma: **micchāsaṅkappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsaṅkappa | 0.15 | 16 | 2 |

### asammussanata

_pi blocks: 11; sense clusters: 2; inflected forms: asammussanatā_

#### cluster (1) — top co-lemma: **apilāpanata** (cohesion 1.00, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apilāpanata | 0.96 | 12 | 11 |
| anussati | 0.96 | 12 | 11 |
| saraṇata | 0.96 | 12 | 11 |
| dhāraṇata | 0.96 | 12 | 11 |
| paṭissati | 0.96 | 12 | 11 |
| satibala | 0.61 | 25 | 11 |
| sammāsati | 0.61 | 25 | 11 |
| satindriya | 0.44 | 39 | 11 |

#### cluster (2) — top co-lemma: **satisambojjhaṅga** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| satisambojjhaṅga | 0.53 | 4 | 4 |
| maggapariyāpanna | 0.20 | 30 | 4 |

### aṭṭhindriya

_pi blocks: 11; sense clusters: 2; inflected forms: aṭṭhindriyāni_

#### cluster (1) — top co-lemma: **caturaṅgika** (cohesion 0.87, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| caturaṅgika | 0.59 | 16 | 8 |
| satta | 0.47 | 27 | 9 |
| bala | 0.47 | 27 | 9 |
| dvāyatana | 0.42 | 32 | 9 |
| somanassindriya | 0.40 | 19 | 6 |
| ekaṃ | 0.40 | 34 | 9 |
| ekā | 0.39 | 35 | 9 |
| dhātuya | 0.39 | 35 | 9 |
| dhammadhātu | 0.38 | 37 | 9 |

#### cluster (2) — top co-lemma: **duvaṅgika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| duvaṅgika | 0.50 | 5 | 4 |

### byappana

_pi blocks: 11; sense clusters: 2; inflected forms: byappanā_

#### cluster (1) — top co-lemma: **appana** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appana | 1.00 | 11 | 11 |
| saṅkappa | 1.00 | 11 | 11 |
| abhiniropana | 1.00 | 11 | 11 |
| takka | 1.00 | 11 | 11 |
| sammāsaṅkappa | 0.40 | 19 | 6 |
| vitakka | 0.31 | 59 | 11 |

#### cluster (2) — top co-lemma: **micchāsaṅkappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsaṅkappa | 0.15 | 16 | 2 |

### dhammavicayasambojjhaṅga

_pi blocks: 11; sense clusters: 1; inflected forms: dhammavicayasambojjhaṅgo_

#### cluster (1) — top co-lemma: **kosalla** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kosalla | 0.67 | 22 | 11 |
| paññāobhāsa | 0.67 | 22 | 11 |
| bhūrī | 0.67 | 22 | 11 |
| sallakkhaṇa | 0.67 | 22 | 11 |
| paññāpāsāda | 0.67 | 22 | 11 |
| upaparikkha | 0.67 | 22 | 11 |
| cinta | 0.67 | 22 | 11 |
| paṇḍicca | 0.67 | 22 | 11 |
| paññāpajjota | 0.67 | 22 | 11 |
| upalakkhaṇa | 0.67 | 22 | 11 |

### idappaccayata

_pi blocks: 11; sense clusters: 1; inflected forms: idappaccayatā_

#### cluster (1) — top co-lemma: **pubbantāparanta** (cohesion 0.70, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pubbantāparanta | 1.00 | 11 | 11 |
| pubbanta | 0.96 | 12 | 11 |
| apariyogāhana | 0.82 | 11 | 9 |
| dukkhanirodhagāminiya | 0.78 | 7 | 7 |
| dukkhanirodha | 0.78 | 7 | 7 |
| dukkhasamudaya | 0.78 | 7 | 7 |
| paṭipada | 0.67 | 10 | 7 |
| apaccavekkhaṇa | 0.62 | 5 | 5 |
| sammoha | 0.59 | 6 | 5 |
| avijjogha | 0.59 | 6 | 5 |

### kusalākusala

_pi blocks: 11; sense clusters: 5; inflected forms: kusalākusalā, kusalākusalānaṃ_

#### cluster (1) — top co-lemma: **kammavipāka** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kammavipāka | 0.37 | 16 | 5 |
| nākusala | 0.37 | 16 | 5 |
| kiriya | 0.33 | 19 | 5 |

#### cluster (2) — top co-lemma: **yañca** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yañca | 0.33 | 19 | 5 |
| sāsava | 0.20 | 39 | 5 |

#### cluster (3) — top co-lemma: **arūpāvacara** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpāvacara | 0.22 | 88 | 11 |
| rūpāvacara | 0.19 | 102 | 11 |
| kāmāvacara | 0.17 | 115 | 11 |

#### cluster (4) — top co-lemma: **ācayagāmina** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ācayagāmina | 0.14 | 3 | 1 |

#### cluster (5) — top co-lemma: **uppādina** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppādina | 0.14 | 3 | 1 |

### pubbantāparanta

_pi blocks: 11; sense clusters: 1; inflected forms: pubbantāparante_

#### cluster (1) — top co-lemma: **idappaccayata** (cohesion 0.70, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| idappaccayata | 1.00 | 11 | 11 |
| pubbanta | 0.96 | 12 | 11 |
| apariyogāhana | 0.82 | 11 | 9 |
| dukkhanirodhagāminiya | 0.78 | 7 | 7 |
| dukkhanirodha | 0.78 | 7 | 7 |
| dukkhasamudaya | 0.78 | 7 | 7 |
| paṭipada | 0.67 | 10 | 7 |
| apaccavekkhaṇa | 0.62 | 5 | 5 |
| sammoha | 0.59 | 6 | 5 |
| avijjogha | 0.59 | 6 | 5 |

### sañjānana

_pi blocks: 11; sense clusters: 5; inflected forms: sañjānanā_

#### cluster (1) — top co-lemma: **sañjānitatta** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañjānitatta | 1.00 | 11 | 11 |
| sañña | 0.24 | 80 | 11 |

#### cluster (2) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.34 | 18 | 5 |

#### cluster (3) — top co-lemma: **tajjācakkhuviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātusamphassaja | 0.14 | 3 | 1 |

#### cluster (4) — top co-lemma: **tajjāmanodhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanodhātusamphassaja | 0.14 | 3 | 1 |

#### cluster (5) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.13 | 4 | 1 |

### sañjānitatta

_pi blocks: 11; sense clusters: 5; inflected forms: sañjānitattaṃ_

#### cluster (1) — top co-lemma: **sañjānana** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañjānana | 1.00 | 11 | 11 |
| sañña | 0.24 | 80 | 11 |

#### cluster (2) — top co-lemma: **tajjāmanoviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanoviññāṇadhātusamphassaja | 0.34 | 18 | 5 |

#### cluster (3) — top co-lemma: **tajjācakkhuviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātusamphassaja | 0.14 | 3 | 1 |

#### cluster (4) — top co-lemma: **tajjāmanodhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanodhātusamphassaja | 0.14 | 3 | 1 |

#### cluster (5) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.13 | 4 | 1 |

### saṅkappa

_pi blocks: 11; sense clusters: 2; inflected forms: saṅkappo_

#### cluster (1) — top co-lemma: **takka** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| takka | 1.00 | 11 | 11 |
| appana | 1.00 | 11 | 11 |
| byappana | 1.00 | 11 | 11 |
| abhiniropana | 1.00 | 11 | 11 |
| sammāsaṅkappa | 0.40 | 19 | 6 |
| vitakka | 0.31 | 59 | 11 |

#### cluster (2) — top co-lemma: **micchāsaṅkappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsaṅkappa | 0.15 | 16 | 2 |

### takka

_pi blocks: 11; sense clusters: 2; inflected forms: takko_

#### cluster (1) — top co-lemma: **appana** (cohesion 0.85, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appana | 1.00 | 11 | 11 |
| saṅkappa | 1.00 | 11 | 11 |
| byappana | 1.00 | 11 | 11 |
| abhiniropana | 1.00 | 11 | 11 |
| sammāsaṅkappa | 0.40 | 19 | 6 |
| vitakka | 0.31 | 59 | 11 |

#### cluster (2) — top co-lemma: **micchāsaṅkappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāsaṅkappa | 0.15 | 16 | 2 |

### nissa

_pi blocks: 10; sense clusters: 1; inflected forms: nissāya_

#### cluster (1) — top co-lemma: **uppajji** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajji | 1.00 | 10 | 10 |
| uppajja | 1.00 | 10 | 10 |
| uppajjissati | 0.95 | 11 | 10 |
| uppajjati | 0.67 | 20 | 10 |
| ārabbha | 0.62 | 22 | 10 |
| peta | 0.40 | 40 | 10 |
| pesa | 0.36 | 45 | 10 |
| samudda | 0.33 | 20 | 5 |
| tīra | 0.33 | 20 | 5 |
| orima | 0.33 | 20 | 5 |

### uppajja

_pi blocks: 10; sense clusters: 1; inflected forms: uppajje_

#### cluster (1) — top co-lemma: **uppajji** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uppajji | 1.00 | 10 | 10 |
| nissa | 1.00 | 10 | 10 |
| uppajjissati | 0.95 | 11 | 10 |
| uppajjati | 0.67 | 20 | 10 |
| ārabbha | 0.62 | 22 | 10 |
| peta | 0.40 | 40 | 10 |
| pesa | 0.36 | 45 | 10 |
| samudda | 0.33 | 20 | 5 |
| tīra | 0.33 | 20 | 5 |
| orima | 0.33 | 20 | 5 |

### uppajji

_pi blocks: 10; sense clusters: 1; inflected forms: uppajji_

#### cluster (1) — top co-lemma: **nissa** (cohesion 0.77, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nissa | 1.00 | 10 | 10 |
| uppajja | 1.00 | 10 | 10 |
| uppajjissati | 0.95 | 11 | 10 |
| uppajjati | 0.67 | 20 | 10 |
| ārabbha | 0.62 | 22 | 10 |
| peta | 0.40 | 40 | 10 |
| pesa | 0.36 | 45 | 10 |
| samudda | 0.33 | 20 | 5 |
| tīra | 0.33 | 20 | 5 |
| orima | 0.33 | 20 | 5 |

### uddhacca

_pi blocks: 10; sense clusters: 4; inflected forms: uddhaccaṃ, uddhaccena_

#### cluster (1) — top co-lemma: **bhantatta** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhantatta | 0.46 | 3 | 3 |
| vikkhepa | 0.46 | 3 | 3 |
| avūpasama | 0.46 | 3 | 3 |

#### cluster (2) — top co-lemma: **māna** (cohesion 0.78, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| māna | 0.40 | 5 | 3 |
| thina | 0.35 | 7 | 3 |
| kilesavatthūni | 0.33 | 2 | 2 |

#### cluster (3) — top co-lemma: **kukkucca** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kukkucca | 0.33 | 2 | 2 |
| uddhaccakukkuccanīvaraṇa | 0.29 | 4 | 2 |

#### cluster (4) — top co-lemma: **anottappa** (cohesion 0.80, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anottappa | 0.33 | 20 | 5 |
| ahirika | 0.28 | 19 | 4 |

### atta

_pi blocks: 10; sense clusters: 2; inflected forms: attā, attānaṃ_

#### cluster (1) — top co-lemma: **cāti** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cāti | 0.71 | 7 | 6 |

#### cluster (2) — top co-lemma: **avinīta** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avinīta | 0.57 | 4 | 4 |
| ariyadhamma | 0.57 | 4 | 4 |
| rūpavanta | 0.57 | 4 | 4 |
| puthujjana | 0.57 | 4 | 4 |
| viññāṇavanta | 0.57 | 4 | 4 |
| samanupassati | 0.57 | 4 | 4 |
| sappurisadhamma | 0.57 | 4 | 4 |
| assutava | 0.57 | 4 | 4 |
| attata | 0.57 | 4 | 4 |

### gandha

_pi blocks: 10; sense clusters: 2; inflected forms: gandhamhi, gandhaṃ, gandho_

#### cluster (1) — top co-lemma: **ghāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghāna | 1.00 | 10 | 10 |

#### cluster (2) — top co-lemma: **pupphagandha** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pupphagandha | 0.57 | 4 | 4 |
| sāragandha | 0.57 | 4 | 4 |
| sugandha | 0.57 | 4 | 4 |
| phalagandha | 0.57 | 4 | 4 |
| vissagandha | 0.57 | 4 | 4 |
| tacagandha | 0.57 | 4 | 4 |
| pattagandha | 0.57 | 4 | 4 |
| āmakagandha | 0.57 | 4 | 4 |
| mūlagandha | 0.57 | 4 | 4 |

### ghāna

_pi blocks: 10; sense clusters: 2; inflected forms: ghānamhi, ghānaṃ, ghānena_

#### cluster (1) — top co-lemma: **gandha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gandha | 1.00 | 10 | 10 |

#### cluster (2) — top co-lemma: **pupphagandha** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pupphagandha | 0.57 | 4 | 4 |
| sāragandha | 0.57 | 4 | 4 |
| sugandha | 0.57 | 4 | 4 |
| phalagandha | 0.57 | 4 | 4 |
| vissagandha | 0.57 | 4 | 4 |
| tacagandha | 0.57 | 4 | 4 |
| pattagandha | 0.57 | 4 | 4 |
| āmakagandha | 0.57 | 4 | 4 |
| mūlagandha | 0.57 | 4 | 4 |

### jivha

_pi blocks: 10; sense clusters: 2; inflected forms: jivhaṃ, jivhā, jivhāya_

#### cluster (1) — top co-lemma: **rasa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasa | 0.75 | 6 | 6 |

#### cluster (2) — top co-lemma: **loṇika** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| loṇika | 0.57 | 4 | 4 |
| kaṭuka | 0.57 | 4 | 4 |
| madhura | 0.57 | 4 | 4 |
| puppharasa | 0.57 | 4 | 4 |
| phalarasa | 0.57 | 4 | 4 |
| asādu | 0.57 | 4 | 4 |
| lambila | 0.57 | 4 | 4 |
| kasāva | 0.57 | 4 | 4 |
| pattarasa | 0.57 | 4 | 4 |

### sadda

_pi blocks: 10; sense clusters: 2; inflected forms: saddamhi, saddaṃ, saddo_

#### cluster (1) — top co-lemma: **sota** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sota | 0.75 | 6 | 6 |

#### cluster (2) — top co-lemma: **saṅkhasadda** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṅkhasadda | 0.57 | 4 | 4 |
| vātasadda | 0.57 | 4 | 4 |
| paṇavasadda | 0.57 | 4 | 4 |
| pāṇisadda | 0.57 | 4 | 4 |
| gītasadda | 0.57 | 4 | 4 |
| manussasadda | 0.57 | 4 | 4 |
| nigghosasadda | 0.57 | 4 | 4 |
| amanussasadda | 0.57 | 4 | 4 |
| udakasadda | 0.57 | 4 | 4 |

### hirīyati

_pi blocks: 10; sense clusters: 4; inflected forms: hirīyati_

#### cluster (1) — top co-lemma: **hiriyitabba** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hiriyitabba | 1.00 | 10 | 10 |
| samāpattiya | 0.67 | 20 | 10 |
| pāpaka | 0.61 | 23 | 10 |
| akusala | 0.15 | 123 | 10 |

#### cluster (2) — top co-lemma: **hiribala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hiribala | 0.23 | 16 | 3 |

#### cluster (3) — top co-lemma: **hirī** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hirī | 0.22 | 17 | 3 |

#### cluster (4) — top co-lemma: **ahirika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirika | 0.21 | 19 | 3 |

### ottappati

_pi blocks: 10; sense clusters: 5; inflected forms: ottappati_

#### cluster (1) — top co-lemma: **ottappitabba** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappitabba | 1.00 | 10 | 10 |
| samāpattiya | 0.67 | 20 | 10 |
| pāpaka | 0.61 | 23 | 10 |
| akusala | 0.15 | 123 | 10 |

#### cluster (2) — top co-lemma: **ottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappa | 0.25 | 14 | 3 |

#### cluster (3) — top co-lemma: **ottappabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.23 | 16 | 3 |

#### cluster (4) — top co-lemma: **anottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anottappa | 0.20 | 20 | 3 |

#### cluster (5) — top co-lemma: **imāni** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| imāni | 0.10 | 10 | 1 |

### pītisahagata

_pi blocks: 10; sense clusters: 4; inflected forms: pītisahagataṃ, pītisahagatā_

#### cluster (1) — top co-lemma: **pītiṃ** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pītiṃ | 0.50 | 6 | 4 |
| lokuttaradukatikajjhāna | 0.31 | 3 | 2 |
| rūpāvacaradukatikajjhāna | 0.31 | 3 | 2 |
| somanassasahagatacittuppāda | 0.24 | 7 | 2 |

#### cluster (2) — top co-lemma: **pītibhūmiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| pītibhūmiya | 0.46 | 3 | 3 |

#### cluster (3) — top co-lemma: **kāmāvacarakusalata** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakusalata | 0.31 | 16 | 4 |
| kāmāvacarakusala | 0.27 | 20 | 4 |
| upekkhāsahagatacittuppāda | 0.25 | 6 | 2 |
| āruppa | 0.21 | 9 | 2 |

#### cluster (4) — top co-lemma: **sukhasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sukhasahagata | 0.29 | 11 | 3 |

### kāyika

_pi blocks: 10; sense clusters: 3; inflected forms: kāyikaṃ, kāyiko_

#### cluster (1) — top co-lemma: **vācasika** (cohesion 0.85, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vācasika | 0.57 | 4 | 4 |
| kāyikavācasika | 0.57 | 4 | 4 |
| avītikkama | 0.46 | 3 | 3 |
| sīlasaṃvara | 0.46 | 3 | 3 |
| sabbopi | 0.46 | 3 | 3 |

#### cluster (2) — top co-lemma: **kāyasamphassaja** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyasamphassaja | 0.52 | 13 | 6 |
| asāta | 0.38 | 6 | 3 |
| vedayita | 0.24 | 41 | 6 |
| dukkha | 0.20 | 20 | 3 |

#### cluster (3) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.29 | 4 | 2 |

### sakkāyadiṭṭhi

_pi blocks: 10; sense clusters: 2; inflected forms: sakkāyadiṭṭhi_

#### cluster (1) — top co-lemma: **sīlabbataparāmāsa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sīlabbataparāmāsa | 0.50 | 14 | 6 |

#### cluster (2) — top co-lemma: **avinīta** (cohesion 1.00, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avinīta | 0.43 | 4 | 3 |
| ariyadhamma | 0.43 | 4 | 3 |
| rūpavanta | 0.43 | 4 | 3 |
| puthujjana | 0.43 | 4 | 3 |
| viññāṇavanta | 0.43 | 4 | 3 |
| samanupassati | 0.43 | 4 | 3 |
| sappurisadhamma | 0.43 | 4 | 3 |
| assutava | 0.43 | 4 | 3 |
| attata | 0.43 | 4 | 3 |

### manodhātu

_pi blocks: 10; sense clusters: 3; inflected forms: manodhātu_

#### cluster (1) — top co-lemma: **tīṇindriya** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tīṇindriya | 0.32 | 9 | 3 |
| dhātuya | 0.18 | 35 | 4 |
| dhammadhātu | 0.17 | 37 | 4 |

#### cluster (2) — top co-lemma: **sotaviññāṇa** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotaviññāṇa | 0.25 | 6 | 2 |
| ghānaviññāṇa | 0.25 | 6 | 2 |
| jivhāviññāṇa | 0.25 | 6 | 2 |

#### cluster (3) — top co-lemma: **phoṭṭhabbārammaṇa** (cohesion 0.67, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| phoṭṭhabbārammaṇa | 0.22 | 17 | 3 |
| upekkhindriya | 0.20 | 20 | 3 |
| vitakka | 0.17 | 59 | 6 |
| vicāra | 0.17 | 59 | 6 |

### diṭṭhigatasampayutta

_pi blocks: 10; sense clusters: 2; inflected forms: diṭṭhigatasampayuttaṃ, diṭṭhigatasampayuttesu_

#### cluster (1) — top co-lemma: **lobhasahagata** (cohesion 0.65, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagata | 0.59 | 7 | 5 |
| aṭṭhasu | 0.59 | 7 | 5 |
| sabbākusala | 0.40 | 5 | 3 |
| uppajjati | 0.40 | 20 | 6 |
| diṭṭhigatavippayuttalobhasahagata | 0.35 | 7 | 3 |
| dvīsu | 0.32 | 9 | 3 |
| domanassasahagata | 0.29 | 11 | 3 |
| cittuppāda | 0.24 | 40 | 6 |
| uppajjanti | 0.24 | 24 | 4 |

#### cluster (2) — top co-lemma: **dhammārammaṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhammārammaṇa | 0.22 | 26 | 4 |

### pañcaṅgika

_pi blocks: 10; sense clusters: 2; inflected forms: pañcaṅgikaṃ, pañcaṅgiko_

#### cluster (1) — top co-lemma: **bala** (cohesion 1.00, 8 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bala | 0.32 | 27 | 6 |
| dvāyatana | 0.29 | 32 | 6 |
| ekaṃ | 0.27 | 34 | 6 |
| ekā | 0.27 | 35 | 6 |
| dhātuya | 0.27 | 35 | 6 |
| dhammadhātu | 0.26 | 37 | 6 |
| khandha | 0.25 | 38 | 6 |
| dhammāyatana | 0.24 | 39 | 6 |

#### cluster (2) — top co-lemma: **sammāsamādhi** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sammāsamādhi | 0.24 | 32 | 5 |
| avisāhaṭamānasata | 0.24 | 24 | 4 |

### cetayitatta

_pi blocks: 10; sense clusters: 5; inflected forms: cetayitattaṃ_

#### cluster (1) — top co-lemma: **sañcetana** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sañcetana | 1.00 | 10 | 10 |
| tajjāmanoviññāṇadhātusamphassaja | 0.36 | 18 | 5 |
| cetana | 0.19 | 98 | 10 |

#### cluster (2) — top co-lemma: **manosañcetanāhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manosañcetanāhāra | 0.15 | 3 | 1 |

#### cluster (3) — top co-lemma: **tajjācakkhuviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātusamphassaja | 0.15 | 3 | 1 |

#### cluster (4) — top co-lemma: **tajjāmanodhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanodhātusamphassaja | 0.15 | 3 | 1 |

#### cluster (5) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.14 | 4 | 1 |

### diṭṭhigatasampayuttacittuppāda

_pi blocks: 10; sense clusters: 5; inflected forms: diṭṭhigatasampayuttacittuppādā_

#### cluster (1) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 0.60, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.37 | 17 | 5 |
| siya | 0.31 | 16 | 4 |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.30 | 10 | 3 |

#### cluster (2) — top co-lemma: **vicikicchāsahagata** (cohesion 0.78, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicikicchāsahagata | 0.33 | 26 | 6 |
| cittuppāda | 0.24 | 40 | 6 |
| dassana | 0.21 | 28 | 4 |

#### cluster (3) — top co-lemma: **moha** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.22 | 8 | 2 |
| pahātabbahetuka | 0.20 | 20 | 3 |

#### cluster (4) — top co-lemma: **etthuppanna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| etthuppanna | 0.22 | 27 | 4 |

#### cluster (5) — top co-lemma: **aniyata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aniyata | 0.21 | 9 | 2 |

### diṭṭhigatavippayuttalobhasahagatacittuppāda

_pi blocks: 10; sense clusters: 6; inflected forms: diṭṭhigatavippayuttalobhasahagatacittuppādā_

#### cluster (1) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 0.57, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.52 | 17 | 7 |
| siya | 0.31 | 16 | 4 |

#### cluster (2) — top co-lemma: **vicikicchāsahagata** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicikicchāsahagata | 0.33 | 26 | 6 |
| uddhaccasahagata | 0.32 | 27 | 6 |
| cittuppāda | 0.32 | 40 | 8 |

#### cluster (3) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.30 | 10 | 3 |

#### cluster (4) — top co-lemma: **parāmāsavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsavippayutta | 0.22 | 8 | 2 |

#### cluster (5) — top co-lemma: **moha** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.22 | 8 | 2 |
| etthuppanna | 0.22 | 27 | 4 |

#### cluster (6) — top co-lemma: **aniyata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aniyata | 0.21 | 9 | 2 |

### hiriyitabba

_pi blocks: 10; sense clusters: 4; inflected forms: hiriyitabbena_

#### cluster (1) — top co-lemma: **hirīyati** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hirīyati | 1.00 | 10 | 10 |
| samāpattiya | 0.67 | 20 | 10 |
| pāpaka | 0.61 | 23 | 10 |
| akusala | 0.15 | 123 | 10 |

#### cluster (2) — top co-lemma: **hiribala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hiribala | 0.23 | 16 | 3 |

#### cluster (3) — top co-lemma: **hirī** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hirī | 0.22 | 17 | 3 |

#### cluster (4) — top co-lemma: **ahirika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahirika | 0.21 | 19 | 3 |

### imāni

_pi blocks: 10; sense clusters: 1; inflected forms: imāni_

#### cluster (1) — top co-lemma: **tadekaṭṭha** (cohesion 0.78, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tadekaṭṭha | 0.35 | 13 | 4 |
| manokamma | 0.33 | 14 | 4 |
| kāyakamma | 0.33 | 14 | 4 |
| vacīkamma | 0.33 | 14 | 4 |
| taṃsamuṭṭha | 0.33 | 14 | 4 |
| pahātabbahetū | 0.29 | 4 | 2 |
| suddhīti | 0.27 | 5 | 2 |
| tīṇi | 0.27 | 20 | 4 |
| sīlabbataparāmāsa | 0.25 | 14 | 3 |
| pahātabba | 0.25 | 22 | 4 |

### kusalahetū

_pi blocks: 10; sense clusters: 6; inflected forms: kusalahetū_

#### cluster (1) — top co-lemma: **abyākatahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abyākatahetū | 0.67 | 8 | 6 |

#### cluster (2) — top co-lemma: **akusalahetū** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusalahetū | 0.40 | 5 | 3 |
| kāmāvacarahetū | 0.33 | 2 | 2 |

#### cluster (3) — top co-lemma: **rūpāvacarahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacarahetū | 0.33 | 2 | 2 |

#### cluster (4) — top co-lemma: **arūpāvacarahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpāvacarahetū | 0.33 | 2 | 2 |

#### cluster (5) — top co-lemma: **apariyāpannahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apariyāpannahetū | 0.31 | 3 | 2 |

#### cluster (6) — top co-lemma: **ñāṇa** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇa | 0.24 | 7 | 2 |
| dukkhanirodhagāminiya | 0.24 | 7 | 2 |
| dukkhanirodha | 0.24 | 7 | 2 |
| dukkhasamudaya | 0.24 | 7 | 2 |

### ottappitabba

_pi blocks: 10; sense clusters: 5; inflected forms: ottappitabbena_

#### cluster (1) — top co-lemma: **ottappati** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappati | 1.00 | 10 | 10 |
| samāpattiya | 0.67 | 20 | 10 |
| pāpaka | 0.61 | 23 | 10 |
| akusala | 0.15 | 123 | 10 |

#### cluster (2) — top co-lemma: **ottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappa | 0.25 | 14 | 3 |

#### cluster (3) — top co-lemma: **ottappabala** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ottappabala | 0.23 | 16 | 3 |

#### cluster (4) — top co-lemma: **anottappa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anottappa | 0.20 | 20 | 3 |

#### cluster (5) — top co-lemma: **imāni** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| imāni | 0.10 | 10 | 1 |

### patiṭṭhāha

_pi blocks: 10; sense clusters: 1; inflected forms: patiṭṭhāho_

#### cluster (1) — top co-lemma: **micchāpatha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchāpatha | 0.83 | 14 | 10 |
| diṭṭhivisūkāyika | 0.83 | 14 | 10 |
| abhinivesa | 0.83 | 14 | 10 |
| gāha | 0.83 | 14 | 10 |
| diṭṭhigahana | 0.83 | 14 | 10 |
| titthāyatana | 0.83 | 14 | 10 |
| micchatta | 0.83 | 14 | 10 |
| diṭṭhivipphandita | 0.83 | 14 | 10 |
| diṭṭhikantāra | 0.83 | 14 | 10 |
| kummagga | 0.83 | 14 | 10 |

### paṭipada

_pi blocks: 10; sense clusters: 1; inflected forms: paṭipadā, paṭipadāya_

#### cluster (1) — top co-lemma: **dukkhanirodhagāminiya** (cohesion 0.85, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dukkhanirodhagāminiya | 0.82 | 7 | 7 |
| dukkhanirodha | 0.82 | 7 | 7 |
| dukkhasamudaya | 0.82 | 7 | 7 |
| idappaccayata | 0.67 | 11 | 7 |
| pubbantāparanta | 0.67 | 11 | 7 |
| apaccavekkhaṇa | 0.67 | 5 | 5 |
| pubbanta | 0.64 | 12 | 7 |
| avijjogha | 0.62 | 6 | 5 |
| sammoha | 0.62 | 6 | 5 |
| apaccakkhakamma | 0.62 | 6 | 5 |

### sañcetana

_pi blocks: 10; sense clusters: 5; inflected forms: sañcetanā_

#### cluster (1) — top co-lemma: **cetayitatta** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cetayitatta | 1.00 | 10 | 10 |
| tajjāmanoviññāṇadhātusamphassaja | 0.36 | 18 | 5 |
| cetana | 0.19 | 98 | 10 |

#### cluster (2) — top co-lemma: **manosañcetanāhāra** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| manosañcetanāhāra | 0.15 | 3 | 1 |

#### cluster (3) — top co-lemma: **tajjācakkhuviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjācakkhuviññāṇadhātusamphassaja | 0.15 | 3 | 1 |

#### cluster (4) — top co-lemma: **tajjāmanodhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjāmanodhātusamphassaja | 0.15 | 3 | 1 |

#### cluster (5) — top co-lemma: **tajjākāyaviññāṇadhātusamphassaja** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tajjākāyaviññāṇadhātusamphassaja | 0.14 | 4 | 1 |

### kilesasampayutta

_pi blocks: 9; sense clusters: 8; inflected forms: kilesasampayutto, kilesasampayuttā_

#### cluster (1) — top co-lemma: **kilesavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesavippayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **kilesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesa | 0.23 | 34 | 5 |

#### cluster (3) — top co-lemma: **kilesātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesātipi | 0.17 | 3 | 1 |

#### cluster (4) — top co-lemma: **māna** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| māna | 0.14 | 5 | 1 |
| thina | 0.12 | 7 | 1 |

#### cluster (5) — top co-lemma: **asaṃkilesika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkilesika | 0.13 | 6 | 1 |

#### cluster (6) — top co-lemma: **akusalacittuppāda** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusalacittuppāda | 0.13 | 6 | 1 |
| dvādasa | 0.12 | 7 | 1 |

#### cluster (7) — top co-lemma: **sampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampayutta | 0.13 | 22 | 2 |

#### cluster (8) — top co-lemma: **yattha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yattha | 0.12 | 8 | 1 |

### āsavasampayutta

_pi blocks: 9; sense clusters: 7; inflected forms: āsavasampayutto, āsavasampayuttā_

#### cluster (1) — top co-lemma: **āsava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsava | 0.38 | 17 | 5 |

#### cluster (2) — top co-lemma: **āsavavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavavippayutta | 0.33 | 9 | 3 |

#### cluster (3) — top co-lemma: **āsavātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavātipi | 0.18 | 2 | 1 |

#### cluster (4) — top co-lemma: **avijjāsava** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avijjāsava | 0.15 | 4 | 1 |
| diṭṭhāsava | 0.15 | 4 | 1 |
| bhavāsava | 0.15 | 4 | 1 |
| kāmāsava | 0.15 | 4 | 1 |

#### cluster (5) — top co-lemma: **anāsava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anāsava | 0.13 | 6 | 1 |

#### cluster (6) — top co-lemma: **sampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampayutta | 0.13 | 22 | 2 |

#### cluster (7) — top co-lemma: **moha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| moha | 0.12 | 8 | 1 |

### ganthasampayutta

_pi blocks: 9; sense clusters: 6; inflected forms: ganthasampayutto, ganthasampayuttā_

#### cluster (1) — top co-lemma: **gantha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| gantha | 0.36 | 19 | 5 |

#### cluster (2) — top co-lemma: **ganthavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthavippayutta | 0.33 | 9 | 3 |

#### cluster (3) — top co-lemma: **abhijjhākāyagantha** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| abhijjhākāyagantha | 0.18 | 2 | 1 |
| idaṃsaccābhinivesa | 0.17 | 3 | 1 |

#### cluster (4) — top co-lemma: **ganthātipi** (cohesion 0.75, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthātipi | 0.18 | 2 | 1 |
| domanassasahagatacittuppāda | 0.15 | 17 | 2 |
| lobhasahagatacittuppāda | 0.15 | 4 | 1 |
| aṭṭha | 0.13 | 6 | 1 |

#### cluster (5) — top co-lemma: **aganthaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aganthaniya | 0.13 | 6 | 1 |

#### cluster (6) — top co-lemma: **sampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampayutta | 0.13 | 22 | 2 |

### nīvaraṇasampayutta

_pi blocks: 9; sense clusters: 4; inflected forms: nīvaraṇasampayuttā_

#### cluster (1) — top co-lemma: **nīvaraṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇa | 0.36 | 19 | 5 |

#### cluster (2) — top co-lemma: **nīvaraṇavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇavippayutta | 0.33 | 9 | 3 |

#### cluster (3) — top co-lemma: **nīvaraṇātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇātipi | 0.18 | 2 | 1 |

#### cluster (4) — top co-lemma: **uddhaccanīvaraṇa** (cohesion 1.00, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccanīvaraṇa | 0.18 | 2 | 1 |
| kukkuccanīvaraṇa | 0.18 | 2 | 1 |
| byāpādanīvaraṇa | 0.15 | 4 | 1 |
| kāmacchandanīvaraṇa | 0.15 | 4 | 1 |
| avijjānīvaraṇa | 0.15 | 4 | 1 |
| vicikicchānīvaraṇa | 0.15 | 4 | 1 |
| thinamiddhanīvaraṇa | 0.14 | 5 | 1 |

### saṃyojanasampayutta

_pi blocks: 9; sense clusters: 4; inflected forms: saṃyojanasampayuttā_

#### cluster (1) — top co-lemma: **saṃyojanavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanavippayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **saṃyojana** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojana | 0.30 | 24 | 5 |

#### cluster (3) — top co-lemma: **saṃyojanātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanātipi | 0.18 | 2 | 1 |

#### cluster (4) — top co-lemma: **macchariyasaṃyojana** (cohesion 1.00, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| macchariyasaṃyojana | 0.15 | 4 | 1 |
| vicikicchāsaṃyojana | 0.15 | 4 | 1 |
| issāsaṃyojana | 0.15 | 4 | 1 |
| bhavarāgasaṃyojana | 0.15 | 4 | 1 |
| kāmarāgasaṃyojana | 0.15 | 4 | 1 |
| mānasaṃyojana | 0.15 | 4 | 1 |
| avijjāsaṃyojana | 0.15 | 4 | 1 |

### upādānasampayutta

_pi blocks: 9; sense clusters: 5; inflected forms: upādānasampayuttā_

#### cluster (1) — top co-lemma: **upādāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādāna | 0.40 | 16 | 5 |

#### cluster (2) — top co-lemma: **upādānavippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānavippayutta | 0.33 | 9 | 3 |

#### cluster (3) — top co-lemma: **upādānātipi** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānātipi | 0.18 | 2 | 1 |
| lobhasahagatacittuppāda | 0.15 | 4 | 1 |
| aṭṭha | 0.13 | 6 | 1 |

#### cluster (4) — top co-lemma: **kāmupāda** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmupāda | 0.15 | 4 | 1 |
| diṭṭhupāda | 0.15 | 4 | 1 |
| attavādupāda | 0.15 | 4 | 1 |
| sīlabbatupāda | 0.15 | 4 | 1 |

#### cluster (5) — top co-lemma: **anupādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādāniya | 0.13 | 6 | 1 |

### ganthavippayutta

_pi blocks: 9; sense clusters: 6; inflected forms: ganthavippayuttā_

#### cluster (1) — top co-lemma: **ganthasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **aganthaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aganthaniya | 0.27 | 6 | 2 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagata** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagata | 0.25 | 7 | 2 |
| paṭigha | 0.24 | 8 | 2 |
| dvīsu | 0.22 | 9 | 2 |
| domanassasahagata | 0.20 | 11 | 2 |

#### cluster (4) — top co-lemma: **ganthaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthaniya | 0.20 | 11 | 2 |

#### cluster (5) — top co-lemma: **ganthātipi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ganthātipi | 0.18 | 2 | 1 |
| lobhasahagatacittuppāda | 0.15 | 4 | 1 |

#### cluster (6) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

### kilesavippayutta

_pi blocks: 9; sense clusters: 5; inflected forms: kilesavippayuttā_

#### cluster (1) — top co-lemma: **kilesasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **asaṃkilesika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkilesika | 0.27 | 6 | 2 |

#### cluster (3) — top co-lemma: **saṃkilesika** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃkilesika | 0.20 | 11 | 2 |
| kusalābyākata | 0.11 | 9 | 1 |

#### cluster (4) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

#### cluster (5) — top co-lemma: **kilesātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesātipi | 0.17 | 3 | 1 |

### nīvaraṇavippayutta

_pi blocks: 9; sense clusters: 5; inflected forms: nīvaraṇavippayuttā_

#### cluster (1) — top co-lemma: **nīvaraṇasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **anīvaraṇiya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anīvaraṇiya | 0.27 | 6 | 2 |

#### cluster (3) — top co-lemma: **nīvaraṇiya** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇiya | 0.20 | 11 | 2 |
| kusalābyākata | 0.11 | 9 | 1 |

#### cluster (4) — top co-lemma: **nīvaraṇātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| nīvaraṇātipi | 0.18 | 2 | 1 |

#### cluster (5) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

### saṃyojanavippayutta

_pi blocks: 9; sense clusters: 6; inflected forms: saṃyojanavippayuttā_

#### cluster (1) — top co-lemma: **saṃyojanasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **asaṃyojaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃyojaniya | 0.27 | 6 | 2 |

#### cluster (3) — top co-lemma: **saṃyojaniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojaniya | 0.20 | 11 | 2 |

#### cluster (4) — top co-lemma: **saṃyojanātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| saṃyojanātipi | 0.18 | 2 | 1 |

#### cluster (5) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

#### cluster (6) — top co-lemma: **uddhaccasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.11 | 27 | 2 |

### upādānavippayutta

_pi blocks: 9; sense clusters: 6; inflected forms: upādānavippayuttā_

#### cluster (1) — top co-lemma: **upādānasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **anupādāniya** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anupādāniya | 0.27 | 6 | 2 |
| dutiyabhāṇavāra | 0.18 | 2 | 1 |
| nikkhepakaṇḍa | 0.17 | 3 | 1 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagata** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagata | 0.25 | 7 | 2 |
| domanassasahagatacittuppāda | 0.15 | 17 | 2 |

#### cluster (4) — top co-lemma: **upādāniya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādāniya | 0.20 | 11 | 2 |

#### cluster (5) — top co-lemma: **upādānātipi** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upādānātipi | 0.18 | 2 | 1 |
| lobhasahagatacittuppāda | 0.15 | 4 | 1 |

#### cluster (6) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

### āsavavippayutta

_pi blocks: 9; sense clusters: 5; inflected forms: āsavavippayuttā_

#### cluster (1) — top co-lemma: **āsavasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavasampayutta | 0.33 | 9 | 3 |

#### cluster (2) — top co-lemma: **anāsava** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anāsava | 0.27 | 6 | 2 |
| paṭhamabhāṇavāra | 0.17 | 3 | 1 |
| nikkhepakaṇḍa | 0.17 | 3 | 1 |

#### cluster (3) — top co-lemma: **dvīsu** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dvīsu | 0.22 | 9 | 2 |
| domanassasahagata | 0.20 | 11 | 2 |
| vicikicchāsahagata | 0.11 | 26 | 2 |
| uddhaccasahagata | 0.11 | 27 | 2 |

#### cluster (4) — top co-lemma: **āsavātipi** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| āsavātipi | 0.18 | 2 | 1 |

#### cluster (5) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

### aniyata

_pi blocks: 9; sense clusters: 5; inflected forms: aniyataṃ, aniyatā_

#### cluster (1) — top co-lemma: **micchattaniyata** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| micchattaniyata | 0.33 | 3 | 2 |
| sammattaniyata | 0.17 | 3 | 1 |

#### cluster (2) — top co-lemma: **niyata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| niyata | 0.29 | 5 | 2 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.21 | 10 | 2 |

#### cluster (4) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.21 | 10 | 2 |
| siya | 0.16 | 16 | 2 |

#### cluster (5) — top co-lemma: **ekavidha** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.18 | 2 | 1 |
| ācayagāmi | 0.17 | 3 | 1 |
| nevasekkhanāsekkha | 0.15 | 4 | 1 |
| nevavipākanavipākadhammadhamma | 0.15 | 4 | 1 |

### dvīsu

_pi blocks: 9; sense clusters: 4; inflected forms: dvīsu_

#### cluster (1) — top co-lemma: **domanassasahagata** (cohesion 0.85, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagata | 0.90 | 11 | 9 |
| vicikicchāsahagata | 0.40 | 26 | 7 |
| cittuppāda | 0.37 | 40 | 9 |

#### cluster (2) — top co-lemma: **lobhasahagata** (cohesion 0.76, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lobhasahagata | 0.62 | 7 | 5 |
| aṭṭhasu | 0.62 | 7 | 5 |
| sabbākusala | 0.57 | 5 | 4 |
| uppajjati | 0.34 | 20 | 5 |
| diṭṭhigatasampayutta | 0.32 | 10 | 3 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagata | 0.50 | 7 | 4 |

#### cluster (4) — top co-lemma: **sasaṅkhārika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhārika | 0.36 | 2 | 2 |

### avijja

_pi blocks: 9; sense clusters: 1; inflected forms: avijjā, avijjāya_

#### cluster (1) — top co-lemma: **aññāṇa** (cohesion 0.93, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññāṇa | 0.82 | 8 | 7 |
| adassana | 0.82 | 8 | 7 |
| avijjālaṅgī | 0.82 | 8 | 7 |
| ananubodha | 0.80 | 6 | 6 |
| avijjogha | 0.80 | 6 | 6 |
| sammoha | 0.80 | 6 | 6 |
| apaccakkhakamma | 0.80 | 6 | 6 |
| anabhisamaya | 0.80 | 6 | 6 |
| avijjāpariyuṭṭha | 0.80 | 6 | 6 |
| avijjāyoga | 0.80 | 6 | 6 |

### pathavīdhātu

_pi blocks: 9; sense clusters: 1; inflected forms: pathavīdhātu_

#### cluster (1) — top co-lemma: **kakkhaḷa** (cohesion 0.81, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kakkhaḷa | 0.71 | 5 | 5 |
| tejodhātu | 0.67 | 6 | 5 |
| vāyodhātu | 0.67 | 6 | 5 |
| saṇha | 0.62 | 4 | 4 |
| lahuka | 0.62 | 4 | 4 |
| muduka | 0.62 | 4 | 4 |
| pharusa | 0.62 | 4 | 4 |
| garuka | 0.62 | 4 | 4 |
| phoṭṭhabbadhātu | 0.61 | 14 | 7 |
| sukhasamphassa | 0.53 | 6 | 4 |

### arūpīna

_pi blocks: 9; sense clusters: 1; inflected forms: arūpīnaṃ_

#### cluster (1) — top co-lemma: **vattana** (cohesion 0.91, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vattana | 0.78 | 14 | 9 |
| āyu | 0.78 | 14 | 9 |
| jīvita | 0.78 | 14 | 9 |
| iriyana | 0.78 | 14 | 9 |
| yapana | 0.78 | 14 | 9 |
| pālana | 0.78 | 14 | 9 |
| yāpana | 0.75 | 15 | 9 |
| tīṇindriya | 0.56 | 9 | 5 |
| tesa | 0.49 | 28 | 9 |
| ṭhiti | 0.32 | 47 | 9 |

### kusalābyākata

_pi blocks: 9; sense clusters: 6; inflected forms: kusalābyākatā_

#### cluster (1) — top co-lemma: **mahaggata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| mahaggata | 0.31 | 4 | 2 |

#### cluster (2) — top co-lemma: **rūpakkhandha** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpakkhandha | 0.22 | 28 | 4 |
| vippayutta | 0.17 | 15 | 2 |
| sāsava | 0.17 | 39 | 4 |

#### cluster (3) — top co-lemma: **arūpāvacara** (cohesion 0.85, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpāvacara | 0.19 | 88 | 9 |
| rūpāvacara | 0.16 | 102 | 9 |
| kāmāvacara | 0.11 | 115 | 7 |

#### cluster (4) — top co-lemma: **araṇa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| araṇa | 0.17 | 3 | 1 |

#### cluster (5) — top co-lemma: **asaṃkiliṭṭhasaṃkilesika** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkiliṭṭhasaṃkilesika | 0.15 | 4 | 1 |

#### cluster (6) — top co-lemma: **asaṃkiliṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkiliṭṭha | 0.15 | 4 | 1 |

### rūpāvacaratikacatukkajjhāna

_pi blocks: 9; sense clusters: 3; inflected forms: rūpāvacaratikacatukkajjhānā_

#### cluster (1) — top co-lemma: **lokuttaratikacatukkajjhāna** (cohesion 0.66, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lokuttaratikacatukkajjhāna | 0.71 | 5 | 5 |
| somanassasahagatacittuppāda | 0.50 | 7 | 4 |
| kāmāvacarakusalata | 0.48 | 16 | 6 |
| vipākata | 0.42 | 34 | 9 |
| pañca | 0.36 | 13 | 4 |

#### cluster (2) — top co-lemma: **anārammaṇa** (cohesion 0.71, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anārammaṇa | 0.47 | 8 | 4 |
| kiriyāhetukamanoviññāṇadhātu | 0.46 | 4 | 3 |
| ākāsānañcāyatana | 0.38 | 7 | 3 |
| ākiñcaññāyatana | 0.38 | 7 | 3 |

#### cluster (3) — top co-lemma: **ñāṇavippayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇavippayuttacittuppāda | 0.36 | 2 | 2 |

### samaṇabrāhmaṇa

_pi blocks: 9; sense clusters: 2; inflected forms: samaṇabrāhmaṇā, samaṇabrāhmaṇānaṃ_

#### cluster (1) — top co-lemma: **sīlabbata** (cohesion 0.92, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sīlabbata | 0.80 | 6 | 6 |
| suddhi | 0.80 | 6 | 6 |
| sīla | 0.80 | 6 | 6 |
| suddhīti | 0.71 | 5 | 5 |

#### cluster (2) — top co-lemma: **sacchikatva** (cohesion 1.00, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sacchikatva | 0.50 | 3 | 3 |
| pita | 0.50 | 3 | 3 |
| opapātika | 0.50 | 3 | 3 |
| māta | 0.50 | 3 | 3 |
| dinna | 0.50 | 3 | 3 |
| pavedentīti | 0.50 | 3 | 3 |

### tīṇindriya

_pi blocks: 9; sense clusters: 1; inflected forms: tīṇindriyāni_

#### cluster (1) — top co-lemma: **arūpīna** (cohesion 0.84, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpīna | 0.56 | 9 | 5 |
| dvāyatana | 0.44 | 32 | 9 |
| yapana | 0.43 | 14 | 5 |
| pālana | 0.43 | 14 | 5 |
| vattana | 0.43 | 14 | 5 |
| āyu | 0.43 | 14 | 5 |
| jīvita | 0.43 | 14 | 5 |
| iriyana | 0.43 | 14 | 5 |
| ekaṃ | 0.42 | 34 | 9 |
| yāpana | 0.42 | 15 | 5 |

### āruppa

_pi blocks: 9; sense clusters: 3; inflected forms: āruppā_

#### cluster (1) — top co-lemma: **upekkhāsahagatacittuppāda** (cohesion 0.74, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| upekkhāsahagatacittuppāda | 0.67 | 6 | 5 |
| kāmāvacarakusalata | 0.48 | 16 | 6 |
| vipākata | 0.42 | 34 | 9 |
| kāmāvacarakusala | 0.34 | 20 | 5 |

#### cluster (2) — top co-lemma: **aṭṭha** (cohesion 0.83, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aṭṭha | 0.40 | 6 | 3 |
| lokuttaradukadukajjhāna | 0.36 | 2 | 2 |
| rūpāvacaradukadukajjhāna | 0.36 | 2 | 2 |
| ekādasa | 0.29 | 5 | 2 |

#### cluster (3) — top co-lemma: **lokuttaratikatikajjhāna** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| lokuttaratikatikajjhāna | 0.36 | 2 | 2 |
| rūpāvacaratikatikajjhāna | 0.36 | 2 | 2 |

### aññāṇa

_pi blocks: 8; sense clusters: 1; inflected forms: aññāṇaṃ_

#### cluster (1) — top co-lemma: **adassana** (cohesion 0.89, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| adassana | 1.00 | 8 | 8 |
| avijjālaṅgī | 1.00 | 8 | 8 |
| asampajañña | 0.93 | 7 | 7 |
| ananubodha | 0.86 | 6 | 6 |
| avijjogha | 0.86 | 6 | 6 |
| sammoha | 0.86 | 6 | 6 |
| apaccakkhakamma | 0.86 | 6 | 6 |
| anabhisamaya | 0.86 | 6 | 6 |
| avijjāpariyuṭṭha | 0.86 | 6 | 6 |
| avijjāyoga | 0.86 | 6 | 6 |

### chandādhipateyyanti

_pi blocks: 8; sense clusters: 1; inflected forms: chandādhipateyyanti_

#### cluster (1) — top co-lemma: **animitta** (cohesion 0.87, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| animitta | 0.57 | 20 | 8 |
| appaṇihita | 0.36 | 36 | 8 |
| suññata | 0.36 | 37 | 8 |
| pañcama | 0.33 | 40 | 8 |
| tatiya | 0.29 | 47 | 8 |
| dutiya | 0.27 | 51 | 8 |
| vūpasama | 0.22 | 38 | 5 |
| vitakkavicāra | 0.21 | 40 | 5 |
| catuttha | 0.20 | 72 | 8 |
| bhūmiya | 0.19 | 75 | 8 |

### hetusampayutta

_pi blocks: 8; sense clusters: 6; inflected forms: hetusampayutto, hetusampayuttā_

#### cluster (1) — top co-lemma: **hetuvippayutta** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hetuvippayutta | 0.31 | 5 | 2 |
| hetūtipi | 0.20 | 2 | 1 |

#### cluster (2) — top co-lemma: **kāmāvacarakiriyata** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakiriyata | 0.29 | 6 | 2 |
| moha | 0.12 | 8 | 1 |

#### cluster (3) — top co-lemma: **aññamañña** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññamañña | 0.20 | 2 | 1 |

#### cluster (4) — top co-lemma: **hetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hetū | 0.19 | 44 | 5 |

#### cluster (5) — top co-lemma: **sampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sampayutta | 0.13 | 22 | 2 |

#### cluster (6) — top co-lemma: **yattha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yattha | 0.12 | 8 | 1 |

### cittasamuṭṭha

_pi blocks: 8; sense clusters: 2; inflected forms: cittasamuṭṭhānaṃ_

#### cluster (1) — top co-lemma: **cittahetuka** (cohesion 0.94, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittahetuka | 0.86 | 6 | 6 |
| cittaja | 0.86 | 6 | 6 |
| kammaññata | 0.33 | 34 | 7 |
| lahuta | 0.33 | 34 | 7 |
| muduta | 0.33 | 35 | 7 |
| saddāyatana | 0.27 | 44 | 7 |
| ākāsadhātu | 0.26 | 46 | 7 |
| gandhāyatana | 0.22 | 55 | 7 |
| āpodhātu | 0.22 | 57 | 7 |

#### cluster (2) — top co-lemma: **cittasamuṭṭhāna** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittasamuṭṭhāna | 0.31 | 5 | 2 |

### ñāṇavippayutta

_pi blocks: 8; sense clusters: 4; inflected forms: ñāṇavippayuttaṃ, ñāṇavippayutte, ñāṇavippayuttā_

#### cluster (1) — top co-lemma: **sasaṅkhāra** (cohesion 0.74, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.50 | 12 | 5 |
| somanassasahagata | 0.38 | 18 | 5 |
| dhammārammaṇa | 0.35 | 26 | 6 |
| panārabbha | 0.32 | 30 | 6 |
| rūpārammaṇa | 0.29 | 34 | 6 |
| uppanna | 0.25 | 49 | 7 |

#### cluster (2) — top co-lemma: **sattindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sattindriya | 0.40 | 2 | 2 |

#### cluster (3) — top co-lemma: **ñāṇasampayutta** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇasampayutta | 0.38 | 8 | 3 |
| abyākatamūla | 0.36 | 3 | 2 |

#### cluster (4) — top co-lemma: **alobha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| alobha | 0.25 | 32 | 5 |

### saṃkiliṭṭha

_pi blocks: 8; sense clusters: 3; inflected forms: saṃkiliṭṭhā_

#### cluster (1) — top co-lemma: **asaṃkiliṭṭha** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| asaṃkiliṭṭha | 0.33 | 4 | 2 |
| kilesātipi | 0.18 | 3 | 1 |

#### cluster (2) — top co-lemma: **kilesa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kilesa | 0.29 | 34 | 6 |

#### cluster (3) — top co-lemma: **akusalacittuppāda** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusalacittuppāda | 0.14 | 6 | 1 |
| dvādasa | 0.13 | 7 | 1 |

### appaṇihitanti

_pi blocks: 8; sense clusters: 2; inflected forms: appaṇihitanti_

#### cluster (1) — top co-lemma: **suññatanti** (cohesion 0.85, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññatanti | 1.00 | 8 | 8 |
| animittanti | 1.00 | 8 | 8 |
| pañcama | 0.33 | 40 | 8 |
| tatiya | 0.29 | 47 | 8 |
| dutiya | 0.27 | 51 | 8 |
| vūpasama | 0.22 | 38 | 5 |
| vitakkavicāra | 0.21 | 40 | 5 |
| catuttha | 0.20 | 72 | 8 |
| bhūmiya | 0.19 | 75 | 8 |

#### cluster (2) — top co-lemma: **suddhikapaṭipada** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suddhikapaṭipada | 0.20 | 2 | 1 |

### suññatanti

_pi blocks: 8; sense clusters: 2; inflected forms: suññatanti_

#### cluster (1) — top co-lemma: **appaṇihitanti** (cohesion 0.85, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| appaṇihitanti | 1.00 | 8 | 8 |
| animittanti | 1.00 | 8 | 8 |
| pañcama | 0.33 | 40 | 8 |
| tatiya | 0.29 | 47 | 8 |
| dutiya | 0.27 | 51 | 8 |
| vūpasama | 0.22 | 38 | 5 |
| vitakkavicāra | 0.21 | 40 | 5 |
| catuttha | 0.20 | 72 | 8 |
| bhūmiya | 0.19 | 75 | 8 |

#### cluster (2) — top co-lemma: **suddhikapaṭipada** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suddhikapaṭipada | 0.20 | 2 | 1 |

### parāmāsavippayutta

_pi blocks: 8; sense clusters: 6; inflected forms: parāmāsavippayuttā_

#### cluster (1) — top co-lemma: **parāmāsasampayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsasampayutta | 0.33 | 4 | 2 |

#### cluster (2) — top co-lemma: **aparāmaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aparāmaṭṭha | 0.29 | 6 | 2 |

#### cluster (3) — top co-lemma: **diṭṭhigatavippayuttalobhasahagatacittuppāda** (cohesion 1.00, 4 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.22 | 10 | 2 |
| domanassasahagatacittuppāda | 0.16 | 17 | 2 |
| vicikicchāsahagata | 0.12 | 26 | 2 |
| uddhaccasahagata | 0.11 | 27 | 2 |

#### cluster (4) — top co-lemma: **parāmaṭṭha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmaṭṭha | 0.21 | 11 | 2 |

#### cluster (5) — top co-lemma: **vippayutta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vippayutta | 0.17 | 15 | 2 |

#### cluster (6) — top co-lemma: **parāmāsa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| parāmāsa | 0.11 | 27 | 2 |

### ñāṇasampayutta

_pi blocks: 8; sense clusters: 3; inflected forms: ñāṇasampayuttaṃ, ñāṇasampayuttā_

#### cluster (1) — top co-lemma: **sasaṅkhāra** (cohesion 0.69, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sasaṅkhāra | 0.50 | 12 | 5 |
| somanassasahagata | 0.46 | 18 | 6 |
| dhammārammaṇa | 0.35 | 26 | 6 |
| panārabbha | 0.32 | 30 | 6 |
| rūpārammaṇa | 0.29 | 34 | 6 |
| uppanna | 0.28 | 49 | 8 |

#### cluster (2) — top co-lemma: **ñāṇavippayutta** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇavippayutta | 0.38 | 8 | 3 |
| abyākatamūla | 0.36 | 3 | 2 |

#### cluster (3) — top co-lemma: **hīna** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| hīna | 0.21 | 11 | 2 |
| paṇīta | 0.21 | 11 | 2 |

### ahetuka

_pi blocks: 8; sense clusters: 3; inflected forms: ahetukaṃ, ahetukā_

#### cluster (1) — top co-lemma: **ahetukamanoviññāṇadhātuya** (cohesion 1.00, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ahetukamanoviññāṇadhātuya | 0.36 | 3 | 2 |
| manodhātuya | 0.33 | 4 | 2 |
| tissa | 0.29 | 6 | 2 |
| dvepañcaviññāṇa | 0.27 | 7 | 2 |
| pañca | 0.19 | 13 | 2 |

#### cluster (2) — top co-lemma: **sahetuka** (cohesion 0.50, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sahetuka | 0.21 | 11 | 2 |
| hetūtipi | 0.20 | 2 | 1 |

#### cluster (3) — top co-lemma: **ekavidha** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.20 | 2 | 1 |
| ācayagāmi | 0.18 | 3 | 1 |
| nevasekkhanāsekkha | 0.17 | 4 | 1 |

### ogha

_pi blocks: 8; sense clusters: 1; inflected forms: ogho, oghā_

#### cluster (1) — top co-lemma: **jīvitāsa** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jīvitāsa | 0.55 | 3 | 3 |
| jappana | 0.55 | 3 | 3 |
| paṇidhi | 0.55 | 3 | 3 |
| rūpataṇha | 0.55 | 3 | 3 |
| taṇhājāla | 0.55 | 3 | 3 |
| lata | 0.55 | 3 | 3 |
| saddataṇha | 0.55 | 3 | 3 |
| gedha | 0.55 | 3 | 3 |
| anurodha | 0.55 | 3 | 3 |
| dhanāsa | 0.55 | 3 | 3 |

### abyākatahetū

_pi blocks: 8; sense clusters: 7; inflected forms: abyākatahetū_

#### cluster (1) — top co-lemma: **kusalahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kusalahetū | 0.67 | 10 | 6 |

#### cluster (2) — top co-lemma: **apariyāpannahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| apariyāpannahetū | 0.55 | 3 | 3 |

#### cluster (3) — top co-lemma: **akusalahetū** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akusalahetū | 0.46 | 5 | 3 |
| kāmāvacarahetū | 0.40 | 2 | 2 |

#### cluster (4) — top co-lemma: **rūpāvacarahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpāvacarahetū | 0.40 | 2 | 2 |

#### cluster (5) — top co-lemma: **arūpāvacarahetū** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| arūpāvacarahetū | 0.40 | 2 | 2 |

#### cluster (6) — top co-lemma: **sabbākusala** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sabbākusala | 0.15 | 5 | 1 |
| kāmāvacarakiriyata | 0.14 | 6 | 1 |

#### cluster (7) — top co-lemma: **alobha** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| alobha | 0.15 | 32 | 3 |
| vipākata | 0.14 | 34 | 3 |

### anārammaṇa

_pi blocks: 8; sense clusters: 3; inflected forms: anārammaṇaṃ, anārammaṇā_

#### cluster (1) — top co-lemma: **kiriyāhetukamanoviññāṇadhātu** (cohesion 0.78, 6 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kiriyāhetukamanoviññāṇadhātu | 0.50 | 4 | 3 |
| rūpāvacaratikacatukkajjhāna | 0.47 | 9 | 4 |
| ākāsānañcāyatana | 0.40 | 7 | 3 |
| ākiñcaññāyatana | 0.40 | 7 | 3 |
| siya | 0.33 | 16 | 4 |
| sāmaññaphala | 0.22 | 28 | 4 |

#### cluster (2) — top co-lemma: **ñāṇavippayuttacittuppāda** (cohesion 0.78, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ñāṇavippayuttacittuppāda | 0.40 | 2 | 2 |
| ñāṇasampayuttacittuppāda | 0.40 | 2 | 2 |
| sabba | 0.27 | 14 | 3 |

#### cluster (3) — top co-lemma: **ekavidha** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekavidha | 0.20 | 2 | 1 |

### aññindriya

_pi blocks: 8; sense clusters: 5; inflected forms: aññindriyaṃ_

#### cluster (1) — top co-lemma: **kāmarāgabyāpāda** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmarāgabyāpāda | 0.55 | 3 | 3 |
| tanubhāva | 0.40 | 2 | 2 |

#### cluster (2) — top co-lemma: **anavasesappahāna** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anavasesappahāna | 0.55 | 3 | 3 |
| rūparāgaarūparāgamānauddhaccaavijja | 0.40 | 2 | 2 |

#### cluster (3) — top co-lemma: **aññātāvindriya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| aññātāvindriya | 0.20 | 2 | 1 |

#### cluster (4) — top co-lemma: **sacchikiriya** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sacchikiriya | 0.20 | 2 | 1 |
| diṭṭha | 0.18 | 3 | 1 |

#### cluster (5) — top co-lemma: **bhāvitatta** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| bhāvitatta | 0.20 | 33 | 4 |
| lokuttara | 0.17 | 85 | 8 |
| tasseva | 0.17 | 39 | 4 |

### dhammāyatanapariyāpanna

_pi blocks: 8; sense clusters: 4; inflected forms: dhammāyatanapariyāpannaṃ_

#### cluster (1) — top co-lemma: **yañca** (cohesion 0.83, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yañca | 0.52 | 19 | 7 |
| appaṭigha | 0.44 | 24 | 7 |
| anidassana | 0.22 | 55 | 7 |

#### cluster (2) — top co-lemma: **anidassanaappaṭigha** (cohesion 0.67, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anidassanaappaṭigha | 0.50 | 4 | 3 |
| tika | 0.36 | 3 | 2 |

#### cluster (3) — top co-lemma: **ekādasavidha** (cohesion 0.67, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ekādasavidha | 0.40 | 2 | 2 |
| ekādasaka | 0.40 | 2 | 2 |
| mātika | 0.20 | 2 | 1 |

#### cluster (4) — top co-lemma: **rūpakaṇḍa** (cohesion 1.00, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rūpakaṇḍa | 0.20 | 2 | 1 |
| niṭṭhita | 0.15 | 5 | 1 |

### gandhadhātu

_pi blocks: 8; sense clusters: 1; inflected forms: gandhadhātu_

#### cluster (1) — top co-lemma: **sugandha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sugandha | 0.67 | 4 | 4 |
| phalagandha | 0.67 | 4 | 4 |
| vissagandha | 0.67 | 4 | 4 |
| tacagandha | 0.67 | 4 | 4 |
| pattagandha | 0.67 | 4 | 4 |
| duggandha | 0.67 | 4 | 4 |
| āmakagandha | 0.67 | 4 | 4 |
| mūlagandha | 0.67 | 4 | 4 |
| pupphagandha | 0.67 | 4 | 4 |
| sāragandha | 0.67 | 4 | 4 |

### ghānadhātu

_pi blocks: 8; sense clusters: 2; inflected forms: ghānadhātu_

#### cluster (1) — top co-lemma: **sotadhātu** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotadhātu | 0.50 | 8 | 4 |
| jivhādhātu | 0.50 | 8 | 4 |
| kāyadhātu | 0.42 | 11 | 4 |

#### cluster (2) — top co-lemma: **ghānindriya** (cohesion 0.90, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| ghānindriya | 0.50 | 12 | 5 |
| ghānāyatana | 0.45 | 14 | 5 |
| ghāna | 0.44 | 10 | 4 |
| gandha | 0.44 | 10 | 4 |
| tīra | 0.29 | 20 | 4 |
| orima | 0.29 | 20 | 4 |
| samudda | 0.29 | 20 | 4 |

### jivhādhātu

_pi blocks: 8; sense clusters: 4; inflected forms: jivhādhātu_

#### cluster (1) — top co-lemma: **sotadhātu** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sotadhātu | 0.50 | 8 | 4 |
| ghānadhātu | 0.50 | 8 | 4 |
| kāyadhātu | 0.42 | 11 | 4 |

#### cluster (2) — top co-lemma: **jivhindriya** (cohesion 0.88, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhindriya | 0.50 | 12 | 5 |
| jivha | 0.44 | 10 | 4 |
| jivhāyatana | 0.37 | 19 | 5 |
| orima | 0.29 | 20 | 4 |
| tīra | 0.29 | 20 | 4 |

#### cluster (3) — top co-lemma: **yāya** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| yāya | 0.31 | 5 | 2 |

#### cluster (4) — top co-lemma: **rasa** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| rasa | 0.29 | 6 | 2 |

### moha

_pi blocks: 8; sense clusters: 5; inflected forms: mohaṃ_

#### cluster (1) — top co-lemma: **uddhaccasahagata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| uddhaccasahagata | 0.34 | 27 | 6 |

#### cluster (2) — top co-lemma: **domanassasahagatacittuppāda** (cohesion 0.64, 5 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| domanassasahagatacittuppāda | 0.32 | 17 | 4 |
| etthuppanna | 0.29 | 27 | 5 |
| pahātabbahetuka | 0.29 | 20 | 4 |
| siya | 0.25 | 16 | 3 |
| diṭṭhigatavippayuttalobhasahagatacittuppāda | 0.22 | 10 | 2 |

#### cluster (3) — top co-lemma: **vicikicchāsahagata** (cohesion 0.57, 2 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| vicikicchāsahagata | 0.29 | 26 | 5 |
| cittuppāda | 0.25 | 40 | 6 |

#### cluster (4) — top co-lemma: **kāmāvacarakiriyata** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāmāvacarakiriyata | 0.29 | 6 | 2 |

#### cluster (5) — top co-lemma: **diṭṭhigatasampayuttacittuppāda** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| diṭṭhigatasampayuttacittuppāda | 0.22 | 10 | 2 |

### rasadhātu

_pi blocks: 8; sense clusters: 1; inflected forms: rasadhātu_

#### cluster (1) — top co-lemma: **madhura** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| madhura | 0.67 | 4 | 4 |
| puppharasa | 0.67 | 4 | 4 |
| phalarasa | 0.67 | 4 | 4 |
| asādu | 0.67 | 4 | 4 |
| lambila | 0.67 | 4 | 4 |
| sādu | 0.67 | 4 | 4 |
| kasāva | 0.67 | 4 | 4 |
| pattarasa | 0.67 | 4 | 4 |
| loṇika | 0.67 | 4 | 4 |
| kaṭuka | 0.67 | 4 | 4 |

### saddadhātu

_pi blocks: 8; sense clusters: 1; inflected forms: saddadhātu_

#### cluster (1) — top co-lemma: **dhātūna** (cohesion 0.96, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| dhātūna | 0.71 | 6 | 5 |
| saṅkhasadda | 0.67 | 4 | 4 |
| vātasadda | 0.67 | 4 | 4 |
| paṇavasadda | 0.67 | 4 | 4 |
| pāṇisadda | 0.67 | 4 | 4 |
| gītasadda | 0.67 | 4 | 4 |
| manussasadda | 0.67 | 4 | 4 |
| nigghosasadda | 0.67 | 4 | 4 |
| amanussasadda | 0.67 | 4 | 4 |
| udakasadda | 0.67 | 4 | 4 |

### sotadhātu

_pi blocks: 8; sense clusters: 2; inflected forms: sotadhātu_

#### cluster (1) — top co-lemma: **sota** (cohesion 0.90, 7 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| sota | 0.57 | 6 | 4 |
| sotindriya | 0.50 | 12 | 5 |
| sadda | 0.44 | 10 | 4 |
| sotāyatana | 0.31 | 24 | 5 |
| tīra | 0.29 | 20 | 4 |
| orima | 0.29 | 20 | 4 |
| samudda | 0.29 | 20 | 4 |

#### cluster (2) — top co-lemma: **jivhādhātu** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| jivhādhātu | 0.50 | 8 | 4 |
| ghānadhātu | 0.50 | 8 | 4 |
| kāyadhātu | 0.42 | 11 | 4 |

### adassana

_pi blocks: 8; sense clusters: 1; inflected forms: adassanaṃ_

#### cluster (1) — top co-lemma: **avijjālaṅgī** (cohesion 0.89, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| avijjālaṅgī | 1.00 | 8 | 8 |
| aññāṇa | 1.00 | 8 | 8 |
| asampajañña | 0.93 | 7 | 7 |
| ananubodha | 0.86 | 6 | 6 |
| avijjogha | 0.86 | 6 | 6 |
| sammoha | 0.86 | 6 | 6 |
| apaccakkhakamma | 0.86 | 6 | 6 |
| anabhisamaya | 0.86 | 6 | 6 |
| avijjāpariyuṭṭha | 0.86 | 6 | 6 |
| avijjāyoga | 0.86 | 6 | 6 |

### akakkhaḷata

_pi blocks: 8; sense clusters: 4; inflected forms: akakkhaḷatā_

#### cluster (1) — top co-lemma: **akathinata** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akathinata | 1.00 | 8 | 8 |
| maddavata | 1.00 | 8 | 8 |
| muduta | 0.37 | 35 | 8 |

#### cluster (2) — top co-lemma: **maddava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maddava | 0.20 | 2 | 1 |

#### cluster (3) — top co-lemma: **cittamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittamuduta | 0.19 | 13 | 2 |

#### cluster (4) — top co-lemma: **kāyamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyamuduta | 0.19 | 13 | 2 |

### akathinata

_pi blocks: 8; sense clusters: 4; inflected forms: akathinatā_

#### cluster (1) — top co-lemma: **akakkhaḷata** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akakkhaḷata | 1.00 | 8 | 8 |
| maddavata | 1.00 | 8 | 8 |
| muduta | 0.37 | 35 | 8 |

#### cluster (2) — top co-lemma: **maddava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maddava | 0.20 | 2 | 1 |

#### cluster (3) — top co-lemma: **cittamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittamuduta | 0.19 | 13 | 2 |

#### cluster (4) — top co-lemma: **kāyamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyamuduta | 0.19 | 13 | 2 |

### animittanti

_pi blocks: 8; sense clusters: 2; inflected forms: animittanti_

#### cluster (1) — top co-lemma: **suññatanti** (cohesion 0.85, 9 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suññatanti | 1.00 | 8 | 8 |
| appaṇihitanti | 1.00 | 8 | 8 |
| pañcama | 0.33 | 40 | 8 |
| tatiya | 0.29 | 47 | 8 |
| dutiya | 0.27 | 51 | 8 |
| vūpasama | 0.22 | 38 | 5 |
| vitakkavicāra | 0.21 | 40 | 5 |
| catuttha | 0.20 | 72 | 8 |
| bhūmiya | 0.19 | 75 | 8 |

#### cluster (2) — top co-lemma: **suddhikapaṭipada** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| suddhikapaṭipada | 0.20 | 2 | 1 |

### avijjālaṅgī

_pi blocks: 8; sense clusters: 1; inflected forms: avijjālaṅgī_

#### cluster (1) — top co-lemma: **adassana** (cohesion 0.89, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| adassana | 1.00 | 8 | 8 |
| aññāṇa | 1.00 | 8 | 8 |
| asampajañña | 0.93 | 7 | 7 |
| ananubodha | 0.86 | 6 | 6 |
| avijjogha | 0.86 | 6 | 6 |
| sammoha | 0.86 | 6 | 6 |
| apaccakkhakamma | 0.86 | 6 | 6 |
| anabhisamaya | 0.86 | 6 | 6 |
| avijjāpariyuṭṭha | 0.86 | 6 | 6 |
| avijjāyoga | 0.86 | 6 | 6 |

### maddavata

_pi blocks: 8; sense clusters: 4; inflected forms: maddavatā_

#### cluster (1) — top co-lemma: **akathinata** (cohesion 1.00, 3 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| akathinata | 1.00 | 8 | 8 |
| akakkhaḷata | 1.00 | 8 | 8 |
| muduta | 0.37 | 35 | 8 |

#### cluster (2) — top co-lemma: **maddava** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| maddava | 0.20 | 2 | 1 |

#### cluster (3) — top co-lemma: **cittamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| cittamuduta | 0.19 | 13 | 2 |

#### cluster (4) — top co-lemma: **kāyamuduta** (cohesion 1.00, 1 co-lemma)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| kāyamuduta | 0.19 | 13 | 2 |

### manovilekha

_pi blocks: 8; sense clusters: 1; inflected forms: manovilekho_

#### cluster (1) — top co-lemma: **thambhitatta** (cohesion 0.78, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| thambhitatta | 0.88 | 8 | 7 |
| vicikicchati | 0.86 | 6 | 6 |
| kaṅkhati | 0.86 | 6 | 6 |
| satthari | 0.86 | 6 | 6 |
| kaṅkhāyana | 0.77 | 5 | 5 |
| saṃsaya | 0.77 | 5 | 5 |
| dvedhāpatha | 0.77 | 5 | 5 |
| dveḷhaka | 0.77 | 5 | 5 |
| kaṅkhāyitatta | 0.77 | 5 | 5 |
| anekaṃsaggāha | 0.77 | 5 | 5 |

### pañcindriya

_pi blocks: 8; sense clusters: 1; inflected forms: pañcindriyāni_

#### cluster (1) — top co-lemma: **tivaṅgika** (cohesion 0.80, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| tivaṅgika | 0.57 | 6 | 4 |
| caturaṅgika | 0.42 | 16 | 5 |
| dvāyatana | 0.40 | 32 | 8 |
| ekaṃ | 0.38 | 34 | 8 |
| ekā | 0.37 | 35 | 8 |
| dhātuya | 0.37 | 35 | 8 |
| dhammadhātu | 0.36 | 37 | 8 |
| khandha | 0.35 | 38 | 8 |
| bala | 0.34 | 27 | 6 |
| dhammāyatana | 0.34 | 39 | 8 |

### paṭigha

_pi blocks: 8; sense clusters: 1; inflected forms: paṭighaṃ_

#### cluster (1) — top co-lemma: **anattha** (cohesion 1.00, 10 co-lemmas)

| pāli co-lemma | dice | pi blocks | sub-blocks |
| --- | ---: | ---: | ---: |
| anattha | 0.77 | 5 | 5 |
| piya | 0.77 | 5 | 5 |
| kujjhitatta | 0.77 | 5 | 5 |
| jāyati | 0.77 | 5 | 5 |
| appiya | 0.77 | 5 | 5 |
| paṭighāta | 0.77 | 5 | 5 |
| āghāta | 0.77 | 5 | 5 |
| amanāpa | 0.77 | 5 | 5 |
| carissatīti | 0.77 | 5 | 5 |
| kujjhana | 0.77 | 5 | 5 |

