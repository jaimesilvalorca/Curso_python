# Crear una funcion para sumar los valores recibidos de tipo numero,
# utilizando argumentos variables *args como paramentro de la funcion
# y regresar como resultado la suma de todos los valores pasados como argumentos

def SumarValores(*args):
    resultado = 0
    #iterar cada elemento
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado 
        

# llamada a la funcion

print(SumarValores(3, 5, 9, 4, 6))

