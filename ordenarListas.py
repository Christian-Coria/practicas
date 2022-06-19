miLista = []
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False# no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)
