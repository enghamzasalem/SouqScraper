# Search Engine Spider Django Project

This is a Django project that includes: 
- a web crawling utility using a Spider class. It allows you to crawl web pages, extract information, and store results in the database. 
- The project also provides a Django management command to initiate the crawling process.
- there is also Django templates UI to allow search in the scraping data.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- BeautifulSoup
- Requests

### Installation

1. Clone SouqScraper repository and move to search_engine_spider Django project.

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Rename .env_template file into .env and change database settings to yours.
> I recommend you to use PostgreSQL because it supports "Concurrent Access" and you can crawl links and store their data in parallel.
> you can use SQLite if you want, but then you must crawl links one by one.

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

### Spider Class

The `Spider` class in the `scraping_results/spiders/general_spider.py` module allows you to crawl web pages and extract information. It uses the `requests` library for making HTTP requests and `BeautifulSoup` for parsing the page content. The extracted information is stored in the `ScrapingResult` model.

### Django Management Command

The project includes a Django management command named `crawl`. This command allows you to initiate the crawling process with specified parameters.

To use the command, run:

```bash
python manage.py crawl <url> <depth> [--parallel]
```

- `<url>`: The URL from which to start crawling.
- `<depth>`: The depth of crawling (how many levels of links to follow).
- `--parallel`: Optional flag to enable parallel crawling.
> parallel crawling can't be used with SQLite database.

Example:

```bash
python manage.py crawl http://example.com 2 --parallel
```

This will start crawling the specified URL with a depth of 2, and if `--parallel` is provided, it will use parallel crawling.

### Web Interface

The project includes a simple web interface where users can enter a search query and see search results. The search results are fetched from the `ScrapingResult` model and displayed with pagination.

To access the search page, run the development server:

```bash
python manage.py runserver
```

Then visit `http://localhost:8000` in your web browser.

---
