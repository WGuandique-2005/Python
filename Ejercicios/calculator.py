# Ejercicio de practica
# Crearemos una calculadora con las operaciones basicas
# Suma, Resta, Multiplicacion, Division, Exponenciacion

def calculadora():
    while True:
        print("Calcualadora")
        print("_________________")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Exponenciacion")
        print("6. Raiz Cuadrada")
        print("_________________")
        op = input("Ingrese la opcion que desea realizar: ")
        if op == "1":
            print("____________")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("____________")
            print("La suma de los dos numeros es: ", a + b)
        elif op == "2":
            print("____________")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("____________")
            print("La resta de los dos numeros es: ", a - b)
        elif op == "3":
            print("____________")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("____________")
            print("La multiplicacion de los dos numeros es: ", a * b)
        elif op == "4":
            print("____________")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            if b != 0:
                print("____________")
                print("La division de los dos numeros es: ", a / b)
            else:
                print("____________")
                print("No se puede dividir por cero")
        elif op == "5":
            print("____________")
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("____________")
            print("La exponenciacion de los dos numeros es: ", a ** b)
        elif op =="6":
            import math
            print("____________")
            a = float(input("Ingrese un numero: "))
            print("____________")
            print("La raiz cuadrada de el numero es: ", math.sqrt(a) )
        else:
            print("____________")
            print("Operacion no valida")
            print("_________________")
            
        cont = input("Desea realizar otra operacion? (s/n): ")
        if cont.lower() == "n":
            print("____________")
            print("Programa cerrado")
            break
        else:
            continue

calculadora() 