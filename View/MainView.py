from View.MainViewDesign import UiMainWindow
from View.AdditionalMenu import AdditionalMenu
from Model.NewsScrapper import NewsScrapper
from Model.NewsUpdater import NewsUpdater
from Repository.DatabaseUpdater import DataBaseUpdater
from Repository.WebStarter import WebStarter
from PySide6.QtWidgets import QMainWindow
import random
from settings import stress_colors, patience_colors, duration_autoscrape_of_news, duration_autoupdate_of_news, url_to_parse

class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Best App Ever')

        self.ui.write_button.clicked.connect(self.update_spinboxes)
        self.ui.stress_menu.clicked.connect(self.display_stress_menu)
        self.ui.patience_menu.clicked.connect(self.display_patience_menu)

        self.news_scrapper_thread = NewsScrapper(url_to_parse, duration_autoscrape_of_news)
        self.news_scrapper_thread.start()

        self.news_updater_thread = NewsUpdater(duration_autoupdate_of_news)
        self.news_updater_thread.signal_updater.connect(self.update_labels)
        self.news_updater_thread.start()

        self.db_updater_thread = DataBaseUpdater()
        self.db_updater_thread.start()

        self.web_db_updater_thread = WebStarter()
        self.web_db_updater_thread.start()

    def update_spinboxes(self):
        if self.db_updater_thread.signal_db_updater == 1:
            self.ui.write_button.setEnabled(False)
        else:
            self.ui.write_button.setEnabled(True)
        self.db_updater_thread.update_data(self.ui.stress_spinBox.value(), self.ui.patiense_spinBox.value())
        self.ui.patiense_spinBox.setValue(0)
        self.ui.stress_spinBox.setValue(0)

    def update_labels(self):
        limit = 42
        text = self.news_scrapper_thread.news[random.randint(1,10)]
        if len(text) > limit:
            text = text[:limit] + '...'
        self.ui.news_label_1.setText(text)

    def display_stress_menu(self):
        window = AdditionalMenu(stress_colors)
        window.draw_table()
        window.setFixedSize(300, 270)
        window.exec()

    def display_patience_menu(self):
        window = AdditionalMenu(patience_colors)
        window.draw_table()
        window.setFixedSize(260, 180)
        window.exec()
