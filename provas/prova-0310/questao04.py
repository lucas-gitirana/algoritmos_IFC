vetor = []
matriz = []

print('-----VETOR-----')
for i in range(3):
    vetor.append(int(input(f'Informe um valor para a posição {i}: ')))

print('-----MATRIZ-----')
for i in range(3):
    linha = []
    for j in range(4):
        linha.append(int(input(f'Informe um valor para A{i}{j}: ')))
    matriz.append(linha)

print('-------------------------------------')
print('Matriz original:')
for i in range(3):
        print(matriz[i])   
print('Vetor original: ', vetor)

# TROCA DE VALORES
for i in range(3):
    aux = vetor[i]
    vetor[i] = matriz[i][1]
    matriz[i][1] = aux

print('-------------------------------------')
print('Matriz modificada:')
for i in range(3):
        print(matriz[i])  
print('Vetor modificado: ', vetor)