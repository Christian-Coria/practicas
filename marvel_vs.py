def separando_grupo(nombre,fan):
    if nombre <= "m" and fan == "m" or nombre >= "n" and fan == "c":
        print("Tu Grupo es el A")
    else:
        print("Tu Grupo es el B")

nombre = input("ingresa tu nombre: ")
fan = input("ingresa tu preferencia C (CAPCOM) o M (MARVEL):  ")

separando_grupo(nombre,fan)



