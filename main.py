from scraper import Scraper
from article_parser import ArticleParser

scrape = Scraper()
url_list = scrape.get_articles()

article_parser = ArticleParser(url_list)
article_parser.parse()