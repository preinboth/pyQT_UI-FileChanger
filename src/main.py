import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from first import First
from second import Second
from src.third import Third


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pages.ui', self)
        self.first = First()
        self.stackedWidget.addWidget(self.first)
        self.change_btn_to_first.clicked.connect(self.go_to_first)
        self.second = Second()
        self.stackedWidget.addWidget(self.second)
        self.change_btn_to_second.clicked.connect(self.go_to_second)

        self.third = Third()
        self.stackedWidget.addWidget(self.third)
        self.change_btn_to_third.clicked.connect(self.go_to_third)

        self.show()
    def go_to_first(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_to_second(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_to_third(self):
        self.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
