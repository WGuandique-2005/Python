"""
* Un concesionario de carros vende vehiculos nacionales e importados
! Todos tienen 4 ruedas y capacidad para 5 pasajeros (se debe registrar esto, por razones de ley)
todo\ Requiere un programa que le permita ingrersar las primeras 10 cualidades de los carros
? El precio de venta de cada auto es el precio de compra por 1.4 que corresponde al margen de ganancia
"""

class carro(): # Creamos una clase llamada carro que contenga las cualidades de los carros
    def __init__(self, marca, modelo, año, color, tipo_combustible, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.precio_compra = precio_compra
        self.pasejeros = 5 # esto es un dato que se debe registrar esto, por razones de ley
        self.ruedas = 4 # al igual este
        self.precio_venta = self.precio_venta() # creamos una funcion para obtener el precio de venta con un margen de ganancia
    
    def precio_venta(self): # Aqui esta la funcion
        return self.precio_compra * 1.4
    
    def mostrar_datos(self): # Aqui muestro los datos de la clase de manera ordenada
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
        print(f"Precio de compra: {self.precio_compra}")
        print(f"Precio de venta: {self.precio_venta}")
        
class consecionario(): # define una clase, pero principalmente para que almacene las funciones que realice el consecionario (almacenar datos, registrar y mostrarlos)
    def __init__(self):
        self.carros = []
    
    def registrar_carro(self,marca, modelo, año, color, tipo_combustible, precio_compra):
        self.carros.append(carro(marca, modelo, año, color, tipo_combustible, precio_compra))
    
    def mostrar(self):
        if not self.carros:
            print("No hay carros registrados \nIngrese algun carro, por favor")
        else:
            for i in self.carros:
                print(i.mostrar_datos())
                print("________________")
    
# Aqui una funcion que actue como menu
    def menu(self):
        while True:
            print("---------------------")
            print("Bienvenido")
            print("---------------------")
            print("1. Registrar un carro")
            print("2. Mostrar los carros")
            print("3. Salir")
            print("---------------------")
            op = input("Escoja una opcion: ") # op para que el usuario decida que hacer
            match op: # uso un match case, matcheo a op, para que dependiendo el caso se ejecute la debida sentencia
                case "1":
                    print("________________")
                    marca = input("Ingrese la marca del carro: ")
                    modelo = input("Ingrese el modelo del carro: ")
                    año = input("Ingrese el año del carro: ")
                    color = input("Ingrese el color del carro: ")
                    tipo_combustible = input("Ingrese el tipo de combustible del carro: ")
                    precio_compra = float(input("Ingrese el precio de compra del carro: "))
                    self.registrar_carro(marca, modelo, año, color, tipo_combustible, precio_compra)
                    print("Carro registrado con exito\n") # Recolecto los datos para mandar los parametros a la clase 
                case "2":
                    print("________________")
                    self.mostrar() # Ejecuto la funcion msotrar los carros de la clase consecionario que mostraria todo lo que se almaceno en la lista y dicha lista la recorro con un ciclo for
                case "3":
                    print("________________")
                    print("Gracias por utilizar el sistema\n")
                    break # cierra el programa
                case _:
                    print("Opcion invalida, por favor ingrese una opcion valida\n")
                    continue # continua el programa hasta que inserte una opcion valida
                
consecionario = consecionario() # almacenamos la clase en una variable
consecionario.menu() # y ahora llamamos a la funcion menu que la creamos dentro de la clase