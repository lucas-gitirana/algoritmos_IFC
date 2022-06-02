inferior = float(input("Limite inferior: "))
superior = float(input("Limite superior: "))

x = inferior
soma = 0

while x <= superior:
    if (x % 2 == 0):
        print(x)
        soma += x
    
    x+=1
    
print("Soma: ", soma)