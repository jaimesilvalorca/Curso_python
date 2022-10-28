class Persona:
    def __init__(self, nombre,apellido,edad):
        self.__nombre = nombre #restringir los atributos
        self.__apellido = apellido
        self.__edad = edad
    
    def __str__(self):
        return f'Persona: {self.__nombre} {self.__apellido} {self.__edad}'


    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getEdad(self):
        return self.__edad 

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.__edad = edad  

    def mostrarDetalle(self):
        print(f'Persona: {self.__nombre} {self.__apellido} {self.__edad}')

class Empleado(Persona):
    def __init__(self,nombre,apellido,edad, sueldo):
        super().__init__(nombre,apellido,edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} {self.sueldo}'
        
