actual = 0
siguiente = 1

for _ in range(25):
    print(actual)
    siguiente, actual = actual + siguiente, siguiente
    