import random
import json
import numpy as np
import markovify

with open('corporas/mark_pirogi.txt', 'r', encoding="utf-8") as f:
    text = f.read().replace('\n\n', '.')
    text_model = markovify.NewlineText(text)

with open("dictionaries/coll_bigram_perc.json", 'r', encoding="utf-8") as f:
    bi_collocations = json.load(f)
    bi_words = [x for x in bi_collocations]

with open("dictionaries/collocations_percents.json", 'r', encoding="utf-8") as f:
    collocations = json.load(f)
    words = [x for x in collocations]

with open("dictionaries/syllabs.json", 'r', encoding="utf-8") as f:
    syllabs = json.load(f)

with open("dictionaries/last_words_perc.json", 'r', encoding="utf-8") as f:
    last_words = json.load(f)

with open("dictionaries/last_bigrams_perc.json", 'r', encoding="utf-8") as f:
    last_bigrams = json.load(f)


class Poem:
    lines = [[], [], [], []]  # так в моём понимании выглядит четверостишие
    line_count = 0  # отслеживает на какой мы строчке четверостишия

    def generate_token(self, ngram, token):
        if ngram == "bigram":
            coll_dict = bi_collocations
        elif ngram == "unigram":
            coll_dict = collocations

        def rhyme(candidate):  # filter function
            if ngram == "bigram":
                curr_word = token.split()[1]
                candidate = candidate.split()[0]
            elif ngram == "unigram":
                curr_word = token

            if curr_word not in syllabs or len(syllabs[curr_word]) == 1 or len(syllabs[curr_word]) == 0:
                return True

            elif candidate not in syllabs:
                return False

            elif syllabs[curr_word][-1] == "V":
                if len(syllabs[candidate]) == 1 or len(syllabs[candidate]) == 0:
                    return True
                elif syllabs[candidate][1] == "'":
                    return True
                else:
                    return False

            elif syllabs[curr_word][-1] == "'":
                if len(syllabs[candidate]) == 1 or len(syllabs[candidate]) == 0:
                    return True
                elif syllabs[candidate][1] == "V":
                    return True
                else:
                    return False

        candidates = [x for x in coll_dict[token]]  # список коллокатов слова
        candidates = list(filter(rhyme, candidates))  # отфильстрованный по ударениям список коллокатов слова

        if len(candidates) == 0:  # если ни одно не подходит - возьмем любое
            candidates = [x for x in coll_dict[token]]

        freqs = [coll_dict[token][coll] for coll in candidates]  # массив с частотами коллокатов

        if sum(freqs) != 1:  # иногда возникает баг из-за округления в питоне и сумма != 1
            freqs[random.randint(0, len(freqs) - 1)] += 1 - sum(freqs)  # тогда прибавляем разницу рандомному слову

        new_token = np.random.choice(candidates, 1, p=freqs)[0]


        if len(self.lines[self.line_count]) == 4:  # число 5 отвечает за количество слов в строке так что можно подбирать
            self.line_count += 1
            if self.line_count > 3:
                return

        self.lines[self.line_count].append(token)

        self.generate_token(ngram, new_token)

    def generate_markov(self, model=text_model):  # markov generator
        def chunks(lst, n):
            out = []
            for i in range(0, len(lst), n):
                out.append(lst[i:i + n])
            return out

        res = None
        while res is None:
            res = text_model.make_short_sentence(200)
        res = res.split()
        self.lines = chunks(res, 5)

    def show(self):  # func that returns generated thing
        response = ''
        for line in self.lines:
            for word in line:
                response += word + ' '
            response += '\n'
        return response

    def clear(self):
        self.lines = [[], [], [], []]
        self.line_count = 0
