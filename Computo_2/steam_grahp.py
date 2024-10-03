import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("steam.csv")
frec = df["Review_type"].value_counts()
#plt.plot(frec.index,frec.values)
#plt.bar(frec.index, frec.values)
plt.pie(frec.values, labels=frec.index)
plt.show()