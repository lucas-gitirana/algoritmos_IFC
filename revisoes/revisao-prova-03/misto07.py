k = []

for i in range(20):
    k.append(input(f'Informe um valor para a posição {i}: '))

print(f'Vetor original: {k}')

for i in range(6):
    if i < 5:
        if i % 2 != 0:
            aux = k[i]
            k[i] = k[i + 1]
            k[i + 1] = aux
    
print(f'Vetor modificado: {k}')
