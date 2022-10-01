import numpy as np

vetor = np.zeros(5)

for i in range(len(vetor)):
    vetor[i] = int(input(f'Informe um valor para a posição {i}: '))

print('Vetor: ', vetor)
print('Média do vetor: ', vetor.mean())