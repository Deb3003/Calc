#ivkrugl@tut.by
#написано на VScode, версия Python 3.10
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QDialog, QInputDialog, QLineEdit)

def vi2():
        number = vvod.text()
        number = int(number, 2)
        vivod.setText(str(number))

def vi10():
        number = bin(int(vvod.text()))
        vivod.setText(number[2:])
        




app = QApplication([])
cal = QWidget()
cal.show()

tex = QLabel('Калькулятор систем исчисления')

btn1 = QPushButton('2 - 10')
btn2 = QPushButton('10 - 2')
vvod = QLineEdit()
vivod = QLabel('Ответ')



layout1 = QVBoxLayout()   
layout2 = QHBoxLayout() 
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()

layout4.addWidget(btn1, alignment=Qt.AlignCenter)
layout4.addWidget(btn2, alignment=Qt.AlignCenter)
layout3.addWidget(vvod, alignment=Qt.AlignCenter)
layout3.addWidget(vivod, alignment=Qt.AlignCenter)
layout2.addWidget(tex, alignment=Qt.AlignCenter)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
layout1.addLayout(layout4)

cal.setLayout(layout1)
btn1.clicked.connect(vi2)
btn2.clicked.connect(vi10)
#btn4.clicked.connect()

 
app.exec_()