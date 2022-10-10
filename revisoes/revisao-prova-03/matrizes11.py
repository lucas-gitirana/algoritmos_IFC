vetor = [1,2,3,4,5]
m = [
    [1,2,3,4,5], 
    [6,7,8,9,1], 
    [2,3,4,5,6],
    [7,8,9,1,2],
    [3,4,5,6,7]
    ]

resultado = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(vetor[i] * m[i][j])
    resultado.append(linha)

for i in range(5):
    print(resultado[i])