import random
import json
import numpy as np
        
with open("dictionaries/collocations_percents.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)
    words = [x for x in collocations]

with open("dictionaries/syllabs.json", 'r', encoding="utf-8") as f:
    syllabs = json.load(f)


def generate(word, amount):
    def rhyme(candidate):           #filter function
        if len(syllabs[word]) == 1 or len(syllabs[word]) == 0:
            return True

        elif candidate not in syllabs:
            return False

        elif syllabs[word][-1] == "V":
            if len(syllabs[candidate]) == 1 or len(syllabs[candidate]) == 0:
                return True
            elif syllabs[candidate][1] == "'":
                return True
            else:
                return False

        elif syllabs[word][-1] == "'":
            if len(syllabs[candidate]) == 1 or len(syllabs[candidate]) == 0:
                return True
            elif syllabs[candidate][1] == "V":
                return True
            else:
                return False

    candidates = [x for x in collocations[word]]
    candidates = list(filter(rhyme, candidates))

    if len(candidates) == 0:
        candidates = [x for x in collocations[word]]

    freqs = [collocations[word][coll] for coll in candidates]
    #print(freqs)
    if sum(freqs) != 1:
        freqs[random.randint(0, len(freqs)-1)] += 1 - sum(freqs)
    new_word = np.random.choice(candidates, 1, p=freqs)[0]
    print(word)
    generate(new_word, amount)


test_word = random.choice(words)

generate(test_word, 5)