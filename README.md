# SouqScraper
Script for scarping items from souq.com using BeautifulSoup and Python3 
you need to install Python3 and BeautifulSoup 

the code is very simple 

```sh
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w',encoding='utf8')
file = open('SouqDataapple.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://saudi.souq.com/sa-ar/apple/new/a-c/s/?section=2&page='
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
file.write("\n]")
filecsv.close()
file.close()
```
and the output will be :
```sh
[
{"name": "سماعات ابل اير بودز اللاسلكية، ابيض - MMEF2                ", "price": "665.00", "img": "https://cf4.s3.souqcdn.com/item/2016/10/06/11/64/54/16/item_M_11645416_16747749.jpg"},
{"name": "ابل ايفون 6 مع فيس تايم - 32 جيجا، الجيل الرابع ال تي اي، رمادي                ", "price": "1,160.34", "img": "https://cf4.s3.souqcdn.com/item/2017/03/06/22/15/33/89/item_M_22153389_29502098.jpg"},
{"name": "ابل ايفون X مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, رمادي                ", "price": "3,199.00", "img": "https://cf5.s3.souqcdn.com/item/2018/01/30/24/05/14/26/item_M_24051426_102956405.jpg"},
{"name": "ابل ايفون 8 مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, ذهبي                ", "price": "2,224.99", "img": "https://cf3.s3.souqcdn.com/item/2017/09/12/24/05/14/31/item_M_24051431_35103527.jpg"},
{"name": "ابل ايفون 8 Plus مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, ذهبي                ", "price": "2,548.99", "img": "https://cf5.s3.souqcdn.com/item/2017/09/12/24/05/14/47/item_M_24051447_35103542.jpg"},
{"name": "ابل ايفون 6 بدون فيس تايم- 32 جيجا، الجيل الرابع ال تي اي، ذهبي                ", "price": "1,148.00", "img": "https://cf3.s3.souqcdn.com/item/2017/03/06/22/15/34/81/item_M_22153481_29502385.jpg"},
{"name": "ابل ايفون 6s مع فيس تايم - 64 جيجا، الجيل الرابع LTE، رمادي                ", "price": "3,270.00", "img": "https://cf3.s3.souqcdn.com/item/2015/09/10/89/92/27/3/item_M_8992273_9434431.jpg"},
{"name": "ساعة كورين للرجال - رياضية بسوار من الجلد الصناعي - 8139                ", "price": "23.50", "img": "https://cf2.s3.souqcdn.com/item/2014/05/02/68/93/69/6/item_M_6893696_4618742.jpg"},
{"name": "عطر كالفن كلاين ذا ون للرجال و النساء، متوسط التركيز، 200مل                ", "price": "101.78", "img": "https://cf2.s3.souqcdn.com/item/2015/07/21/46/37/21/4/item_M_4637214_8674641.jpg"},
{"name": "عطر بيوتي النسائي من كالفن كلاين - او دي بارفان، 100 مل                ", "price": "109.85", "img": "https://cf5.s3.souqcdn.com/item/2017/02/20/45/50/82/3/item_M_4550823_28793157.jpg"},
{"name": "سماعات ابل اير بودز اللاسلكية، ابيض - MMEF2                ", "price": "665.00", "img": "https://cf4.s3.souqcdn.com/item/2016/10/06/11/64/54/16/item_M_11645416_16747749.jpg"},
{"name": "ابل ايفون 6 مع فيس تايم - 32 جيجا، الجيل الرابع ال تي اي، رمادي                ", "price": "1,160.34", "img": "https://cf4.s3.souqcdn.com/item/2017/03/06/22/15/33/89/item_M_22153389_29502098.jpg"},
{"name": "ابل ايفون X مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, رمادي                ", "price": "3,199.00", "img": "https://cf5.s3.souqcdn.com/item/2018/01/30/24/05/14/26/item_M_24051426_102956405.jpg"},
{"name": "ابل ايفون 8 مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, ذهبي                ", "price": "2,224.99", "img": "https://cf3.s3.souqcdn.com/item/2017/09/12/24/05/14/31/item_M_24051431_35103527.jpg"},
{"name": "ابل ايفون 8 Plus مع فايس تايم - 64 جيجا, الجيل الرابع ال تي اي, ذهبي                ", "price": "2,548.99", "img": "https://cf5.s3.souqcdn.com/item/2017/09/12/24/05/14/47/item_M_24051447_35103542.jpg"},
{"name": "ابل ايفون 6 بدون فيس تايم- 32 جيجا، الجيل الرابع ال تي اي، ذهبي                ", "price": "1,148.00", "img": "https://cf3.s3.souqcdn.com/item/2017/03/06/22/15/34/81/item_M_22153481_29502385.jpg"},
{"name": "ابل ايفون 6s مع فيس تايم - 64 جيجا، الجيل الرابع LTE، رمادي                ", "price": "3,270.00", "img": "https://cf3.s3.souqcdn.com/item/2015/09/10/89/92/27/3/item_M_8992273_9434431.jpg"},
{"name": "ساعة كورين للرجال - رياضية بسوار من الجلد الصناعي - 8139                ", "price": "23.50", "img": "https://cf2.s3.souqcdn.com/item/2014/05/02/68/93/69/6/item_M_6893696_4618742.jpg"},
{"name": "عطر كالفن كلاين ذا ون للرجال و النساء، متوسط التركيز، 200مل                ", "price": "101.78", "img": "https://cf2.s3.souqcdn.com/item/2015/07/21/46/37/21/4/item_M_4637214_8674641.jpg"},
{"name": "عطر بيوتي النسائي من كالفن كلاين - او دي بارفان، 100 مل                ", "price": "109.85", "img": "https://cf5.s3.souqcdn.com/item/2017/02/20/45/50/82/3/item_M_4550823_28793157.jpg"},
{"name": "سماعات ابل اير بودز اللاسلكية، ابيض - MMEF2                ", "price": "665.00", "img": "https://cf4.s3.souqcdn.com/item/2016/10/06/11/64/54/16/item_M_11645416_16747749.jpg"},
]

```
