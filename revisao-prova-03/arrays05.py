import numpy as np

x = np.zeros(10)

for i in range(len(x)):
    x[i] = int(input(f'Informe um valor para a posição {i}: '))

print(f'Vetor: ', x)
print(f'O maior valor é {x.max()} e sua posição é {x.argmax()}')
print(f'O menor valor é {x.min()} e sua posição é {x.argmin()}')
