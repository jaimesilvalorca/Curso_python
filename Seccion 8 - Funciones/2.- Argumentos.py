def mi_funcion(nombre,apellido): #si de declaran variables en funcion se deben llenar al llamarlos
    print('saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}') 

mi_funcion('Juan', 'Perez') #si se ejecuta el codigo asi, solo enviara saludos desde mi funcion
mi_funcion('Karla', 'Perez')

#primer llamado de la funcion
# nombre = Juan
# Apellido = Perez
#segundo llamado vuelve a ejectuar la funcion desde la linea 2 hasta la 3
# nombre = karla
# apellido = perez