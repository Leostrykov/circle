import sys
from UI import Ui_MainWindow

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class MiniSuprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.r = 0
        self.isPainting = False
        self.x = 0
        self.y = 0
        self.color = None
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.isPainting = True
        self.x = randint(0, self.width())
        self.y = randint(0, self.height())
        self.r = randint(0, 200)
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.update()

    def paintEvent(self, event):
        if self.isPainting:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(self.color)
            qp.drawEllipse(int(self.x - self.r / 2), int(self.y - self.r / 2), self.r, self.r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MiniSuprematism()
    a.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
