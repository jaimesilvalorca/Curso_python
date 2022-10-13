# ejercicio: calculadora de impuestos
# crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)

montoImpuesto = int(input("Ingrese el monto sin impuesto: "))
impuesto = int(input("Ingrese el impuesto: "))

def funcionImpuesto(impuestos,montos):
    pago_total = impuestos + impuestos *(montos/100)
    return pago_total

resultado = funcionImpuesto(montoImpuesto,impuesto)
print(f'''
    Valor sin impuestos: {montoImpuesto}
    Valor del impuesto: {impuesto}
    Pago con impuesto: {resultado}
''')