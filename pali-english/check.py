from db_query.lookup import PaliLookup

lookup = PaliLookup()

entries = lookup.get_translations("dhamme")

for entry in entries:
    print(f"{entry.lemma} | {entry.lemma_clean} | {entry.pos} | {entry.meaning_1} | {entry.meaning_lit} | {entry.meaning_2}")