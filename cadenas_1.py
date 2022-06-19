def repitiendo(nom,num):
    for i in nom:
        nombre = i * num
        print (nombre)

try:
    nombre = input("introduce tu nombre: ")
    numero = int(input("introduce la cantidad de veces que se repetira el nombre: "))

except Exception as e:
    print("Error, en nombre ungresa solo letras y en numeros solo numeros")
else:
    repitiendo(nombre,numero)



nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

