# Password hasheada
"""
password = "Wjgr_2005"
pw_encoded = password.encode()

#? SALT determina la fuerza de hasheo
salt = bcrypt.gensalt(12)
hash_pw = bcrypt.hashpw(pw_encoded,salt)
print(hash_pw)
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
                            QFormLayout, QLineEdit, QPushButton, QLabel,
                            QMessageBox)
import bcrypt
import mysql.connector
import smtplib


class MyLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100,100,350,250)
        self.setContentsMargins(20,20,20,20)
        
        self.db_conn = mysql.connector.connect(
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
        
        self.label = QLabel("¿Crear una cuenta?")
        self.reg = QPushButton("Registrarse")
        self.reg.clicked.connect(self.clicked_reg)
        
        layout.addRow(lbl)
        layout.addRow(lbl_un, self.txt_un)
        layout.addRow(lbl_pw, self.txt_pw)
        layout.addRow(self.btn)
        layout.addRow(self.label, self.reg)
        center.setLayout(layout)
        self.setCentralWidget(center)
        
    def clicked_btn(self):
        user = self.txt_un.text()  # Obtener el texto del campo de usuario
        pw = self.txt_pw.text()  # Obtener el texto del campo de contraseña
        
        if not user or not pw:
            QMessageBox.warning(self, "Error", "Por favor ingrese su usuario y contraseña")
        else:
            cursor = self.db_conn.cursor()
            cursor.execute(f"select * from user where user_name ='{user}'")
            result = cursor.fetchone()

            if result:
                username = result[1]
                stored_pw = result[2].encode()  # No es necesario encodear la contraseña almacenada
                pw_encoded = pw.encode()
                if bcrypt.checkpw(pw_encoded, stored_pw):
                    QMessageBox.information(self, "Sesión iniciada", "Bienvenido")
                else:
                    QMessageBox.warning(self, "Error", "Contraseña incorrecta")
            else:
                QMessageBox.warning(self, "Error", "Usuario no encontrado")
                
    def clicked_reg(self):
        reg_window = RegisterWindow(self)
        reg_window.show()
        
class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Registrarse")
        self.setGeometry(100,100,350,250)
        self.setContentsMargins(20,20,20,20)
        
        center = QWidget()
        layout = QFormLayout()
        
        lbl = QLabel("Registrarse")
        lbl_un = QLabel("Ingrese su nombre de usuario:")
        lbl_pw = QLabel("Contraseña: ")
        lbl_pw2 = QLabel("Confirmar contraseña: ")
        
        self.txt_un = QLineEdit()
        self.txt_pw = QLineEdit()
        self.txt_pw.setEchoMode(QLineEdit.Password)
        self.txt_pw2 = QLineEdit()
        self.txt_pw2.setEchoMode(QLineEdit.Password)
        self.btn_reg = QPushButton("Registrarse")
        self.btn_reg.clicked.connect(self.register_user)
        
        layout.addRow(lbl)
        layout.addRow(lbl_un, self.txt_un)
        layout.addRow(lbl_pw, self.txt_pw)
        layout.addRow(lbl_pw2, self.txt_pw2)
        layout.addRow(self.btn_reg)
        center.setLayout(layout)
        self.setCentralWidget(center)
        
    def register_user(self):
        user = self.txt_un.text()
        pw = self.txt_pw.text()
        pw2 = self.txt_pw2.text()
        
        if not user or not pw or not pw2:
            QMessageBox.warning(self, "Error", "Por favor ingrese todos los campos")
        elif pw != pw2:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
        else:
            pw_encoded = pw.encode()
            salt = bcrypt.gensalt(12)
            hash_pw = bcrypt.hashpw(pw_encoded, salt)
            
            cursor = self.parent.db_conn.cursor()
            cursor.execute("INSERT INTO user (user_name, password) VALUES (%s, %s)", (user, hash_pw))
            self.parent.db_conn.commit()
            
            QMessageBox.information(self, "Registro exitoso", "Usuario creado con éxito")
            self.close()

app = QApplication(sys.argv)
main = MyLogin()
main.show()
app.exec()