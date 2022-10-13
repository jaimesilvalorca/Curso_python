# Crear una funcion para multiplicar los valores recibidos de tipo numero,
# utilizando argumentos variables *args como paramentro de la funcion
# y regresar como resultado la multiplicacion de todos los valores pasados como argumentos


def multiplicar_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

print(multiplicar_valores(2,2,2))