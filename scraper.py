from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

class Scraper:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.cnbctv18.com/market/"
        self.date = datetime.today().strftime("%b %d, %Y")
        self.articles = []

    def open_page(self):
        self.driver.get(self.url)

    def scrape_articles(self):
        while True:
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            new_articles = soup.find_all("a", class_="mkt-news-ttl")
            stop_scraping = False

            for article in new_articles:
                title = article.find("h3", class_= "small-inner-ttl")
                date = article.find("div", class_= "mkt-ts")
                link = article["href"] if article.has_attr("href") else None

                if title and date and link:
                    title = title.text.strip()
                    article_date_time = date.text.strip().split("\n")[0]

                    if article_date_time.startswith(self.date):
                        self.articles.append({"Title": title, "Date": self.date, "URL": link})
                    else:
                        stop_scraping = True
                        break
            
            if stop_scraping:
                print(f"All articles found for {self.date}.")
                break

            try:
                view_more_button = self.driver.find_element(By.CLASS_NAME, "view-more-yellow")
                self.driver.execute_script("arguments[0].click();", view_more_button)
                time.sleep(2)
            except Exception:
                break

    def close_driver(self):
        self.driver.quit()

    def run_scraper(self):
        self.open_page()
        self.scrape_articles()
        self.close_driver()

    def get_articles(self):
        return self.articles
    
    def generate_csv(self):
        self.run_scraper()
        articles = self.get_articles()
        df = pd.DataFrame(articles)
        file_path = "output/articles.csv"
        df.to_csv(file_path, index=False)
        print(f"csv successfully updated!")