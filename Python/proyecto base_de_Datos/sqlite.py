import sqlite3

# Nombre del archivo de base de datos que se creará en la carpeta del script
DB = "gestion_notas.db"

def obtener_conexion():
    """Establece la conexión con SQLite y activa el soporte de claves foráneas."""
    conn = sqlite3.connect(DB)
    # PRAGMA asegura que si borras un alumno, se respeten las restricciones de sus notas
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def inicializar_db():
    """Crea las tablas necesarias si no existen al arrancar el programa."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    # Tabla de Alumnos: ID autoincremental y nombre único
    cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE NOT NULL)")
    
    # Tabla de Asignaturas: ID autoincremental y nombre único
    cursor.execute("CREATE TABLE IF NOT EXISTS asignaturas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE NOT NULL)")
    
    # Tabla de Notas: Relaciona alumnos con asignaturas. 
    # PRIMARY KEY compuesta evita que un alumno tenga dos notas en la misma asignatura.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            alumno_id INTEGER, 
            asignatura_id INTEGER, 
            nota REAL CHECK(nota >= 0 AND nota <= 10),
            PRIMARY KEY(alumno_id, asignatura_id),
            FOREIGN KEY(alumno_id) REFERENCES alumnos(id),
            FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id)
        )
    """)
    conn.commit()
    conn.close()

def pedir_texto(msg):
    """Bucle para asegurar que el usuario no deje campos de texto vacíos."""
    while True:
        txt = input(msg).strip()
        if txt: return txt
        print("Error: El texto no puede estar vacío.")

def pedir_nota(msg):
    """Valida que la entrada sea un número decimal entre 0 y 10."""
    while True:
        try:
            n = float(input(msg))
            if 0 <= n <= 10: return n
        except ValueError: pass # Ignora si el usuario escribe letras
        print("Error: Nota válida entre 0 y 10.")

def query(sql, params=(), multi=False):
    """Función genérica para ejecutar comandos SQL (INSERT, UPDATE o SELECT)."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    # Si multi es True, devuelve los datos (SELECT), si no, guarda cambios (COMMIT)
    res = cursor.fetchall() if multi else conn.commit()
    conn.close()
    return res

def seleccionar_id(tabla, tipo):
    """Muestra una lista de elementos y pide al usuario que elija uno por su ID."""
    items = query(f"SELECT id, nombre FROM {tabla}", multi=True)
    if not items:
        print(f"No hay {tipo} registrados.")
        return None
    
    for i in items: print(f"{i[0]}: {i[1]}")
    
    while True:
        try:
            sel = int(input(f"Elija ID de {tipo}: "))
            # Comprueba que el ID introducido existe en la lista obtenida de la DB
            if sel in [i[0] for i in items]: return sel
        except ValueError: pass
        print("ID no válido.")

def menu():
    """Interfaz principal del programa."""
    inicializar_db()
    while True:
        print("\n1.Crear Alumno\n2.Crear Asignatura\n3.Nota\n4.Mostrar\n5.Salir")
        op = input("Opción: ")
        
        if op == "1":
            try: 
                query("INSERT INTO alumnos (nombre) VALUES (?)", (pedir_texto("Nombre: "),))
            except: 
                print("Ya existe.") # Salta si el nombre viola la restricción UNIQUE
                
        elif op == "2":
            try: 
                query("INSERT INTO asignaturas (nombre) VALUES (?)", (pedir_texto("Asignatura: "),))
            except: 
                print("Ya existe.")
                
        elif op == "3":
            # Proceso para asignar nota: primero elegir alumno, luego asignatura
            aid = seleccionar_id("alumnos", "alumno")
            sid = seleccionar_id("asignaturas", "asignatura")
            if aid and sid:
                nt = pedir_nota("Nota: ")
                # UPSERT: Si ya existe la nota, la actualiza; si no, la crea
                query("INSERT INTO notas VALUES (?,?,?) ON CONFLICT(alumno_id, asignatura_id) DO UPDATE SET nota=excluded.nota", (aid, sid, nt))
        
        elif op == "4":
            # Consulta compleja con JOIN para unir las 3 tablas y mostrar nombres en lugar de IDs
            sql = """
                SELECT al.nombre, asig.nombre, n.nota 
                FROM notas n 
                JOIN alumnos al ON n.alumno_id = al.id 
                JOIN asignaturas asig ON n.asignatura_id = asig.id
            """
            for r in query(sql, multi=True): 
                print(f"{r[0]} | {r[1]} | Nota: {r[2]}")
                
        elif op == "5": 
            break

if __name__ == "__main__":
    menu()