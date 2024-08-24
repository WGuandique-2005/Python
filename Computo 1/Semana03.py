# Semana 3 - Programacion III
# Tuplas, listas, diccionarios y conjuntos

# Listas       -4       -3      -2          -1
my_list= ["william","josue","guandique","rivera"]
        #   0           1       2           3
# my_list.index() # Retorna el indice que tiene ese valor
# my_list.append() # Agregar valores, estos se agregan al final de la lista
# my_list.insert() # Agregar valores en una posicion especifica de la lista
# my_list.remove() # Eliminar un valor de la lista
# my_list.pop() # Eliminar un valor de la lista, este valor se devuelve  
# my_list.sort() # Ordenar la lista de menor a mayor
# my_list.reverse() # Invertir la lista
# my_list.clear() # Eliminar todos los valores de la lista



# Tuplas
my_tuple = ("william","josue","guandique","rivera")
# Tuplas son inmutables, no se pueden modificar, son mas rapidas y seguras que las listas


# Diccionarios
my_dict = {"nombre": "william", 
           "apellido":"guandique",
           "edad": 18, 
           "ciudad":"san miguel",
           "estatura": 1.70,
           "peso": 73.0}
# Diccionarios son como listas pero con claves y valores, son mutables

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get())
my_dict.setdefault("universidad","ugb")
my_dict["universidad"]="universidad gerrado barrios"


# Conjuntos
my_set = {1, 2, 3, 4, 5, 6,7,8,9}
# Conjuntos son inmutables, no se pueden modificar, son mas rapidas y seguras
# que las listas, no se pueden repetir valores en un conjunto, no se pueden ordenar
# no se pueden acceder a los valores de un conjunto, no se pueden eliminar valores
# de un conjunto, no se pueden agregar valores a un conjunto, no se pueden buscar valores
# en un conjunto, no se pueden contar los valores de un conjunto, no se pueden
# obtener el indice de un valor en un conjunto, no se pueden obtener el valor de un indice en un conjunto



