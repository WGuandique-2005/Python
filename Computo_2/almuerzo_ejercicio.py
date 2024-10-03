import matplotlib.pyplot as plt

x=['Res','Pollo','Lengua','Birria']
y=[6,3,2,6]
plt.pie(y,labels=x)
plt.title("Tacos")
plt.xlabel('Prefrencias')
plt.ylabel('Frecuencia')
plt.show()