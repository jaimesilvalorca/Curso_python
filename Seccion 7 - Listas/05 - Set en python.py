#set

#set no guarda ningun orden
planetas = {'Martes', 'Jupiter', 'Venus'}
print(planetas)

#tamaño del set
print(len(planetas))

#revisar si existe algun elemento del set
print('Martes' in planetas)

#agregar un elemento a nuestor set
planetas.add('Tierra')
print(planetas)

#no se puede agregar duplicados
planetas.add('Tierra')
print(planetas) #solo tendremos un solo elemento de tierra

#eliminar un elemento
planetas.remove('Tierra')
print(planetas)
planetas.discard('Jupiter')

#eliminar el set
planetas.clear()
print(planetas)

del planetas
print(planetas)