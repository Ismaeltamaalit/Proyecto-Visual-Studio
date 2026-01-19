import random

class Heroe:
    def __init__(self, nombre:str, salud:int):
        self.nombre = nombre
        self.salud = salud
        
    def recibir_daño(self, cantidad:int):
        self.salud = max(0, self.salud - cantidad)
       
    def ser_curado(self, cantidad:int):
        self.salud += cantidad
        
    def atacar(self, otro_heroe):
        pass

class Guerrero(Heroe):
    def __init__(self, nombre:str, salud:int, fuerza:int):
        super().__init__(nombre, salud)
        self.fuerza = fuerza
            
    def atacar(self, otro_heroe):
        dado = random.randint(1, 20)
        daño_total = dado + int(self.fuerza/2)
        otro_heroe.recibir_daño(daño_total)
        print(f"{self.nombre} ataca a {otro_heroe.nombre} causando {daño_total} de daño.")

class Mago(Heroe): 
    def __init__(self, nombre:str, salud:int, inteligencia:int):
        super().__init__(nombre, salud)
        self.inteligencia = inteligencia
            
    def atacar(self, otro_heroe):
        dado = random.randint(1, 20)
        daño_total = dado + self.inteligencia
        otro_heroe.recibir_daño(daño_total)
        print(f"{self.nombre} ataca a {otro_heroe.nombre} causando {daño_total} de daño.")

class Picaro(Heroe):
    def __init__(self, nombre:str, salud:int, destreza:int):
        super().__init__(nombre, salud)
        self.destreza = destreza
        
    def atacar(self, otro_heroe):
        dado1 = random.randint(1, 10)
        dado2 = random.randint(1, 10)
        daño_total = dado1 + dado2 + self.destreza
        otro_heroe.recibir_daño(daño_total) 
        print(f"{self.nombre} apuñala a {otro_heroe.nombre} causando {daño_total} de daño.")

class Paladin(Heroe):
    def __init__(self, nombre:str, salud:int, fuerza:int, fe:int):
        super().__init__(nombre, salud)
        self.fuerza = fuerza
        self.fe = fe
            
    def atacar(self, otro_heroe): 
        dado = random.randint(1, 10)
        daño_total = dado + self.fuerza 
        otro_heroe.recibir_daño(daño_total)
        print(f"{self.nombre} golpea a {otro_heroe.nombre} causando {daño_total} de daño.")    

    def curar(self, otro_heroe): 
        dado = random.randint(1, 5)
        curacion_total = dado + self.fe
        otro_heroe.ser_curado(curacion_total)
        print(f"{self.nombre} bendice a {otro_heroe.nombre} curando {curacion_total} puntos.")

class Clerigo(Heroe):
    def __init__(self, nombre: str, salud: int, fe: int):
        super().__init__(nombre, salud)
        self.fe = fe

    def atacar(self, otro_heroe):
        print(f"{self.nombre} no puede atacar.")

    def curar(self, otro_heroe):
        dado = random.randint(1, 10)
        curacion_total = dado + self.fe
        otro_heroe.ser_curado(curacion_total)
        print(f"{self.nombre} sana a {otro_heroe.nombre} {curacion_total} puntos.")

if __name__=="__main__":
    karlach = Guerrero("Karlach", 100, 15)
    faralda = Mago("Faralda", 80, 20)
    astarion = Picaro("Astarion", 90, 15)
    tirion = Paladin("Tirion Vadín", 150, 12, 10)
    anduin = Clerigo("Anduin Wrynn", 75, 25)
            
    print("--- ESTADO INICIAL ---")
    print(f"{karlach.nombre}: {karlach.salud} HP")
    
    print("\n-- ACCIONES --")
    karlach.atacar(astarion)
    faralda.atacar(tirion)
    
    tirion.curar(karlach) 
    anduin.curar(faralda)
    
    print("\n--- ESTADO FINAL ---")
    print(f"{astarion.nombre}: {astarion.salud} HP")
    print(f"{faralda.nombre}: {faralda.salud} HP")
    print(f"{tirion.nombre}: {tirion.salud} HP")