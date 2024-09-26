import json

with open("dictionaries/last_bigrams.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)

summ = 0

for word in collocations:
    summ += collocations[word]

print(summ)

for word in collocations:
    collocations[word] = collocations[word] / summ

with open("dictionaries/last_bigrams_perc.json", "w", encoding="utf-8") as write_file:
    json.dump(collocations, write_file, indent=4, ensure_ascii=False)

print("done")