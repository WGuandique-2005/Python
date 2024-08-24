
#* Una veterinaria atiende solamente perros y registra en una base de datos.
#todo/ Se desea un programa que lea la informacion basica del perro y se muestre en pantalla. 
# En esta veterinariatodos los animales que llegan, entran con el estado 
#! inicial NO ATENDIDO y cuando se registra cambia automaticamente a ATENDIDO. 
# Por ahora como la veterinaria solo atiende perros, basado en el peso 
#? (menos de 10 kg 0 mas de 10 kg) lo registra como "Perro Grande" o "Perro Pequeño".

class perro():
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre # nombre del animal
        self.raza = raza # raza
        self.edad = edad # edad
        self.peso = peso # peso
        self.tipo= self.det_tipo() # llamamos a la funcion
        self.estado = self.estado() # llamamos a la funcion
        
    def det_tipo(self): # Funcion que basado en el peso (menos de 10 kg o mas de 10 kg) lo registra como "Perro Grande" o "Perro Pequeño".
        if self.peso < 10:
                return "Perro Pequeño"
        else:
                return "Perro Grande"
            
    def estado(self): # devuelve el estado atendido
        self.estado="ATENDIDO"
        return self.estado
    
    def mostrar_datos(self): # funcion para mostrar los datos
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")
        print("-----------------------")
        
class veterinaria(): # clase que nos permitira realizar todas las opciones (opciones, recoger datos, mostrar y cerrar el programa), en pocas palabras una interfaz para el usuario
    def __init__(self):
        self.perros = [] # creacion de una lista para almacenar
    
    def registrar_perros(self, nombre, raza, edad, peso): # funcion que registra los perros en la lista
        self.perros.append(perro(nombre, raza, edad, peso))
        
    def mostrar(self): # funcion que muestra los datos
        for i in self.perros: # recorre la lista con un for
            print("-----------------------")
            print(i.mostrar_datos()) # y llamo a la funcion de la clase perro
    
    def menu(self): # funcion que cumple el papel de menu
        while True:
            print("1. Registrar perro")
            print("2. Mostrar perros")
            print("3. Salir")
            print("-----------------------")
            opcion = input("Ingrese una opcion: ") # da opciones al usuario
            match opcion: # matchea el resultado y ejecuta una sentencia distinta segun el caso 
                case "1":
                    print("-----------------------")
                    nombre = input("Ingrese el nombre del perro: ")
                    raza = input("Ingrese la raza del perro: ")
                    edad = int(input("Ingrese la edad del perro: "))
                    peso = int(input("Ingrese el peso del perro: ")) # Obtenemos los datos de los perros
                    self.registrar_perros(nombre, raza, edad, peso) # y le mandamos los parametros necesarios
                case "2":
                    print("-----------------------")
                    self.mostrar() # aqui mostramos los datos ya ordenados
                case "3":
                    print("-----------------------")
                    print("Gracias por utilizar el sistema")
                    break # termina el programa
                case _:
                    print("-----------------------")
                    print("Opcion invalida")
                    continue # esto permite que aunque falle el programa, no surja error, sino que le permita al usuario poner una opcion validad
veterinaria = veterinaria() # almacenamos en una variable a la clase
veterinaria.menu() # llamamos al menu que es nuestar interfaz para comunicarnos con el usuario