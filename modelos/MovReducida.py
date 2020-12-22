from modelos.Vehiculo import Vehiculo

class MovilidadReducida(Vehiculo):
    def __init__(self, matricula, tarifaMinuto=0.10):
        super().__init__(matricula, tarifaMinuto)
