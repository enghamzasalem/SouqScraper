import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('managa.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
file = open('manga.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = [ 'chapter','img']
page=319
for page in range(400,700):
    print('---', page, '---')
    url = 'https://3asq.org/manga/one-piece/'+str(page)+'/?style=list'
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all(
        'img',{'class':'wp-manga-chapter-img'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    #print(ancher)
    for i in ancher:
      writer.writeheader()
      name = i.find('img')
      writer.writerow({'chapter':page,'img': " ".join(i.get('src').split())})
      data['chapter']=page
      data['img'] = " ".join(i.get('src').split())
      json_data = json.dumps(data, ensure_ascii=False)
      file.write(json_data)
      file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()