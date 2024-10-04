# Ejercicio segun mi perspectiva de aplicacion de la documentacion
#! Proceder a la creacion de una tienda
#todo\ Crear un sistema de inventario
#* Función para realizar una compra

#* Defino una clase llamada producto, que contiene las caracteristicas de los productos que usare en la tienda que me plantea 
class producto:
    def __init__(self, nombre, precio, cantidad): # creo el constructor
        self.nombre = nombre # nombre de producto
        self.precio = precio # precio del producto
        self.cantidad = cantidad # cantidad (para mantener un conteo de los productos disponibles)
        self.impuestos = self.mas_impuestos() # el precio total mas impuestos

    def mas_impuestos(self): # esta funcion calculo el precio final |(precio*iva)+precio|
        return (self.precio * 0.13) + self.precio

    def mostrar_datos(self): # muestra los datos organizadamente 
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Total: {self.impuestos}")

# Creo una clase tienda, para definir las funciones que tendre disponible en mi tienda (menu,ingresar prodcutos, mostrarlos y comprar)
class tienda:
    def __init__(self): # Aqui el constructor de esta clase
        self.my_stock = {} # un diccionario para almacenar mi stock de la tienda
        self.productos_comprados = []  # una lista para mis productos comprados, y posiblemente mostrar un resumen de la compra que se realice
        self.total = 0  # total de la compra que se realice

    def ingresar_producto(self): # funcion para ingresar productos
        # los solicito lso datos al usuario
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        # los almaceno en mi diccionario que cree haya arriba en el constructor
        self.my_stock[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"producto {nombre} agregado al inventario.") # mensaje para indicar que el producto fue ingresado

    def mostrar_stock(self): # funcion para mostrar los datos
        if not self.my_stock:
            print("No hay productos en el inventario \nReabastezca el Inventario")
        else:
            for key, value in self.my_stock.items(): # recorro mi diccionario con un for
                print(f"Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad: {value['cantidad']}") # muestro los datos
                print("--------------------------------------------")

    def comprar(self): # funcion para mostrar los productos 
        nombre = input("Ingrese el nombre del producto: ") # solicitamos el nombre o la key del producto
        cantidad = int(input("Ingrese la cantidad a comprar: ")) # cantidad de producto a comprar 
        if nombre in self.my_stock: # un  if para comprobar si hay ese producto para ejecutar la compra
            if self.my_stock[nombre]["cantidad"] >= cantidad: # si la cantidad del producto es mayor a la que hay en el stock
                # restamos la cantidad al stock de la tienda
                self.my_stock[nombre]["cantidad"] -= cantidad
                self.productos_comprados.append((nombre, cantidad)) # agrego esto a la lista, para mostrar mostrar un resumen de la compra
                self.total += self.my_stock[nombre]["precio"] * cantidad # (al total le sumo el precio del producto) y lo multiplico por la cantidad que se lleva del producto
                print(f"Se ha comprado {cantidad} unidades de {nombre}") # un mensaje
            else: # si la cantidad en el stock es menor a la cantidad que se desea llevar
                # se imprime el siguiente mensaje:
                print(f"No hay suficiente stock de {nombre}")
        else: # sino hay ese producto, se imprime:
            print(f"No hay {nombre} en el inventario")

        # Resumen de la compra
        print("\nResumen de la compra:")
        for producto, cantidad in self.productos_comprados: #  recorro la lista, donde almacene los productos que se compraron anteriormente
            print(f"{producto}: {cantidad} x {self.my_stock[producto]['precio']} = {self.my_stock[producto]['precio'] * cantidad}") # muestro un resumen de la compra
        print(f"Total: {self.total}") # precio total
        cash = float(input("Ingrese el efectivo: ")) # Solicito el efectivo
        if cash >= self.total: # compruebo si hay el efectivo
            cambio = cash - self.total # Si hay, doy cel cambio, he imprimo:
            print(f"Cambio: {round(cambio,2)}")
        else: #sino, imprimo:
            print("No hay suficiente efectivo.")

    def menu(self): # el menu
        while True:
            print("---------------------")
            print("BIENVENIDO")
            print("---------------------")
            print("\nMenu:")
            print("1. Ingresar productos")
            print("2. Mostrar stock")
            print("3. Comprar")
            print("4. Salir")
            print("------------------------")
            opcion = input("Ingrese una opcion: ") # opcion ayuda al usuario a esocger que hacer
            match opcion: # matcheo esa opcion, para ejecutar una sentencia dependiendo el caso
                case "1": # caso uno, ingresar productos
                    print("------------------------")
                    self.ingresar_producto()
                case "2": # caso dos, mostrarlos
                    print("------------------------")
                    self.mostrar_stock()
                case "3": # caso tres, realizar compra
                    print("------------------------")
                    self.comprar()
                case "4":
                    print("------------------------")
                    print("Gracias por utilizar el sistema de inventario")
                    break # finalizar programa
                case _:
                    print("------------------------")
                    print("Opcion invalida. Por favor, ingrese una opcion valida.")
                    continue # continuar ejecutando el menu, si la opcion no es valida
                
tienda = tienda() # Almaceno la clase en una variable
tienda.menu() # llamo a la funcion que funge la forma de menu de manera que el usuario pueda realizar las acciones que este contiene