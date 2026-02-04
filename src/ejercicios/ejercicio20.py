cadena = input("Ingrese una cadena de texto: ")
abecedario = "abcdefghijklmnñopqrstuvwxyz"
cadena_nueva = ""
corrimiento = int(input("Ingrese el corrimiento (número entero): "))

for c in cadena:
    i = abecedario.find(c)
    cadena_nueva = cadena_nueva + abecedario[(i + corrimiento) % 27]

print(cadena_nueva)