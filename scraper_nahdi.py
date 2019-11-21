import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('nahdionline.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.nahdionline.com/ar/daily-essentials/hair-products/hair-styling?p='
file = open('nahdionline.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name', 'category', 'img']
for page in range(4):
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
        writer.writerow({'name': name.text})
        data['name'] = name.text
        writer.writerow({'category': url.rsplit('/', 1)[1]})
        data['category'] = url.rsplit('/', 1)[1]
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
