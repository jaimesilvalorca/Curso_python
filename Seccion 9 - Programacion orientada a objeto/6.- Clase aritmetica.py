class Aritmetica():
    """
    Clase aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self,operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #se va a crear un metodo llamado sumar

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB
        


aritmetica1 = Aritmetica(4,5)

print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())
