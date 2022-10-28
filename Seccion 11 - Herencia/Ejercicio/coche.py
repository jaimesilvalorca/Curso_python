from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color,ruedas,velocidad):
        super().__init__(color,ruedas)

        self.__velocidad = velocidad #restringir los atributos
    
    def __str__(self):
        return f'{super().__str__()} {self.__velocidad}'


    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

coche1= Coche('rojo',4,'50km/h')
print(coche1)
