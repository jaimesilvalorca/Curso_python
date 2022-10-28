from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color,ruedas,tipo):
        super().__init__(color,ruedas)

        self.__tipo = tipo #restringir los atributos
    
    def __str__(self):
        return f'{super().__str__()} {self.__tipo}'


    def getVelocidad(self):
        return self.__tipo

    def setVelocidad(self, tipo):
        self.__tipo = tipo