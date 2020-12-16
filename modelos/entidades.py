class Vehiculo():
    def __init__(self, matricula, tarifaMinuto):
        self.matricula=matricula,
        self.tarifaMinuto=tarifaMinuto

class Turismo(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.12):
        super().__init__(matricula, tarifaMinuto)

class Motocicleta(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.08):
        super().__init__(matricula, tarifaMinuto)

class MovilidadReducida(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.10):
        super().__init__(matricula, tarifaMinuto)

class Cliente():
    def __init__(self, nombre, idPlaza, pin, vehiculo):

class Persona():
    def __init__(self, nombre, apellidos):
        self.nombre=nombre,
        self.apellidos=apellidos

class Empleado(Persona):

    def __init__(self, nombre, apellidos, sueldo):
        super().__init__(nombre, apellidos) #Manera 1 (Para herencia simple normalmente)
        self.sueldo=sueldo #Manera 2 (Hace lo mismo que la frase de arriba

    def __str__(self):
        return f"{self.nombre} {self.apellidos} Sueldo: {self.sueldo}"
