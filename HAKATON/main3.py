import requests
from bs4 import BeautifulSoup as BS
import csv
from modul import Product

def parser(url: str, max_item: int):
    create_csv()
    page = 1
    count_items = 0
    while count_items < max_item:
        list_products = []
        res = requests.get(f"{url}?page={page}")
        soup = BS(res.text , 'lxml')
        phones = soup.find_all('div', class_ = 'item product_listbox oh')

        for phone in phones:
            if count_items >= max_item:
                break
            count_items += 1
            title = phone.find('div', class_ = 'listbox_title oh').find('a').text.strip()
            price = phone.find('div', class_ = 'listbox_price text-center').text.strip().split('сом')[0] +'сом'
            img = 'https://www.kivano.kg/' + phone.find('img').get('src')
            list_products.append(Product(title=title,
                                        price=price,
                                        img=img))
        
        write_csv(list_products)
        page += 1

def create_csv():
    with open('kivano.csv', 'w') as file_:
        writter = csv.writer(file_)
        writter.writerow([
            'Телефон',
            'Цена',
            'Ссылка на фото'
        ])

def write_csv(phones: list[Product]):
    with open('kivano.csv', 'a') as file_:
        writer = csv.writer(file_)
        for product in phones:
                writer.writerow([
                    product.title,
                    product.price,
                    product.img
                ])

parser(url = 'https://www.kivano.kg/mobilnye-telefony', max_item=401)





























# if __name__ == "__main__":