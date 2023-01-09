import os
import subprocess
import sys
import time

import requests
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit, QGridLayout
)

DURATION_INT = 10
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
        self.cmd_text = None
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
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.labelPath, 3, 0)

        self.textEdit = QTextEdit()
        # self.textEdit.setPlainText("sudo digitemp_DS9097U -i -s /dev/ttyUSB0 -c /home/Desktop/BMS/digitemp.conf")
        self.textEdit.setPlainText("sudo digitemp_DS9097U -i -s /dev/ttyUSB0 -c /home/Desktop/BMS/digitemp.conf")

        self.textEdit.adjustSize()
        self.textEdit.setFixedSize(500, 30)
        layout.addWidget(self.textEdit, 3, 1)

        self.labelPath = QLabel("init cmd: ")
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.labelPath, 4, 0)

        self.init_cmd = QTextEdit()
        # self.textEdit.setPlainText("sudo digitemp_DS9097U -i -s /dev/ttyUSB0 -c /home/Desktop/BMS/digitemp.conf")
        self.init_cmd.setPlainText("")

        self.init_cmd.adjustSize()
        self.init_cmd.setFixedSize(500, 120)
        layout.addWidget(self.init_cmd, 4, 1)

        self.labelPath = QLabel("Odczyt temperatur: ")
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.labelPath, 5, 0)

        button = QPushButton("Start", self)
        button.clicked.connect(self.start)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 6, 0)

        button = QPushButton("Stop")
        button.clicked.connect(self.stop)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 6, 1)

        button = QPushButton("Wyczyść")
        button.clicked.connect(self.clear)
        button.setFixedSize(80, 25)
        layout.addWidget(button, 8, 1)

        self.label = QLabel("CMD: ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label, 7, 0)

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("")
        layout.addWidget(self.textEdit, 7, 1)

    def start(self):
        print("Start")
        self.time_left_int = DURATION_INT
        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)
        self.cmd_text =''

    def stop(self):
        print("Stop")
        self.myTimer.stop()
        self.cmd_text = ''

    def clear(self):
        print("Wyczyść")
        self.cmd_text = ''

    def init(self):
        print("Init")
        # directories = os.system("ls -lh")
        # print(directories)
        directories = os.system("ls")
        # directories = os.system("sudo digitemp_DS9097U -i -s /dev/ttyUSB0 -c /home/Desktop/BMS/digitemp.conf")
        print(directories)
        self.init_cmd.setPlainText("test")

        # subprocess.call(["init.sh", "--input_file=input.txt"])
        # subprocess.call(['sudo', 'digitemp_DS9097U', '-i', '-s', '/dev/ttyUSB0', '-c', '/home/Desktop/BMS/digitemp.conf'], shell=True)
        # subprocess.Popen([sys.executable, "init.py"])

    def timerTimeout(self):
        self.time_left_int -= 1
        if self.time_left_int == 0:
            self.time_left_int = DURATION_INT
            self.odczyt()
        self.update_gui()

    def update_gui(self):
        minsec = secs_to_minsec(self.time_left_int)
        self.textEdit.setPlainText(self.cmd_text)

        print("timer", minsec)
        print("cmd_text\n", self.cmd_text)

    def odczyt(self):
        fo = open(cmd1, "r+")
        Lines = fo.readlines()
        for line in Lines:
            S = str.split(line, " ")
            if S[2] == "Sensor":
                my_string = S[0] + " " + S[1] + " " + S[5] + " " + S[3]
                # print("my_string", my_string)
                # self.textEdit.setPlainText(my_string)
                self.cmd_text +=str(time.strftime('%Y-%m-%d %H:%M:%S')) + " " + str(my_string) + "\n"
                try:
                    # Execute the SQL command
                    r = requests.post('https://tempapi.ct8.pl/addtemp',
                                      json={'my_epoch': S[0], 'nr_hex': S[1], 'temp': S[5], 'nr_czujnika': S[3]})
                except:
                    # Rollback in# case there is any error
                    print("błąd wysłania do API")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
