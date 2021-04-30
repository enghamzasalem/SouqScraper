import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('OpenSouqnew.csv', 'w', encoding='utf8')
file = open('OpenSouqnew.json', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://jo.opensooq.com/ar/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9?page='
file.write('[\n')
data = {}
csv_columns = ['name', 'price', 'img', 'km', 'year', 'type']
for page in range(5):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('li', {'class': 'rectLi'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    print(len(ancher))
    writer.writeheader()
    for pt in ancher:
      name = pt.find('h2', {'class': 'mb15'})
      if name :
        print(name.text)
        price = pt.find('span', {'class': 'inline ltr'})
        img = pt.find('img', {'class': 'block'})
        all_li = pt.find_all('li', {'class': 'ml8'})
        writer.writerow({'name': name.text})
        data['name'] = name.text
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
