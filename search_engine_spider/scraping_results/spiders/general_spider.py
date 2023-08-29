import os
import sys
from urllib.parse import urlparse

# Set up Django environment
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'search_engine_spider.settings'
import django
django.setup()

import requests
from bs4 import BeautifulSoup
from scraping_results.models import ScrapingResult


class Spider:
    # crawl a URL
    def crawl(self, url, depth):
        # try to perform HTTP GET request
        try:
            print('Crawling url: "%s" at depth: %d' % (url, depth))
            response = requests.get(url)
        except:
            print('Failed to perform HTTP GET request on "%s"\n' % url)
            return

        # parse page content
        content = BeautifulSoup(response.text, 'lxml')

        # try to extract page title and text content
        try:
            title = content.find('title').text
            page_content = ''
            for tag in content.findAll():
                if hasattr(tag, 'text'):
                    page_content += tag.text.strip().replace('\n', ' ')
        except:
            print('Failed to extract title and description of "%s"\n' % url)
            return

        # store the result structure
        ScrapingResult.objects.get_or_create(url=url, defaults={'title': title, 'content': page_content})

        # return when depth is exhausted
        if depth == 0:
            return

        # extract all the available links on the page
        links = content.findAll('a')

        # loop over links
        for link in links:
            # try to crawl links recursively
            try:
                if link['href'].startswith('http'):
                    self.crawl(link['href'], depth - 1)
                else:
                    parsed_url = urlparse(url)
                    protocol = parsed_url.scheme
                    domain = parsed_url.netloc
                    self.crawl(f'{protocol}://{domain}{link["href"]}', depth - 1)
            except KeyError:
                pass


# Using the Spider
# spider = Spider()
# spider.crawl('https://www.stackoverflow.com', 2)
