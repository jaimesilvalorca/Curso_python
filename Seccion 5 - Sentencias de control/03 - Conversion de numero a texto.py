numero = int(input("proporciona un valor entre uno y tres: "))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'valor fuer de rango'

print(f'Numero proporcionado: {numero} - {numeroTexto}')