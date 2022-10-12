#Diccionario (key,value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OPP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

#conocer el largo de un diccionario
print(len(diccionario))

#acceder a un elemento (key)
print(diccionario['IDE'])

#otra forma de tener un elemento
print(diccionario.get('OPP'))

#modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

#recorrer los elementos del diccionario

for termino, valor in diccionario.items(): #valor y llave
    print(termino,valor)

for termino in diccionario.keys(): #llaves
    print(termino)

for valor in diccionario.values(): #valor
    print(valor)

#comprobar existencia de algun elemento

print('IDE' in diccionario)

#agregar un elemento

diccionario ['PK'] = 'Primary Key' #no es posible agregar llaves duplicadas, si agregamos una llave existente sobreescribe la llave con el nuevo valor
print(diccionario)

#remover un elemento

diccionario.pop('DBMS') #se debe especificar la llave
print(diccionario)

#limpiar el diccionario

diccionario.clear()
print(diccionario)

#eliminar el diccionaro

del diccionario
print(diccionario)

