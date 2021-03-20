import requests
from bs4 import BeautifulSoup
import time

"""
pages = []
read = ' '
while read != '':
    read = input("Enter URLs: ")
    pages.append(read)
"""
output_file_path = input("Path to output file: ")

output_file = open(output_file_path, 'w', encoding="utf-8")

print("Loading started")

start = time.time()

for page in range(1, 601):
    URL = 'https://poetory.ru/pir/rating/'
    URL += str(page)
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_="item-text")

    print("Page", str(page) + "...")

    for item in quotes:
        stikh = str(item)
        stikh = stikh.lstrip('<div class="item-text">').rstrip('</div>')
        output_file.write(stikh + '\n\n')
    print(stikh)
    print("Done")

print(time.time() - start)