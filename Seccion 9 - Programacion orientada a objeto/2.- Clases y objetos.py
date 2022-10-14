class Persona:
   # pass declarando una clase sin contenido  // #self = uno mismo, para crear una clase en python hay que usar un constructor y para eso se llama el __init__
   def __init__(self, nombre, apellido,edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

Persona1 = Persona('Juan','Perez',30)
Persona2 = Persona('Karla','Gomez',30)


print(f'Objeto persona 1:{Persona1.nombre} {Persona1.apellido} {Persona1.edad}')
#se puede agregar variables pero se debe respetar la clase

print(f'Objeto persona 2:{Persona2.nombre} {Persona2.apellido} {Persona2.edad}')