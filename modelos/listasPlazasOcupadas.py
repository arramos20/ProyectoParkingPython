from modelos.Parking import *

class ListasPlazasOcupadas():
    def __init__(self):
        self.listaPlazasTotales=[],
        self.listaPlazasTurismos=[],
        self.listaPlazasMotos=[],
        self.listaPlazasMovRed=[]

    def agregarAlistaPlazasTotales(self, vehiculo):
        for i in range(Parking.plazasLibres):
            self.listaPlazasTotales.append(vehiculo)

    def agregarAlistaPlazasTurismos(self, vehiculo):
        for i in range(Parking.plazasTurismos):
            self.listaPlazasTotales.append(vehiculo)

    def agregarAlistaPlazasMotos(self, vehiculo):
        for i in range(Parking.plazasMotos):
            self.listaPlazasTotales.append(vehiculo)

    def agregarAlistaPlazasMovReducida(self, vehiculo):
        for i in range(Parking.plazasMovRed):
            self.listaPlazasTotales.append(vehiculo)

    def borrarDeListaObjetivo(self, lista, vehiculo):
        for i in range(lista):
            if (lista(i)==vehiculo):
                lista.pop(i)


