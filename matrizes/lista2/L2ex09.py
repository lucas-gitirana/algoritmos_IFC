import linecache


a = []
b = []
c = []

n = int(input('Informe o tamanho das DUAS MATRIZES: '))

#PREENCHENDO AS MATRIZES
print('MATRIZ A')
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Informe um valor para A{i}{j}: '))
        linha.append(valor)
    a.append(linha)

print('MATRIZ B')
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Informe um valor para B{i}{j}: '))
        linha.append(valor)
    b.append(linha)

# MULTIPLICANDO AS MATRIZES

# PEGA A LINHA DA MATRIZ A
linhaA = []

for i in range(n):
    linhaA = a[i]

    # PEGA A COLUNA DA MATRIZ B
    linhaC = []
    for x in range(n):
        colunaB = []        
        acumulador = 0
        for y in range(n):          
            colunaB.append(b[y][x])

            acumulador += linhaA[y] * colunaB[y]
        
        linhaC.append(acumulador)

    c.append(linhaC)

    """ linhaC = []
    for x in range(len(linhaA)):
        acumulador += linhaA[x] * colunaB[x] """
    
    
    """ c.append(linhaC) """

print(c)


