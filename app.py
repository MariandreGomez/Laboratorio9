import tkinter as tk

def saludar():
    etiqueta.config(text="Hola, mundo")

ventana = tk.Tk()
ventana.title("Mi primer GUI")

boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()