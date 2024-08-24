# Crear una calculadora con _tkinter
# Que realice las operaciones basicas, tales como:
# suma, resta, multiplicacion, division, potencia.
# Crear una calculadora con _tkinter
# Que realice las operaciones basicas, tales como:
# suma, resta, multiplicacion, division, potencia.
import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        # Creamos los campos de texto para la entrada de números
        self.numero1 = tk.Entry(self.ventana)
        self.numero1.grid(row=0, column=0)

        self.numero2 = tk.Entry(self.ventana)
        self.numero2.grid(row=0, column=2)

        # Creamos los botones para las operaciones
        self.suma = tk.Button(self.ventana, text="+", command=self.sumar)
        self.suma.grid(row=1, column=0)

        self.resta = tk.Button(self.ventana, text="-", command=self.restar)
        self.resta.grid(row=1, column=1)

        self.multiplicacion = tk.Button(self.ventana, text="*", command=self.multiplicar)
        self.multiplicacion.grid(row=1, column=2)

        self.division = tk.Button(self.ventana, text="/", command=self.dividir)
        self.division.grid(row=2, column=0)

        self.potencia = tk.Button(self.ventana, text="^", command=self.potenciar)
        self.potencia.grid(row=2, column=1)

        # Creamos un campo de texto para mostrar el resultado
        self.resultado = tk.Label(self.ventana, text="")
        self.resultado.grid(row=3, column=0, columnspan=3)

    def sumar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 + num2
            self.resultado.config(text=f"{num1} + {num2} = {resultado}")
        except ValueError:
            self.resultado.config(text="Error: ingrese números válidos")

    def restar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 - num2
            self.resultado.config(text=f"{num1} - {num2} = {resultado}")
        except ValueError:
            self.resultado.config(text="Error: ingrese números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 * num2
            self.resultado.config(text=f"{num1} * {num2} = {resultado}")
        except ValueError:
            self.resultado.config(text="Error: ingrese números válidos")

    def dividir(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            if num2 != 0:
                resultado = num1 / num2
                self.resultado.config(text=f"{num1} / {num2} = {resultado}")
            else:
                self.resultado.config(text="Error: no se puede dividir por cero")
        except ValueError:
            self.resultado.config(text="Error: ingrese números válidos")

    def potenciar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 ** num2
            self.resultado.config(text=f"{num1} ^ {num2} = {resultado}")
        except ValueError:
            self.resultado.config(text="Error: ingrese números válidos")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()