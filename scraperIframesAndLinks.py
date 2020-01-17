from bs4 import BeautifulSoup
import re
import requests
site = ["https://anime4up.com"]
allsite = []
linkes = []
for l in site:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^https:")}):
        allsite.append(link.get('href'))
print(allsite)
for l in allsite:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('iframe', attrs={}):
        linkes.append(link.get('src'))
        print(link.get('src'))
print("Finsihed")
