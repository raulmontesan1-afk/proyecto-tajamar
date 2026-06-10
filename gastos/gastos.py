def crear_gasto(nombre: str, precio: float) -> dict:
    return {
        "nombre": nombre,
        "precio": precio
    }

def formatear_gasto(gasto: dict) -> dict:
    return {
        "nombre": gasto["nombre"].title(),
        "precio": f"{gasto['precio']:.2f} €"
    }