import sqlite3

DB = "gestion_notas.db"

def obtener_conexion():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def inicializar_db():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS asignaturas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE NOT NULL)")
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
    while True:
        txt = input(msg).strip()
        if txt: return txt
        print("Error: El texto no puede estar vacío.")

def pedir_nota(msg):
    while True:
        try:
            n = float(input(msg))
            if 0 <= n <= 10: return n
        except ValueError: pass
        print("Error: Nota válida entre 0 y 10.")

def query(sql, params=(), multi=False):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    res = cursor.fetchall() if multi else conn.commit()
    conn.close()
    return res

def seleccionar_id(tabla, tipo):
    items = query(f"SELECT id, nombre FROM {tabla}", multi=True)
    if not items:
        print(f"No hay {tipo} registrados.")
        return None
    for i in items: print(f"{i[0]}: {i[1]}")
    while True:
        try:
            sel = int(input(f"Elija ID de {tipo}: "))
            if sel in [i[0] for i in items]: return sel
        except ValueError: pass
        print("ID no válido.")

def menu():
    inicializar_db()
    while True:
        print("\n1.Crear Alumno\n2.Crear Asignatura\n3.Nota\n4.Mostrar\n5.Salir")
        op = input("Opción: ")
        if op == "1":
            try: query("INSERT INTO alumnos (nombre) VALUES (?)", (pedir_texto("Nombre: "),))
            except: print("Ya existe.")
        elif op == "2":
            try: query("INSERT INTO asignaturas (nombre) VALUES (?)", (pedir_texto("Asignatura: "),))
            except: print("Ya existe.")
        elif op == "3":
            aid = seleccionar_id("alumnos", "alumno")
            sid = seleccionar_id("asignaturas", "asignatura")
            if aid and sid:
                nt = pedir_nota("Nota: ")
                query("INSERT INTO notas VALUES (?,?,?) ON CONFLICT(alumno_id, asignatura_id) DO UPDATE SET nota=excluded.nota", (aid, sid, nt))
        elif op == "4":
            sql = "SELECT al.nombre, asig.nombre, n.nota FROM notas n JOIN alumnos al ON n.alumno_id = al.id JOIN asignaturas asig ON n.asignatura_id = asig.id"
            for r in query(sql, multi=True): print(f"{r[0]} | {r[1]} | Nota: {r[2]}")
        elif op == "5": break

if __name__ == "__main__":
    menu()