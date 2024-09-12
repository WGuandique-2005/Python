# Sumar 2 numeros

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLineEdit, QHBoxLayout, QLabel

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Semana 08")
        
        boton = QPushButton("Guardar")
        boton.clicked.connect(self.evento_click)
        
        self.label = QLabel()
        
        self.inputxt1 = QLineEdit()
        self.inputxt2 = QLineEdit()
        
        central = QWidget()
        layout = QHBoxLayout()
        
        layout.addWidget(boton)
        layout.addWidget(self.inputxt1)
        layout.addWidget(self.inputxt2)
        layout.addWidget(self.label)
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        
        
    def evento_click(self):
        num1 = float(self.inputxt1.text())
        num2 = float(self.inputxt2.text())
        result = num1 + num2
        self.label.setText(f"La suma es: {result}")



app = QApplication(sys.argv)
ventana = ventana()
ventana.show()
app.exec()