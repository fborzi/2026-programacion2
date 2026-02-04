"""
Escribir un programa que solicite al usuario ingresar dos números enteros y luego realice las siguientes operaciones:
"""

number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))

suma = number1 + number2
print("La suma de los dos numeros es:", suma)

resta = number1 - number2
print("La resta del primer numero menos el segundo es:", resta)
multiplicacion = number1 * number2
print("La multiplicacion de los dos numeros es:", multiplicacion)
if number2 != 0:
    division = number1 / number2
    print("La division del primer numero entre el segundo es:", division)
    resto = number1 % number2
    print("El resto de la division del primer numero entre el segundo es:", resto)
    entera = number1 // number2
    print("La division entera del primer numero entre el segundo es:", entera)
else:
    print("No se puede dividir por cero.")

absoluto1 = abs(number1)
absoluto2 = abs(number2)
print("El valor absoluto del primer numero es:", absoluto1)
print("El valor absoluto del segundo numero es:", absoluto2)
