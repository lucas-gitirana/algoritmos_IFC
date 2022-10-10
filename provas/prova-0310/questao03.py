import numpy as np

array = np.zeros(18)
maiorValor = 0
menorValor = 0
posMaior = 0
posMenor = 0

for i in range(len(array)):
    array[i] = int(input(f'Informe um valor para a posição {i}: '))

for i in range(len(array)):
    if i == 0:
        maiorValor = array[i]
        posMaior = i
        menorValor = array[i]
        posMenor = i
    elif array[i] > maiorValor:
        maiorValor = array[i]
        posMaior = i
    elif array[i] < menorValor:
        menorValor = array[i]
        posMenor = i

print('------------------')
print(f'Array: ', array)
print(f'O maior valor é {maiorValor} e sua posição é {posMaior}')
print(f'O menor valor é {menorValor} e sua posição é {posMenor}')