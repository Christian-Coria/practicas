bloques = int(input("Ingrese el número de bloques:"))
 
 
cotaSuperior = 0 #Cada piso (altura) de la pirámide, tiene un número máximo de bloques que se pueden utilizar
altura = 0
altura2: 0
 
while True:
 
#Aplico la condición para que mi contador vaya avanzado hasta alcanzar un máximo de bloques a una altura.
 
      if bloques <= cotaSuperior:
 
            # Si el límite superior menos los bloques ingresados es igual a cero ( no sobran ni faltan bloques), imprime el contador altura, hasta donde haya avanzado.
         if (cotaSuperior - bloques) == 0:
 
          print("La altura de la pirámide:", altura)
          break
 
            # Si el límite superior menos los bloques ingresados es mayor a cero (faltan bloques para completar el nivel), imprime el contador altura aterior (altura2).
         if (cotaSuperior - bloques) > 0:
 
          print("La altura de la pirámide:", altura2)
          break
 
      else:
 
        altura = altura + 1
        altura2 = altura - 1
 
      # Este es el contador que viene asociado con los bloques utilizados por cada altura alcanzada.
        cotaSuperior = cotaSuperior + altura