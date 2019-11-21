import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://jamalon.com/en/books?p='
file = open('jamlon.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
for page in range(200):
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
        if name:
            data['name'] = name.text
            data['price'] = price.text
            json_data = json.dumps(data, ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
