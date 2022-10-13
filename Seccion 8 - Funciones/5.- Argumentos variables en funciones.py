def listarNombres(*nombres): # el * es debido a que no se sabe la cantidad de arguemntos que va a tener la funcion, python lo convierte en una tupla
    for nombre in nombres: # Tambien podemos encontrar en la lista *args para poder declarar multples argumentos
        print(nombre)

listarNombres('Juan','Karla','Maria','Ernesto') # se transforma en una tupla, y lista los nombres
listarNombres('Laura','Carlos')