# imprimir numeros de 5 a 1 de manera descenete usando funciones recursivas.
# puede ser cualquier valor positivo, ejempli, si pasamos el valor de 5, debe imprimir
#5
#4
#3
#2
#1
#en caso de pasar el valro de 3, debe imprimir:
#3
#2
#1

#si se pasan valores negativos no se imprime nada

def descendente(numeros):
    if numeros == 0:
        return 1
    elif numeros < 0:
        print("Valor incorrecto")
    else:
        print(numeros)
        numeros -= 1
        return descendente(numeros)
            

descendente(5)