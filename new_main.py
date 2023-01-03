from PyQt6.QtWidgets import (
      QApplication, QVBoxLayout, QWidget, QLabel, QPushButton,QTextEdit,QGridLayout
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
        layout.addWidget(self.label ,0,0,1,2)


        self.labelPath = QLabel("path: ")
        self.labelPath.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        layout.addWidget(self.labelPath, 1,0)

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("sudo digitemp_DS9097U  -a  -c /home/pi/Desktop/BMS/digitemp1.conf")
        self.textEdit.adjustSize()
        layout.addWidget(self.textEdit,1,1)

        button = QPushButton("START",self)
        button.clicked.connect(self.start)
        button.move(10,10)
        layout.addWidget(button,2,0)
 
        button = QPushButton("Stop")
        button.clicked.connect(self.stop)
        layout.addWidget(button,2,1)

        self.label = QLabel("text: ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label, 3,0)
        
        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("text")
        layout.addWidget(self.textEdit,3,1)

    def start(self):
        self.label.setText("New and Updated Text")
     
    def stop(self):
        print(self.label.text())
         
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())