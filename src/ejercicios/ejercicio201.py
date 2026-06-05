"""
Escribir un programa que solicite al usuario ingresar dos números
enteros y luego realice las siguientes operaciones:
"""

division = 0.0
resto = 0
entera = 0

number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2

if number2 != 0:
    division = number1 / number2
    resto = number1 % number2
    entera = number1 // number2
else:
    print("No se puede dividir por cero.")

absoluto1 = abs(number1)
absoluto2 = abs(number2)

print("La suma de los dos numeros es:", suma)
print("La resta del primer numero menos el segundo es:", resta)
print("La multiplicacion de los dos numeros es:", multiplicacion)
print("La division del primer numero entre el segundo es:", division)
print("El resto de la division del primer numero entre el segundo es:", resto)
print("La division entera del primer numero entre el segundo es:", entera)
print("El valor absoluto del primer numero es:", absoluto1)
print("El valor absoluto del segundo numero es:", absoluto2)
