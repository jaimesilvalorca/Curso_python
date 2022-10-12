#Instrucciones de la tarea:
#- En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo,
#para ello deberemos crear las siguientes variables:

#alto (int)
#ancho (int)

#- El usuario debe proporcionar los valores de alto y ancho,
#y después se debe imprimir el resultado en el siguiente formato
#(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

#Proporciona el alto:
#Proporciona el ancho:
#Area: <area>
#Perimetro: <perimetro>

#Las formulas para calcular el area y el perimetro de un Rectangulo son:
#Area: alto * ancho
#Perimetro: (alto + ancho) * 2

alto:int = int(input("Alto del triangulo: "))
ancho:int = int(input("Ancho del triangulo: "))

area = alto * ancho
perimetro = (alto + ancho) *2

print(f'Proporciona el alto: {alto}')
print(f'Proporciona el ancho: {ancho}')
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')



