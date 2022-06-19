def invirtiendo(cantidad,interes,años):
    capital_obtenido = cantidad * ( interes / 100 + 1) ** años
    print(f"El Capital resultante de la inversion de $ {cantidad} en {años} años, es ${capital_obtenido:.2f} ")

cantidad = float(input("introduce el monto a invertir: "))
interes = float(input("introduce el interes (%): "))
años = float(input("introduce los años para tu inversion: "))

invirtiendo(cantidad,interes,años)
