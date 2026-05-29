import tkinter as tk
from tkinter import messagebox
import math

class Figura:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(Figura):
    def __init__(self, radio, altura):
        super().__init__()

        self.radio = radio
        self.altura = altura

        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_superficie(self):
        area_ladoA = 2 * math.pi * self.radio * self.altura
        area_ladoB = 2 * math.pi * self.radio ** 2

        return area_ladoA + area_ladoB

class Esfera(Figura):
    def __init__(self, radio):
        super().__init__()

        self.radio = radio

        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2

class Piramide(Figura):
    def __init__(self, base, altura, apotema):
        super().__init__()

        self.base = base
        self.altura = altura
        self.apotema = apotema

        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lado = 2 * self.base * self.apotema

        return area_base + area_lado

class VentanaCilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Cilindro")
        self.resizable(False, False)
        self.geometry("300x250")

        self.etq_radio = tk.Label(self, text="Radio:")
        self.etq_radio.place(x=20, y=20)

        self.cmp_radio = tk.Entry(self)
        self.cmp_radio.place(x=120, y=20)

        self.etq_altura = tk.Label(self, text="Altura:")
        self.etq_altura.place(x=20, y=60)

        self.cmp_altura = tk.Entry(self)
        self.cmp_altura.place(x=120, y=60)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=120, y=100)

        self.etq_volumen = tk.Label(self, text="Volumen = ")
        self.etq_volumen.place(x=20, y=150)

        self.etq_superficie = tk.Label(self, text="Superficie = ")
        self.etq_superficie.place(x=20, y=180)

    def calcular(self):
        try:
            radio = float(self.cmp_radio.get())
            altura = float(self.cmp_altura.get())

            cilindro = Cilindro(radio, altura)

            volumen = cilindro.get_volumen()
            superficie = cilindro.get_superficie()

            self.etq_volumen.config(text=f"Volumen = {volumen:.2f}")
            self.etq_superficie.config(text=f"Superficie = {superficie:.2f}")

        except:
            messagebox.showerror("Error", "Datos inválidos")

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Esfera")
        self.resizable(False, False)
        self.geometry("300x250")

        self.etq_radio = tk.Label(self, text="Radio:")
        self.etq_radio.place(x=20, y=20)

        self.cmp_radio = tk.Entry(self)
        self.cmp_radio.place(x=120, y=20)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=120, y=60)

        self.etq_volumen = tk.Label(self, text="Volumen = ")
        self.etq_volumen.place(x=20, y=150)

        self.etq_superficie = tk.Label(self, text="Superficie = ")
        self.etq_superficie.place(x=20, y=180)

    def calcular(self):
        try:
            radio = float(self.cmp_radio.get())

            esfera = Esfera(radio)

            volumen = esfera.get_volumen()
            superficie = esfera.get_superficie()

            self.etq_volumen.config(text=f"Volumen = {volumen:.2f}")
            self.etq_superficie.config(text=f"Superficie = {superficie:.2f}")

        except:
            messagebox.showerror("Error", "Datos inválidos")

class VentanaPiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Piramide")
        self.resizable(False, False)
        self.geometry("300x300")

        self.etq_base = tk.Label(self, text="Base:")
        self.etq_base.place(x=20, y=20)

        self.cmp_base = tk.Entry(self)
        self.cmp_base.place(x=120, y=20)

        self.etq_altura = tk.Label(self, text="Altura:")
        self.etq_altura.place(x=20, y=60)

        self.cmp_altura = tk.Entry(self)
        self.cmp_altura.place(x=120, y=60)

        self.etq_apotema = tk.Label(self, text="Apotema:")
        self.etq_apotema.place(x=20, y=100)

        self.cmp_apotema = tk.Entry(self)
        self.cmp_apotema.place(x=120, y=100)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=120, y=140)

        self.etq_volumen = tk.Label(self, text="Volumen = ")
        self.etq_volumen.place(x=20, y=200)

        self.etq_superficie = tk.Label(self, text="Superficie = ")
        self.etq_superficie.place(x=20, y=230)

    def calcular(self):
        try:
            base = float(self.cmp_base.get())
            altura = float(self.cmp_altura.get())
            apotema = float(self.cmp_apotema.get())

            piramide = Piramide(base, altura, apotema)

            volumen = piramide.get_volumen()
            superficie = piramide.get_superficie()

            self.etq_volumen.config(text=f"Volumen = {volumen:.2f}")
            self.etq_superficie.config(text=f"Superficie = {superficie:.2f}")

        except:
            messagebox.showerror("Error", "Datos inválidos")

class VentanMain(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Figuras")
        self.resizable(False, False)
        self.geometry("350x180")

        self.btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.btn_cilindro.place(x=20, y=60)

        self.btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.btn_esfera.place(x=130, y=60)

        self.btn_piramide = tk.Button(self, text="Piramide", command=self.abrir_piramide)
        self.btn_piramide.place(x=240, y=60)

    def abrir_cilindro(self):
        VentanaCilindro()

    def abrir_esfera(self):
        VentanaEsfera()

    def abrir_piramide(self):
        VentanaPiramide()

if __name__ == "__main__":
    app = VentanMain()
    app.mainloop()