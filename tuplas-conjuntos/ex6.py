dict = {}
dictMil = {}

for i in range(5):
    modelo = input("Informe um modelo: ")    
    consumo = float(input(f"Informe o consumo do carro {modelo}: "))

    dict[modelo] = consumo

    if i == 0:
        maisEco = modelo
        consumoMaisEco = consumo
    else:
        if consumo < consumoMaisEco:
            maisEco = modelo
            consumoMaisEco = consumo
    
    dictMil[modelo] = consumo * 1000 

print(dict)

print("Modelo mais econômico: ", maisEco)   
print("Litros para percorrer mil km: ", dictMil)

