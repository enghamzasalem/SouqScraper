import requests
# import urllib.request offline
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('nahdionline.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.nahdionline.com/ar/daily-essentials/hair-products/hair-styling?p='
file = open('nahdionline.json', 'w', encoding='utf8')
API_ENDPOINT = "https://f.firebaseio.com/products.json"
file.write('[\n')
data = {}
csv_columns = ['name', 'category', 'price', 'img']
for page in range(20):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all(
        'li', {'class': 'item product product-item'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    writer.writeheader()
    for pt in ancher:
        name = pt.find('strong', {'class': 'product name product-item-name'})
        price = pt.find('span', {'class': 'price'})
        img = pt.find('span', {'class': 'product-image-wrapper'})
        data['img'] = img.find('img')['src']
        writer.writerow({'name': name.text})
        writer.writerow({'img': data['img']})
        writer.writerow({'price': price.text})
        data['price'] = price.text
        data['name'] = name.text.replace('                                \n', '').replace(
            '\n\n                                    ', '')
        writer.writerow({'category': url.rsplit('/', 1)[1]})
        data['category'] = url.rsplit('/', 1)[1].replace('?p=', '')
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        r = requests.post(url=API_ENDPOINT, data=json_data.encode('utf-8'))
        file.write(",\n")
file.write("\n]")
# defining the api-endpoint
filecsv.close()
file.close()
