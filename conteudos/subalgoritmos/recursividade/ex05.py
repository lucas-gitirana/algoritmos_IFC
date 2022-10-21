def simetrica(m):
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != m[j][i]:
                cont += 1
    
    if cont == 0:
        return True
    else:
        return False

matriz = []
tamanho = int(input('Informe o tamanho da matriz: '))

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(int(input(f'Valor para A{i}{j}: ')))
    matriz.append(linha)

print('=====================')
if simetrica(matriz):
    print('Simétrica')
else:
    print('Não simétrica')
#print(simetrica(matriz))


