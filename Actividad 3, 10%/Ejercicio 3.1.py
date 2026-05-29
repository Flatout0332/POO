import tkinter as tk
import math
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5
        
    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)
    
    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0
        for i in self.lista_notas:
            suma += (i - prom) ** 2
        return math.sqrt(suma / len(self.lista_notas))
    
    def calcular_menor(self):
        return min(self.lista_notas)
    
    def calcular_mayor(self):
        return max(self.lista_notas)
    
    class VentanaMain(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Notas")
            self.resizable(False, False)
            self.geometry("280x380")
            self.notas = Notas()
            self._crear_componentes()
        
        def _crear_componentes(self):
        
            self.campos= []
            for i in range(5):
                etq = tk.Label(self, text=f"Nota {i+1}:")
                etq.place(x=20, y=20 + 30*i, width=80, height=23)
                cmp = tk.Entry(self)
                cmp.place(x=105, y=20 + 30*i, width=135, height=23)
                self.campos.append(cmp)
                
            bot_calcular = tk.Button(self, text="Calcular", command=self.calcular)
            bot_calcular.place(x=20, y=170, width=100, height=23)
            bot_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
            bot_limpiar.place(x=125, y=170, width=80, height=23)
            
            self.etq_promedio = tk.Label(self, text="Promedio = ")
            self.etq_promedio.place(x=20, y=210)
            self.etq_desviacion = tk.Label(self, text="Desviación estándar = ")
            self.etq_desviacion.place(x=20, y=240)
            self.etq_mayor = tk.Label(self, text="Nota mayor = ")
            self.etq_mayor.place(x=20, y=270)
            self.etq_menor = tk.Label(self, text="Nota menor = ")
            self.etq_menor.place(x=20, y=300)
            
        def calcular(self):
            for i, cmp in enumerate(self.campos):
                texto = cmp.get().strip()
                self.notas.lista_notas[i] = float(texto) if texto else 0.0


            prom = self.notas.calcular_promedio()
            desv = self.notas.calcular_desviacion()
            mayor = self.notas.calcular_mayor()
            menor = self.notas.calcular_menor()
            
            self.etq_promedio.config(text=f"Promedio = {prom:.2f}")
            self.etq_desviacion.config(text=f"Desviación estándar = {desv:.2f}")
            self.etq_mayor.config(text=f"Nota mayor = {mayor:.2f}")
            self.etq_menor.config(text=f"Nota menor = {menor:.2f}")
            
        def limpiar(self):
            for cmp in self.campos:
                cmp.delete(0, tk.END)
            self.etq_promedio.config(text="Promedio = ")
            self.etq_desviacion.config(text="Desviación estándar = ")
            self.etq_mayor.config(text="Nota mayor = ")
            self.etq_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    ventana = Notas.VentanaMain()
    ventana.mainloop()