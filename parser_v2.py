from threading import Thread
import time
import requests
from bs4 import BeautifulSoup

"""
pages = []
read = ' '
while read != '':
    read = input("Enter URLs: ")
    pages.append(read)
"""

def parse(first, last):
    
    for page in range(first, last+1):
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

output_file_path = input("Path to output file: ")

output_file = open(output_file_path, 'w', encoding="utf-8")

print("Loading started")

th = Thread(target=parse, args=(1, 100))
th.start()
th = Thread(target=parse, args=(101, 200))
th.start()
th = Thread(target=parse, args=(201, 300))
th.start()

print(time.time() - start)