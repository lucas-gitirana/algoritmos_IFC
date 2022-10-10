from audioop import mul

vetor = []
matriz = []
resultado = []

#PREENCHENDO A LISTA
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f'Informe um valor para A{i}{j}: '))
        linha.append(valor)    
    matriz.append(linha)

# PREENCHENDO O VETOR
for i in range(2):
    valor = int(input(f'Informe um valor para a posição {i}: '))
    vetor.append(valor)

# MULTIPLICANDO O VETOR PELA MATRIZ
for i in range(2):
    linha = []
    for j in range(2):
        multiplicacao = vetor[i] * matriz[i][j]
        linha.append(multiplicacao)
    resultado.append(linha)

# APRESENTAÇÃO
print(f'Matriz: {matriz}')
print(f'Vetor: {vetor}')
print('Matriz resultado')
for i in range(2):
    print(resultado[i])
