import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(url.text, 'html.parser')

popular_news = soup.find(attrs={'class': 'grid-row list-content'})

titles = popular_news.findAll(attrs={'class': 'media__title'})
images = popular_news.findAll(attrs={'class': 'media__image'})

for i in images:
    print(i.find('a').find('img')['title'])
