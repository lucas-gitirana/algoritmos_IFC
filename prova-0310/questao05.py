m = []
maiorElemento = 0
linhaMaior = 0
minimax = 0

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe um valor para M{i}{j}: ')))
    m.append(linha)

# ENCONTRA O MAIOR VALOR DA MATRIZ
for i in range(5):
    for j in range(5):
        if i == 0 and j == 0:
            maiorElemento = m[i][j]
            linhaMaior = i
        elif m[i][j] > maiorElemento:
            maiorElemento = m[i][j]
            linhaMaior = i

# DETERMINA MINIMAX
for j in range(5):
    if j == 0:
        minimax = m[linhaMaior][j]
    elif m[linhaMaior][j] < minimax:
        minimax = m[linhaMaior][j]

print('-------------------------------------')
print(f'Matriz: ')
for i in range(5):
    print(m[i])
print('-----')
print(f'Minimax da matriz: {minimax}')


