x = 1
soma_pos = 0
cont_neg = 0

while x <= 20:
    num = float(input("Número: "))

    if num > 0:
        soma_pos += num
    else:
        cont_neg += 1

    x+=1

print("Soma dos positivos: ", soma_pos)
print("Total de negativos; ", cont_neg)