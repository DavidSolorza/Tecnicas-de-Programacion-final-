import os
import csv

# Ruta base donde se encuentran los archivos csv
RUTA_BASE = "./archivos"

def cargar_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve su contenido como una lista de diccionarios.
    """
    ruta_archivo = os.path.join(RUTA_BASE, nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la ruta '{RUTA_BASE}'.")
        return []

def simular_compra():
    """
    Permite a un cliente simular una compra dentro de su presupuesto.
    """
    productos = cargar_csv('productos.csv')
    if not productos:
        print("Error: No se pudieron cargar los productos.")
        return

    try:
        presupuesto = float(input("\nPresupuesto disponible: $"))
    except ValueError:
        print("Error: Presupuesto inválido.")
        return

    carrito = []
    while presupuesto > 0:
        for idx, p in enumerate(productos, 1):
            print(f"{idx}. {p['nombre']} - ${p['precio']}")

        try:
            eleccion = int(input("\nSelecciona un producto (0 para salir): "))
            if eleccion == 0:
                break
            cantidad = int(input("¿Cantidad?: "))
            producto = productos[eleccion - 1]
            costo = cantidad * float(producto['precio'])

            if costo <= presupuesto:
                carrito.append(producto['nombre'])
                presupuesto -= costo
            else:
                print("No tienes suficiente presupuesto.")
        except (ValueError, IndexError):
            print("Selección inválida.")

    print("\nCompra completada:")
    print(", ".join(carrito))

