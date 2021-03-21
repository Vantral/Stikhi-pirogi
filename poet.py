import random
import json
import numpy as np
import time
import markovify
        
with open("dictionaries/collocations_percents.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)
    words = [x for x in collocations]

with open("dictionaries/syllabs.json", 'r', encoding="utf-8") as f:
    syllabs = json.load(f)


class Poem:
    lines = [[], [], [], []]            #так в моём понимании выглядит четверостишие

    first_word = random.choice(words)
    line_count = 0                      #отслеживает на какой мы строчке четверостишия

    def generate_random(self, word=first_word):
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

        candidates = [x for x in collocations[word]]        #список коллокатов слова
        candidates = list(filter(rhyme, candidates))        #отфильстрованный по ударениям список коллокатов слова

        if len(candidates) == 0:                            #если ни одно не подходит - возьмем любое
            candidates = [x for x in collocations[word]]

        freqs = [collocations[word][coll] for coll in candidates]       #массив с частотами коллокатов
        
        if sum(freqs) != 1:                                             #иногда возникает баг из-за округления в питоне и сумма != 1
            freqs[random.randint(0, len(freqs)-1)] += 1 - sum(freqs)    #тогда прибавляем разницу рандомному слову

        new_word = np.random.choice(candidates, 1, p=freqs)[0]

        if len(self.lines[self.line_count]) == 5:                       #число 5 отвечает за количество слов в строке так что можно подбирать
            self.line_count += 1
            if self.line_count > 3:
                return
        
        self.lines[self.line_count].append(word)
        
        self.generate_random(word=new_word)

    def generate_markov(self, model=''):                                #не работает на материале пирожков
        with open(model, 'r', encoding="utf-8") as f:
            text = f.read().replace('\n\n', '.')
        text_model = markovify.Text(text)
        res = None
        while res == None:
            res = text_model.make_short_sentence(22)
        print(res)

    def show(self):
        for line in self.lines:
            for word in line:
                print(word, end=' ')
            print('')


my_first_one = Poem()
print("Random")
my_first_one.generate_random()
my_first_one.show()
print("Markov")
my_first_one.generate_markov('pirogi.txt')