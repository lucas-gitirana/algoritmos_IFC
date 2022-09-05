import numpy as np

modelos = []
consumo = []
milKm = []

consumoMaisEconomico = 0
maisEconomico = ""

for i in range(5):
    modelo = input("Informe o modelo: ")
    modelos.append(modelo)

for i in range(5):
    valor = float(input("Informe o consumo do carro em km/l: "))
    consumo.append(valor)
    
    if i == 0:
        consumoMaisEconomico = consumo[i]
        maisEconomico = modelos[i]
    elif consumo[i] > consumoMaisEconomico:
        consumoMaisEconomico = consumo[i]
        maisEconomico = modelos[i]

for i in range(5):
    milKm.append(consumo[i] * 1000)

print("Lista de modelos: ", modelos)
print("Lista dos respectivos consumos: ", consumo)
print("Modelo mais econômico: ", maisEconomico)
print("Quantidade de litros necessários para percorres 1000km: ", milKm)
