import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class my_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ejercicio 2")
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()

        self.keyInput = QLineEdit()
        self.keyInput.setEchoMode(QLineEdit.Password)  # Hide input characters
        layout.addWidget(self.keyInput)

        btn = QPushButton("Submit")
        btn.clicked.connect(self.click_btn)
        layout.addWidget(btn)

        self.setLayout(layout)

    def click_btn(self):
        clave = self.keyInput.text()
        print(f"Secret key: {clave}")

app = QApplication(sys.argv)
window = my_window()
window.show()
sys.exit(app.exec_())