class Vehiculo:
    def __init__(self, color,ruedas):
        self.__color = color #restringir los atributos
        self.__ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculo: {self.__color} {self.__ruedas}'


    def getColor(self):
        return self.__color

    def getRuedas(self):
        return self.__ruedas

    def setColor(self, color):
        self.__color = color

    def setRuedas(self, ruedas):
        self.ruedas = ruedas

vehiculo1 = Vehiculo('rojo',2)
print(vehiculo1)