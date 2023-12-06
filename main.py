from bs4 import BeautifulSoup
import requests


def title(url):
    url = requests.get(url).text
    soup = BeautifulSoup(url, 'html.parser')
    box = soup.find('div', class_='countries-list')
    country_block = box.find('ul', class_='list')
    countries = country_block.findAll('li')
    for country in countries:
        country_name = country.find('a').get_text(strip=True)
        print(country_name)


example = title('https://kun.uz/')
input()

