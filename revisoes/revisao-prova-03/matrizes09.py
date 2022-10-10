m = []
produto = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

sl = []
sc = []

for i in range(5):
    somaLinha = 0
    somaColuna = 0

    for j in range(5):
        somaLinha += m[i][j]
        somaColuna += m[j][i]
    sl.append(somaLinha)
    sc.append(somaColuna)

for i in range(5):
    print(m[i])

print(f'Soma das linhas: ', sl)
print(f'Soma das colunas: ', sc)