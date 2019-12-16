import requests
# import urllib.request offline
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('jamlon.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://jamalon.com/en/books?p='
#https://jamalon.com/en/books?p=7292
# 2055
file = open('jamlon.json', 'w', encoding='utf8')
API_ENDPOINT = "https://f.firebaseio.com/books.json"
file.write('[\n')
data = {}
csv_columns = ['name', 'category', 'price', 'img']
for page in range(50):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all(
        'div', {'class': "col-sm-4 col-md-4 col-xs-12"})
    i = 0
    for pt in ancher:
        name = pt.find('h4')
        price = pt.find('span', {'class': 'num'})
        img = pt.find('a', {'class': 'product-image'})
        if name:
            data['name'] = name.text
            data['price'] = price.text
            data['img'] = img.find('img')['src']
            json_data = json.dumps(data, ensure_ascii=False)
            r = requests.post(url=API_ENDPOINT, data=json_data.encode('utf-8'))
            file.write(json_data)
            file.write(",\n")
file.write("\n]")
# defining the api-endpoint
filecsv.close()
file.close()
