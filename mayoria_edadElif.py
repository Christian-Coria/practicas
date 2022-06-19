def verificando_edad(edad):
    if edad >= 18:
        print (f"Por Tu Edad {edad}, YA ERES MAYOR")
    elif edad >= 12:
        print (f"Por tu edad {edad}, eres ADOLESCENTE")
    elif edad <= 11 and edad >= 0:
        print (f"Disfruta de tu edad, hay tiempo para  crecer")
    else:
        print ("no puedes tener una edad menor a cero")

edad = int(input("Ingresa tu edad: "))
verificando_edad(edad)


