#premisa es usar break para finalizar ciclo
palabra = None
while palabra != 0:
    palabra = input("ingresa una palabra: ")
    if palabra == "chupacabra":
        break
print("ingresaste: chupacabra")