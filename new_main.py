# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton,QLabel,QVBoxLayout,QWidget

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         self.setGeometry(100,100,400,400)

#         layout = QVBoxLayout()
#         self.setLayout(layout)
 
#         # self.label = QLabel("Aplikacja do zarządzania pomiarami temperatur")
#         # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         # self.label.adjustSize()
#         # layout.addWidget(self.label)
#         label = QLabel("Zarządzanie pomiarami temperatur", self)
#         label.adjustSize()
#         label.move(20, 20)
#         layout.addWidget(label)

#         button = QPushButton("Start",self)        
#         button.move(150,150)
#         button.clicked.connect(self.button_clicked)
#         layout.addWidget(button)
        
#     def button_clicked(self):
#         print( "clicked")
#         self.label.setText("New and Updated Text")


# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())
from PyQt6.QtWidgets import (
      QApplication, QVBoxLayout, QWidget, QLabel, QPushButton
)
from PyQt6.QtCore import Qt
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Pomiary temperatur")
 
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.label = QLabel("Zarządzanie pomiarami temperatur")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.adjustSize()
        layout.addWidget(self.label)
 
        button = QPushButton("START",self)
        button.clicked.connect(self.start)
        # button.move(10,10)
        layout.addWidget(button)
 
        button = QPushButton("Stop")
        button.clicked.connect(self.stop)
        layout.addWidget(button)
 
    def start(self):
        self.label.setText("New and Updated Text")
     
    def stop(self):
        print(self.label.text())
         
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())