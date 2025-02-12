from scraper import Scraper

scrape = Scraper()
scrape.run_scraper()
articles = scrape.get_articles()

print(articles)