""" Faça uma sub-rotina que receba como parâmetro uma matriz(lista 
de lista) A[5][5] e retorne a soma de todos os seus elementos. """

def soma(m):
    soma_elementos = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma_elementos += m[i][j]
    
    return soma_elementos

print('OLÁ!')
print('----- Enunciado: -----')
print('Faça uma sub-rotina que receba como parâmetro uma matriz(lista de lista) A[5][5] e retorne a soma de todos os seus elementos. ')
print('----------------------------------------------------------------------------------')

matriz = []
tam = int(input('Tamanho da matriz quadrada: '))

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(int(input(f'A{i}{j}: ')))
    matriz.append(linha)

print('=======MATRIZ ORIGINAL:=======')
for i in range(len(matriz)):
    print(matriz[i])

print('=======SOMA DE TODOS OS ELEMENTOS=======')
print(soma(matriz))