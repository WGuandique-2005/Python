# Semana 3 - Programacion III
# Colecciones y estructuras de repetición

# IF: tiene clausulas (elif,else)
"""
name=input("Escribe tu nombre:")
if name=="Alice":
    print("Hola Alice")
else:
    print("No eres Alice")
"""
"""
num1=int(input("Escribe un numero:"))
num2=int(input("Escribe un numero:"))
num3=int(input("Escribe un numero:"))
if (num1>num2 and num1>num3):
    print(f"El numero mayor es {num1}")
    if (num2>num3):
        print(f"El numero medio es {num2}")
        print(f"El numero menor es {num3}")
    else:
        print(f"El numero medio es {num3}")
        print(f"El numero menor es {num2}")
        
elif (num2>num1 and num2>num3):
    print(f"El numero mayor es {num2}")
    if (num1>num3):
        print(f"El numero medio es {num1}")
        print(f"El numero menor es {num3}")
    else:
        print(f"El numero medio es {num3}")
        print(f"El numero menor es {num1}")
else:
    print(f"El numero mayor es {num3}")

    if (num1>num2):
        print(f"El numero medio es {num1}")
        print(f"El numero menor es {num2}")
    else:
        print(f"El numero medio es {num2}")
        print(f"El numero menor es {num1}")
    
"""

# WHILE
spam=0
while spam<5:
    print("Este mensaje se imprime 5 veces")
    spam+=1

while True:
    num1=int(input("Escribe un numero:"))
    num2=int(input("Escribe un numero:"))
    num3=int(input("Escribe un numero:"))
    if (num1>num2 and num1>num3):
        print(f"El numero mayor es {num1}")
        if (num2>num3):
            print(f"El numero medio es {num2}")
            print(f"El numero menor es {num3}")
        else:
            print(f"El numero medio es {num3}")
            print(f"El numero menor es {num2}")
            
    elif (num2>num1 and num2>num3):
        print(f"El numero mayor es {num2}")
        if (num1>num3):
            print(f"El numero medio es {num1}")
            print(f"El numero menor es {num3}")
        else:
            print(f"El numero medio es {num3}")
            print(f"El numero menor es {num1}")
    else:
        print(f"El numero mayor es {num3}")

        if (num1>num2):
            print(f"El numero medio es {num1}")
            print(f"El numero menor es {num2}")
        else:
            print(f"El numero medio es {num2}")
            print(f"El numero menor es {num1}")
            
    op=input("N o S?")
    if op=="N":
        break
    else:
        op=input("¿Desea continuar? (S/N):")
        continue
        
        
    