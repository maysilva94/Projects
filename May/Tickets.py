import pickle
import sys
import os
import random

# Limpio la pantalla 
if os.name == 'posix':
    os.system('clear')  # Linux/macOS
else:
    os.system('cls')  # Windows

# Inicializo una lista para almacenar los tickets
tickets = []

def alta_ticket():
    nombre = input("Ingrese el nombre: ")
    sector = input("Ingrese el sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Ingrese el problema: ")

    # Genero un número de ticket aleatorio entre 1000 y 9999
    numero_ticket = random.randint(1000, 9999)

    # Creo el ticket como un diccionario
    ticket = {
        "Número de Ticket": numero_ticket,
        "Nombre": nombre,
        "Sector": sector,
        "Asunto": asunto,
        "Problema": problema
    }

    # Agrego el ticket a la lista de tickets
    tickets.append(ticket)

    # Muestro el ticket recién creado
    print("\nTicket creado:")
    for key, value in ticket.items():
        print(f"{key}: {value}")

    guardar_ticket(ticket)  # Guardar el ticket en un archivo

    # Pregunto si desea crear otro ticket
    crear_otro = input("\n¿Desea crear otro ticket? (s/n): ")
    if crear_otro.lower() == 's':
        alta_ticket()

def guardar_ticket(ticket):
    guardar = f"ticket_{ticket['Número de Ticket']}.pickle"  # Nombre del archivo basado en el número de ticket
    with open(guardar, "wb") as f:
        pickle.dump(ticket, f)

def leer_ticket():
    numero_ticket = int(input("Ingrese el número de ticket que desea leer: "))
    encontrado = False

    for ticket in tickets:
        if ticket["Número de Ticket"] == numero_ticket:
            print("\nTicket encontrado:")
            for key, value in ticket.items():
                print(f"{key}: {value}")
            encontrado = True
            break
    
    if not encontrado:
        print("\nTicket no encontrado.")

    # Pregunta si desea leer otro ticket
    leer_otro = input("\n¿Desea leer otro ticket? (s/n): ")
    if leer_otro.lower() == 's':
        leer_ticket()

def cargar_tickets():
    for archivo in os.listdir():
        if archivo.endswith(".pickle"):
            with open(archivo, "rb") as f:
                ticket = pickle.load(f)
                tickets.append(ticket)

# Verifica si ya existen archivos de tickets y cargarlos
cargar_tickets()

while True:
    print("\nMENU:")
    print("1. Alta ticket")
    print("2. Leer ticket")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        alta_ticket()
    elif opcion == '2':
        leer_ticket()
    elif opcion == '3':
        confirmacion = input("¿Seguro que desea salir? (s/n): ")
        if confirmacion.lower() == 's':
            break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Salir del programa
sys.exit()


