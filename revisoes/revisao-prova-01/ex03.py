precoFabrica = float(input("Preço de fábrica: "))
percLucro = float(input("Precentual de lucro do distribuidor: "))
percImpostos = float(input("Percentual de impostos: "))

lucro = precoFabrica * (percLucro/100)
impostos = precoFabrica * (percImpostos/100)
precoFinal = precoFabrica + lucro + impostos

print("O valor correspondente ao lucro do distribuidor: ", lucro)
print("O valor correspondente aos impostos: ", impostos)
print("O preço final do veículo: ", precoFinal)
