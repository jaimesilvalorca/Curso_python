calificacion = int(input('Proporcione su calificacion entre 1 y 10: '))
letra = None
if calificacion >= 9 and calificacion <= 10:
    letra = 'A'
elif calificacion >= 8 and calificacion < 9:
    letra = 'B'
elif calificacion >= 7 and calificacion < 8:
    letra = 'C'
elif calificacion >= 6 and calificacion < 7:
    letra = 'D'
elif calificacion >= 0 and calificacion < 6:
    letra = 'F'
else:
    letra = 'Calificacion invalida'

print(f'Su calificacion es: {calificacion} y su letra es: {letra}')

