from datetime import datetime

import requests
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QGridLayout
)
from PyQt6.QtCore import Qt
import sys
import time

DURATION_INT = 60
Start = 0
cmd = 'digitemp1.conf'
cmd1 = './temp'
timefmt = '%Y-%m-%d %H:%M:%S'

def secs_to_minsec(secs: int):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.time_left_int = DURATION_INT
        self.myTimer = QtCore.QTimer(self)

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
        # odczyt(self, Start)
        self.time_left_int = DURATION_INT

        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)

    def stop(self):
        Start = 0
        print("Stop")


    def init(self):
        print("Init")

    def timerTimeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.time_left_int = DURATION_INT
            self.odczyt()

        self.update_gui()

    def update_gui(self):
        minsec = secs_to_minsec(self.time_left_int)
        # self.timerLabel.setText(minsec)
        print ("timer", minsec)

    def odczyt(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(2)
        fo = open(cmd1, "r+")
        Lines = fo.readlines()
        print(Lines)
        count = 0
        for line in Lines:
            S = str.split(line, " ")
            # G = S[3]
            # print(G)
            # print(S)
            # count += 1
            # print("Line{}: {}".format(count, line.strip()))
            if S[2] == "Sensor":
                #     print (S)
                print(S[0], S[1], S[3], S[4], S[5], S[6])
                my_date = datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d %H:%M:%S')
                print(my_date)
                #     mydate = datetime.datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d')
                #     # print mydate
                mytime = datetime.fromtimestamp(float(S[0])).strftime('%H:%M:%S')
                print(mytime)
                # print S[0]
                my_string = S[0] + " " + S[1] + " " + S[6] + " " + S[4]
                print(my_string)
                try:
                    # Execute the SQL command
                    r = requests.post('https://tempapi.ct8.pl/addtemp',
                                      json={'my_epoch': S[0], 'nr_hex': S[1], 'temp': S[6], 'nr_czujnika': S[4]})
                except:
                    # Rollback in# case there is any error
                    print("błąd wysłania do API")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
