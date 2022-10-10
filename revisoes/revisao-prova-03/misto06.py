modelos = []
carros = {}
carros100 = {}
maisEconomico = ''
valorMaisEconomico = 0 

for i in range(5):
    modelos.append(input('Informe um modelo de carro: '))

x = 0
for modelo in modelos:
    carros[modelo] = input(f'Informe o consumo (km/L) do carro {modelo}: ')
    
    if x == 0:
        maisEconomico = modelo
        valorMaisEconomico = int(carros[modelo])
    elif int(carros[modelo]) > valorMaisEconomico:
        maisEconomico = modelo
        valorMaisEconomico = int(carros[modelo])
    
    x += 1

    carros100[modelo] = int(carros[modelo]) * 100

print('Valores: ', carros)
print('Carro mais economico', maisEconomico)
print('Litros para percorrer 100 km: ', carros100)