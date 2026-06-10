from tabulate import tabulate
from gastos import crear_gasto, formatear_gasto

items = [
    crear_gasto("café", 1.50),
    crear_gasto("libro python", 29.99),
    crear_gasto("teclado", 75.00),
]

if __name__ == "__main__":
    items_formateados = [formatear_gasto(g) for g in items]
    print(tabulate(items_formateados, headers="keys"))
