from datetime import datetime

#imprimimos un titulo, Lo centramos he imprimimos un espacio antes de la primer opcion
print("Software de Calculo de Facturacion en 5 Meses".center(60,"-"))
print("")

#creamos la Clase Calculo y la inicializamos con el contructor y 
# (el Atributo Instancia Privado) de Lista 
class Facturando5Meses:
    def __init__(self,lista):
        self._lista = lista     #
    #encapsulamos el atributo de instancia
    @property #permite obtener o usar el atributo en diferentes metodos con el decorador @property
    def lista(self):
        return self._lista
    
    @lista.setter # damos acceso para asignar un valor fuera de la clase si asi se deseara con el decorador @setter
    def lista(self,lista):
        self._lista = lista

    def __str__(self): # el metodo __str__ devuelve la cadenacon los atributos que queremos mostrar si es llamado
        return f"Los Importes Vendidos en Cada Mes Ingresados a la Lista son: {self._lista}"
    
    # Definimos el Metodo de la Clase para sumar todos los valores que incluye la lista
    def sumando_lista(self,lista):        
        Suma_de_lista = sum(lista) #creando funcion suma_de_lista sum()
        return Suma_de_lista

    # Definimos el Metodo de la Clase para identificar el menor valor incluido en la lista
    def calculando_minimo(self,lista):
        min = lista[0] #asigno a min el valor del primer numero de la lista
        for i in range (1, len(lista)):
            if lista[i] < min: #preguntamos si el valor de la lista del momento es menor al que tiene min
                min = lista[i] #se lo asignamos
            return min #por ultimo mandamos el numero final menor que quedo en la variable al programa general

    # Definimos el Metodo de la Clase para identificar el mayor valor incluido en la lista
    def calculando_maximo(self,lista):
        max = lista[0] #asigno a max el valor del primer numero de la lista
        for i in range (1, len(lista)):
            if lista[i] > max: #preguntamos si el valor de la lista del momento es mayor al que tiene max
                max = lista[i] # se lo asignamos 
            return max #por ultimo mandamos el numero final mayor que quedo en la variable al programa general
    
    # Definimos el Metodo de la Clase promedio que devuelve el promedio de Facturacion de los periodos
    def promediando(self,lista):
        return sum(lista) / len (lista)

# iniciamos el bloque try para manejar errores de ingreso por parte del usuario
try:  
    #creamos una lista vacia
    lista = []
    #iniciamos un ciclo while, con la funcion len condicionamos el ciclo q que se rompa (en false)
    # cuando la longitud de la lista llegue a 5 ingresos
    while len(lista) <= 4:
        #pedimos al usuario el ingreso de los datos correspondientes
        valor = int(input("INGRESE el TOTAL de VENTAS de CADA MES, Redondeando a Numeros Enteros: "))
        #agregamos por medio de append a la lista lo ingresado
        lista.append(valor)
        
# atrapamos el error de existir he indicamos el mismo
except Exception as e:
    print("Error: Debe Ingresar SOLO NUMEROS ENTEROS!, Inicie nuevamente Para Volver a Ingresar (SOLO NUMEROS ENTEROS!)")
# caso contrario  
else:
    #creamos un objeto 
    calculo1 = Facturando5Meses(lista)
    #inicializamos el menu
    print("MENU DE OPCIONES".center(50,"*"))
    print("""
    OPCION 1 => TOTAL de Venta de 5 Periodos
    OPCION 2 => MENOR venta mensual de 5 Periodos
    OPCION 3 => MAYOR venta mensual de 5 Periodos
    OPCION 4 => PROMEDIO de venta de 5 Periodos
    OPCION 5 => SALIR
    """)
    #manejamos tanto errores (try-except), como un menu ciclico (while)
    while True:
        try:
            opcion = int(input("Ingrese la Opcion Deseada: "))
        except Exception as e:
            print("Error: Debe ingresar solo numeros enteros y las opciones del Menu!")
        else: # si no hubo error entramos verificando la condicion de lo digitado para llamar al metodo de la clase que corresponda he imprimir el resultado.
            if opcion == 1:
                print("La Suma total de ventas de los 5 periodos es: ",calculo1.sumando_lista(lista),"DOLARES\n")
            elif opcion == 2:
                print("La venta menor de los 5 periodos es: ",calculo1.calculando_minimo(lista),"DOLARES\n")
            elif opcion == 3:
                print("La Mayor venta de los 5 periodos es: ", calculo1.calculando_maximo(lista),"DOLARES\n")
            elif opcion == 4: 
                print("El Promedio de ventas de los 5 periodos es: ", calculo1.promediando(lista),"DOLARES\n")
            elif opcion == 5:
                print("Consulta Realizada el ",datetime.now())
                print("Saliendo-------\n")
                break
            else:
                print("Error opcion de Menu NO VALIDA\n")
                
if __name__ == "__main__": # verificamos que todo lo que se ejecute se ejecute dentro del mismo modulo
    #saludamos al finalizar he informamos el horario y dia de la consulta
    print("Gracias por Usar Nuestro SOFTWARE...\n")