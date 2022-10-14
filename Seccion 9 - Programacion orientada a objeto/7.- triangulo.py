# se debe crear una clase llamado rectangulo y debe tener un metodo de calcular area
class Triangulo ():
    def __init__(self,base,altura,area=None):
        self.base = base
        self.altura = altura
        self.area = area

    def calcularArea(self):
        self.area = self.base * self.altura
        return self.area

base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura"))

triangulo1 = Triangulo(base,altura)
print(triangulo1.calcularArea())
print(triangulo1.area)

