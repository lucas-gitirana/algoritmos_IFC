#FATORIAL

n = int(input("Número: "))

acumulador = 1
for i in range(1, n+1):
    acumulador *= i

print(acumulador)