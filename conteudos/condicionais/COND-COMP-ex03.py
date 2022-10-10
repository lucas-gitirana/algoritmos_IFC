precoFabrica = float(input("Preço de fábrica: "))
# tranformar em 0.00
percLucroDist = float(input("Precentual de lucro do distribuidor: "))
percImposto = float(input("Percentual de imposto: "))

lucroDist = precoFabrica * (percLucroDist/100)
valorImposto = precoFabrica * (percImposto/100)
precoFinal = precoFabrica + lucroDist + valorImposto

print("Lucro do distribuidor: ", lucroDist)
print("Valor de imposto: ", valorImposto)
print("Preço final: ", precoFinal)
