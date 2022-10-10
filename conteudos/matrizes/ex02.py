import numpy as np

matriz = np.zeros((5,5))

for j in range(5):
    for i in range(5):
        matriz[i][j] = int(input(f"Informe um valor para a linha {i} e coluna {j}: "))

print(matriz)