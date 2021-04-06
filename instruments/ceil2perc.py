import json

with open("dictionaries/collocations.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)

for word in collocations:
    summ = 0
    for coll in collocations[word]:
        summ += collocations[word][coll]

    for coll in collocations[word]:
        collocations[word][coll] = collocations[word][coll] / summ

with open("dictionaries/collocations_percents.json", "w", encoding="utf-8") as write_file:
    json.dump(collocations, write_file, indent=4, ensure_ascii=False)

print("done")