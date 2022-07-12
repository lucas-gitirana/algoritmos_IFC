x = 1
contMaiores = 0

while x <= 15:
    num = int(input("Número: "))

    if num > 30:
        contMaiores += 1
    
    x += 1

print("Números maiores que 30: ", contMaiores)