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
for page in range(100):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('li', {'class': 'rectLi ie relative mb15'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    writer.writeheader()
    for pt in ancher:
        if pt.find('span', {'class': 'inline vMiddle postSpanTitle'}) and pt.find('span', {'class': 'inline ltr'}):
            name = pt.find('span', {'class': 'inline vMiddle postSpanTitle'})
            price = pt.find('span', {'class': 'inline ltr'})
            img = pt.find('img', {'class': 'block'})
            all_li = pt.find_all('li', {'class': 'ml8'})
            print(len(all_li))
            if len(all_li) > 3:
                type = all_li[1].find('a').get('title')
                year = all_li[2].find('a').get('title')
                km = all_li[3].find('a').get('title')
                print(km.split('-'))
                print(km[0])
                print(km[1])
                print(km[2])
                writer.writerow({'name': name.text, 'price': price.text.replace(',', ''), 'img': img.get(
                    'src'), 'type': type, 'year': year, 'km': km})
                data['name'] = name.text
                data['price'] = price.text.replace(',', '')
                data['year'] = year
                data['type'] = type
                data['km'] = km
                data['img'] = img.get('src')
                json_data = json.dumps(data, ensure_ascii=False)
                file.write(json_data)
                file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
