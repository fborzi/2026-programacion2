cantidad = int(input("Ingrese la cantidad de numero a procesar: "))
suma = 0
pares = 0
impares = 0

numero = int(input("Ingrese un numero: "))
while numero >= 0 and cantidad >= 0:
    suma += numero
    if numero % 2 == 0:
        pares += numero
    else:
        impares += numero
    numero = int(input("Ingrese un numero: "))
    cantidad -= 1

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)