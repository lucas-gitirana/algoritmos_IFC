matriz_a = []
matriz_b = []
soma = []

# PEDINDO O TAMANHO DAS MATRIZESnxn
n = int(input('Informe o tamanho das matrizes: '))

# PREENCHENDO A MATRIZ A
for i in range(n):
    linha = []
    for j in range(2):
        valor = int(input(f'Informe um valor para A{i + 1}{j + 1}: '))
        linha.append(valor)
    
    matriz_a.append(linha)

# PREENCHENDO A MATRIZ B
for i in range(n):
    linha = []
    for j in range(2):
        valor = int(input(f'Informe um valor para B{i + 1}{j + 1}: '))
        linha.append(valor)
    
    matriz_b.append(linha)

# CALCULANDO A SOMA DAS MATRIZES
for i in range(n):
    linha = []
    for j in range(n):
        valorSoma = matriz_a[i][j] + matriz_b[i][j]
        linha.append(valorSoma)
    
    soma.append(linha)

# APRESENTAÇÃO
print(f'Matriz A: ')
for i in range(n):
    print(matriz_a[i])

print(f'Matriz B: ')
for i in range(n):
    print(matriz_b[i])

print(f'Soma das matrizes: ')
for i in range(n):
    print(soma[i])


