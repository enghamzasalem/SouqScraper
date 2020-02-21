import requests
# import urllib.request offline
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('meme.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://imgflip.com/?page='
# https://jamalon.com/en/books?p=7292
# 2055
file = open('meme.json', 'w', encoding='utf8')
API_ENDPOINT = " .firebaseio.com/memes.json"
file.write('[\n')
data = {}
csv_columns = ['name', 'category', 'price', 'img']
for page in range(20):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all(
        'div', {'class': "base-unit clearfix"})
    i = 0
    for pt in ancher:
        img = pt.find('img', {'class': 'base-img'})
        print(img)
        if img:
            data['img'] = img['src']
            json_data = json.dumps(data, ensure_ascii=False)
            r = requests.post(url=API_ENDPOINT, data=json_data.encode('utf-8'))
            file.write(json_data)
            file.write(",\n")
file.write("\n]")
# defining the api-endpoint
filecsv.close()
file.close()
