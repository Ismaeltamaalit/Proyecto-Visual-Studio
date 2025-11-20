tasas = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0
}

cantidad = float(input("Cantidad: "))
desde = input("Desde: ").upper()
hacia = input("Hacia: ").upper()

resultado = cantidad * tasas[hacia] / tasas[desde]
print(resultado)