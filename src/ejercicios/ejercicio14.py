cadena = input("Ingrese una cadena de texto: ").strip()

cantidad_palabras = cadena.count(" ") + 1 if cadena else 0
print("La cantidad de palabras en la cadena es:", cantidad_palabras)

letras = ""
cantidad_letras = 0

cadena = cadena + " "

for caracter in cadena:
    if caracter != " ":
        cantidad_letras += 1
        letras += caracter
    elif cantidad_letras > 0:
        print(f"La palabra '{letras}' tiene {cantidad_letras} letras.")
        cantidad_letras = 0
        letras = ""