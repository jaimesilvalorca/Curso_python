min = 20
max = 30

edad = int(input("Ingrese su edad: "))

rango = (edad >= min) and (edad <= max)

if rango:
    print(f'Su edad: {edad} está en el rango')
else:
    print(f'Su edad: {edad} no está en el rango')