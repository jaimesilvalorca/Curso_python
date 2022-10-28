class Persona:
    def __init__(self, nombre,apellido,edad,*valores,**terminos):
        self.__nombre = nombre #restringir los atributos
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    

    #**terminos es un diccionario de datos
    #*valores es una tupla
    def mostrarDetalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
