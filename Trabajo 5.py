import os
import tkinter as tk
from tkinter import ttk, messagebox

ARCHIVO = "friendsContact.txt"
TEMPORAL = "temp.txt"


def crear_archivo():
    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w").close()


def agregar_contacto(nombre, numero):
    crear_archivo()

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split("!")

            if len(datos) == 2:
                if datos[0] == nombre or datos[1] == str(numero):
                    return False

    with open(ARCHIVO, "a") as archivo:
        archivo.write(f"{nombre}!{numero}\n")

    return True


def obtener_contactos():
    crear_archivo()
    contactos = []

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split("!")

            if len(datos) == 2:
                contactos.append((datos[0], datos[1]))

    return contactos


def actualizar_contacto(nombre, nuevo_numero):
    crear_archivo()

    encontrado = False

    with open(ARCHIVO, "r") as archivo, open(TEMPORAL, "w") as temporal:

        for linea in archivo:
            datos = linea.strip().split("!")

            if len(datos) == 2:

                if datos[0] == nombre:
                    temporal.write(f"{nombre}!{nuevo_numero}\n")
                    encontrado = True
                else:
                    temporal.write(linea)

    os.replace(TEMPORAL, ARCHIVO)

    return encontrado


def eliminar_contacto(nombre):
    crear_archivo()

    encontrado = False

    with open(ARCHIVO, "r") as archivo, open(TEMPORAL, "w") as temporal:

        for linea in archivo:
            datos = linea.strip().split("!")

            if len(datos) == 2:

                if datos[0] == nombre:
                    encontrado = True
                else:
                    temporal.write(linea)

    os.replace(TEMPORAL, ARCHIVO)

    return encontrado


class Agenda(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Agenda de Contactos")
        self.geometry("600x450")
        self.resizable(False, False)

        tk.Label(self, text="Nombre").place(x=30, y=20)

        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.place(x=110, y=20)

        tk.Label(self, text="Número").place(x=30, y=60)

        self.entry_numero = tk.Entry(self, width=30)
        self.entry_numero.place(x=110, y=60)

        ttk.Button(self, text="Agregar", command=self.agregar).place(x=420, y=18)

        ttk.Button(self, text="Actualizar", command=self.actualizar).place(x=420, y=58)

        ttk.Button(self, text="Eliminar", command=self.eliminar).place(x=420, y=98)

        ttk.Button(self, text="Mostrar contactos", command=self.mostrar).place(x=30, y=100)

        columnas = ("Nombre", "Número")

        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=12)

        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Número", text="Número")

        self.tabla.column("Nombre", width=250)
        self.tabla.column("Número", width=250)

        self.tabla.place(x=30, y=150)

        self.mostrar()

    def limpiar(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_numero.delete(0, tk.END)

    def mostrar(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        contactos = obtener_contactos()

        for contacto in contactos:
            self.tabla.insert("", tk.END, values=contacto)

    def agregar(self):

        nombre = self.entry_nombre.get().strip()
        numero = self.entry_numero.get().strip()

        if nombre == "" or numero == "":
            messagebox.showwarning("Aviso", "Complete todos los campos.")
            return

        if agregar_contacto(nombre, numero):
            messagebox.showinfo("Éxito", "Contacto agregado.")
            self.limpiar()
            self.mostrar()
        else:
            messagebox.showerror("Error", "El contacto ya existe.")

    def actualizar(self):

        nombre = self.entry_nombre.get().strip()
        numero = self.entry_numero.get().strip()

        if nombre == "" or numero == "":
            messagebox.showwarning("Aviso", "Complete todos los campos.")
            return

        if actualizar_contacto(nombre, numero):
            messagebox.showinfo("Éxito", "Contacto actualizado.")
            self.limpiar()
            self.mostrar()
        else:
            messagebox.showerror("Error", "El contacto no existe.")

    def eliminar(self):

        nombre = self.entry_nombre.get().strip()

        if nombre == "":
            messagebox.showwarning("Aviso", "Ingrese un nombre.")
            return

        if eliminar_contacto(nombre):
            messagebox.showinfo("Éxito", "Contacto eliminado.")
            self.limpiar()
            self.mostrar()
        else:
            messagebox.showerror("Error", "El contacto no existe.")


if __name__ == "__main__":
    app = Agenda()
    app.mainloop()
    