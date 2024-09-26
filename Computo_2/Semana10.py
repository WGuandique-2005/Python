"""
* Programacion Computacional II - Semana 10
? Numpy y Pandas
"""

import pandas as pd


#! Hacer por columnnas
df = pd.read_csv("steam.csv")
subsel = df[["Name","Price","Review_type"]]
print(subsel.head(30))

#! Para ordenar por una columna
subsel = df[["Name","Price","Review_type"]].sort_values(by="Price",ascending=False)
print(subsel.head(30))


#! Para buscar en base a un valor 
subsel = df[["Name","Price","Review_type"]][(df["Price"]<=50.0)&(df["Price"]!=0.0)]
