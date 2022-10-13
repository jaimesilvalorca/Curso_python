def sumar (a=1,b=0): # se pueden agregar valores por default a las funciones
    return a+b

resultado = sumar()

print(f'resultado de la suma es: {resultado}')

print(f'resultado sumar: {sumar(5,3)}')

def sumar (a=1,b=0): # se pueden agregar valores por default a las funciones
    return 'saludos'
 
resultado = sumar() # el retorno va entregar un 'saludos' en el retorno

print(f'resultado de la suma es: {resultado}')

print(f'resultado sumar: {sumar(5,3)}')