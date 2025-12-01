class RespuestaInvalida(Exception):
    pass


def crear_preguntas():
    preguntas_facil = [
        {
            "enunciado": "¿De que color es el cielo?",
            "opciones": {
                "A": "Rojo",
                "B": "Verde", 
                "C": "Azul",
                "D": "Amarillo"
            },
            "correcta": "C"
        },
        {
            "enunciado": "¿Cuantas extremidades tiene una persona?",
            "opciones": {
                "A": "2",
                "B": "4",
                "C": "6", 
                "D": "8"
            },
            "correcta": "B"
        },
        {
            "enunciado": "¿Cuando se adoptó el Euro en España?",
            "opciones": {
                "A": "1999",
                "B": "2000",
                "C": "2001",
                "D": "2002"
            },
            "correcta": "D"
        },
        {
            "enunciado": "¿Cual es la ultima consola de Sony?",
            "opciones": {
                "A": "PlayStation 4",
                "B": "PlayStation 5", 
                "C": "Xbox Series X",
                "D": "Nintendo Switch"
            },
            "correcta": "B"
        },
        {
            "enunciado": "¿Que personaje es el más importante de Nintendo?",
            "opciones": {
                "A": "Sonic",
                "B": "Mario",
                "C": "Pikachu",
                "D": "Lara Croft"
            },
            "correcta": "B"
        }
    ]
    
    preguntas_media = [
        {
            "enunciado": "¿Quien fue el primer emperador de Roma?",
            "opciones": {
                "A": "Julio César",
                "B": "Nerón",
                "C": "Augusto",
                "D": "Constantino"
            },
            "correcta": "C"
        },
        {
            "enunciado": "¿Que dos reyes de dos paises unieron las coronas para formar España?",
            "opciones": {
                "A": "Castilla, y Aragón",
                "B": "Francia, y Portugal",
                "C": "Navarra, y León",
                "D": "Granada, y Cataluña"
            },
            "correcta": "A"
        },
        {
            "enunciado": "¿Cuando se lanzó el primero juego de Zelda?",
            "opciones": {
                "A": "1985",
                "B": "1986", 
                "C": "1987",
                "D": "1988"
            },
            "correcta": "B"
        },
        {
            "enunciado": "¿Cuantos mundiales de futbol ganó España?",
            "opciones": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3"
            },
            "correcta": "B"
        },
        {
            "enunciado": "¿Cuando se ganó?",
            "opciones": {
                "A": "2008",
                "B": "2010",
                "C": "2012", 
                "D": "2014"
            },
            "correcta": "B"
        }
    ]
    
    preguntas_dificil = [
        {
            "enunciado": "¿Cual es el videojuego mas vendido de la historia?",
            "opciones": {
                "A": "GTA V",
                "B": "Tetris",
                "C": "Minecraft",
                "D": "Wii Sports"
            },
            "correcta": "C"
        },
        {
            "enunciado": "¿Cual es la saga de videojuegos más importante de Xbox?",
            "opciones": {
                "A": "Forza",
                "B": "Gears of War",
                "C": "Halo",
                "D": "Fable"
            },
            "correcta": "C"
        },
        {
            "enunciado": "¿Que cientifico propone la primera base matématica sobre los agujeros negros?",
            "opciones": {
                "A": "Albert Einstein",
                "B": "Stephen Hawking",
                "C": "Karl Schwarzschild",
                "D": "Isaac Newton"
            },
            "correcta": "C"
        },
        {
            "enunciado": "¿Cual fue la primera consola de videojuegos en salir al mercado?",
            "opciones": {
                "A": "Atari 2600",
                "B": "Magnavox Odyssey",
                "C": "Nintendo Entertainment System",
                "D": "Sega Master System"
            },
            "correcta": "B"
        },
        {
            "enunciado": "¿Cual es la empresa del mundo gaming más antigua del mundo?",
            "opciones": {
                "A": "Sega",
                "B": "Nintendo",
                "C": "Atari",
                "D": "Sony"
            },
            "correcta": "B"
        }
    ]
    
    return preguntas_facil, preguntas_media, preguntas_dificil


def mostrar_menu():
    print("\n=== QUIEN QUIERE SER MILLONARIO ===")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")


def leer_opcion_menu():
    return input("Selecciona una opción (1-3): ")


def mostrar_instrucciones():
    print("\n=== INSTRUCCIONES ===")
    print("Responde 15 preguntas para ganar.")
    print("5 fáciles, 5 medias y 5 difíciles.")
    print("Escribe P para plantarte.")


def obtener_pregunta_por_numero(numero, facil, media, dificil):
    if 1 <= numero <= 5:
        return facil[numero - 1]
    elif 6 <= numero <= 10:
        return media[numero - 6]
    elif 11 <= numero <= 15:
        return dificil[numero - 11]


def mostrar_pregunta(numero, pregunta):
    print(f"\nPregunta {numero}:")
    print(f"{pregunta['enunciado']}")
    print("Opciones:")
    for letra, texto in pregunta['opciones'].items():
        print(f"{letra}: {texto}")


def leer_respuesta():
    try:
        respuesta = input("Tu respuesta (A/B/C/D) o P para plantarse: ").upper()
        if respuesta not in ["A", "B", "C", "D", "P"]:
            raise RespuestaInvalida("Respuesta no válida")
        return respuesta
    except RespuestaInvalida as e:
        print(f"Error: {e}")
        return leer_respuesta()


def jugar_partida(preguntas_facil, preguntas_media, preguntas_dificil):
    puntuacion = 0
    
    for numero in range(1, 16):
        pregunta_actual = obtener_pregunta_por_numero(
            numero, 
            preguntas_facil, 
            preguntas_media, 
            preguntas_dificil
        )
        
        mostrar_pregunta(numero, pregunta_actual)
        respuesta_usuario = leer_respuesta()
        
        if respuesta_usuario == "P":
            print(f"Te plantaste. Ganaste: {puntuacion} puntos")
            return
        
        if respuesta_usuario == pregunta_actual["correcta"]:
            puntuacion += 1
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta era {pregunta_actual['correcta']}")
            print(f"Ganaste: {puntuacion} puntos")
            return
    
    print(f"¡GANASTE! Puntuación final: {puntuacion}")


def main():
    facil, media, dificil = crear_preguntas()
    
    while True:
        mostrar_menu()
        opcion = leer_opcion_menu()
        
        if opcion == "1":
            jugar_partida(facil, media, dificil)
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
