'''
1. Получить html-код страницы
2. Получить блок с товарами из html-кода
3. Получить данные из блока 
4. Созранить полученные данные в файл (json, csv, txt)
'''
import json

import requests
from bs4 import BeautifulSoup as BS


URL = 'https://enter.kg/computers/noutbuki_bishkek'


def get_html(url):
    html = requests.get(url)
    return html.text
# get_html(URL)


def soup_html(html):
    soup = BS(html, 'lxml')
    return soup

# html = get_html(URL)
# soup_html(html)


def get_data(soup):
    data = soup.find_all('div', class_ = 'row')
    list_ = []
    for nout in data:
        title = nout.find('span', class_ = 'prouct_name').text
        img = 'https://enter.kg' + nout.find('img').get('src')
        price = nout.find('span', class_ = 'price').texts
        list_.append({'title': title, 'img':img, 'price':price})
    return list_

html = get_html(URL)
soup = soup_html(html)
get_data(soup)



















def get_total_page(url, count):
    html = requests.get(f'{url}/results, {count * 100 + 1}-{count * 100}')
    return html.text


def get_last_page(url):
    html = get_html(url)
    soup = soup_html(html)
    last_page = soup.find('span', class_ = 'vm-page-counter').text[-2:]
    return last_page

def write_to_json(data):
    with open('db.json', 'w') as file:
        json_data = json.dumps(data)
        file.write(json_data)


def main(url):
    count = 0
    last_page = get_last_page(url)
    data = []
    while count < int(last_page):
        print(count)
        html = get_total_page(url, count)
        soup = soup_html(html)
        data.append(get_data(soup))
        print(f'спарсилась страница {count+1}')
        count += 1
    write_to_json(data)

main(URL)

















# 'requests-модуль для отправки запросов на сайт'
# 'BS4-он форматирует html в более удобный вид и позволяет использовать методы find, find_all, для поиска тегов'
# 'lxml- парсер, позволяет стягивать информацию с soup'

# # find - метод, который позволяет найти первый тег 
# # find_all - метод, который позволяет найти все теги под каким-то классом. Прилетает list с найденными тегами 

# # .get - мы получаем атрибуты тегов (href, src) 

