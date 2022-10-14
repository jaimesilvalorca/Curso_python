#calcular el area de de un cubo, clase cubo y metodo calcular area cubo

class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calculoArea(self):
        area = self.ancho * self.alto * self.profundo
        return area

ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
profundo = int(input("Ingrese la profundidad: "))

cubo1 = Cubo(ancho,alto,profundo)

print(cubo1.calculoArea())
