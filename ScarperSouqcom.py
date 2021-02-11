import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="hamza")
filecsv = open('OpenSouqRealEstate.csv', 'w', encoding='utf8')
file = open('OpenSouqRealEstate.json', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://jo.opensooq.com/ar/%D8%B9%D9%85%D8%A7%D9%86/%D8%B9%D9%82%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%B4%D9%82%D9%82-%D9%84%D9%84%D8%A8%D9%8A%D8%B9?page='
file.write('[\n')
data = {}
csv_columns = ['name', 'price', 'img', 'km', 'bathroom', 'sleepingroom','latitude','longitude','address','address_accurate','row_address']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()
for page in range(100):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('li', {'class': 'rectLi'})
    i = 0

    print(len(ancher))
    for pt in ancher:
        #print(pt)
        name = pt.find('a', {'class': 'postSpanTitle'})
        price = pt.find('span', {'class': 'inline ltr'})
        img = pt.find('img', {'class': 'block'})
        all_li = pt.find_all('span', {'class': 'font-12 inline'})
        all_span = pt.find('div', {'class': 'clear font-12'})
        if all_span:
            all_span = pt.find('div', {'class': 'clear font-12'}).text.split('|')
            if len(all_span[1].strip().split())>3:
                loc=all_span[1].strip().split()[0]+" "+all_span[1].strip().split()[1]
            else:
                loc=all_span[1].strip().split()[0]
            print(loc)
            print(all_span[0].strip().split()[0])
            location = geolocator.geocode(str(loc) +" "+all_span[0].strip().split()[0],timeout=10)
            #print(location)
            if location and price:
                if len(all_li) > 3:
                    sleepingroom = all_li[1].get('title')
                    bathroom = all_li[2].get('title')
                    km = all_li[3].get('title')
                    writer.writerow({'name': name.text,
                    'price': price.text.replace(',', ''),
                    'img': img.get('src'),
                    'sleepingroom': sleepingroom,
                    'bathroom': bathroom,
                    'km': km,'latitude':location.latitude 
                    ,'longitude': location.longitude
                    ,'address':str(loc) +" "+all_span[0].strip().split()[0]
                    ,'address_accurate':location.address
                    ,'row_address': location.raw})
                    data['name'] = name.text
                    data['price'] = price.text.replace(',', '')
                    data['bathroom'] = bathroom
                    data['sleepingroom'] = sleepingroom
                    data['km'] = km
                    data['latitude'] = location.latitude 
                    data['longitude'] = location.longitude
                    data['address'] =str(loc) +" "+all_span[0].strip().split()[0]
                    data['address_accurate'] = location.address
                    data['row_address'] = location.raw
                    data['img'] = img.get('src')
                    json_data = json.dumps(data, ensure_ascii=False)
                    file.write(json_data)
                    file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
