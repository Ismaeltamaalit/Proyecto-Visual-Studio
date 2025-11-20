def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def posicion_primo(n):
    contador = 0
    for i in range(2, n + 1):
        if es_primo(i):
            contador += 1
    return contador

def descomposicion_primos(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores

while True:
    entrada = input("Número: ")
    if entrada.upper() == "EXIT":
        break
    numero = int(entrada)
    
    if es_primo(numero):
        pos = posicion_primo(numero)
        print(f"Es primo. Posición: {pos}")
    else:
        factores = descomposicion_primos(numero)
        print(f"Descomposición: {factores}")