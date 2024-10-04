# Crea una apliacacion para sacar el area de un triangulo
# El usuario ingresa la base y la altura del triangulo
# La aplicacion debe calcular y mostrar el area del triangulo
# con PyQt5

# Importamos los módulos necesarios de PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                            QLabel, QLineEdit, 
                            QPushButton, QVBoxLayout)

# Definimos una clase llamada TriangleAreaApp que hereda de QWidget
class TriangleAreaApp(QWidget):
    def __init__(self):
        # Llamamos al constructor de la clase padre (QWidget)
        super().__init__()

        # Inicializamos la interfaz de usuario
        self.initUI()

    def initUI(self):
        # Establecemos la geometría de la ventana (x, y, ancho, alto)
        self.setGeometry(300, 300, 300, 200)
        
        # Establecemos el título de la ventana
        self.setWindowTitle('Calculadora de Área de Triángulo')

        # Creamos un layout vertical para organizar los widgets
        layout = QVBoxLayout()

        # Creamos una etiqueta y un campo de texto para la base del triángulo
        label_base = QLabel('Base:')
        self.base_input = QLineEdit()
        layout.addWidget(label_base)
        layout.addWidget(self.base_input)

        # Creamos una etiqueta y un campo de texto para la altura del triángulo
        label_altura = QLabel('Altura:')
        self.altura_input = QLineEdit()
        layout.addWidget(label_altura)
        layout.addWidget(self.altura_input)

        # Creamos un botón para calcular el área
        calculate_button = QPushButton('Calcular Área')
        
        # Conectamos el botón con el método calculateArea
        calculate_button.clicked.connect(self.calculateArea)
        layout.addWidget(calculate_button)

        # Creamos una etiqueta para mostrar el área calculada
        self.area_label = QLabel('')
        layout.addWidget(self.area_label)

        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def calculateArea(self):
        # Obtenemos los valores de la base y la altura de los campos de texto
        base = float(self.base_input.text())
        altura = float(self.altura_input.text())
        
        # Calculamos el área del triángulo
        area = 0.5 * base * altura
        
        # Establecemos el texto de la etiqueta de área con el valor calculado
        self.area_label.setText(f'Área: {area:.2f}')

if __name__ == '__main__':
    # Creamos una instancia de QApplication
    app = QApplication(sys.argv)
    
    # Creamos una instancia de la clase TriangleAreaApp
    window = TriangleAreaApp()
    
    # Mostramos la ventana
    window.show()
    
    # Iniciamos el bucle de eventos de la aplicación
    sys.exit(app.exec_())