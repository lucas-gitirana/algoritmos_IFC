num = int(input("Número: "))

acumulador = num

for i in range(1, num):
    aux = num - i
    acumulador = aux * acumulador

print(acumulador)

    