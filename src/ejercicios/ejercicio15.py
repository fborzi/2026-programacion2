"""algo"""
cadena = input("Ingrese una cadena de texto: ").lower()
VOCALES = "aeiou"

vocales_aparecen = ""

for caracter in cadena:
    if caracter in VOCALES:
        if caracter not in vocales_aparecen:
            vocales_aparecen = vocales_aparecen + caracter

print(f"Las vocales que aparecen en la cadena son: {vocales_aparecen}")
