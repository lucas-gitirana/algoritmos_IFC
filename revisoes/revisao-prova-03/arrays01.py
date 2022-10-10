from wsgiref.validate import validator
import numpy as np

x = np.zeros(10)

for i in range(10):
    x[i] = int(input(f'Informe um valor para x{i}: '))

print('Vetor final: ', x)
