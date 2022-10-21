""" Escreva um programa que preencha um vetor de inteiros 
de 10 posições e solicite ao usuário um valor inteiro 
para ser procurado no vetor. Crie uma função que receba 
como parâmetro o vetor e o número a ser procurado.
 Ao final, retorne quantas vezes o número foi encontrado no vetor.
"""


def procura_vetor(vetor, valor):
    return vetor.count(valor)


vetor = []

for i in range(10):
    vetor.append(int(input(f'Informe um valor para a posição {i}:')))

valor = int(input('Informe um valor inteiro para ser procurado no vetor: '))

print('================')
print(f'Quantidade de vezes que o número aparece na lista: {procura_vetor(vetor, valor)}')

