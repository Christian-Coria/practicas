miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista =[]

for i in miLista:
    if i not in nuevaLista:
        nuevaLista.append(i)
    
print("La lista solo con elementos únicos:", nuevaLista)

