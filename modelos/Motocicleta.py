from modelos.Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.08):
        super().__init__(matricula, tarifaMinuto)
