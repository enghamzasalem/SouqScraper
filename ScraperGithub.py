import requests
import re
import time
# import urllib.request offline
from bs4 import BeautifulSoup
# Set the URL you want to webscrape from
url = 'https://github.com/search?q=ionic&type=Users&p='
data = {}
for page in range(10):
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        print(link.get('href'))
