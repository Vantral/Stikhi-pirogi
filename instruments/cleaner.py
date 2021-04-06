import re

with open('corporas/poetry_corpora.txt', 'r', encoding="utf-8") as f:
    text = f.read()

time = re.compile(r"\d+\d*\.\d+\d+\.\d{4}")
link = re.compile(r"http.*\//.*")
hashtag = re.compile(r"#.+")
title = re.compile(r"«+\s*.*\s*»+")
names = re.compile(r"\([А-Я][а-я]* [А-Я][а-я]*\)")

text = re.sub(time, '', text)
text = re.sub(link, '', text)
text = re.sub(hashtag, '', text)
text = re.sub(title, '', text)
text = re.sub(names, '', text)

with open('corporas/poetry_corpora_clear.txt', 'w', encoding="utf-8") as f:
    f.write(text)
