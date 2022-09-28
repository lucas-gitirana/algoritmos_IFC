matriz = []
extendida = []

n = int(input('Informe o tamanho da matriz'))

# PREENCHENDO A MATRIZ
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Informe um valor para a{i}{j}: '))
        linha.append(valor)
    matriz.append(linha)

#CRIANDO A MATRIZ PARA FAZER O DETERMINANTE
for i in range(n):
    linha = []
    for j in range(n + 1):
        
        if j <= n-1:
            linha.append(matriz[i][j])
        else:
            for x in range(2):
                linha.append(matriz[i][x])
    
    extendida.append(linha)

# CALCULAR DETERMINANTE

somaPrincipal = 0
somaSecundaria = 0

for i in range(n + 2):
    for j in range(n + 2):
        if (i == 0) and (j <= n - 1):
            diagPrincipal = 1
            for x in range(n):
                diagPrincipal *= extendida[i+x][j+x]        
            somaPrincipal += diagPrincipal
        
        if (i == n - 1) and (j <= n - 1):
            diagSecundaria = 1
            for x in range(n):
                diagSecundaria *= extendida[i - x][j + x]
            somaSecundaria += diagSecundaria
        
det = somaPrincipal - somaSecundaria

for i in range(n):
    print(extendida[i])

print(f'Determinante: {det}')