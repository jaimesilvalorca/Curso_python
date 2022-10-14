class Persona:
   # pass declarando una clase sin contenido  // #self = uno mismo, para crear una clase en python hay que usar un constructor y para eso se llama el __init__
   def __init__(self):#atributos de objetos para la clase
    self.nombre = 'Juan' #es mala practica asignar datos default
    self.apellido = 'Perez'
    self.edad = 28

persona1 = Persona()
print(persona1.nombre) #se accede a los atributos de la clase el nombre
print(persona1.apellido) # se accede a los atributos de la clase el apellido
print(persona1.edad) # se accede a los atributos de la clase edad.    