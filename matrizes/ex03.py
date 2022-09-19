import numpy as np

matriz = np.zeros((5,5))
diagonal = []

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Informe um valor para linha {i} e coluna {j}: "))

for i in range(5):
    for j in range(5):
        if i == j:
            diagonal.append(matriz[i][j])

print(f'Diagonal principal: ', diagonal)
