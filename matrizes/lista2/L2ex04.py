matriz = []
sl = []
sc = []
valorSoma = 0

# CRIA A MATRIZ
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input("Informe um valor: "))
        linha.append(valor)
    
    matriz.append(linha)

# SOMA DAS LINHAS DA MATRIZ
for i in range(5):
    valorSoma = 0
    for j in range(5):
        valorSoma += matriz[i][j]
    
    sl.append(valorSoma)

# SOMA DAS COLUNAS DA MATRIZ
for j in range(5):
    valorSoma = 0
    for i in range(5):
        valorSoma += matriz[i][j]

    sc.append(valorSoma)

# APRESENTAÇÃO DA MATRIZ
print('Matriz: ')
for i in range(5):
        print(matriz[i])

print('Soma das colunas: ', sc)
print('Soma das linhas: ', sl)

