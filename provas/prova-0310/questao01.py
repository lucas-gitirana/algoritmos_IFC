a = []
b = []
aInversa = []
bInversa = []

print('A: ')
for i in range(3):
    a.append(int(input(f'Informe um valor para a posição {i}: ')))

print('B: ')
for i in range(3):
    b.append(int(input(f'Informe um valor para a posição {i}: ')))

# APRESENTANDO EM ORDEM INVERSA
for i in range(3):
    aInversa.append(a[2 - i])
    bInversa.append(b[2 - i])

print('-------------------------------')
print('Vetores originais:')
print('A: ', a)
print('B: ', b)
print('-------------------------------')
print('Vetores invertidos:')
print('A: ', aInversa)
print('B: ', bInversa)

