import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semana 08")
        self.setGeometry(200, 300, 400, 400)
        boton = QPushButton("salir")
        self.setCentralWidget(boton)
        boton.clicked.connect(exit)


app = QApplication(sys.argv)
ventana = myapp()
ventana.show()
app.exec()
