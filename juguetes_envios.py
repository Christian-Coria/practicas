

def despachando_juguetes(cant_payaso,cant_muñeca):
    peso1 = cant_payaso * 112
    peso2 = cant_muñeca * 69
    peso_total = peso1 + peso2
    print(f"el peso total es {peso_total} Kg")

try:

    payasos = int(input("introduce la cantidad de payasos a enviar: "))
    muñecas = int(input("introduce la cantidad de muñecas a enviar: "))
except Exception as e:
    print ("Error, debes ingresar solo numeros")

else:

    despachando_juguetes(payasos,muñecas)
