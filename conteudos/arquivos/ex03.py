""" Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem ser armazenados. 
Em seguida, ler do arquivo os valores armazenados copiando-os para uma lista de inteiros e os imprimindo na tela. """

numeros = []

for i in range(5):
    numeros.append(int(input(f'Informe um número para a posição {i}: ')))

nome_arq = input('Qual o nome do arquivo para armazenar os números? ')+".txt"

with open(nome_arq, "w") as arquivo:
    for i in range(len(numeros)):
        arquivo.write(f'{numeros[i]}\n')

lista = []

with open(nome_arq, "r") as arquivo:
    inteiros = arquivo.readlines()
    for i in inteiros:
        lista.append(int(i))
        #lista.append(i)

print('-------------CONTEÚDO DO ARQUIVO-------------')
print(inteiros)
for i in range(len(lista)):
    print(lista[i])

