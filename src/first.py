from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class First(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('first.ui', self)