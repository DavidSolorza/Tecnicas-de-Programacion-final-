import os
import csv
from datetime import datetime

# Defino la ruta base donde se encuentran los archivos CSV
RUTA_BASE = "./archivos"


def cargar_csv(archivo):
    """
    Cargo un archivo CSV y devuelvo su contenido como una lista de diccionarios.
    """
    ruta_archivo = os.path.join(RUTA_BASE, archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            # Leo todas las filas del archivo y las devuelvo como lista de diccionarios
            return [fila for fila in lector]
    except FileNotFoundError:
        # Si el archivo no se encuentra, informo del error y devuelvo una lista vacía
        print(f"Error: No se encontró el archivo '{archivo}' en la ruta '{RUTA_BASE}'.")
        return []


def filtrar_ventas_por_producto(ventas, id_producto):
    """
    Filtro las ventas de un producto específico y las convierto en un formato procesable.
    """
    try:
        # Proceso cada venta, convirtiendo la fecha y la cantidad a los formatos esperados.
        return [
            {
                "fecha": datetime.strptime(venta["fecha"], "%Y-%m-%d"),
                "cantidad": int(venta["cantidad"])
            }
            for venta in ventas if venta["id_producto"] == id_producto
        ]
    except Exception as e:
        # Si ocurre un error al procesar las ventas, lo informo.
        print(f"Error al procesar las ventas: {e}")
        return []


def calcular_tasa_cambio(ventas):
    """
    Calculo la tasa de cambio promedio entre las cantidades de ventas mensuales.
    """
    if len(ventas) < 2:
        # Si hay menos de dos ventas, no es posible calcular tendencias.
        return 0

    tasas = []
    for i in range(1, len(ventas)):
        cantidad_actual = ventas[i]["cantidad"]
        cantidad_anterior = ventas[i - 1]["cantidad"]
        # Calculo la tasa de cambio entre la venta actual y la anterior.
        tasa = (cantidad_actual - cantidad_anterior) / cantidad_anterior if cantidad_anterior != 0 else 0
        tasas.append(tasa)

    # Devuelvo el promedio de todas las tasas calculadas.
    return sum(tasas) / len(tasas) if tasas else 0


def estimar_ventas_futuras():
    """
    Proyecta ventas futuras de un producto.
    """
    ventas = cargar_csv('ventas.csv')
    if not ventas:
        print("Error: Ventas no disponibles.")
        return

    id_producto = input("ID del producto: ")
    ventas_producto = filtrar_ventas_por_producto(ventas, id_producto)
    ventas_producto.sort(key=lambda x: x["fecha"])

    if not ventas_producto:
        print(f"Sin datos para el producto {id_producto}.")
        return

    tasa_cambio = calcular_tasa_cambio(ventas_producto)
    ultima_cantidad = ventas_producto[-1]["cantidad"]
    proyeccion = ultima_cantidad * (1 + tasa_cambio)

    print(f"Tasa promedio: {tasa_cambio * 100:.2f}%")
    print(f"Proyección: {proyeccion:.2f} unidades.")

