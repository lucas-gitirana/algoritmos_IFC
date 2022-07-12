sup = int(input("Limite superior: "))
inf = int(input("Limite inferior: "))

x = inf
somador = 0

while x <= sup:
    
    if x % 2 == 0:
        print(x)
        somador += x
    
    x+=1

print("Soma: ", somador)