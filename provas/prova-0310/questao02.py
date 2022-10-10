a = []
menoresQueZero = []
posicoes = []
contMenores = 0

for i in range(10):
    a.append(int(input(f'Informe um valor para a posição {i}: ')))

    if a[i] <= 0:
        contMenores += 1
        menoresQueZero.append(a[i])
        posicoes.append(i)
    
if contMenores == 0:
    print('Não há números menores ou iguais a zero na estrutura.')
else:
    print('=== NÚMEROS MENORES OU IGUAIS A ZERO ===')
    for i in range(len(menoresQueZero)):
        print('------------------')
        print(f'Número: {menoresQueZero[i]}')
        print(f'Posição: {posicoes[i]}')