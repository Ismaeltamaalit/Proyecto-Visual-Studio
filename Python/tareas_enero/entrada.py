
alumnos = []

def añadir_alumno():
    while True:
        nombre = input("Nombre y dos apellidos: ")
        if len(nombre.split()) == 3:
            datos_nombre = nombre.replace(" ", ";")
            break
        print("Error: Pon nombre y dos apellidos.")

    while True:
        nota = input("Nota (0-10): ")
        if nota.replace('.', '', 1).isdigit() and 0 <= float(nota) <= 10:
            break
        print("Error: Nota no válida.")

    
    with open("Python/tareas_enero/notas.txt", "a", encoding="utf-8") as f:
        f.write(f"{datos_nombre};{nota}\n")
    
    print("¡Guardado!")    
    

def mostrar_alumnos():
    try:
        with open("Python/tareas_enero/notas.txt", "r", encoding="utf-8") as f:
            print("\n{:<20} | {:<5}".format("ALUMNO", "NOTA"))
            print("-" * 30)
            
            for linea in f:
                datos = linea.strip().split(";")
                nombre_completo = f"{datos[0]} {datos[1]} {datos[2]}"
                nota = datos[3]
                print(f"{nombre_completo:<20} | {nota:<5}")
                
    except FileNotFoundError:
        print("\n[!] El archivo 'notas.txt' no existe todavía.")
    


def menu_principal():
    while True:
        print("\n--- MENÚ DE GESTIÓN ---")
        print("1. Añadir alumno")
        print("2. Mostrar alumnos")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            añadir_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


menu_principal()