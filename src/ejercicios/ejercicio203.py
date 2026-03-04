"""
Escribir un programa que solicite al usuario ingresar dos números enteros y luego
"""
number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))

if number1 > number2:
    print(f"{number1} es mayor que {number2}.")
elif number1 < number2:
    print(f"{number1} es menor que {number2}.")
else:
    print(f"{number1} es igual que {number2}.")
