from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from fake_useragent import UserAgent

ua = UserAgent()

def write_to_file(response):
    soup = BeautifulSoup(response, 'lxml')
    quotes = soup.find_all('div', class_="text")
    # print("Page", str(response.url) + "...")
    try:
        for item in quotes:
            item.text = item.text.replace('<br>', '')
            item.text = item.text.replace('"', '')
            output_file.write(item.text + '\n\n')
    except:
        output_file.write(item.text + '\n\n')
    print("Done")


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


async def fetch(session, url, header):
    async with session.get(url, headers=header, verify_ssl=False) as response:
        resp = await response.text()
        write_to_file(resp)
        return resp


async def fetch_all(pages):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in pages:
            header = {'User-Agent': str(ua.random)}
            tasks.append(
                fetch(
                    session,
                    f"https://stihi.ru/2021/04/04/{page}",
                    header
                )
            )
        responses = await asyncio.gather(*tasks)
        return responses


def run(pages):
    responses = asyncio.run(fetch_all(pages))
    return responses


page = []

for i in range(1, 8704):
    page.append(i)

start = time.time()

run(page)

print(time.time() - start)
