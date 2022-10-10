import numpy as np

vetor = np.zeros(5)

for i in range(len(vetor)):
    vetor[i] = int(input(f'Informe um valor para a posição {i}: '))

print('Vetor: ', vetor)
print(f'Maior valor do vetor: {vetor.max()}')
print(f'Menor valor do vetor: {vetor.min()}')