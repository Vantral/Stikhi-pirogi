import json
from russtress import Accent

collocations = {}
stresses = {}
stikhi = []
all_words = []
vowels = "уеыаоэяиюё"

path2file = input("Enter path to file: ")

with open(path2file, 'r', encoding="utf-8") as f:
    text = f.read().replace(',.!?-;:()"[]', ' ').split()

def syllabs(word):
  accent = Accent()
  stressed_word = accent.put_stress(word)

  for letter in stressed_word:
    if letter not in vowels and letter != "'":
      letter = ''
    elif letter in vowels:
      letter = "V"
    else:
      continue
    
  return stressed_word

for i in range(0, len(text)-1):
    word = text[i]
    if word not in all_words:
      all_words.append(word)

    next_word = text[i+1]
    if next_word not in all_words:
      all_words.append(next_word)

    if word not in collocations:
        collocations[word] = {}

    if next_word in collocations[word]:
        collocations[word][next_word] += 1
    else:
        collocations[word][next_word] = 1

print("Words in")
length = len(all_words)
for word in all_words:
  stresses[word] = syllabs(word)
  length -= 1
  print(length)

with open('syllab/'.join(path2file.replace('.txt', '.json')), "w", encoding="utf-8") as write_file:
    json.dump(stresses, write_file, indent=4, ensure_ascii=False)

with open('coll/'.join(path2file.replace('.txt', '.json')), "w", encoding="utf-8") as write_file:
    json.dump(collocations, write_file, indent=4, ensure_ascii=False)

print("Done")