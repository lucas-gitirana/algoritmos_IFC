m = []
diag = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

for i in range(5):
    for j in range(5):
        if i == j:
            diag.append(m[i][j])

print('Diagonal principal: ', diag)
