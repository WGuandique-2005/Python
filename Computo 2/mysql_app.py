"""
* Una aplicaion usando PyQt5 y mySQL
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                            QLineEdit, QTextEdit, QLabel, QPushButton,
                            QFormLayout)
import mysql.connector

class myApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,450,380)
        self.setWindowTitle("MySQL")
        self.setContentsMargins(25,10,25,20)
        
        self.db = mysql.connector.connect(
            user="root",
            password="12345",
            host="localhost",
            database="mysql01"
        )
        
        center = QWidget()
        layout = QFormLayout()
        
        lbl1 = QLabel("Ingrese los datos del producto:\n")
        lbl_name = QLabel("Ingrese el nombre:")
        self.txt_name = QLineEdit()
        lbl_price = QLabel("Ingrese el precio: ")
        self.txt_price = QLineEdit()
        lbl_quantity = QLabel("Ingrese la cantidad:")
        self.txt_quantity = QLineEdit()
        self.btn_add = QPushButton("Agregar producto")
        self.btn_see = QPushButton("Ver productos")
        self.btn_add.clicked.connect(self.clicked_add)
        self.btn_see.clicked.connect(self.clicked_see)
        self.view = QTextEdit()
        
        layout.addRow(lbl1)
        layout.addRow(lbl_name, self.txt_name)
        layout.addRow(lbl_price, self.txt_price)
        layout.addRow(lbl_quantity, self.txt_quantity)
        layout.addRow(self.btn_add, self.btn_see)
        layout.addRow(self.view)
        
        center.setLayout(layout)
        self.setCentralWidget(center)
    
    def clicked_add(self):
        try:
            cursor = self.db.cursor()
            name = self.txt_name.text()
            price = float(self.txt_price.text())
            quantity = int(self.txt_quantity.text())
            
            cursor.execute(f"insert into producto (nombre, precio, cantidad) values ('{name}',{price},{quantity});")
            self.view.setText("Producto agregado con exito")
            self.db.commit()
        except:
            self.view.setText("Error al agregar producto")
    
    def clicked_see(self):
        cursor = self.db.cursor()
        cursor.execute("select * from producto")
        resultados = cursor.fetchall()
        
        texto = "Productos:\n"
        texto += "---------\n"
        for fila in resultados:
            texto += f"_id: {fila[0]}\n"
            texto += f"Nombre: {fila[1]}\n"
            texto += f"Precio: {fila[2]}\n"
            texto += f"Cantidad: {fila[3]}\n"
            texto += "---------\n"
        
        self.view.setText(texto)

app = QApplication(sys.argv)
main = myApp()
main.show()
app.exec()