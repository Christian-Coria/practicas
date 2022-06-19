def descontando(barras_pan):
    valor_final = barras_pan * 3.49 - (1 * 0.6 )
    print(f"el valor final del pan con descuento es : {valor_final:.2f}")

try:
    barras = int(input("ingresa la cantidad de barras de pan compradas: "))
except Exception as e:
    print("Error, debes introducir un numero!")
else:
    descontando(barras)


barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")
