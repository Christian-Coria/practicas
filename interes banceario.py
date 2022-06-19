
def calculando_interes(deposito):
    año1 = (deposito  * 4 / 100) + deposito
    año2 = (año1 * 4 / 100) + deposito
    año3 = (año2 * 4 / 100) + deposito
    print (f"""
    La Ganancia del Primer año es {año1}
    La Ganancia del Segundo año es {año2}
    La Ganancia del Tercer año es {año3}
    """)

try:
    deposito = float(input("Ingresa el Monto del depostito: "))
except Exception as e:
    print("Error, debes ingresar solo numeros, error: {type(e)}")
else:
    calculando_interes(deposito)