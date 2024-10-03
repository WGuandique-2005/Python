# Grafico de barras:

import matplotlib.pyplot as plt

deparments =['San Miguel', 'La Union','Morazan','Usulutan']
frecc = [11,4,0,1]
colors = ["blue","red","green","purple"]
plt.bar(deparments,frecc,color=colors)
plt.title("Lugar de procedencia")
plt.xlabel("Departamento")
plt.ylabel("Frecuencia")
plt.show()

# 