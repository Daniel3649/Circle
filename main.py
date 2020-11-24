import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from Ul import Ui_MainWindow


class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        R, G, B = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setPen(QColor(R, G, B))
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
