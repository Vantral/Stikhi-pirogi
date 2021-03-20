from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp

def write_to_file(response):
    soup = BeautifulSoup(response, 'lxml')
    quotes = soup.find_all('div', class_="item-text")
    # print("Page", str(response.url) + "...")
    for item in quotes:
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

async def fetch(session, url):
    async with session.get(url, verify_ssl=False) as response:
        resp = await response.text()
        write_to_file(resp)
        return resp

async def fetch_all(pages):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in pages:
            tasks.append(
                fetch(
                    session,
                    f"https://poetory.ru/pir/rating/{page}",
                )
            )
        responses = await asyncio.gather(*tasks)
        return responses

def run(pages):
    responses = asyncio.run(fetch_all(pages))
    return responses

page = []

for i in range(1, 1601):
    page.append(i)

start = time.time()




run(page)

print(time.time() - start)