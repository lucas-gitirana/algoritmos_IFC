import numpy as np

m = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        valor = int(input(f"Informe um valor para a linha {i} e a coluna {j}: "))
        m[i][j] = valor

print(m)