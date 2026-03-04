"""algo"""
alumno = int(input("Ingrese el legajo del alumno: "))
aprobados = 0
desaprobados = 0

while alumno != 0:
    nota = float(input("Ingrese la primera nota: "))
    if nota >= 4:
        aprobados += 1
    else:
        desaprobados += 1
    alumno = int(input("Ingrese el legajo del alumno (0 para terminar): "))

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)
