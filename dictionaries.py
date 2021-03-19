import json

collocations = {}
stikhi = []

with open("pirogi.txt", 'r', encoding="utf-8") as f:
    stikhi = f.read().split('\n\n')

for item in stikhi:
    item = item.replace('\n', ' ').split()
    for i in range(0, len(item)-1):
        word = item[i]
        next_word = item[i+1]
        if word not in collocations:
            collocations[word] = {}

        if next_word in collocations[word]:
            collocations[word][next_word] += 1
        else:
            collocations[word][next_word] = 1

#print(collocations)

with open("collocations.json", "w", encoding="utf-8") as write_file:
    json.dump(collocations, write_file, indent=4, ensure_ascii=False)

print("Done")