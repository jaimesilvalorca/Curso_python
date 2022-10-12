#las listas son modificables , pero la tupla es inmutable

#definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba')

#saber el tamaño de la tupla

print(len(frutas))
print(frutas)

#acceder a un elemento

print(frutas[0])

#navegacion inversa
print(frutas[-3])

#acceder a un rango
print(frutas[0:2]) #no se incluye el ultimo valor

#recorrer elementos

for fruta in frutas:
    print(fruta)

#cambiar el valor de una tupla
#frutas[0] = 'Pera'
#print(frutas) NO SE PUEDE MODIFICAR UNA TUPLA

frutasLista = list(frutas) #transformar una tupla a una lista
frutasLista[0] = 'Pera'
fruta = tuple(frutasLista) #trasnformar una lista en tupla

print(fruta)

#eliminar la tupla por completo

del(frutas)
print(frutas)



