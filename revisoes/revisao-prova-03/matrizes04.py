m = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

soma = 0
for i in range(5):
    for j in range(5):
        if i == 3:
            soma += m[i][j]

for i in range(5):
    print(m[i])

print('Soma da linha 4: ', soma)