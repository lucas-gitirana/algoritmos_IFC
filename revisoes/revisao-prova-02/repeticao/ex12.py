somaPos = 0
contNeg = 0

for i in range (20):
    num = int(input("Número: "))

    if num > 0:
        somaPos += num
    elif num < 0:
        contNeg += 1

print("Soma dos positivos: ", somaPos)
print("Total de negativos: ", contNeg)