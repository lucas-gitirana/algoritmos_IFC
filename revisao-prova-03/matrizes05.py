m = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

somaColuna = 0
somaDiag = 0

for i in range(10):
    for j in range(10):
        if j == 1:
            somaColuna += m[i][j]
        
        if i == j:
            somaDiag += m[i][j]

for i in range(10):
    print(m[i])

print('Soma da coluna 2: ', somaColuna)
print('Soma da diagonal principal: ', somaDiag)