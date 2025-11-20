import random

print("Juguemos a piedra, papel o tijera")

cadena = ['piedra', 'papel', 'tijera']
marcador=0
derrotas=0
empates=0

while True: 
    oponente = random.choice(cadena)
    eleccion = input("Elige piedra, papel o tijera (o 'exit' para salir): ").casefold()
    
    if eleccion == "exit":
        print("Hasta luego")
        break
    
    if eleccion not in cadena:
        print("Elección no válida. Por favor elige piedra, papel o tijera.")
        continue
    
    print("La computadora eligió: " + oponente)
    
    if eleccion == oponente:
        print("Empate")
        empates+=1
    elif eleccion == "piedra" and oponente == "tijera":
        print("Has ganado")
        marcador+=1
    elif eleccion == "piedra" and oponente == "papel":
        print("Has perdido")
        derrotas+=1
    elif eleccion == "papel" and oponente == "piedra":
        print("Has ganado")
        marcador+=1
    elif eleccion == "papel" and oponente == "tijera":
        print("Has perdido")
        derrotas+=1
    elif eleccion == "tijera" and oponente == "papel":
        print("Has ganado")
        marcador+=1
    elif eleccion == "tijera" and oponente == "piedra":
        print("Has perdido")
        derrotas+=1
        
    print("Empates:", empates)
    print("Victorias:", marcador)
    print("Derrotas:", derrotas)
    print("-" * 20)  