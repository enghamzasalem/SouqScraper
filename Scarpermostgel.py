import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://academy.hsoub.com/freelance/?page='
file = open('hsoubacademy.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name']
for page in range(17):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all(
        'article', {'class': "cCmsCategoryFeaturedEntry "})
    # print(ancher)
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    writer.writeheader()
    for pt in ancher:
        name = pt.find('h2', {'class': 'ipsType_pageTitle'})
        writer.writerow({'name': name})
        name = name.find('a', {})
        data['name'] = name.text
        data['link'] = name.href
        print(name.text)
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
