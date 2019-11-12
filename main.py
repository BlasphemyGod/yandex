from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.pushButton.clicked.connect(self.clicked)

        self.circles = []

    def paintEvent(self, *args, **kwargs):
        for circle in self.circles:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.drawEllipse(circle[0] - circle[2], circle[1] - circle[2],
                           circle[0] + circle[2], circle[1] - circle[2])
            qp.end()

    def clicked(self):
        self.circles.append((randint(0, self.width()), randint(0, self.height()), randint(10, 500)))

        self.update()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    exit(app.exec())