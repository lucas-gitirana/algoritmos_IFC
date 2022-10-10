n = int(input("Número de consumidores: "))
precoKwh = float(input("Preço do kWh: "))

maiorConsumo = 0
menorConsumo = 0
totalResidencial = 0
totalComercial = 0
totalIndustrial = 0

x = 1

while x <= n:
    consumoMes = float(input("Consumo do mês em kWh: "))
    codigoConsumidor = int(input("Código (1 - residencial, 2 - comercial, 3 - industrial): "))
    
    print("Total a pagar: R$ ", (consumoMes * precoKwh))

    if x == 1:
        maiorConsumo = consumoMes
        menorConsumo = consumoMes
    else:
        if consumoMes > maiorConsumo:
            maiorConsumo = consumoMes
        elif consumoMes < menorConsumo:
            menorConsumo = consumoMes
        
    if codigoConsumidor == 1:
        totalResidencial += consumoMes
    elif codigoConsumidor == 2:
        totalComercial += consumoMes
    elif codigoConsumidor == 3:
        totalIndustrial += consumoMes
    else:
        print("Código inválido!")

    x += 1

print("Maior consumo da amostra: ",  maiorConsumo)
print("Menor consumo da amostra: ", menorConsumo)
print("Total do consumo residencial: ", totalResidencial)
print("Total do consumo comercial: ", totalComercial)
print("Total do consumo industrial: ", totalIndustrial)