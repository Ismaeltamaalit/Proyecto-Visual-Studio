texto = input("Texto: ").lower().split()
contador = {}

for palabra in texto:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)