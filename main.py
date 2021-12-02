from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPen
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QCursor
from PyQt5 import uic
from random import randint


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.setText("Нажми на меня")
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_(self, qp):
        qp.setBrush(QColor(255, 255, 0))  # randint(0, 255), randint(0, 255), randint(0, 255)
        qp.drawEllipse(randint(10, 500), randint(10, 500), randint(10, 300), randint(10, 300))


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())

