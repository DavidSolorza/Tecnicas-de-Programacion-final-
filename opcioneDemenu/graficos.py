import os
import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(productos_path, ventas_path):
    """
    Carga y combina los datos de productos y ventas.
    """
    productos_df = pd.read_csv(productos_path)
    ventas_df = pd.read_csv(ventas_path)

    # Combinar ventas con productos
    ventas_productos = ventas_df.merge(productos_df, on="id_producto")
    ventas_productos['fecha'] = pd.to_datetime(ventas_productos['fecha'])
    ventas_productos.rename(columns={"cantidad_x": "cantidad_vendida"}, inplace=True)

    return ventas_productos

def graficar_ventas_por_categoria(ventas_productos, output_path):
    """
    Genera un gráfico de ventas totales por categoría.
    """
    ventas_categoria = ventas_productos.groupby('categoria')['cantidad_vendida'].sum()
    plt.figure(figsize=(10, 6))
    ventas_categoria.plot(kind='bar')
    plt.title('Ventas Totales por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'ventas_totales_categoria.png'))
    plt.close()

def graficar_productos_mas_vendidos(ventas_productos, output_path):
    """
    Genera un gráfico de los 5 productos más vendidos.
    """
    productos_mas_vendidos = ventas_productos.groupby('nombre')['cantidad_vendida'].sum().nlargest(5)
    plt.figure(figsize=(10, 6))
    productos_mas_vendidos.plot(kind='bar', color='orange')
    plt.title('Top 5 Productos Más Vendidos')
    plt.xlabel('Producto')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'productos_mas_vendidos.png'))
    plt.close()

def graficar_tendencia_ventas_por_fecha(ventas_productos, output_path):
    """
    Genera un gráfico de tendencias de ventas por fecha.
    """
    ventas_por_fecha = ventas_productos.resample('M', on='fecha')['cantidad_vendida'].sum()
    plt.figure(figsize=(12, 6))
    ventas_por_fecha.plot(kind='line', marker='o')
    plt.title('Tendencia de Ventas por Fecha (Mensual)')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad Vendida')
    plt.grid()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'tendencia_ventas_fecha.png'))
    plt.close()

def graficar_comparativo_por_categoria(ventas_productos, output_path):
    """
    Genera un gráfico comparativo de ventas por categoría.
    """
    comparativo_categoria = ventas_productos.groupby(['categoria', 'fecha'])['cantidad_vendida'].sum().unstack('categoria').fillna(0)
    comparativo_categoria.plot(figsize=(12, 6))
    plt.title('Comparativo de Ventas por Categoría')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad Vendida')
    plt.legend(title='Categoría', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'comparativo_ventas_categoria.png'))
    plt.close()

def graficar_tendencia_general_ventas(ventas_productos, output_path):
    """
    Genera un gráfico de tendencia general de ventas.
    """
    ventas_tendencia_general = ventas_productos.groupby('fecha')['cantidad_vendida'].sum()
    plt.figure(figsize=(12, 6))
    ventas_tendencia_general.plot(kind='line', marker='o', color='green')
    plt.title('Tendencia General de Ventas')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad Vendida')
    plt.grid()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'tendencia_general_ventas.png'))
    plt.close()

def generar_graficos(productos_path, ventas_path, output_path):
    """
    Genera todos los gráficos solicitados y los guarda en la carpeta de salida.
    """
    os.makedirs(output_path, exist_ok=True)
    ventas_productos = cargar_datos(productos_path, ventas_path)

    graficar_ventas_por_categoria(ventas_productos, output_path)
    graficar_productos_mas_vendidos(ventas_productos, output_path)
    graficar_tendencia_ventas_por_fecha(ventas_productos, output_path)
    graficar_comparativo_por_categoria(ventas_productos, output_path)
    graficar_tendencia_general_ventas(ventas_productos, output_path)

    print(f"Gráficos generados en la carpeta: {output_path}")
