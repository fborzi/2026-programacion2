weekday = input("Ingrese un dia de la semana: ").strip().lower()
products = int(input("Ingrese la cantidad de articulos comprados: "))

if weekday == "lunes" and products >= 3:
    print("Accede al descuento.")


