import opcioneDemenu.mostrarInicial as mostrarInicial
import opcioneDemenu.ventasFuturas as ventasFuturas
import opcioneDemenu.simularCompra as simularCompra
import opcioneDemenu.revisionPresupuesto as revisionPresupuesto
import opcioneDemenu.relacionProductoCliente as relacionProductoCliente
from graficos import generar_graficos


def menu_principal():
    opciones = {
        "1": mostrarInicial.mostrar_resumen_inicial,
        "2": ventasFuturas.estimar_ventas_futuras,
        "3": simularCompra.simular_compra,
        "4": revisionPresupuesto.revisar_presupuesto,
        "5": relacionProductoCliente.relacionProductoCliente,
        "6": lambda: generar_graficos(
            './archivos/productos.csv', './archivos/ventas.csv', './graficos'
        ),
    }

    while True:
        print("\nMenú Principal")
        print("1. Resumen inicial")
        print("2. Estimar ventas futuras")
        print("3. Simular compra")
        print("4. Revisar presupuesto")
        print("5. Analizar clientes")
        print("6. Generar gráficos")
        print("7. Salir")

        opcion = input("Opción: ").strip()
        if opcion == "7":
            print("Gracias por usar el sistema.")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida.")
if __name__ == '__main__':
    menu_principal()