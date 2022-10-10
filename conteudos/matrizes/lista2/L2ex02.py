matriz = []

valor = 0
#PREENCHENDO A MATRIZ
for i in range(10):
    linha = []
    for j in range(10):
        #valor = int(input(f'Informe um valor para A{i}{j}: '))
        valor += 1
        linha.append(valor)
    matriz.append(linha)

# TROCA DE VALORES
aux = []
aux2 = []
for i in range(10):
    aux.append(matriz[7][i])
    matriz[7][i] = matriz[1][i]
    matriz[1][i] = aux[i]

    aux2.append(matriz[4][i])
    matriz[4][i] = matriz[i][8]
    matriz[8][i] = aux2[i]

# APRESENTAÇÃO DA MATRIZ
print('=====MATRIZ=====')
for i in range(10):
    print(matriz[i])