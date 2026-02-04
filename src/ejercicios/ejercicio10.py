monto = float(input("Ingrese el monto de venta: "))
total_ventas = 0.0

while monto != 0:
    if monto < 0.0:
        print("El monto ingresado es negativo.")
    else:
        total_ventas += monto
    monto = float(input("Ingrese el monto de venta: "))

print("La suma total de las ventas es:", total_ventas)