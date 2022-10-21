def inversa(m):
    matriz_inversa = []

    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            linha.append(matriz[j][i])
        matriz_inversa.append(linha)

    return matriz_inversa

matriz = []

tamanho = int(input('Informe o tamanho da matriz quadrada: '))

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(int(input(f'A{i}{j}: ')))
    matriz.append(linha)

print('=========================================')
print('MATRIZ ORIGINAL: ')
for i in range(tamanho):
    print(matriz[i])

print('MATRIZ INVERSA: ')
for i in range(len(inversa(matriz))):
    print(inversa(matriz)[i])

