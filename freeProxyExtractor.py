import requests
from bs4 import BeautifulSoup

def getProxies():
    try:
        r = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('tbody')
        proxies = []
        for row in table:
            if row.find_all('td')[4].text =='elite proxy':
                proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
                proxies.append(proxy)
            else:
                pass
        return proxies
    except:
        print("Error getting proxies")
        pass

if __name__ == '__main__':
    proxies = getProxies()
    print(proxies)