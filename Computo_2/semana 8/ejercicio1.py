import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                            QLabel)

class my_window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,350,200)
        self.setWindowTitle("Ejercicio 1")
        
        label = QLabel("William Josue Guandique Rivera, 18 años")        
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = my_window()
window.show()
app.exec()