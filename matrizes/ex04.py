import numpy as np

matriz = np.zeros((5,5))
somaLinha4 = 0

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Informe um valor para linha {i} e coluna {j}: "))

        if i == 3:
            somaLinha4 += matriz[i][j]

print(f"Soma da linha 4: ", somaLinha4)