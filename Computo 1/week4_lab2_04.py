"""
* Un almacen vende dispositivos electronicos (celulares, tablets y portatiles)
! Todos PHR es una nueva marca que va ingresando en el mercado
todo\ Se requiere almacenar sus 6 principales caracteristicas
? Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 (margen de ganancia)
"""
# defini 3 clases que almacenan sus principales caracteristicas
class celular():
    def __init__(self, pantalla, ram, almacenamiento, precio_compra):
        self.pantalla = pantalla
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = self.precio_venta()
        self.marca = "PHR"
    
    def precio_venta(self): # en las 3 clases cree una funcion para obtener el precio de venta
        return self.precio_compra * 1.7
    
    def mostrar_datos(self): # muestro los datos de manera ordenada (la misma funcion para las 3 clases)
        print(f"Celular Marca: {self.marca}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        
class tablet():
    def __init__(self, pantalla, ram, almacenamiento, precio_compra):
        self.pantalla = pantalla
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = self.precio_venta()
        self.marca = "PHR"
        
    def precio_venta(self):
        return self.precio_compra * 1.7
    
    def mostrar_datos(self):
        print(f"Tablet Marca: {self.marca}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        
class portatiles():
    def __init__(self, pantalla, ram, almacenamiento, precio_compra):
        self.pantalla = pantalla
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = self.precio_venta()
        self.marca = "PHR"
        
    def precio_venta(self):
        return self.precio_compra * 1.7
    
    def mostrar_datos(self):
        print(f"Portatil Marca: {self.marca}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        
class almacen(): # Aqui obte por crear una clase para todas las funciones del almacem (menu, insertar datos y mostrarlos)
    def __init__(self):
        self.productos = [] # lista para guardar los productos
        
    # las siguientes 3 funciones ingresan los datos en la lista 
    def ingresar_celular(self,pantalla,ram,almacenamiento,precio_compra):
        self.productos.append(celular(pantalla,ram,almacenamiento,precio_compra))
        
    def ingresar_tablet(self,pantalla,ram,almacenamiento,precio_compra):
        self.productos.append(tablet(pantalla,ram,almacenamiento,precio_compra))
    
    def ingresar_portatil(self, pantalla, ram, almcenamiento, precio_compra):
        self.productos.append(portatiles(pantalla, ram, almcenamiento, precio_compra))
        
    def mostrar(self): # muestro los datos
        if not self.productos:
            print("No hay productos \nPor favor ingrese algun producto")
        else:
            for i in self.productos: # recorro mi lista con una ciclo for
                print(i.mostrar_datos())
                print("----------------")
            
    # El menu que da una interfaz para que el usuario interactue   
    def menu(self):
        while True:
            print("---------------------")
            print("Bienvenido")
            print("---------------------")
            print("1. Ingresar Celular")
            print("2. Ingresar Tablet")
            print("3. Ingresar Portatil")
            print("4. Mostrar Productos")
            print("5. Salir")
            print("----------------")
            opcion = input("Ingrese una opcion: ") # op sirve para que el usuario decidad
            match opcion: # un match case para las opciones del menu
                case "1":
                    print("----------------")
                    pantalla = float(input("Ingrese la pantalla del celular: "))
                    ram = int(input("Ingrese la RAM del celular: "))
                    almacenamiento = int(input("Ingrese el almacenamiento del celular: "))
                    precio_compra = int(input("Ingrese el precio de compra del celular: "))
                    self.ingresar_celular(pantalla,ram,almacenamiento,precio_compra)
                case "2":
                    print("----------------")
                    pantalla = float(input("Ingrese la pantalla del tablet: "))
                    ram = int(input("Ingrese la RAM del tablet: "))
                    almacenamiento = int(input("Ingrese el almacenamiento del tablet: "))
                    precio_compra = int(input("Ingrese el precio de compra del tablet: "))
                    self.ingresar_tablet(pantalla,ram,almacenamiento,precio_compra)
                case "3":
                    print("----------------")
                    pantalla = float(input("Ingrese la pantalla del portatil: "))
                    ram = int(input("Ingrese la RAM del portatil: "))
                    almacenamiento = int(input("Ingrese el almacenamiento del portatil: "))
                    precio_compra = int(input("Ingrese el precio de compra del portatil: "))
                    self.ingresar_portatil(pantalla, ram, almacenamiento, precio_compra)
                case "4":
                    print("----------------")
                    self.mostrar() # llamo la funcion para mostrar los datos
                case "5":
                    print("----------------")
                    print("Gracias por utilizar el sistema\n")
                    break # acaba el programa
                case _:
                    print("----------------")
                    print("Opcion invalida, por favor ingrese una opcion valida")
                    continue # continua hasta obtener una opcion valida
                
almacen= almacen() # almaceno la clase en una variable
almacen.menu() # llamo a funcion de la clase que me ejecuta el menu