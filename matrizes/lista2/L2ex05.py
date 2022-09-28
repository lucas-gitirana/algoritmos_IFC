matriz = []
determinante = 0

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f'Informe um valor para a{i}{j}: '))
        linha.append(valor)
    matriz.append(linha)

diagPrincipal = 1
diagSecundaria = 1
determinante = 0
for i in range(2):
    for j in range(2):
        # ENCONTRAR DIAGONAL PRINCIPAL
        if (i - j) == 0:
            diagPrincipal *= matriz[i][j]
        else:
            diagSecundaria *= matriz[i][j]

determinante = diagPrincipal - diagSecundaria

for i in range(2):
    print(matriz[i])

print(f'DETERMINANTE: {determinante}')
