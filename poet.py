import random
import json
import numpy as np
        
with open("dictionaries/collocations_percents.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)
    words = [x for x in collocations]

with open("dictionaries/syllabs.json", 'r', encoding="utf-8") as f:
    syllabs = json.load(f)


count = [0]

def generate(word, amount):
    def rhyme(candidate):                                                       #filter function
        if len(syllabs[word]) == 1 or len(syllabs[word]) == 0:
            return True

        elif syllabs[word][-1] == "V":
            if len(syllabs[candidate]) == 1:
                return True
            elif syllabs[candidate][1] == "'":
                return True
            else:
                return False

        elif syllabs[word][-1] == "'":
            if len(syllabs[candidate]) == 1:
                return True
            elif syllabs[candidate][1] == "V":
                return True
            else:
                return False

    candidates = [x for x in collocations[word]]
    candidates = list(filter(rhyme, candidates))
    print(candidates)

    if len(candidates) != 0:
        freqs = [collocations[word][coll] for coll in candidates]
        new_word = np.random.choice(candidates, 1, p=freqs)[0]
        print(word)
        generate(new_word, amount)

    else:
        candidates = [x for x in collocations[word]]
        freqs = [collocations[word][coll] for coll in candidates]
        new_word = np.random.choice(candidates, 1, p=freqs)[0]
        print(word)
        generate(new_word, amount)

    count[0] += 1
    if count[0] > amount:
        return

test_word = random.choice(words)

generate(test_word, 5)