n = int(input("Número de amostras: "))
precoKW = float(input("Preço do kWh: "))

somaConsumo1 = 0
somaConsumo2 = 0
somaConsumo3 = 0


x = 1
while x <= n:

    consumoMes = float(input("Consumo no mês: "))
    codigo = int(input("Código do tipo de consumidor (1,2,3): "))

    total = precoKW * consumoMes
    print("Total a pagar: ", total)

    if x == 1:
        maiorConsumo = consumoMes
        menorConsumo = consumoMes
    else:
        if consumoMes > maiorConsumo:
            maiorConsumo = consumoMes
        elif consumoMes < menorConsumo:
            menorConsumo = consumoMes
    
    if codigo == 1:
        somaConsumo1 += consumoMes
    elif codigo == 2:
        somaConsumo2 += consumoMes
    elif codigo == 3:
        somaConsumo3 += consumoMes
    else:
        print("Código inválido")

    x += 1

print("Maior consumo da amostra: ", maiorConsumo)
print("Menor consumo da amostra: ", menorConsumo)
print("Total residencial: ", somaConsumo1)
print("Total comercial: ", somaConsumo2)
print("Total industrial: ", somaConsumo3)