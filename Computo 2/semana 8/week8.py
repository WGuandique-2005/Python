# Semana 8

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLineEdit, QHBoxLayout, QLabel

#! Signals de PyQt5
# clicked, textChanged, toggled, valueChanged

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Semana 08")
        
        
        boton = QPushButton("Guardar")
        boton.clicked.connect(self.evento_click)
        
        self.label = QLabel()
        
        
        self.inputxt= QLineEdit()
        # inputxt.textChanged.connect(self.evento_text)
        
        central = QWidget()
        layout = QHBoxLayout()
        
        layout.addWidget(boton)
        layout.addWidget(self.inputxt)
        layout.addWidget(self.label)
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        
        #? self.setCentralWidget(boton)
        
    def evento_click(self):
        #print("Has hecho clic en el botón")
        txtint = self.inputxt.text()
        self.label.setText(txtint)
        
    def evento_text(self):
        print("El texto ha cambiado")

app = QApplication(sys.argv)
ventana = ventana()
ventana.show()
app.exec()