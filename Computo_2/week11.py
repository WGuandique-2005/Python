import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ds = pd.DataFrame({
    'Nombre':['William','Jimmy','Emerson'
            ,'Alfredo','Javier','Roberto'
            ,'Derick','Yoshua','Brian','Berta','Ximena','Briseily'
            ,'Camila'],
    'Edades':[18,27,20,18,19,21,20,19,20,19,19,20,20]
})
frecc = ds['Edades'].value_counts()
plt.bar(frecc.index.astype(str), frecc.values)
plt.title("Edades del Grupo A3")
plt.ylabel("Frecuencia")
plt.xlabel("Edades")
plt.show()
