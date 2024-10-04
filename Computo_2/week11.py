# Importar bibliotecas necesarias
import matplotlib.pyplot as plt  # para crear gráficos
import pandas as pd  # para manejar y analizar datos

# Crear un DataFrame con datos de nombres y edades
ds = pd.DataFrame({
    'Nombre':['William','Jimmy','Emerson',  # lista de nombres
            'Alfredo','Javier','Roberto',
            'Derick','Yoshua','Brian','Berta','Ximena','Briseily',
            'Camila'],
    'Edades':[18,27,20,18,19,21,20,19,20,19,19,20,20]  # lista de edades
})

# Contar la frecuencia de cada edad
frecc = ds['Edades'].value_counts()  # devuelve un objeto Series con frecuencias

# Crear un gráfico de barras con las frecuencias
plt.bar(frecc.index.astype(str), frecc.values)  # índices como etiquetas x, valores como alturas de barras

# Configurar el gráfico
plt.title("Edades del Grupo A3")  # título del gráfico
plt.ylabel("Frecuencia")  # etiqueta del eje y
plt.xlabel("Edades")  # etiqueta del eje x
plt.show()