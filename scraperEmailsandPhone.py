from bs4 import BeautifulSoup
import re
import requests

allsite = ["https://enghamzasalem.com/",
           "https://www.ionixxtech.com/", "https://sumatosoft.com", "https://4irelabs.com/", "https://www.leewayhertz.com/",
           "https://stackoverflow.com", "https://www.vardot.com/en", "http://www.clickjordan.net/", "https://vtechbd.com/"]
emails = []
tels = []
for l in allsite:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
print(emails)
print(tels)
