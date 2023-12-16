import sys
import io

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randint


class MiniSuprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.r = 0
        self.isPainting = False
        self.x = 0
        self.y = 0
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.isPainting = True
        self.x = randint(0, self.width())
        self.y = randint(0, self.height())
        self.r = randint(0, 200)
        self.update()

    def paintEvent(self, event):
        if self.isPainting:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(int(self.x - self.r / 2), int(self.y - self.r / 2), self.r, self.r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MiniSuprematism()
    a.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
