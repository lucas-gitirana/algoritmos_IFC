contPrimos = 0

x = 1
while contPrimos < 10:

    y = 1
    contZeros = 0

    while y <= x:
        resto = x % y
        if (resto == 0):
            contZeros += 1
        y += 1
                

    if (contZeros == 2):
        print(x)
        contPrimos += 1
           

    x+=1 
        
