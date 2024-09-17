"""
* Una aplicaion usando PyQt5 y mySQL
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QLineEdit, QTextEdit, QLabel, QPushButton,
                            QFormLayout, QComboBox, QDialog, QRadioButton)
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
        self.lbl_name = QLabel("Ingrese el nombre:")
        self.txt_name = QLineEdit()
        self.lbl_price = QLabel("Ingrese el precio: ")
        self.txt_price = QLineEdit()
        self.lbl_quantity = QLabel("Ingrese la cantidad:")
        self.txt_quantity = QLineEdit()
        self.btn_add = QPushButton("Agregar producto")
        self.btn_see = QPushButton("Ver productos")
        self.btn_add.clicked.connect(self.clicked_add)
        self.btn_see.clicked.connect(self.clicked_see)
        self.view = QTextEdit()
        
        self.btn_update = QPushButton("Actualizar producto")
        self.btn_update.clicked.connect(self.clicked_update)
        self.btn_delete = QPushButton("Eliminar producto")
        self.btn_delete.clicked.connect(self.clicked_deleted)
        self.btn_search = QPushButton("Buscar producto")
        self.btn_search.clicked.connect(self.clicked_search)
        self.btn_exit = QPushButton("Salir")
        self.btn_exit.clicked.connect(self.clicked_exit)
        
        layout.addRow(lbl1)
        layout.addRow(self.lbl_name, self.txt_name)
        layout.addRow(self.lbl_price, self.txt_price)
        layout.addRow(self.lbl_quantity, self.txt_quantity)
        layout.addRow(self.btn_add, self.btn_see)
        layout.addRow(self.view)
        layout.addRow(self.btn_update, self.btn_delete)
        layout.addRow(self.btn_search)
        layout.addRow(self.btn_exit)
        
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
        
    def clicked_update(self):
        self.question = QDialog()
        self.question.setWindowTitle("Actualizar datos")

        self.lbl_id = QLabel("ID:")
        self.txt_id = QLineEdit()
        self.lbl_name = QLabel("Nombre:")
        self.txt_name_update = QLineEdit()
        self.lbl_price = QLabel("Precio:")
        self.txt_price_update = QLineEdit()
        self.lbl_quantity = QLabel("Cantidad:")
        self.txt_quantity_update = QLineEdit()
        btn_yes = QPushButton("Actualizar")
        btn_yes.clicked.connect(self.exec_update)

        layout = QFormLayout()
        layout.addRow(self.lbl_id, self.txt_id)
        layout.addRow(self.lbl_name, self.txt_name_update)
        layout.addRow(self.lbl_price, self.txt_price_update)
        layout.addRow(self.lbl_quantity, self.txt_quantity_update)
        layout.addRow(btn_yes)

        self.question.setLayout(layout)

        if self.question.exec_() == QDialog.Accepted:
            self.exec_update()

    def exec_update(self):
        try:
            cursor = self.db.cursor()
            id = int(self.txt_id.text())
            name = self.txt_name_update.text()
            price = float(self.txt_price_update.text())
            quantity = int(self.txt_quantity_update.text())

            cursor.execute(f"update producto set nombre = '{name}', precio = {price}, cantidad = {quantity} where id = {id};")
            self.view.setText("Producto actualizado con éxito")
            self.db.commit()
            self.question.accept()
        except:
            self.view.setText("Error al actualizar producto")
        
    
    def clicked_deleted(self):
        pass
    
    def clicked_search(self):
        pass
    
    def clicked_exit(self):
        self.question = QDialog()
        self.setWindowTitle("Salir")
        
        layout = QVBoxLayout()
        label = QLabel("¿Está seguro de cerrar la aplicación?")
        btn_yes = QRadioButton("Si")
        btn_no = QRadioButton("No")
        btn_no.setChecked(True)
        
        btn_yes.clicked.connect(lambda: self.close(exit()))
        btn_no.clicked.connect(lambda: self.question.reject())
        
        layout.addWidget(label)
        layout.addWidget(btn_yes)
        layout.addWidget(btn_no)
        
        self.question.setLayout(layout)
        if self.question.exec_() == QDialog.Accepted:
            self.close()

app = QApplication(sys.argv)
main = myApp()
main.show()
app.exec()