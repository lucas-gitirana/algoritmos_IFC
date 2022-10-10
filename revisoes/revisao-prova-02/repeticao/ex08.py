x = 1

while x <= 10:

    num = int(input("Número: "))

    if x == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num

    x += 1

print(maior)
print(menor)