import re

# Read input and output files
input_file = '/sessions/upbeat-busy-davinci/mnt/abhidhamma-rails/retry-batches/retry-14.txt'
output_file = '/sessions/upbeat-busy-davinci/mnt/abhidhamma-rails/outputs/retry-14.txt'

# Note: We need to adjust paths for running in the workspace
import os
import sys

# Try both workspace and host paths
ws_input = input_file
ws_output = output_file

# For now, read from what we already have in memory
in_text = """@@^1-1142  (EXPECTED_TOKENS=82)
\gla Tattha katamo byāpādo kāyagantho Anatthaṃ me acarī ti āghāto jāyati anatthaṃ me caratīti āghāto jāyati anatthaṃ me carissatīti āghāto jāyati piyassa me manāpassa anatthaṃ acari…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati aṭṭhāne vā pana āghāto jāyati Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa ayaṃ vuccati byāpādo kāyagantho
\t   do not tend to become tied? The Paths that are the Unincluded and the Fruits of the Paths, and unconditioned element. Which are the states that are

@@^1-1143  (EXPECTED_TOKENS=35)
\gla Tattha katamo sīlabbataparāmāso kāyagantho Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena suddhi sīlabbatena suddhītiः yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummagro micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho ayaṃ vuccati sīlabbataparāmāso kāyagantho
\t   associated with the Ties? The states connected with those four afore-named states; [in other words] the four skandhas.

@@^1-1144  (EXPECTED_TOKENS=117)
\gla Tattha katamo idaṃsaccābhiniveso kāyagantho Sassato loko idameva saccaṃ moghamaññanti vā asassato loko idameva saccaṃ moghamaññanti vā antavā loko idameva saccaṃ moghamaññanti vā anantavā loko idameva saccaṃ moghamaññanti vā taṃ jīvaṃ taṃ sarīraṃ idameva saccaṃ moghamaññanti vā aññaṃ jīvaṃ aññaṃ sarīraṃ idameva saccaṃ moghamaññanti vā hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā na hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā hoti ca na ca hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vā neva hoti na na hoti tathāgato paraṃ maraṇā idameva saccaṃ moghamaññanti vāः yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummagro micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho ayaṃ vuccati idaṃsaccābhiniveso kāyagantho Ṭhapetvā sīlabbataparāmāsaṃ kāyaganthaṃ sabbāpi micchādiṭṭhi idaṃsaccābhiniveso kāyagantho Ime dhammā ganthā
\t   disconnected with the Ties? The states which are disconnected with those [four afore-named] states; [in other words] the four skandhas; all [material] form also, and unconditioned element. Which are the states that

@@^1-1145  (EXPECTED_TOKENS=25)
\gla Katame dhammā no ganthā Te dhamme ṭhapetvā avasesā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā vedanākkhandho…pe… viññāṇakkhandho sabbañca rūpaṃ asaṅkhatā ca dhātu ime dhammā no ganthā
\t   are themselves Ties and tend to become tied? The Ties themselves are both

@@^1-1146  (EXPECTED_TOKENS=14)
\gla Katame dhammā ganthaniyā Sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthaniyā
\t   tend to become tied, but are not Ties? The states which tend to become tied by those [four afore-named] states, that is, every state, good, bad and indeterminate, which is not included in the latter, whether it relates to the worlds of Sense, of Form, or of the Formless; [in other words] the five skandhas. Which are the states that are

@@^1-1148  (EXPECTED_TOKENS=13)
\gla Katame dhammā ganthasampayuttā Tehi dhammehi ye dhammā sampayuttā vedanākkhandho…pe… viññāṇakkhandho ime dhammā ganthasampayuttā
\t   associated with the Ties but not Ties? The states which are associated with the four states afore-named (the Ties), the latter themselves excepted; [in other words] the four skandhas. Which are the states that

@@^1-1149  (EXPECTED_TOKENS=18)
\gla Katame dhammā ganthavippayuttā Tehi dhammehi ye dhammā vippayuttā vedanākkhandho…pe… viññāṇakkhandho sabbañca rūpaṃ asaṅkhatā ca dhātu ime dhammā ganthavippayuttā
\t   are disconnected with the Ties, but tend to become tied? The states which are disconnected with the afore-named states, that is, good, bad and indeterminate states relating to the worlds of Sense, of Form, or of the Formless, which are co-Āsava; [in other words], the five skandhas.

@@^1-1150  (EXPECTED_TOKENS=12)
\gla Katame dhammā ganthā ceva ganthaniyā ca Teva ganthā ganthā ceva ganthaniyā ca
\t   are disconnected with the Ties and do not tend to become tied? The Paths that are the Unincluded and the Fruits of the Paths, and uncompounded element. The Group of the Floods ( ogha-gocchakaṃ )

@@^1-1151  (EXPECTED_TOKENS=31)
\gla Katame dhammā ganthaniyā ceva no ca ganthā Tehi dhammehi ye dhammā ganthaniyā te dhamme ṭhapetvā avasesā sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthaniyā ceva no ca ganthā
\t   Which are the states that are Floods? … [continue as in the Group of Fetters]. The Group of the Bonds ( yoga-gocchakaṃ )

@@^1-1152  (EXPECTED_TOKENS=40)
\gla Katame dhammā ganthā ceva ganthasampayuttā ca Sīlabbataparāmāso kāyagantho abhijjhākāyaganthena gantho ceva ganthasampayutto ca abhijjhākāyagantho sīlabbataparāmāsena kāyaganthena gantho ceva ganthasampayutto ca idaṃsaccābhiniveso kāyagantho abhijjhākāyaganthena gantho ceva ganthasampayutto ca abhijjhākāyagantho idaṃsaccābhinivesena kāyaganthena gantho ceva ganthasampayutto ca ime dhammā ganthā ceva ganthasampayuttā ca
\t   Which are the states that are Hindrances? The six Hindrances, to wit, the Hindrance of sensual desire, the Hindrance of ill will, the Hindrance of stolidity and torpor, the Hindrance of distraction and worry, the Hindrance of perplexity, the Hindrance of ignorance. In this connexion

@@^1-1153  (EXPECTED_TOKENS=24)
\gla Katame dhammā ganthasampayuttā ceva no ca ganthā Tehi dhammehi ye dhammā sampayuttā te dhamme ṭhapetvā vedanākkhandho…pe… viññāṇakkhandho ime dhammā ganthasampayuttā ceva no ca ganthā
\t   What is the Hindrance of sensual desire? Answer as for the "Intoxicant of sensuality", § 1097 .

@@^1-1154  (EXPECTED_TOKENS=21)
\gla Katame dhammā ganthavippayuttā ganthaniyā Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā kāmāvacarā rūpāvacarā arūpāvacarā rūpakkhandho…pe… viññāṇakkhandho ime dhammā ganthavippayuttā ganthaniyā
\t   What is the Hindrance of ill will? Answer as for the "Tie of ill will", § 1137 .

@@^1-1156  (EXPECTED_TOKENS=9)
\gla Katame dhammā oghā Cattāro oghā…pe… ime dhammā oghavippayuttā oghaniyā
\t   What is stolidity? That which is indisposition, unwieldiness of mind; adhering and cohering: clinging, cleaving to, stickiness; stolidity, that is, a stiffening, a rigidity of the mind—this is called stolidity.

@@^1-1157  (EXPECTED_TOKENS=9)
\gla Katame dhammā yogā Cattāro yogā…pe… ime dhammā yogavippayuttā yoganiyā
\t   What is torpor? That which is indisposition and unwieldiness of sense, a shrouding, enveloping, barricading within; torpor that is sleep, drowsiness; sleep, slumbering, somnolence—this is called torpor.

@@^1-1160  (EXPECTED_TOKENS=79)
\gla Tattha katamaṃ byāpādanīvaraṇaṃ Anatthaṃ me acarīti āghāto jāyati anatthaṃ me caratīti āghāto jāyati anatthaṃ me carissatīti āghāto jāyati piyassa me manāpassa anatthaṃ acari…pe… anatthaṃ carati…pe… anatthaṃ carissatīti āghāto jāyati appiyassa me amanāpassa atthaṃ acari…pe… atthaṃ carati…pe… atthaṃ carissatīti āghāto jāyati aṭṭhāne vā pana āghāto jāyati Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa idaṃ vuccati byāpādanīvaraṇaṃ
\t   What is distraction? That distraction of mind which is disquietude, agitation of heart, turmoil of mind—this is called distraction.
"""

