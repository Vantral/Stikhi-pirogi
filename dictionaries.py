import json
from russtress import Accent

collocations = {}
stresses = {}
stikhi = []
vowels = "уеыаоэяиюё"

accent = Accent()

with open("pirogi.txt", 'r', encoding="utf-8") as f:
    stikhi = f.read().split('\n\n')

def syllabs(word):
  stressed_word = accent.put_stress(word)
  res = ''
  for letter in stressed_word:
    if letter == "'":
      res += "'"
    elif letter in vowels:
      res += "V"
    else:
      continue
    
  return res

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

length = len(collocations)

for word in collocations:
  stresses[word] = syllabs(word)
  length -= 1
  print(length)


with open("syllabs.json", "w", encoding="utf-8") as write_file:
    json.dump(stresses, write_file, indent=4, ensure_ascii=False)


with open("collocations.json", "w", encoding="utf-8") as write_file:
    json.dump(collocations, write_file, indent=4, ensure_ascii=False)

print("Done")