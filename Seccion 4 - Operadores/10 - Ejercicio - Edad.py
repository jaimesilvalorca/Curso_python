edadAdulto:int = 18
edadPersona = int(input("Ingrese su edad: "))

if edadPersona >= edadAdulto:
    print(f'Eres mayor de edad porque tienes: {edadPersona}')
else:
    print(f'Eres menor de edad porque tienes: {edadPersona}')