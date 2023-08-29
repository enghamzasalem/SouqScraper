from django.core.management.base import BaseCommand

from scraping_results.spiders.general_spider import Spider


class Command(BaseCommand):
    help = 'Crawl a URL using the Spider class'

    def add_arguments(self, parser):
        parser.add_argument('url', help='The URL to start crawling from')
        parser.add_argument('depth', type=int, help='The depth of crawling')
        parser.add_argument('--parallel', action='store_true', help='Enable parallel crawling')

    def handle(self, *args, **options):
        url = options['url']
        depth = options['depth']
        parallel = options['parallel']

        spider = Spider()
        spider.crawl(url, depth, parallel=parallel)
