def calculando_resto(a,b):
    c = a // b
    r = a % b
    print(f" {a} entre {b}, tiene un cociente de {c} y un resto de {r:.2f}")

a = float(input("ingresa un numero a dividir: "))
b = float(input("ingresa el numero dividor "))

calculando_resto(a,b)