import os
import sys

# Set up Django environment
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'search_engine_spider.settings'
import django
django.setup()

import requests
from bs4 import BeautifulSoup
from scraping_results.models import ScrapingResult
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


class Spider:
    # crawl a URL
    def crawl(self, url, depth, parallel=True):
        # set parallel=False if you use sqlite or any database which doesn't support concurrent access

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
            print('Failed to extract title and text content of "%s"\n' % url)
            return

        # store the result structure
        ScrapingResult.objects.get_or_create(url=url, defaults={'title': title, 'content': page_content})

        # return when depth is exhausted
        if depth == 0:
            return

        # extract all the available links on the page
        links = content.findAll('a')

        def crawl_link(link):
            try:
                href = link['href']
                if href.startswith('http'):
                    self.crawl(href, depth - 1)
                else:
                    parsed_url = urlparse(url)
                    protocol = parsed_url.scheme
                    domain = parsed_url.netloc
                    self.crawl(f'{protocol}://{domain}{href}', depth - 1)
            except KeyError:
                pass

        if parallel:
            # loop over links in parallel
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(crawl_link, links)
        else:
            # loop over links one by one
            for link in links:
                crawl_link(link)


# Using the Spider
# spider = Spider()
# spider.crawl('https://www.stackoverflow.com', 2)
