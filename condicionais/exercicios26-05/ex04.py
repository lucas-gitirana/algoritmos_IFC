x = int(input("X: "))
y = int(input("Y: "))

if ((x + y) * 0.3) > 500:
    aux = x
    x = y
    y = aux
    print("X: ", x , "Y: ", y)
else:
    if x > y:
        print("Menor valor: ",y)
    else:
        print("Menor valor: ",x)