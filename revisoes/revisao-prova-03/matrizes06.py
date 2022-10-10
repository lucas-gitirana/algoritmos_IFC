n = int(input('Informe o tamanho das duas matrizes Mnxn: '))

a = []
b = []
c = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input(f'Informe um valor para A{i}{j}: ')))
    a.append(linha)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input(f'Informe um valor para B{i}{j}: ')))
    b.append(linha)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(a[i][j] + b[i][j])
    c.append(linha)

for i in range(n):
    print(c[i])

