#ejercicio1. iterar un rango entre 0 y 10 e imprimir numeros divisables entre 3

for i in range (11):
    if i % 3 == 0:
        print(i)

#ejercicio 2. Crear un rango de numeros de 2 a 6, imprimelos
print('----------------')
rango = range(2,7)

for i in rango:
    print(i)

#ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2

rango = range(3,11,2)

print('----------------')
for i in rango:
    print(i)