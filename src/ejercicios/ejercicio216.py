"""algo"""
cadena = input("Ingrese una cadena de texto: ").lower()
caracter = input("Ingrese un caracter a reemplazar: ").lower()
nueva_cadena = ""

for c in cadena:
    if caracter == c:
        nueva_cadena = nueva_cadena + "*"
    else:
        nueva_cadena = nueva_cadena + c

print(nueva_cadena)
