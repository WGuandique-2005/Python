import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, 
                            QPushButton, QLineEdit, QLabel, QVBoxLayout)

class mi_ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 300, 350)
        self.setWindowTitle("Calculadora") 
        
        center = QWidget()
        layout = QVBoxLayout()
                
        btnCalc = QPushButton("Calcular")
        label0 = QLabel("Ingrese que desea realizar:")
        self.editTxtop = QLineEdit("+  -  /  *")
        labelx = QLabel("_____________________________________________")
        self.label = QLabel()
        self.editTxt1 = QLineEdit()
        self.editTxt2 = QLineEdit()
        
        btnCalc.clicked.connect(self.calc_action)

        layout.addWidget(label0)
        layout.addWidget(labelx)
        layout.addWidget(self.editTxt1)
        layout.addWidget(self.editTxtop)
        layout.addWidget(self.editTxt2)
        layout.addWidget(btnCalc)
        layout.addWidget(self.label)
        
        center.setLayout(layout)   
        self.setCentralWidget(center) 

    def get_numbers(self):
        try:
            num1 = float(self.editTxt1.text())
            num2 = float(self.editTxt2.text())
            return num1, num2
        except ValueError:
            self.label.setText("Error: Invalid input")
            return None, None

    def calc_action(self):
        num1, num2 = self.get_numbers()
        if num1 is None or num2 is None:
            return

        match self.editTxtop.text():
            case "+":
                result = num1 + num2
                self.label.setText(f"La suma es: {result}")
            case "-":
                result = num1 - num2
                self.label.setText(f"La resta es: {result}")
            case "/":
                if num2 != 0:
                    result = num1 / num2
                    self.label.setText(f"La division es: {result}")
                else:
                    self.label.setText("Error: Division por zero")
            case "*":
                result = num1 * num2
                self.label.setText(f"La multiplicacion es de: {result}")

app = QApplication(sys.argv)
vent = mi_ventana()
vent.show()
app.exec()