import numpy as np

m = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        m[i][j] = int(input(f'Informe um valor para m{i}{j}: '))

for i in range(5):
    print(m[i])

