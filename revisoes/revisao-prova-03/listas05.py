a = []
b= []
c = []

print('LISTA A: ')
for i in range(5):
    a.append(int(input(f'Informe um valor para a posição {i}: ')))

print('LISTA B: ')
for i in range(5):
    b.append(int(input(f'Informe um valor para a posição {i}: ')))

c = a + b

print(f'A: {a}')
print(f'B: {b}')
print(f'C: {c}')