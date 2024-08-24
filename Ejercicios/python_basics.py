# Fundamentos de python

#! Variables
"""
* Variables numéricas (enteras y reales):
* Enteras (int): almacenan números enteros, como 1, 2, 3, etc.
* Reales (float): almacenan números decimales, como 3.14, -0.5, etc.
* Variables de texto (cadenas de caracteres):
todo / Cadenas de caracteres (string): almacenan secuencias de caracteres, como "hola", "adiós", etc.
* Variables lógicas (booleanas):
todo / Booleanas (bool): almacenan valores lógicos, como true (verdadero) o false (falso).
* Variables de fecha y hora:
todo / Fecha y hora (date y time): almacenan fechas y horas, como "2022-07-25 14:30:00".
! Declaración de variables
"""

# ? La declaración de variables es el proceso de asignar un nombre y un tipo a una variable. 
# * La sintaxis para declarar variables varía según el lenguaje de programación. 
# * A continuación, te muestro algunos ejemplos de declaración de variables en diferentes lenguajes:

x = 5  #! variable entera
y = 3.14  #! variable real
nombre = "Juan"  #! variable de texto
isAdmin = True  #! variable lógica

#* Asignación de valores
#? Una vez declarada una variable, se le puede asignar un valor utilizando el operador de asignación (=). Por ejemplo:
x = 5; #? asigna el valor 5 a la variable x

"________________________________________________________"

#* Funciones
"""
todo / En Python, una función es un bloque de código que se puede ejecutar varias veces desde diferentes partes del programa. Las funciones son útiles para:

todo / Reutilizar código: en lugar de escribir el mismo código varias veces, puedes escribir una función y llamarla cuando la necesites.
todo / Organizar el código: las funciones ayudan a estructurar el código en bloques lógicos y fáciles de entender.
todo / Reducir la complejidad: las funciones pueden simplificar el código al encapsular operaciones complejas en un solo bloque.

* Definición de una función

? En Python, se define una función utilizando la palabra clave def seguida del nombre de la función 
? y un par de paréntesis que contienen los parámetros de la función. La sintaxis básica es:
"""

def nombre_de_la_función(parámetros):
    return

def saludar(nombre):
    print("Hola, " + nombre + "!")
saludar("Juan")  # imprime "Hola, Juan!"

#todo / Funciones sin parámetros: no reciben ningún valor como entrada.
def saludar():
    print("Hola!")
saludar()

#todo / Funciones con parámetros opcionales: pueden recibir o no recibir valores como entrada.
def saludar(nombre="mundo"):
    print("Hola, " + nombre + "!")
saludar()

#todo / Funciones con parámetros variables: pueden recibir un número variable de valores como entrada.
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
        return resultado
salida = suma( 5,5)
print(salida)

#todo / Funciones lambda: son funciones anónimas que se definen en una sola línea de código.
suma = lambda x, y: x + y

def saludar(nombre):  # parámetro
    print("Hola, " + nombre + "!")

saludar("Juan")  # argumento


"________________________________________"
#* Estructuras de control
"""
!1. Condicionales (if-else)

todo / Los condicionales permiten ejecutar diferentes bloques de código dependiendo de una condición.

* if: ejecuta un bloque de código si la condición es verdadera.
* else: ejecuta un bloque de código si la condición es falsa.
* elif: ejecuta un bloque de código si la condición es verdadera y la condición anterior es falsa.
? Ejemplo:
"""
x = 5
if x > 10:
    print("x es mayor que 10")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 10")

"""
!2. Bucles (for y while)
todo / Los bucles permiten ejecutar un bloque de código repetidamente.

* for: ejecuta un bloque de código para cada elemento de una secuencia (lista, tupla, cadena, etc.).
* while: ejecuta un bloque de código mientras una condición sea verdadera.
? Ejemplos:
"""
#todo / Bucle for
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

#todo / Bucle while
x = 0
while x < 5:
    print(x)
    x += 1
    
