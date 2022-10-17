import requests
from bs4 import BeautifulSoup
import time
from PySide6 import QtCore
from settings import autoscrape_of_news

class NewsScrapper(QtCore.QThread):
    signal_scraper = QtCore.Signal()

    def __init__(self, url, duration):
        super().__init__()
        self.url = url
        self.duration = duration
        self.news = [' ' for i in range(11)]

    def run(self) -> None:
        while autoscrape_of_news == 1:
            try:
                response = requests.get(self.url)
                print(response.status_code)
            except Exception as ex:
                print(ex)
                break

            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('span', class_='card-mini__title')
            news_list = []
            for quote in quotes[:11]:
                news_list.append(quote.text)
            self.news = news_list
            self.signal_scraper.emit()
            time.sleep(self.duration)
