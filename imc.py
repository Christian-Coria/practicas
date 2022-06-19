def calculando_masa(peso,altura):
    imc = peso / altura **2.2
    print(f"Tu IMC es {imc:.2f} ")

peso = float(input("introduce tu Peso: "))
altura = float(input("introduce tu altura: "))

calculando_masa(peso,altura)
