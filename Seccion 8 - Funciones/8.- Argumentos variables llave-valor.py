def listarTerminos (**terminos): #kwargs es para declarar un diccionario en una funcion.
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Developement Environment',PK='Primary Key') #la llave(key) no lleva comillas y el valor puede ser cualquier tipo de dato
listarTerminos(BD='Base de datos')