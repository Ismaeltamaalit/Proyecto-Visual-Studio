from unidecode import unidecode

def verificar_dni(dni):
    if len(dni) not in [9, 10]:
        return False
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = dni[:-1]
    letra = dni[-1].upper()
    try:
        return letras[int(numero) % 23] == letra
    except:
        return False

def crear_identificador(nombre, dni):
    nombre_sin_acentos = unidecode(nombre.lower())
    palabras = nombre_sin_acentos.split()
    iniciales = ''.join(palabra[:2] for palabra in palabras)
    ultimos_digitos = dni[-4:-1]
    return iniciales + ultimos_digitos

socios = {}

while True:
    nombre = input("Nombre completo: ")
    if nombre.upper() == "EXIT":
        break
    dni = input("DNI: ")
    
    if not verificar_dni(dni):
        print("DNI inválido")
        continue
    
    identificador = crear_identificador(nombre, dni)
    socios[identificador] = {"nombre": nombre, "dni": dni}
    print(f"Identificador: {identificador}")

print("\nSocios registrados:")
for iden, datos in sorted(socios.items()):
    print(f"{iden}: {datos['nombre']} - {datos['dni']}")