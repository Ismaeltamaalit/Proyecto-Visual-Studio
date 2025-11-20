from unidecode import unidecode

texto = input("Texto: ").split()
anagramas = {}

for palabra in texto:
    clave = ''.join(sorted(unidecode(palabra.lower())))
    if clave not in anagramas:
        anagramas[clave] = []
    anagramas[clave].append(palabra)

for grupo in anagramas.values():
    if len(grupo) > 1:
        print(grupo)