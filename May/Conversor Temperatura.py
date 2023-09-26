from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk

def celsius_a_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.set(f"{celsius} °C = {fahrenheit} °F")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico en grados Celsius.")

def fahrenheit_a_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        resultado.set(f"{fahrenheit} °F = {celsius} °C")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico en grados Fahrenheit.")

# Configuración de la ventana principal
root = Tk()
root.title("Conversor de Temperatura")
root.geometry("300x150")

# Mis variables para almacenar las entradas y los resultados
celsius_entry = StringVar()
fahrenheit_entry = StringVar()
resultado = StringVar()

# Etiquetas
Label(root, text="Celsius a Fahrenheit:", justify=CENTER).pack()
Label(root, text="Fahrenheit a Celsius:", justify=CENTER).pack()

# Entradas
celsius_input = ttk.Entry(root, textvariable=celsius_entry)
fahrenheit_input = ttk.Entry(root, textvariable=fahrenheit_entry)

celsius_input.pack()
fahrenheit_input.pack()

# Botones para realizar las conversiones
ttk.Button(root, text="Convertir a Fahrenheit", command=celsius_a_fahrenheit).pack()
ttk.Button(root, text="Convertir a Celsius", command=fahrenheit_a_celsius).pack()

# Muestra el resultado
Label(root, textvariable=resultado, justify=CENTER).pack()

root.mainloop()