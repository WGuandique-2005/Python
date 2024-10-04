# Importamos las bibliotecas necesarias para trabajar con gráficos y análisis de datos
import matplotlib.pyplot as plt
import pandas as pd

#? Leemos un archivo CSV llamado "steam.csv" y lo guardamos en un DataFrame de pandas llamado "df"
df = pd.read_csv("steam.csv")

#? Contamos la frecuencia de cada valor único en la columna "Review_type" del DataFrame "df" y lo guardamos en una Serie de pandas llamada "frec"
frec = df["Review_type"].value_counts()

#? Esta línea estaba comentada, pero si la descomentamos, crearía un gráfico de línea con los índices de "frec" en el eje x y los valores de "frec" en el eje y
# plt.plot(frec.index, frec.values)

#? Esta línea estaba comentada, pero si la descomentamos, crearía un gráfico de barras con los índices de "frec" en el eje x y los valores de "frec" en el eje y
# plt.bar(frec.index, frec.values)

#? Creamos un gráfico de pie (tarta) con los valores de "frec" y los índices de "frec" como etiquetas
plt.pie(frec.values, labels=frec.index)
plt.show()