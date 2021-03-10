import requests
from bs4 import BeautifulSoup

pages = []
read = ' '
while read != '':
    read = input("Enter URLs: ")
    pages.append(read)

output_file_path = input("Path to output file: ")

output_file = open(output_file_path, 'w', encoding="utf-8")

for URL in pages:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_="item-text")

    for item in quotes:
        stikh = str(item)
        stikh = stikh.lstrip('<div class="item-text">').rstrip('</div>')
        output_file.write(stikh + '\n\n')