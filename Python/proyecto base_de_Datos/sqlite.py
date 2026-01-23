import sqlite3

DB_NAME = "gestion_notas.db"

def obtener_conexion():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def crear_tablas():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asignaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            alumno_id INTEGER,
            asignatura_id INTEGER,
            nota REAL CHECK (nota >= 0 AND nota <= 10),
            PRIMARY KEY (alumno_id, asignatura_id),
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
            FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
        )
    """)
    conn.commit()
    conn.close()

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El texto no puede estar vacío.")

def pedir_nota(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 10:
                return valor
            print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Introduce un número válido.")

def ejecutar_consulta(query, params=()):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(query, params)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def ejecutar_modificacion(query, params=()):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error de integridad: {e}")
    finally:
        conn.close()

def crear_alumno():
    nombre = pedir_texto("Nombre del alumno: ")
    ejecutar_modificacion("INSERT INTO alumnos (nombre) VALUES (?)", (nombre,))

def crear_asignatura():
    nombre = pedir_texto("Nombre de la asignatura: ")
    ejecutar_modificacion("INSERT INTO asignaturas (nombre) VALUES (?)", (nombre,))

def listar_alumnos():
    return ejecutar_consulta("SELECT id, nombre FROM alumnos")

def listar_asignaturas():
    return ejecutar_consulta("SELECT id, nombre FROM asignaturas")

def seleccionar_id(lista, tipo):
    if not lista:
        print(f"No hay {tipo} registrados.")
        return None
    
    ids_validos = []
    for item in lista:
        print(f"ID: {item[0]} - Nombre: {item[1]}")
        ids_validos.append(item[0])
    
    while True:
        try:
            seleccion = int(input(f"Seleccione el ID del {tipo}: "))
            if seleccion in ids_validos:
                return seleccion
            print("ID no válido.")
        except ValueError:
            print("Introduce un número.")

def gestionar_nota():
    alumno_id = seleccionar_id(listar_alumnos(), "alumno")
    if alumno_id is None: return
    
    asignatura_id = seleccionar_id(listar_asignaturas(), "asignatura")
    if asignatura_id is None: return
    
    nota = pedir_nota("Introduce la nota: ")
    ejecutar_modificacion("""
        INSERT INTO notas (alumno_id, asignatura_id, nota) 
        VALUES (?, ?, ?)
        ON CONFLICT(alumno_id, asignatura_id) DO UPDATE SET nota = excluded.nota
    """, (alumno_id, asignatura_id, nota))

def mostrar_notas():
    query = """
        SELECT alumnos.nombre, asignaturas.nombre, notas.nota
        FROM notas
        JOIN alumnos ON notas.alumno_id = alumnos.id
        JOIN asignaturas ON notas.asignatura_id = asignaturas.id
    """
    resultados = ejecutar_consulta(query)
    if not resultados:
        print("No hay notas registradas.")
    else:
        for r in resultados:
            print(f"Alumno: {r[0]} | Asignatura: {r[1]} | Nota: {r[2]}")

def menu():
    crear_tablas()
    while True:
        print("\n--- GESTIÓN DE NOTAS ---")
        print("1. Crear alumno")
        print("2. Crear asignatura")
        print("3. Asignar o actualizar nota")
        print("4. Mostrar notas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": crear_alumno()
        elif opcion == "2": crear_asignatura()
        elif opcion == "3": gestionar_nota()
        elif opcion == "4": mostrar_notas()
        elif opcion == "5": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()