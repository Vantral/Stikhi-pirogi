import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent

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
ua = UserAgent()

for page in range(1, 8704):
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    URL = 'https://stihi.ru/2021/04/04/'
    URL += str(page)
    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_="item-text")

    print("Page", str(page) + "...")

    try:
        for item in quotes:
            item.text = item.text.replace('<br>', '')
            item.text = item.text.replace('"', '')
            output_file.write(item.text + '\n\n')
    except:
        output_file.write(item.text + '\n\n')
    print("Done")

print(time.time() - start)
