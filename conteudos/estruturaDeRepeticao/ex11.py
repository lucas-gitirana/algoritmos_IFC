x = 1
cont_30 = 0

while x <= 15:

    num = float(input("Número: "))

    if (num > 30):
        cont_30 += 1
        print(num , "é maior que 30!")

    x+=1

print("Total de números maiores que 30: ", cont_30)
