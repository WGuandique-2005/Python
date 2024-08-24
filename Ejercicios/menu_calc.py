# Menu

op = -1
while op != 7:
    print("Calculadora")
    print("_________________")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponenciacion")
    print("6. Raiz Cuadrada")
    print("7. Salir")
    print("_________________")
    opcion = input("Ingrese la opcion que desea realizar: ")

    match int(opcion):
        case 1:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("La suma de los dos numeros es: ", a + b)
        case 2:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("La resta de los dos numeros es: ", a - b)
        case 3:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("La multiplicacion de los dos numeros es: ", a * b)
        case 4:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            if b != 0 and a != 0:
                print("La division de los dos numeros es: ", a / b)
            else:
                print("No se puede dividir entre cero")
        case 5:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("La exponenciacion de los dos numeros es: ", a ** b)
        case 6:
            import math
            a = float(input("Ingrese el numero: "))
            if a < 0:
                print("No se puede calcular la raiz cuadrada de un numero negativo")
            else:
                print("La raiz cuadrada de el numero es: ", math.sqrt(a))
        case 7:
            print("Programa cerrado")
            op = 7
