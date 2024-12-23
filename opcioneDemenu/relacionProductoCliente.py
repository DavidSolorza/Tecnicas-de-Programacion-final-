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
    except Exception as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
        return []

def relacionProductoCliente():
    """
    Encuentra los clientes que han comprado más productos en las categorías seleccionadas usando fuerza bruta.
    """
    productos = cargar_csv('productos.csv')
    ventas = cargar_csv('ventas.csv')
    clientes = cargar_csv('clientes.csv')

    if not productos or not ventas or not clientes:
        print("Error: No se pudieron cargar los datos necesarios.")
        return

    print("\nCategorías disponibles:")
    categorias = list({producto.get('categoria', 'Desconocida') for producto in productos})
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")

    try:
        seleccionadas = [int(i.strip()) - 1 for i in input("\nSelecciona categorías (1,2,3): ").split(',')]
        categorias_seleccionadas = [categorias[i] for i in seleccionadas if 0 <= i < len(categorias)]
    except (ValueError, IndexError):
        print("Error: Selección inválida. Asegúrate de ingresar números válidos separados por comas.")
        return

    compras_por_cliente = {c.get('id_cliente'): {'nombre': c.get('nombre', 'Desconocido'), 'total_compras': 0} for c in clientes}

    for venta in ventas:
        producto = next((p for p in productos if p.get('id_producto') == venta.get('id_producto')), None)
        if producto and producto.get('categoria') in categorias_seleccionadas:
            compras_por_cliente[venta.get('id_cliente')]['total_compras'] += int(venta.get('cantidad', 0))

    clientes_ordenados = sorted(compras_por_cliente.values(), key=lambda x: x['total_compras'], reverse=True)
    print("\nClientes destacados:")
    for cliente in clientes_ordenados:
        if cliente['total_compras'] > 0:
            print(f"{cliente['nombre']} - Compras: {cliente['total_compras']}")

