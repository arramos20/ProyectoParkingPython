class Parking():
    def __init__(self, plazasLibres=500):
        self.__plazasLibres=plazasLibres,
        self.__plazasTurismos=70%plazasLibres,
        self.__plazasMotos=15%plazasLibres,
        self.__plazasMovRed=15%plazasLibres

    @property #getter PlazasLibres
    def plazasLibres(self):
        return self.__plazasLibres;

    @property #getter PlazasTurismos
    def plazasTurismos(self):
        return self.__plazasTurismos;

    @property #getter PlazasMotocicletas
    def plazasMotos(self):
        return self.__plazasMotos;

    @property #getter PlazasVehiculosMovilidadReducida
    def plazasMovRed(self):
        return self.__plazasLibres;
