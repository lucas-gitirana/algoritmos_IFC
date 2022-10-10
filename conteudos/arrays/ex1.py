import numpy as np

N = 10
vetor = np.zeros(N)

somatorio = 0
maiorValor = 0
indiceMaior = 0
menorValor = 0
indiceMenor = 0

for i in range (N):
    vetor[i] = int(input(f'Informe o valor para V[{i}]: '))
    somatorio += vetor[i]

    if i == 0:
        maiorValor = vetor[i]
        indiceMaior = i
        menorValor = vetor[i]
        indiceMenor = i
    elif vetor[i] > maiorValor:
        maiorValor = vetor[i]
        indiceMaior = i
    elif vetor[i] < menorValor:
        menorValor = vetor[i]
        indiceMenor = i

print("Valores: ", vetor)
print("Somatório: ", somatorio)
print("Média: ", somatorio / N)
print("Maior valor: ", maiorValor)
print("Índice do maior valor: ", indiceMaior)
print("Menor valor: ", menorValor)
print("Índice do menor valor: ", indiceMenor)

############################## TESTE ##############################

# FUNÇÕES PARA RESOLVER O PROBLEMA

#SOMATÓRIO
#print(vetor.sum())

#MÉDIA
#print(vetor.mean())

#MAIOR VALOR
#print(vetor.max())

#MENOR VALOR
#print(vetor.min())

#POSIÇÃO DO MAIOR VALOR
#print(vetor.argmax())

#POSIÇÃO DO MENOR VALOR
#print(vetor.argmin())

