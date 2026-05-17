#!/usr/bin/env python3
import re

# This is the raw input from bash capture
raw_input = r"""@@^1-1142  (EXPECTED_TOKENS=82)
\gla Tattha katamo byāpādo kāyagantho Anatthaṃ me acarī ti āghāto jāyati anatthaṃ me caratīti āghāto jāyati anatthaṃ me carissatīti āghāto jāyati piyassa me manāpassa anatthaṃ acari…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati aṭṭhāne vā pana āghāto jāyati Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa ayaṃ vuccati byāpādo kāyagantho

@@^1-1143  (EXPECTED_TOKENS=35)
\gla Tattha katamo sīlabbataparāmāso kāyagantho Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhītiः yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummagro micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho ayaṃ vuccati sīlabbataparāmāso kāyagantho

@@^1-1144  (EXPECTED_TOKENS=117)
\gla Tattha katamo idaṃsaccābhiniveso kāyagantho Sassato loko idameva saccaṃ moghamaññanti vā asassato loko idameva saccaṃ moghamaññanti vā antavā loko idameva saccaṃ moghamaññanti vā anantavā loko idameva saccaṃ moghamaññanti vā taṃ jīvaṃ taṃ sarīraṃ idameva saccaṃ moghamaññanti vā aññaṃ jīvaṃ aññaṃ sarīraṃ idameva saccaṃ moghamaññanti vā hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā na hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā hoti ca na ca hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā neva hoti na na hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vāः yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummagro micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho ayaṃ vuccati idaṃsaccābhiniveso kāyagantho Ṭhapetvā sīlabbataparāmāsaṃ kāyaganthaṃ sabbāpi micchādiṭṭhi idaṃsaccābhiniveso kāyagantho Ime dhammā ganthā

@@^1-1145  (EXPECTED_TOKENS=25)
\gla Katame dhammā no ganthā Te dhamme ṭhapetvā avasesā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā vedanākkhandho…pe… viññāṇakkhandho sabbañca rūpaṃ asaṅkhatā ca dhātu ime dhammā no ganthā

@@^1-1146  (EXPECTED_TOKENS=14)
\gla Katame dhammā ganthaniyā Sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthaniyā

@@^1-1148  (EXPECTED_TOKENS=13)
\gla Katame dhammā ganthasampayuttā Tehi dhammehi ye dhammā sampayuttā vedanākkhandho…pe… viññāṇakkhandho ime dhammā ganthasampayuttā

@@^1-1149  (EXPECTED_TOKENS=18)
\gla Katame dhammā ganthavippayuttā Tehi dhammehi ye dhammā vippayuttā vedanākkhandho…pe… viññāṇakkhandho sabbañca rūpaṃ asaṅkhatā ca dhātu ime dhammā ganthavippayuttā

@@^1-1150  (EXPECTED_TOKENS=12)
\gla Katame dhammā ganthā ceva ganthaniyā ca Teva ganthā ganthā ceva ganthaniyā ca

@@^1-1151  (EXPECTED_TOKENS=31)
\gla Katame dhammā ganthaniyā ceva no ca ganthā Tehi dhammehi ye dhammā ganthaniyā te dhamme ṭhapetvā avasesā sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthaniyā ceva no ca ganthā

@@^1-1152  (EXPECTED_TOKENS=40)
\gla Katame dhammā ganthā ceva ganthasampayuttā ca Sīlabbataparāmāso kāyagantho abhijjhākāyaganthena gantho ceva ganthasampayutto ca abhijjhākāyagantho sīlabbataparāmāsena kāyaganthena gantho ceva ganthasampayutto ca idaṃsaccābhiniveso kāyagantho abhijjhākāyaganthena gantho ceva ganthasampayutto ca abhijjhākāyagantho idaṃsaccābhinivesena kāyaganthena gantho ceva ganthasampayutto ca ime dhammā ganthā ceva ganthasampayuttā ca

@@^1-1153  (EXPECTED_TOKENS=24)
\gla Katame dhammā ganthasampayuttā ceva no ca ganthā Tehi dhammehi ye dhammā sampayuttā te dhamme ṭhapetvā vedanākkhandho…pe… viññāṇakkhandho ime dhammā ganthasampayuttā ceva no ca ganthā

@@^1-1154  (EXPECTED_TOKENS=21)
\gla Katame dhammā ganthavippayuttā ganthaniyā Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthavippayuttā ganthaniyā

@@^1-1156  (EXPECTED_TOKENS=9)
\gla Katame dhammā oghā Cattāro oghā…pe… ime dhammā oghavippayuttā oghaniyā

@@^1-1157  (EXPECTED_TOKENS=9)
\gla Katame dhammā yogā Cattāro yogā…pe… ime dhammā yogavippayuttā yoganiyā

@@^1-1160  (EXPECTED_TOKENS=79)
\gla Tattha katamaṃ byāpādanīvaraṇaṃ Anatthaṃ me acarīti āghāto jāyati anatthaṃ me caratīti āghāto jāyati anatthaṃ me carissatīti āghāto jāyati piyassa me manāpassa anatthaṃ acari…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati aṭṭhāne vā pana āghāto jāyati Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa idaṃ vuccati byāpādanīvaraṇaṃ"""

# Count tokens in each block
print("Token count verification from input file:")
print("=" * 70)

blocks = re.split(r'@@\^', raw_input)
for block_text in blocks[1:]:  # Skip the first empty split
    lines = block_text.strip().split('\n')
    # First line has the block ID and expected count
    match = re.match(r'(\S+)\s+\(EXPECTED_TOKENS=(\d+)\)', lines[0])
    if match:
        bid = '^' + match.group(1)
        expected = int(match.group(2))

        # Find the \gla line
        for line in lines[1:]:
            if line.startswith('\\gla '):
                gla_text = line[5:]  # Remove '\gla '
                tokens = gla_text.split()
                actual = len(tokens)

                status = 'OK' if actual == expected else 'MISMATCH'
                print(f"{bid:12} expected={expected:3} actual={actual:3} {status}")

                if actual != expected:
                    print(f"  First 5 tokens: {' '.join(tokens[:5])}")
                break
