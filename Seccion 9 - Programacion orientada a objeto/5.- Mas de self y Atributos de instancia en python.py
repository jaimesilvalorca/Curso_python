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
#persona1.mostrarDetalle()
Persona.mostrarDetalle(persona1)
persona1.telefono = '55441122' #en este caso se crea un nuevo atributo llamado telefono, pero este atributo no se comparte con el objeto 2
print(persona1.telefono) # en este caso si se puede acceder al telefono
#se puede llamar de la manera directo de la clase o enviando una variable



persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrarDetalle()
#print(persona2.telefono) no se puede acceder a este atributo porque solo es del objeto persona 1

