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
            all_span = pt.find_all('span', {'class': 'inline vMiddle'})
            location = geolocator.geocode(""+all_span[0].text +" "+all_span[1].text+" ")
            #print(location.address)
            if location:
                if len(all_li) > 3:
                    sleepingroom = all_li[1].find('a').get('title')
                    bathroom = all_li[2].find('a').get('title')
                    km = all_li[3].find('a').get('title')
                    writer.writerow({'name': name.text, 'price': price.text.replace(',', ''), 'img': img.get(
                        'src'), 'sleepingroom': sleepingroom, 'bathroom': bathroom, 'km': km,'latitude':location.latitude 
                    ,'longitude': location.longitude
                    ,'address':all_span[0].text +" "+all_span[1].text
                    ,'address_accurate':location.address
                    ,'row_address': location.raw})
                    data['name'] = name.text
                    data['price'] = price.text.replace(',', '')
                    data['bathroom'] = bathroom
                    data['sleepingroom'] = sleepingroom
                    data['km'] = km
                    data['latitude'] = location.latitude 
                    data['longitude'] = location.longitude
                    data['address'] = all_span[0].text +" "+all_span[1].text
                    data['address_accurate'] = location.address
                    data['row_address'] = location.raw
                    data['img'] = img.get('src')
                    json_data = json.dumps(data, ensure_ascii=False)
                    file.write(json_data)
                    file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()
