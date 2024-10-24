# Funciones para las operaciones booleanas
#todo\ (A*B)' + (C ⊕ D)
def NOT(x):
    return 1 - x  # NOT es 1 menos el valor

def AND(x, y):
    return x * y  # AND es el producto

def OR(x, y):
    return max(x, y)  # OR es el máximo

def XOR(x, y):
    if x != y:
        return 1
    else:
        return 0

# Imprimir la tabla de verdad
print("A | B | C | D | E | Y")
print("-----------------------")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for D in [0, 1]:
                    
                    # (A * B)'
                    term_1 = NOT(AND(A,B))
                    
                    # (C ⊕ D)
                    term_2 = XOR(C,D)
                    result = OR(term_1,term_2)
                    # Calcular Y
                    Y = result
                    
                    # Imprimir los resultados
                    print(f"{A} | {B} | {C} | {D} | {Y}")