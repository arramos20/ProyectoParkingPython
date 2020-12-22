from modelos.Vehiculo import Vehiculo

class Turismo(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.12):
        super().__init__(matricula, tarifaMinuto)
