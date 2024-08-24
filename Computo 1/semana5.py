# Programacion Computacional III - Semana 5
# Introinspeccion y debug

while True:
    
    try:
        b = float(input("Ingrese la base (b): "))
        h = float(input("Ingrese la altura (h): "))
        def area(b, h):
            area = (b*h)/2
            print("El área es:", area)
        area(b, h)
    except ValueError:
        print("Error: Debe ingresar un número")
    except:
        print("Error")
    finally:
        op = input("Desea continuar S/N: ").lower()
        if (op=="s"):
            continue
        else:
            break