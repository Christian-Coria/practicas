resultado = 0
def sueldo_horas(sueldo,horas):
    resultado = sueldo // horas
    print(f"trabajas a {resultado} la hora")


sueldo = float(input("digita tu sueldo: "))
horas = float(input("digita las horas wue trabajas: "))

sueldo_horas(sueldo,horas)
