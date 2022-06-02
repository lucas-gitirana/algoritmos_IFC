x = 1
maior = 0

while x <= 10:
    num = float(input("Número: "))
    
    if(x == 1):
        maior = x
        menor = x
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
    x+=1



print("Maior: ", maior)
print("Menor: ", menor)