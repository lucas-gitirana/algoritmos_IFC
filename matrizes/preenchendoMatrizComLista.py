matriz = []


for i in range(5):
    linha = []
    for j in range(5): 
        valor = int(input("Valor: "))
        linha.append(valor)
    matriz.append(linha)


print(matriz)