# Parse expected tokens
expected = {}
for chunk in re.split(r'^@@', in_text, flags=re.M):
    if not chunk.strip(): continue
    lines = chunk.strip().split('\n')
    m = re.match(r'^(\S+)\s+\(EXPECTED_TOKENS=(\d+)\)', lines[0])
    if m:
        bid = m.group(1)
        if not bid.startswith('^'): bid = '^' + bid
        expected[bid] = int(m.group(2))

print(f"Expected blocks: {len(expected)}")
for bid, n in sorted(expected.items()):
    print(f"  {bid}: {n} tokens")

# Now read output file from the created file
try:
    with open('C:\\Users\\trinley\\Obsidian\\abhidhamma-rails\\outputs\\retry-14.txt') as f:
        out_text = f.read()
except:
    print("Could not read output file")
    out_text = ""

# Parse output blocks
out_blocks = {}
for chunk in re.split(r'^@@', out_text, flags=re.M):
    if not chunk.strip(): continue
    lines = chunk.strip().split('\n')
    bid = lines[0].strip().split()[0]
    if not bid.startswith('^'): bid = '^' + bid
    glb = glc = None
    for ln in lines[1:]:
        if ln.startswith('\\glb '): glb = len(ln.split(None,1)[1].split())
        elif ln.startswith('\\glc '): glc = len(ln.split(None,1)[1].split())
    out_blocks[bid] = (glb, glc)

print(f"\nOutput blocks: {len(out_blocks)}")

# Check failures
fails = []
for bid, n in expected.items():
    ob = out_blocks.get(bid)
    if not ob:
        fails.append((bid, n, None, None))
        continue
    if ob[0] != n or ob[1] != n:
        fails.append((bid, n, ob[0], ob[1]))

print(f'\nFailures: {len(fails)}')
if fails:
    for bid, exp, glb_cnt, glc_cnt in fails:
        print(f'  {bid}: expected {exp}, got glb={glb_cnt} glc={glc_cnt}')
else:
    print('  None - all blocks passing!')

print(f"\nBLOCKS_PROCESSED: {len(expected)}")
print(f"BLOCKS_PASSING_VERIFICATION: {len(expected) - len(fails)}")
print(f"BLOCKS_FAILED: {len(fails)}")
if fails:
    print(f"FAILED_IDS: {[f[0] for f in fails]}")
else:
    print(f"FAILED_IDS: none")
