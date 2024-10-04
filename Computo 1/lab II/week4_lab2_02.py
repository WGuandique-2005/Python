"""
* Una papeleria vende cuadernos y lapices
! Los cuadernos pueden ser de 50 a 100 hojas
! Los lapices puedem ser de colores o de grafito
? El precio de venta es igual al precio de la compra multiplicado por 1.30 que corresponde al margen de ganancia
todo / la papeleria requiere construir un programa que le permita registrar y visualizar por lo menos dos articulos de item
* Todos los cuadernos son marca HOJITA y los lapices marca  RAYA
? ya que la papeleria es un distribuidor exclusivo
"""

class cuaderno(): # Creamos una clase cuaderno
    def __init__(self, num_hojas, precio_compra): # creamos el constructor, que almacena de manera automatica valores
        self.num_hojas = num_hojas # numero de hojas del cuaderno
        self.precio_compra = precio_compra # precio de compra
        self.marca = "HOJITA" # la marca que ya viene preestablecida
        self.precio_venta = self.precio_venta() 
        
    def precio_venta(self): #funcion para calcualar el precio de la venta a partir de precio de la compra
        return self.precio_compra*1.30 # margen de ganancia
    
    def mostrar_datos(self):  # funcion para mostrar los datos de los cuadernos
        return (
            f"Marca: {self.marca}\n"
            f"Numero de hojas: {self.num_hojas}\n"
            f"Precio de compra: {self.precio_compra}\n"
            f"Precio de venta: {self.precio_venta}\n"
        )
        
class lapiz(): # Clase lapiz
    def __init__(self, tipo, precio_compra): # creamos el constructor, que almacena de manera automatica valores
        self.tipo = tipo # tipo de lapiz grafito/color
        self.precio_compra = precio_compra # precio de compra
        self.marca = "RAYA" # marca preestablecida
        self.precio_venta = self.precio_venta()
    
    def precio_venta(self): # funcion que calcula el precio de venta, con un margen de ganancia ya preestablecido
        return self.precio_compra*1.30
    
    def mostrar_datos(self): # muestra los datos
        return (
            f"Marca: {self.marca}\n"
            f"Tipo: {self.tipo}\n"
            f"Precio de compra: {self.precio_compra}\n"
            f"Precio de venta: {self.precio_venta}\n"
        )
        
class papeleria(): # Aqui obte por crear una clase para todas las funciones de la libreria (menu, insertar datos y mostrarlos)
    def __init__(self): # creamos una lista para almacenar los datos
        self.articulos = []
    
    def registrar_cuaderno(self, num_hojas, precio_compra): # registra los cuadernos en la lista
        self.articulos.append(cuaderno(num_hojas, precio_compra))
        
    def registrar_lapiz(self, tipo, precio_compra): # registra los lapices en la lista
        self.articulos.append(lapiz(tipo, precio_compra))
        
    def mostrar_articulos(self): # muestra los datos almacenado en la lista previamente creada
        if not self.articulos:
            print("No hay articulos registrados \nPor favor ingrese articulos")
        else:
            for i in self.articulos: # con un for recorro toda la lista
                print(i.mostrar_datos()) # y llamo a la funcion mostrar datos que esta en la clases (cuaderno/lapiz)
                print("_______________")
                
    def menu(self): # Un menu para la intefaz de usuario
        while True:
            print("---------------------")
            print("Bienvenido \n")
            print("---------------------")
            print("1. Registrar cuaderno")
            print("2. Registrar lapiz")
            print("3. Mostrar articulos")
            print("4. Salir")
            print("_______________")
            op = input("Escoja una opcion: ") # op para que el usuario decida que hacer
            match op: # uso un match case, matcheo a op, para que dependiendo el caso se ejecute la debida sentencia
                case "1": 
                    print("_______________")
                    num_hojas = int(input("Ingrese el numero de hojas: "))
                    precio_compra = float(input("Ingrese el precio de compra: "))
                    self.registrar_cuaderno(num_hojas, precio_compra) # Recolecto los datos para mandar los parametros a la clase 
                case "2":
                    print("_______________")
                    tipo = input("Ingrese el tipo de lapiz: ")
                    precio_compra = float(input("Ingrese el precio de compra: "))
                    self.registrar_lapiz(tipo, precio_compra) # Recolecto los datos para mandar los parametros a la clase 
                case "3":
                    print("_______________")
                    self.mostrar_articulos() # Ejecuto la funcion msotrar articulos de la clase papeleria que mostraria todo lo que se almaceno en la lista y dicha lista la recorro con un ciclo for
                case "4":
                    print("_______________")
                    print("Programa cerrado") # cierre del programa
                    break
                case _:
                    print("_______________")
                    print("Opcion invalida, por favor intente de nuevo")
                    continue # si la opcion no es validad, que el programa no de error, sino que el menu vuelva a ejecutarse
papeleria = papeleria() # almacenamos la clase en una variable
papeleria.menu() # y ahora llamamos a la funcion menu que la creamos dentro de la clase