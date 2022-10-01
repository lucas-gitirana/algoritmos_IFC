a = int(input(f'Informe um valor qualquer: '))

m = []
produto = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

for i in range(4):
    for j in range(4):
        produto.append(m[i][j] * a)


for i in range(4): 
    print(m[i])

print(f'Multiplicação: {produto}')