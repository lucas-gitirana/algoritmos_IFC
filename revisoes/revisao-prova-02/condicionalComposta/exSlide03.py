maior = 0
menor = 0

for i in range(5):
    num = int(input("Número: "))
    
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print(maior, menor)