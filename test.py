import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets
import datetime


def display_time():

    current_time = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
    label.setText(current_time)

    print('current_time:', current_time)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # some GUI in window
    label = QtWidgets.QLabel(window, text='???', alignment=Qt.AlignCenter)
    window.setCentralWidget(label)
    window.show()

    # timer which repate function `display_time` every 1000ms (1s)
    timer = QTimer()
    timer.timeout.connect(display_time)  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    sys.exit(app.exec())
