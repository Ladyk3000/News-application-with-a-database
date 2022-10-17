from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(506, 241)
        MainWindow.setFixedSize(506, 241)

        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.MainWidget.setMouseTracking(False)

        self.layoutWidget = QWidget(self.MainWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 14, 481, 211))

        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(False)

        self.stress_label = QLabel(self.layoutWidget)
        self.stress_label.setObjectName(u"stress_label")
        self.stress_label.setFont(font)
        self.stress_label.setScaledContents(True)

        self.stress_spinBox = QSpinBox(self.layoutWidget)
        self.stress_spinBox.setObjectName(u"stress_spinBox")
        self.stress_spinBox.setStyleSheet(u"")

        self.stress_menu = QToolButton(self.layoutWidget)
        self.stress_menu.setObjectName(u"stress_menu")

        self.stress_line_layout = QHBoxLayout()
        self.stress_line_layout.setObjectName(u"stress_line_layout")
        self.stress_line_layout.addWidget(self.stress_label)
        self.stress_line_layout.addWidget(self.stress_spinBox, 0, Qt.AlignRight)
        self.stress_line_layout.addWidget(self.stress_menu)

        self.patience_label = QLabel(self.layoutWidget)
        self.patience_label.setObjectName(u"patience_label")
        self.patience_label.setScaledContents(True)

        self.patiense_spinBox = QSpinBox(self.layoutWidget)
        self.patiense_spinBox.setObjectName(u"patiense_spinBox")

        self.patience_menu = QToolButton(self.layoutWidget)
        self.patience_menu.setObjectName(u"patience_menu")

        self.patience_line_layout = QHBoxLayout()
        self.patience_line_layout.setObjectName(u"patience_line_layout")
        self.patience_line_layout.addWidget(self.patience_label)
        self.patience_line_layout.addWidget(self.patiense_spinBox, 0, Qt.AlignRight)
        self.patience_line_layout.addWidget(self.patience_menu)

        self.write_button = QPushButton(self.layoutWidget)
        self.write_button.setObjectName(u"write_button")

        self.news_title_label = QLabel(self.layoutWidget)
        self.news_title_label.setObjectName(u"news_title_label")
        self.news_title_label.setScaledContents(True)

        self.news_label_1 = QLabel(self.layoutWidget)
        self.news_label_1.setObjectName(u"news_label_1")
        self.news_label_1.setEnabled(True)
        self.news_label_1.setFont(font)
        self.news_label_1.setScaledContents(True)

        self.all_objects_vertical_layout = QVBoxLayout(self.layoutWidget)
        self.all_objects_vertical_layout.setObjectName(u"all_objects_vertical_layout")
        self.all_objects_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.all_objects_vertical_layout.addLayout(self.stress_line_layout)
        self.all_objects_vertical_layout.addLayout(self.patience_line_layout)
        self.all_objects_vertical_layout.addWidget(self.write_button, 0, Qt.AlignRight)
        self.all_objects_vertical_layout.addWidget(self.news_title_label)
        self.all_objects_vertical_layout.addWidget(self.news_label_1)

        MainWindow.setCentralWidget(self.MainWidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainWidget.setProperty("window title", QCoreApplication.translate("MainWindow", u"qw", None))
        self.stress_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u0442\u0440\u0435\u0441\u0441\u0430", None))
        self.stress_menu.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.patience_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0442\u0435\u0440\u043f\u0435\u043d\u0438\u044f", None))
        self.patience_menu.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.write_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.news_title_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438:", None))
        self.news_label_1.setText("")


