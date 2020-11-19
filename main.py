import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.check_paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_paint = False

    def draw(self, qp):
        qp.setPen(QColor(255, 211, 25))
        r = randint(20, 60)
        qp.drawEllipse(230, 100, r * 2, r * 2)

    def check_paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle = Circle()
    circle.show()
    sys.exit(app.exec_())
