# Semana 8

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Semana 08")
        
        boton = QPushButton("Haz click aquí")
        boton.clicked.connect(self.evento_click)
        self.setCentralWidget(boton)
        
    def evento_click(self):
        print("Has hecho clic en el botón")

app = QApplication(sys.argv)
ventana = ventana()
ventana.show()
app.exec()