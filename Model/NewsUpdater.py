from PySide6 import QtCore
from settings import autoupdate_of_news
import time

class NewsUpdater(QtCore.QThread):
    signal_updater = QtCore.Signal()

    def __init__(self, duration):
        super().__init__()
        self.duration = duration

    def run(self) -> None:
        while autoupdate_of_news == 1:
            self.signal_updater.emit()
            time.sleep(self.duration)