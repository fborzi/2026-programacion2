"""algo"""
primo = int(input("Primo: "))

for i in range(2, int(primo ** 0.5) + 1):
    if primo % i == 0:
        print(f"El numero {primo} no es PRIMO.")
        break
else:
    print(f"El numero {primo} es PRIMO.")
