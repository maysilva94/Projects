import tkinter as tk

# Función para manejar el inicio de sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    documento = entry_documento.get()
    # Verificar si el usuario y el documento son válidos (implementar la lógica de autenticación aquí)
    # Si son válidos, puedes mostrar la página principal, de lo contrario, mostrar un mensaje de error

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Salud")

# Crear etiquetas y campos de entrada para el inicio de sesión
label_usuario = tk.Label(ventana, text="Usuario o Email:")
label_documento = tk.Label(ventana, text="Número de Documento:")
entry_usuario = tk.Entry(ventana)
entry_documento = tk.Entry(ventana, show="*")  # Puedes usar "show" para ocultar la contraseña

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)

# Colocar elementos en la ventana
label_usuario.pack()
entry_usuario.pack()
label_documento.pack()
entry_documento.pack()
boton_iniciar_sesion.pack()

# Ejecutar la aplicación
ventana.mainloop()