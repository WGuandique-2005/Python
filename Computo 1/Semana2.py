# Semana 2 - Programacion III
# Variables y funciones

# Ejemplo 1
def mifuncion():
    print("Progrmacion III")
    
mifuncion()

# Ejemplo 2

a = float(input("Ingrese un numero:"))
def par(numero):
    if numero % 2 == 0:
        print("EL numero es par")
    else :
        print("El numero es impar")
par(a)

#Funciones: pow()

#pow(): Esta función integrada usa dos argumentos: la base y el exponente. Devuelve el resultado de elevar la base al exponente. También permite un tercer argumento opcional para la exponenciación modular. Ejemplo: pow(x, y) .

# Ejemplo pow()
num1 = float(input("Ingrese un numero:"))
num2 = float(input("Ingrese la potencia a la cual lo desea elevar:"))
def elevar(num,numE):
    elev =pow(num,numE)
    print(num, "elavado a ", numE, "=", elev)
    
elevar(num1,num2)

numa=float(input("Ingrese un numero:"))
numb  = float(input("Ingrese la potencia a la cual lo desea elevar:"))

elev= pow(numa,numb)
print(numa,"^", numb, "=", elev)

# Ejemplo 4

base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ingrese la medida de la altura: "))

def areatri(base, altura):
    area = base * altura / 2
    print("La area es de ",area)

areatri(base, altura)


# Ejercicio 1

# Area de circulo
print("____________________________________________________")

radio = float(input("Ingrese la medida del radio: "))
def areacirc(radio):
    import math
    pi = math.pi
    area = pi * (radio ** 2)
    print("La area del circulo es", area)
    
areacirc(radio)
print("____________________________________________________")

# Area de rombo

D = float(input("Ingrese la medida de la diagonal mayor: "))
d = float(input("Ingrese la medida de la diagonal menor: "))
def arearom(diagonalMa, diagonalMe):
    area = (diagonalMa*diagonalMe)/2
    print("La area del rombo es", area)
    
arearom(D,d)
print("____________________________________________________")

# Calcular la distancia recorrida

velocidad = float(input("Ingrese la velocidad en km/h: "))
time = float(input("Ingese el tiempo de viaje (en horas):"))

def distanciaRE(veloc, tiempo):
    recorrido= veloc*tiempo
    print("La distancia recorrida es de ", recorrido, "km")
    
distanciaRE(velocidad,time)
print("____________________________________________________")

#Ejercicios con lambda

suma = lambda a,b: a+b
resta = lambda a,b: a-b
div = lambda a,b: a/b
pro = lambda a,b: a*b

exp = lambda a,b: pow(a,b)

mod = lambda a,b: a % b



#Arhumentos con *

# Recibe n cantidad de argumentos, no hya limite de argumentos que puede recibir
def multi(*args):
    return args # lo devuelve como lista

def multi2(**args):
    return args # lo devuelve como diccionario
