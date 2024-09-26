import json

with open('corporas\pirogi.txt', 'r', encoding="utf-8") as f:
    text = f.read()

stikhi = text.split("\n\n")
print('Stikhi in')

text = None
first_words = {}
last_words = {}

length = len(stikhi)

for poem in stikhi:
    try:
        pair = (poem.split()[0]+' '+poem.split()[1], poem.split()[-2]+' '+poem.split()[-1])
        if pair[0] in first_words:
            first_words[pair[0]] += 1
        else:
            first_words[pair[0]] = 1

        if pair[1] in last_words:
            last_words[pair[1]] += 1
        else:
            last_words[pair[1]] = 1
    except:
        continue
    length -= 1
    print(f"{length} last")

with open('dictionaries/first_bigrams.json', "w", encoding="utf-8") as write_file:
    json.dump(first_words, write_file, indent=4, ensure_ascii=False)

with open('dictionaries/last_bigrams.json', "w", encoding="utf-8") as write_file:
    json.dump(last_words, write_file, indent=4, ensure_ascii=False)