"""
!3. Bucle for con enumerate
todo / El bucle for con enumerate permite ejecutar un bloque de código para cada elemento de una secuencia y obtener su índice.
? Ejemplo:
"""

frutas = ["manzana", "banana", "naranja"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

"""
!4. Bucle for con zip
todo / El bucle for con zip permite ejecutar un bloque de código para cada elemento de dos o más secuencias.
? Ejemplo:
"""
nombres = ["Juan", "María", "Pedro"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad}")

"""
!5. Break y continue
* break: sale del bucle actual.
* continue: salta al siguiente elemento del bucle.
"""
#todo / Break
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1

#todo / Continue
x = 0
while x < 5:
    if x == 3:
        continue
    print(x)
    x += 1

"""
!6. Try-except

todo / El bloque try-except permite manejar errores y excepciones en el código.

* try: ejecuta un bloque de código que puede generar un error.
* except: ejecuta un bloque de código si se produce un error en el bloque try.
? Ejemplo:
"""
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: división por cero")

"""
! El bucle while True funciona de la siguiente manera:
todo / El intérprete de Python evalúa la condición True, que siempre es verdadera.
todo / Como la condición es verdadera, el intérprete ejecuta el código dentro del bucle.
todo / El bucle se repite indefinidamente hasta que se encuentra una instrucción break o se produce una excepción.

* El bucle while True se utiliza comúnmente en situaciones donde se necesita ejecutar un código repetidamente hasta que se cumpla una condición específica. Por ejemplo:
* Leer datos de un archivo o una base de datos hasta que se llegue al final.
* Esperar a que el usuario ingrese una respuesta válida.
* Realizar una tarea repetitiva hasta que se complete.
"""

while True:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == "n":
        break
    print("Continuando...")
    
    
"______________________________________"
#* Tuplas, listas, diccionarios y conjuntos
"""
! Tuplas

todo / Las tuplas son estructuras de datos inmutables que almacenan una secuencia de valores. 
* Una vez creada una tupla, no se puede modificar.
? Utilidad, las tuplas son útiles cuando necesitas almacenar una secuencia de valores que no cambiarán. Por ejemplo:
Almacenar constantes
Representar coordenadas en un espacio
Almacenar información de configuración
"""
my_tupla=("william","josue","gaundique","rivera")

"""
! Listas

todo / Las listas son estructuras de datos mutables que almacenan una secuencia de valores. A diferencia de las tuplas, las listas se pueden modificar después de su creación.
? Utilidad, las listas son útiles cuando necesitas almacenar una secuencia de valores que pueden cambiar. Por ejemplo:
Almacenar datos de una base de datos
Representar una cola de tareas
Almacenar información de usuario
"""
my_lista=["william","josue","gaundique","rivera"]

"""
! Diccionarios

todo / Los diccionarios son estructuras de datos que almacenan pares clave-valor. Cada clave es única y se asocia con un valor.
?Utilidad, los diccionarios son útiles cuando necesitas almacenar información con claves únicas. Por ejemplo:
Almacenar información de usuario
Representar una base de datos
Almacenar configuración de una aplicación
"""
my_diccionario={"nombre":"william",
                "apellido":"guandique",
                "edad":18,
                "estatura":1.70,
                "ciudad":"san salvador",
                "pais":"el salvador"
                }

"""
! Conjuntos

todo / Los conjuntos son estructuras de datos que almacenan una colección de valores únicos. No se permiten valores duplicados.
? Utilidad, los conjuntos son útiles cuando necesitas almacenar una colección de valores únicos. Por ejemplo:

Almacenar información de categorías
Representar una lista de opciones
Almacenar información de tags
En resumen, cada estructura de datos tiene su propia utilidad y se debe elegir la que mejor se adapte a las necesidades del problema que se está resolviendo.
"""
conjunto = {1, 2, 3, 4, 5}
print(conjunto)  # {1, 2, 3, 4, 5}
conjunto.add(6)
print(conjunto)  # {1, 2, 3, 4, 5, 6}