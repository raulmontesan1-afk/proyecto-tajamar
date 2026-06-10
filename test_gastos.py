from gastos import crear_gasto, formatear_gasto

def test_crear_gasto():
    gasto = crear_gasto("café", 1.50)
    assert gasto["nombre"] == "café"
    assert gasto["precio"] == 1.50

def test_crear_gasto_precio_cero():
    gasto = crear_gasto("gratis", 0)
    assert gasto["precio"] == 0

def test_formatear_gasto():
    gasto = crear_gasto("café", 1.50)
    resultado = formatear_gasto(gasto)
    assert resultado["nombre"] == "Café"
    assert resultado["precio"] == "1.50 €"