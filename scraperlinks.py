from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

allsite = ["https://enghamzasalem.com/",
           "https://www.ionixxtech.com/", "https://sumatosoft.com", "https://4irelabs.com/", "https://www.leewayhertz.com/",
           "https://stackoverflow.com", "https://www.vardot.com/en", "http://www.clickjordan.net/", "https://vtechbd.com/"]
links = []
tels = []
for l in allsite:
    html_page = urlopen(l).read()
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        links.append(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
print(links)
print(tels)
