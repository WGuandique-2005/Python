# Programacion Computacional III
# Semana 8: PyQt5

# import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)
ventana = QWidget()
boton = QPushButton("Haz click aquí")
boton.show()

app.exec()