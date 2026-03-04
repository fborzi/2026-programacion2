"""algo"""
primo = int(input("Primo: "))
cantidad_primos = 0
while primo != 0:
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            cantidad_primos += 1
            break
    else:
        pass
    primo = int(input("Primo: "))

print("Cantidad de numeros primos ingresados:", cantidad_primos)
