matriz = []
v = []

# PREENCHENDO A MATRIZ
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input("Informe um valor: ")))

    matriz.append(linha)

# PREENCHENDO A VARIÁVEL "A"
a = int(input("Informe um valor para a variável A: "))

# MULTIPLICAÇÃO DE CADA VALOR DA MATRIZ PELA VARIÁVEL
for i in range(4):
    multiplicacao = 0
    for j in range(4):
        multiplicacao = matriz[i][j] * a
        v.append(multiplicacao)

# APRESENTAÇÃO
print('Multiplicação da matriz por A: ', v)
