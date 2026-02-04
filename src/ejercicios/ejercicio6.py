"""algo"""
cantidad = int(input("Ingrese la cantidad de numero a procesar: "))
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero

print("La suma de los numeros es:", suma)
