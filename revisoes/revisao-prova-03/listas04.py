a = []
b = []
produto = []

print('Lista A: ')
for i in range(5):
    a.append(int(input(f'Informe um valor para a posição {i}: ')))

print('Lista B:')
for i in range(5):
    b.append(int(input(f'Informe um valor para a posição {i}: ')))

#PRODUTO DA PRIMEIRA PELO INVERSO DA SEGUNDA
for i in range(len(a)):
    produto.append(a[i] * b[(len(a) - 1) - i])

print(f'A: {a}')
print(f'B: {b}')
print(f'Produto de A pelo inverso de B: {produto}')