matriz = []

def soma_diagonal(x):
    soma = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                soma += x[i][j]
    
    return soma


tamanho = int(input('Informe o tamanho da matriz: '))

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(int(input(f'Valor para A{i}{j}: ')))
    matriz.append(linha)

print('MATRIZ')
for i in range(len(matriz)):
    print(matriz[i])

print(f'Soma da diagonal: {soma_diagonal(matriz)}')

