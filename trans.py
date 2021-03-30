src = open("pirogi.txt", 'r', encoding="utf-8")
out = open("mark_pirogi.txt", 'w', encoding="utf-8")
text = src.read()
text = text.split('\n')
for i in text:
    if i == '':
        out.write('\n')
    out.write(i + ' ')

src.close()
out.close()
print('done')