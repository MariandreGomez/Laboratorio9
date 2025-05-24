import tkinter as tk


saludos = {
    "Español": "Hola, mundo",
    "Inglés": "Hello, world",
    "Francés": "Bonjour, le monde",
    "Alemán": "Hallo, Welt",
    "Italiano": "Ciao, mondo",
    "Japonés": "こんにちは世界",
}


def saludar():
    texto = ""
    for idioma, saludo in saludos.items():
        texto += f"{idioma}: {saludo}\n"
    etiqueta.config(text=texto)

# GUI básica desde rama_gui
ventana = tk.Tk()
ventana.title("Saludos en varios idiomas")

boton = tk.Button(ventana, text="Mostrar saludos", command=saludar)
boton.pack(pady=10)

etiqueta = tk.Label(ventana, text="", justify="left")
etiqueta.pack(padx=10, pady=10)

ventana.mainloop()