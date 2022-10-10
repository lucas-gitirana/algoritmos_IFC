a = []
b = []
soma = []

print('Lista A: ')
for i in range(5):
    a.append(int(input(f'Informe um valor para a posição {i}: ')))

print('Lista B:')
for i in range(5):
    b.append(int(input(f'Informe um valor para a posição {i}: ')))

for i in range(len(a)):
    soma.append(a[i] + b[i])

print('Lista A', a)
print('Lista B', b)
print('Soma das listas: ', soma)