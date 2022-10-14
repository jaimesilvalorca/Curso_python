class Persona:
    def __init__(self, nombre,apellido,edad,*valores,**terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    

    #**terminos es un diccionario de datos
    #*valores es una tupla
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Juan', 'Perez', 28,'444444444',2,3,5, m='manzana',p='pera',)
persona1.mostrarDetalle()
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrarDetalle()