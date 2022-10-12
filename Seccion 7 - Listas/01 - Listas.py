#definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'María']
#imprimir la lista de nombres:
print(nombres)
#acceder a los elementos de una lista
nombres[0]
print(nombres[3])
#acceder a los elementos de una lista de manera inversa
print(nombres[-1])
#imprimir un rango
print(nombres[0:2]) #imprime los valores de 0 y 1
#ir del inici ade la lista al indice (sin incluirlo)
print(nombres[ : 3]) #recorrer la lista 0,1,2
#desde el indice indicado hasta el final
print(nombres[1:]) #indiice 1,2 y 3
#cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar nuestra lista

for nombre in nombres: #se crea una variable en singular para iterarlo de 1 en 1
    print(nombre)
else:
    print("no existen mas nombres")

#preguntar largo de una lista
print(len(nombres))

#agregar un elemento
nombres.append('Lorenzo')
print(nombres)

#insertar un elemento en un indice en especifico
nombres.insert(1,'Octavio')
print(nombres)

#remover un elemento
nombres.remove('Octavio')
print(nombres)

#remover el ultimo valor agregado
nombres.pop() #elimina el ultimo valor por defecto

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar todos los elementos de la lista

nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres) #ahora manda error