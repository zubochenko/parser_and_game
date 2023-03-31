from bs4 import BeautifulSoup
import requests

'''url = "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"

headers = {}
search_response = requests.get(url, headers=headers)
if search_response.status_code ==200:
    soup=BeautifulSoup(search_response.content, 'html.parser')

print(soup.find('h1', {"id": "firstHeading"}).get_text())'''


url = "https://lenta.ru/"
page = requests.get(url)
#print(page.status_code)
filtered_news=[]
all_news = []
soup = BeautifulSoup(page.text, 'html.parser')

all_news = soup.findAll('div', class_='card-mini__text')

for data in all_news:
    if data.find("div") is not None:
        filtered_news.append((data.text))

for data in filtered_news:
    print(data[:-5])