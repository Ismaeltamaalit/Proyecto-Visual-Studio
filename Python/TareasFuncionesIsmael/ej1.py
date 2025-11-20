tasas = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75}

def nueva_moneda(moneda, tasa):
    tasas[moneda] = tasa

def modificar_tasa(moneda, nueva_tasa):
    if moneda in tasas:
        tasas[moneda] = nueva_tasa

def eliminar_moneda(moneda):
    if moneda in tasas:
        del tasas[moneda]

def mostrar_tasas():
    for moneda, tasa in sorted(tasas.items()):
        print(f"{moneda}: {tasa}")

while True:
    opcion = input("1. Nueva moneda\n2. Modificar tasa\n3. Eliminar moneda\n4. Mostrar tasas\n5. Convertir\n6. Salir\nOpción: ")
    
    if opcion == "1":
        moneda = input("Moneda: ").upper()
        tasa = float(input("Tasa: "))
        nueva_moneda(moneda, tasa)
    elif opcion == "2":
        moneda = input("Moneda: ").upper()
        nueva_tasa = float(input("Nueva tasa: "))
        modificar_tasa(moneda, nueva_tasa)
    elif opcion == "3":
        moneda = input("Moneda: ").upper()
        eliminar_moneda(moneda)
    elif opcion == "4":
        mostrar_tasas()
    elif opcion == "5":
        cantidad = float(input("Cantidad: "))
        desde = input("Desde: ").upper()
        hacia = input("Hacia: ").upper()
        resultado = cantidad * tasas[hacia] / tasas[desde]
        print(resultado)
    elif opcion == "6":
        break