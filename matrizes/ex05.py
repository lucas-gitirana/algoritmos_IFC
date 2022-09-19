import numpy as np

matriz = np.zeros((10,10))
somaColuna2 = 0
somaDiagonal = 0

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f'Informe um valor para linha {i} e coluna {j}: '))

        if j == 1:
            somaColuna2 += matriz[i][j]

        if i == j:
            somaDiagonal += matriz[i][j]

print(f'Soma da coluna 2: {somaColuna2}')
print(f"Soma da diagonal principal: {somaDiagonal}")