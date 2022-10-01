x = []

for i in range(10):
    x.append(int(input(f'Informe um valor para a posição {i}: ')))

for i in range(len(x)):
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i

print(f'Lista final: {x}')