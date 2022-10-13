#Ejercicio: Convertidor de temperatura
#Realizar dos funciones para convertir de grados celcius a fahrenheit y viceversa

#(0 °C × 9/5) + 32 = 32 °F
# (32 °F − 32) × 5/9 = 0 °C

print("1.- Celcius a Farenheit")
print("2.- Farenheit a celcius")

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    temperatura = int(input("Ingrese la temperatura que va a convertir a farenheit: "))
    def farenheit(temperatura):
        resultado = temperatura * (9/5) + 32
        return resultado
    resultado = farenheit(temperatura) 
    print(f'Celcius: {temperatura} a Farenheit: {resultado}')

elif opcion == 2:
    temperatura = int(input("Ingrese la temperatura que va a convertir a celcius: "))
    def celcius(temperatura):
        resultado = (temperatura - 32) * (5/9)
        return resultado  
    resultado = celcius(temperatura)
    print(f'Farenheit: {temperatura} a Celcius: {resultado}')

else:
    print("opcion no valida")



