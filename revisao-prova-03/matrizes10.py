m = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

somaP = 1
somaS = 1
for i in range(2):
    for j in range(2):
        if i == j:
            somaP *= m[i][j]
        else:
            somaS *= m[i][j]

det = somaP - somaS

for i in range(2):
    print(m[i])

print('Determinante: ', det)