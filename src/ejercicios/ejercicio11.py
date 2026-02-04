cantidad_enteros = 0
positivos = 0
cantidad_positivos = 0
negativos = 0
ceros = 0
promedio = 0


while cantidad_enteros < 20:
    entero = int(input("Ingrese un numero entre -10 y 10: "))
    if -10 <= entero <= 10:
        if entero > 0:
            positivos += entero
            cantidad_positivos += 1
        elif entero < 0:
            negativos += entero
        else:
            ceros += 1
        cantidad_enteros += 1
    else:
        print("Numero fuera de rango. Intente nuevamente.")


print("La cantidad de numeros negativos es:", negativos)
print("La cantidad de ceros es:", ceros)
print("El promedio de los numeros positivos ingresados es:", positivos / cantidad_enteros)