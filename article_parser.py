import pandas as pd
from newspaper import Article

class ArticleParser:
    def __init__(self, url_list):
        self.url_list = url_list
        self.data = {'Title': [], 'Content': []}

    def parse(self):
        for url in self.url_list:
            article = Article(url)
            article.download()
            article.parse()

            self.data['Title'].append(article.title)
            self.data['Content'].append(article.text)
        
        df = pd.DataFrame(self.data)
        df.to_csv('output/article.csv')