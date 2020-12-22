from modelos.Parking import *
from modelos.Turismo import *
from modelos.Motocicleta import *
from modelos.MovReducida import *

class Cliente():
    def __init__(self, nombre, idPlaza, pin, vehiculo):
        self.nombre=nombre,
        self.idPlaza=idPlaza,
        self.pin=pin,
        self.vehiculo=vehiculo

    #p1 = Parking();

    def depositarVehiculo(self):
        print("Plazas libres totales: " + Parking.plazasLibres + "\n" +
            "Plazas libres para turismos: " + Parking.plazasTurismos +
            "Plazas libres para motocicletas: " + Parking.plazasMotos +
            "Plazas libres para vehículos de Movilidad Reducida: " + Parking.plazasMovRed)

        while(t1.matricula or m1.matricula or mr1.matricula == 0):
            matri=input("Dame la matrícula de tu vehículo: ")

            tipo=input("Introduce '1' si tu vehículo es un turismo.\n"+
                       "Introduce '2' si tu vehículo es una motocicleta.\n" +
                       "Introduce '3' si tu vehículo es uno de movilidad reducida.\n")

            if (tipo==1):
                t1=Turismo(matri)
                #t1.__setattr__(matri, "HOLA123")
            elif(tipo==2):
                m1=Motocicleta(matri)
            elif(tipo==3):
                mr1=MovilidadReducida(matri)
            else:
                print ("Has introducido un valor no válido.\n"+
                       "Por favor, prueba otra vez")


