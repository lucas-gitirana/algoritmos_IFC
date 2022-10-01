from gettext import npgettext


import numpy as np

m = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        m[j][i] = int(input(f'Informe um valor para m{j}{i}: '))

for i in range(5): 
    print(m[i])

