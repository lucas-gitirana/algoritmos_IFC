continuar = 'S'
cont0a25 = 0
cont26a50 = 0 
cont51a75 = 0
cont76a100 = 0

while continuar == 'S':
    num = int(input("Número: "))

    if num < 0:
        print("Você não pode digitar números negativos.")
    else:
        if num >= 0 and num <= 25:
            cont0a25 += 1
        elif num >= 26 and num <= 50:
            cont26a50 += 1
        elif num >= 51 and num <= 75: 
            cont51a75 += 1
        elif num >= 76 and num <= 100:
            cont76a100 += 1
    
    continuar = input("Deseja continuar? (Digite S para sim): ")

print("Quantidade de números entre 0 e 25: ", cont0a25)
print("Quantidade de números entre 26 e 50: ", cont26a50)
print("Quantidade de números entre 51 e 75: ", cont51a75)
print("Quantidade de números entre 76 e 100: ", cont76a100)
