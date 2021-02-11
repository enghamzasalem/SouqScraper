import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://saudi.souq.com/sa-ar/apple/new/a-c/s/?section=2&page='
file = open('SouqDataapple.json','w',encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(1000):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : 'column column-block block-grid-large single-item'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('h6', {'class' : 'title itemTitle'})
        itemPrice=pt.find('span', {'class' : 'itemPrice'})
        img=pt.find('img', {'class' : 'img-size-medium'})
        
        if img:      
            writer.writerow({'name': name.text.replace('                    ', '').strip('\r\n'), 'price': itemPrice.text, 'img': img.get('src')})
            data['name'] =name.text.replace('                    ', '').strip('\r\n')
            data['price'] =itemPrice.text
            data['img'] =img.get('src')
            json_data = json.dumps(data,ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")             
file.write("\n]")
filecsv.close()
file.close()
