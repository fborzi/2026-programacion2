"""algo"""
cadena = input("Ingrese una cadena de texto: ")
ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"
cadena_nueva = ""
corrimiento = int(input("Ingrese el corrimiento (número entero): "))

for c in cadena:
    i = ABECEDARIO.find(c)
    cadena_nueva = cadena_nueva + ABECEDARIO[(i + corrimiento) % 27]

print(cadena_nueva)
