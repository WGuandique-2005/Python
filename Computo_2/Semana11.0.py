# Importamos la biblioteca matplotlib.pyplot y la asignamos a la variable plt
import matplotlib.pyplot as plt

# Definimos una lista de strings que representan los departamentos
deparments = ['San Miguel', 'La Union', 'Morazan', 'Usulutan']

# Definimos una lista de números que representan la frecuencia de cada departamento
frecc = [11, 4, 0, 1]

# Definimos una lista de colores que se utilizarán para cada barra del gráfico
colors = ["blue", "red", "green", "purple"]

# Creamos un gráfico de barras utilizando la función plt.bar, pasando como parámetros:
# - deparments: la lista de departamentos que serán los labels del eje x
# - frecc: la lista de frecuencias que serán la altura de cada barra
# - color: la lista de colores que se utilizarán para cada barra
plt.bar(deparments, frecc, color=colors)

# Agregamos un título al gráfico utilizando la función plt.title
plt.title("Lugar de procedencia")

# Agregamos un label al eje x utilizando la función plt.xlabel
plt.xlabel("Departamento")

# Agregamos un label al eje y utilizando la función plt.ylabel
plt.ylabel("Frecuencia")

# Mostramos el gráfico utilizando la función plt.show
plt.show()