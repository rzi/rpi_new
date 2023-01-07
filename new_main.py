from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QGridLayout
)
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Pomiary temperatur")

        layout = QGridLayout()
        self.setLayout(layout)

        self.label = QLabel("Zarządzanie pomiarami temperatur")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.adjustSize()
        layout.addWidget(self.label, 0, 0, 1, 2)

        self.label = QLabel("Inicjalizacja ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.adjustSize()
        layout.addWidget(self.label, 1, 0)

        button = QPushButton("Init", self)
        button.clicked.connect(self.init)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 2, 0)

        self.labelPath = QLabel("path: ")
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.labelPath, 3, 0)

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("sudo digitemp_DS9097U  -a  -c /home/pi/Desktop/BMS/digitemp1.conf")
        self.textEdit.adjustSize()
        self.textEdit.setFixedSize(500, 60)
        layout.addWidget(self.textEdit, 3, 1)

        self.labelPath = QLabel("Odczyt temperatur: ")
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.labelPath, 4, 0)

        button = QPushButton("START", self)
        button.clicked.connect(self.start)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 5, 0)

        button = QPushButton("Stop")
        button.clicked.connect(self.stop)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 5, 1)

        self.label = QLabel("CMD: ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label, 6, 0)

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("")
        layout.addWidget(self.textEdit, 6, 1)

    def start(self):
        print("Start")

    def stop(self):
        print("Stop")

    def init(self):
        print("Init")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
