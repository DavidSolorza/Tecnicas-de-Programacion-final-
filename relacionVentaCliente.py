import os
import csv

# Ruta base donde se encuentran los archivos CSV
RUTA_BASE = "ruta/a/tu/carpeta"  # Cambia esto por la ruta de tu carpeta

def cargar_csv(nombre_archivo):
    """Función para cargar un archivo CSV."""
    ruta_archivo = os.path.join(RUTA_BASE, nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la ruta '{RUTA_BASE}'")
        return []

def integrar_ventas_clientes():
    """
    Integra ventas con datos de clientes.
    """
    ventas = cargar_csv('ventas_mejorados.csv')
    clientes = cargar_csv('clientes_mejorados.csv')
    clientes_dict = {c['id_cliente']: c for c in clientes}

    for venta in ventas:
        cliente = clientes_dict.get(venta['id_cliente'])
        if cliente:
            venta.update(cliente)

    print("Relación Ventas-Clientes generada con éxito.")


def mostrar_ventas_clientes():
    """Muestra las ventas con la información del cliente."""
    ventas_clientes = integrar_ventas_clientes()
    if ventas_clientes:
        print("\nRelación Ventas-Clientes:")
        for venta in ventas_clientes:
            print(f"Venta ID: {venta['id_venta']}, Producto: {venta['id_producto']}, "
                f"Cantidad: {venta['cantidad']}, Cliente: {venta['nombre_cliente']} {venta['apellido_cliente']}, "
                f"Email: {venta['email_cliente']}")


    mostrar_ventas_clientes()