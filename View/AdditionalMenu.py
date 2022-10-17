from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QColor

class AdditionalMenu(QtWidgets.QDialog):
    def __init__(self, data, parent=None):
        super(AdditionalMenu, self).__init__(parent)
        self.colors = data
        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(len(self.colors))
        self.table.setColumnCount(len(self.colors[0]))
        self.table.setHorizontalHeaderLabels(["Стрессовость", "Цвет"])

    def get_rgb_from_hex(self, code):
        code_hex = code.replace("#", "")
        rgb = tuple(int(code_hex[i:i + 2], 16) for i in (0, 2, 4))
        return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

    def draw_table(self):
        for i, (name, code) in enumerate(self.colors):
            item_name = QtWidgets.QTableWidgetItem(name)
            item_color = QtWidgets.QTableWidgetItem()
            item_color.setBackground(self.get_rgb_from_hex(code))
            self.table.setItem(i, 0, item_name)
            self.table.setItem(i, 1, item_color)

        self.table.resize(150 * len(self.colors[0]), 45 * len(self.colors))
        #self.table.resize(240,180)
        #print(110 * len(self.colors[0]), 38 * len(self.colors))
        self.table.show()
