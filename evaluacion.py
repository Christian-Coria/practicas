año = int(input("Introduzca un año:"))

if año % 4 != 0 and año > 1582:
    print("año comun")
elif año % 100 != 0 and año > 1582:
    print("año bisiesto")
elif año <= 1582:
    print("No dentro del período del calendario gregoriano")

    



