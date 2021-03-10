import requests
from bs4 import BeautifulSoup

URL = "https://poetory.ru/pir/rating"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_="Content")
print(quotes)