# Codigo para la siguiente expresion booleana: Y=((A*B'*C)' + (D´*E))', que pida los datos de A, B, C, D y E

# Funciones para las operaciones booleanas
def NOT(x):
    return 1 - x  # NOT es 1 menos el valor

def AND(x, y):
    return x * y  # AND es el producto

def OR(x, y):
    return max(x, y)  # OR es el máximo

# Solicitar datos al usuario
A = int(input("Ingrese el valor de A (0 o 1): "))
B = int(input("Ingrese el valor de B (0 o 1): "))
C = int(input("Ingrese el valor de C (0 o 1): "))
D = int(input("Ingrese el valor de D (0 o 1): "))
E = int(input("Ingrese el valor de E (0 o 1): "))

# Calcular B' y D'
B_not = NOT(B)
D_not = NOT(D)
# Calcular A * B' * C
term1 = AND(A, AND(B_not, C))
# Calcular D' * E
term2 = AND(D_not, E)
# Calcular (A * B' * C)' + (D' * E)
result = OR(NOT(term1), term2)
# Calcular Y
Y = NOT(result)
print("El resultado de Y es:", Y)