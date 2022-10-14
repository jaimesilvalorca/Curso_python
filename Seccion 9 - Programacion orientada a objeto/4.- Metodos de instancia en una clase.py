class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    #la variable self se utiliza solo cuando estamos dentro de la clase, para cuando estamos fuera de la clase hay que llamar con el nombre de la clase y los atributos que se desea acceder
    # es creando una variable que este apuntando a un objeto directamente
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrarDetalle()
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrarDetalle()
