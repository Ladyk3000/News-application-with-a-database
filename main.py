import sys
from View.MainView import MainView
from PySide6.QtWidgets import QApplication

def  main():
    app = QApplication(sys.argv)
    window = MainView()

    with open("View/ui/styles.css", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
