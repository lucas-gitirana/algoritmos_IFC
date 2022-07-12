precoFabrica = float(input("Preço de fábrica: "))
percLucro = float(input("Percentual de lucro: "))
percImpostos = float(input("Percentual de impostos: "))

lucroDistribuidor = precoFabrica * (percLucro / 100)
valorImpostos = precoFabrica * (percImpostos / 100)
precoFinal = precoFabrica + lucroDistribuidor + valorImpostos

print(lucroDistribuidor)
print(valorImpostos)
print(precoFinal)
