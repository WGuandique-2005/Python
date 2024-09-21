import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QLineEdit, QTextEdit, QLabel, QPushButton,
                            QFormLayout, QComboBox, QDialog, QRadioButton,
                            QMessageBox)
import bcrypt
import mysql.connector
import smtplib

class MyLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100,100,350,150)
        self.setContentsMargins(20,20,20,20)
        
        self.db = mysql.connector.connect(
            user="root",
            password="12345",
            host="localhost",
            database="mysql01"
        )
        
        center = QWidget()
        layout = QFormLayout()
        
        lbl = QLabel("Inicio de sesion")
        lbl_un = QLabel("Ingrese su nombre de usuario:")
        lbl_pw = QLabel("Contraseña: ")
        
        self.txt_un = QLineEdit()
        self.txt_pw = QLineEdit()
        self.txt_pw.setEchoMode(QLineEdit.Password)
        self.btn = QPushButton("Iniciar")
        self.btn.clicked.connect(self.clicked_btn)
        
        layout.addRow(lbl)
        layout.addRow(lbl_un, self.txt_un)
        layout.addRow(lbl_pw, self.txt_pw)
        layout.addRow(self.btn)
        center.setLayout(layout)
        self.setCentralWidget(center)
        
    def clicked_btn(self):
        user = self.txt_un.text()  # Obtener el texto del campo de usuario
        pw = self.txt_pw.text()  # Obtener el texto del campo de contraseña
        
        if not user or not pw:
            QMessageBox.warning(self, "Error", "Por favor ingrese su usuario y contraseña")
        else:
            cursor = self.db.cursor()
            cursor.execute(f"select * from user where user_name ='{user}'")
            result = cursor.fetchone()

            if result:
                username = result[1]
                stored_pw = result[2].encode()  # No es necesario encodear la contraseña almacenada
                pw_encoded = pw.encode()
                if bcrypt.checkpw(pw_encoded, stored_pw):
                    QMessageBox.information(self, "Sesión iniciada", "Bienvenido")
                    self.hide()
                    main_window = myApp(self, self)
                    main_window.show()
                else:
                    QMessageBox.warning(self, "Error", "Contraseña incorrecta")
            else:
                QMessageBox.warning(self, "Error", "Usuario no encontrado")



class myApp(QMainWindow):
    def __init__(self, parent=None, login=None):
        super().__init__(parent)
        self.login = login
        
        self.setGeometry(100,100,450,380)
        self.setWindowTitle("Administración de Productos")
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
        self.btn_exit = QPushButton("Cerrar sesión")
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
        btn_no = QPushButton("Volver")
        btn_no.clicked.connect(lambda: self.question.reject())

        layout = QFormLayout()
        layout.addRow(self.lbl_id, self.txt_id)
        layout.addRow(self.lbl_name, self.txt_name_update)
        layout.addRow(self.lbl_price, self.txt_price_update)
        layout.addRow(self.lbl_quantity, self.txt_quantity_update)
        layout.addRow(btn_yes, btn_no)

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
        self.question = QDialog()
        self.question.setWindowTitle("Eliminar producto")
        
        layout = QFormLayout()
        self.lbl_id = QLabel("Ingrese el ID del producto:")
        self.txt_id = QLineEdit()
        
        btn_yes = QPushButton("Eliminar")
        btn_yes.clicked.connect(self.exec_delete)
        btn_no = QPushButton("Volver")
        btn_no.clicked.connect(lambda: self.question.reject())
        
        layout.addRow(self.lbl_id, self.txt_id)
        layout.addRow(btn_yes, btn_no)
        
        self.question.setLayout(layout)

        if self.question.exec_() == QDialog.Accepted:
            pass  # No necesitamos hacer nada aquí

    def exec_delete(self):
        try:
            cursor = self.db.cursor()
            id = int(self.txt_id.text())
            cursor.execute(f"delete from producto where id = {id}")
            self.view.setText("Producto eliminado con éxito")
            self.db.commit()
        except:
            self.view.setText("Error al eliminar producto")
        finally:
            self.question.accept()
    
    def clicked_search(self):
        self.question = QDialog()
        self.question.setWindowTitle("Buscar producto")
        
        layout = QFormLayout()
        self.lbl_id = QLabel("Ingrese el ID del producto:")
        self.txt_id = QLineEdit()
        
        btn_yes = QPushButton("Buscar")
        btn_yes.clicked.connect(self.exec_search)
        btn_no = QPushButton("Volver")
        btn_no.clicked.connect(lambda: self.question.reject())
        
        layout.addRow(self.lbl_id, self.txt_id)
        layout.addRow(btn_yes, btn_no)
        
        self.question.setLayout(layout)

        if self.question.exec_() == QDialog.Accepted:
            pass  # No necesitamos hacer nada aquí
        
    def exec_search(self):
        try:
            cursor = self.db.cursor()
            id = int(self.txt_id.text())
            cursor.execute(f"select * from producto where id = {id}")
            resultados = cursor.fetchall()
            
            if resultados:
                texto = "Producto encontrado:\n"
                texto += "---------\n"
                for fila in resultados:
                    texto += f"_id: {fila[0]}\n"
                    texto += f"Nombre: {fila[1]}\n"
                    texto += f"Precio: {fila[2]}\n"
                    texto += f"Cantidad: {fila[3]}\n"
                    texto += "---------\n"
                self.view.setText(texto)
            else:
                self.view.setText("Producto no encontrado")
        except:
            self.view.setText("Error al buscar producto")
        finally:
            self.question.accept()
        
    
    def clicked_exit(self):
        self.question = QDialog()
        self.question.setWindowTitle("Cerrar sesión")
        
        layout = QVBoxLayout()
        label = QLabel("¿Está seguro de cerrar sesión?")
        btn_yes = QRadioButton("Si")
        btn_no = QRadioButton("No")
        btn_no.setChecked(True)
        
        btn_yes.clicked.connect(self.exit_main)
        btn_no.clicked.connect(lambda: self.question.reject())
        
        layout.addWidget(label)
        layout.addWidget(btn_yes)
        layout.addWidget(btn_no)
        
        self.question.setLayout(layout)
        if self.question.exec_() == QDialog.Accepted:
            self.close()

    def exit_main(self):
        self.hide()
        self.question.close()
        self.login.txt_un.clear()
        self.login.txt_pw.clear()
        login.show()

app = QApplication(sys.argv)
login = MyLogin()
login.show()
sys.exit(app.exec_())