import json
import numpy as np

with open("dictionaries/first_words_perc.json", 'r', encoding="utf-8") as f:
    first_words = json.load(f)

for i in range(20):
    print(np.random.choice([x for x in first_words.keys()], 1, [x for x in first_words.values()])[0])
