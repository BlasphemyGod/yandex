from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from Ui import Ui_MainWindow


from random import randint


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked)

        self.circles = []

    def paintEvent(self, *args, **kwargs):
        for circle in self.circles:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(circle[3])
            qp.drawEllipse(circle[0] - circle[2], circle[1] - circle[2],
                           circle[0] + circle[2], circle[1] - circle[2])
            qp.end()

    def clicked(self):
        self.circles.append((randint(20, self.width() - 20), randint(20, self.height() - 20), randint(10, 300),
                             QColor(randint(0, 255), randint(0, 255), randint(0, 255))))

        self.update()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    exit(app.exec())