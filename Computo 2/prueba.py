import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QGridLayout, QInputDialog
from PyQt5.QtCore import Qt

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.impuestos = self.mas_impuestos()

    def mas_impuestos(self):
        return (self.precio * 0.13) + self.precio

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\nTotal: {self.impuestos}"

class Tienda(QWidget):
    def __init__(self):
        super().__init__()
        self.my_stock = {}
        self.productos_comprados = []
        self.total = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Tienda')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.menu_label = QLabel("Menu:")
        layout.addWidget(self.menu_label)

        self.ingresar_producto_button = QPushButton("Ingresar productos")
        self.ingresar_producto_button.clicked.connect(self.ingresar_producto)
        layout.addWidget(self.ingresar_producto_button)

        self.mostrar_stock_button = QPushButton("Mostrar stock")
        self.mostrar_stock_button.clicked.connect(self.mostrar_stock)
        layout.addWidget(self.mostrar_stock_button)

        self.comprar_button = QPushButton("Comprar")
        self.comprar_button.clicked.connect(self.comprar)
        layout.addWidget(self.comprar_button)

        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.close)
        layout.addWidget(self.salir_button)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

    def ingresar_producto(self):
        nombre, ok = QInputDialog.getText(self, "Ingresar producto", "Ingrese el nombre del producto:")
        if ok:
            precio, ok = QInputDialog.getDouble(self, "Ingresar producto", "Ingrese el precio del producto:")
            if ok:
                cantidad, ok = QInputDialog.getInt(self, "Ingresar producto", "Ingrese la cantidad del producto:")
                if ok:
                    self.my_stock[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                    self.text_edit.append(f"Producto {nombre} agregado al inventario.")

    def mostrar_stock(self):
        self.text_edit.clear()
        if not self.my_stock:
            self.text_edit.append("No hay productos en el inventario. Reabastezca el Inventario")
        else:
            for key, value in self.my_stock.items():
                self.text_edit.append(f"Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad: {value['cantidad']}")
                self.text_edit.append("--------------------------------------------")

    def comprar(self):
        nombre, ok = QInputDialog.getText(self, "Comprar", "Ingrese el nombre del producto:")
        if ok:
            cantidad, ok = QInputDialog.getInt(self, "Comprar", "Ingrese la cantidad a comprar:")
            if ok:
                if nombre in self.my_stock:
                    if self.my_stock[nombre]["cantidad"] >= cantidad:
                        self.my_stock[nombre]["cantidad"] -= cantidad
                        self.productos_comprados.append((nombre, cantidad))
                        self.total += self.my_stock[nombre]["precio"] * cantidad
                        self.text_edit.append(f"Se ha comprado {cantidad} unidades de {nombre}")
                    else:
                        self.text_edit.append(f"No hay suficiente stock de {nombre}")
                else:
                    self.text_edit.append(f"No hay {nombre} en el inventario")

                self.text_edit.append("\nResumen de la compra:")
                for producto, cantidad in self.productos_comprados:
                    self.text_edit.append(f"{producto}: {cantidad} x {self.my_stock[producto]['precio']} = {self.my_stock[producto]['precio'] * cantidad}")
                self.text_edit.append(f"Total: {self.total}")

                cash, ok = QInputDialog.getDouble(self, "Pagar", "Ingrese el efectivo:")
                if ok:
                    if cash >= self.total:
                        cambio = cash - self.total
                        self.text_edit.append(f"Cambio: {round(cambio,2)}")
                    else:
                        self.text_edit.append("No hay suficiente efectivo.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tienda = Tienda()
    tienda.show()
    sys.exit(app.exec_())