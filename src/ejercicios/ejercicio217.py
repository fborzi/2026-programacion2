"""algo"""
char = input("Ingrese un caracter: ")
cadena = ""

while len(char) == 1 and char != "0":
    cadena = cadena + char
    char = input("Ingrese un caracter: ")

print(cadena)
