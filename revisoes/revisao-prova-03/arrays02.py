import numpy as np

vetor = np.zeros(5)
somatorio = 0

for i in range(5):
    vetor[i] = int(input(f'Informe um valor para a posição {i}: '))
    somatorio += vetor[i]

print('Vetor: ', vetor)
print('Somatório: ', somatorio)