""" Faça um programa que preencha dois vetores de dez elementos numéricos cada um e
mostre o vetor resultante da intercalação deles: 


se o indice é par, coloca vetor A
se o indice é impar, coloca vetor B

"""

v1 = []
v2 = []
intercalacao = []

print('LISTA 1')
for i in range(10):
    valor = int(input("Valor: "))
    v1.append(valor)

print('LISTA 2')
for i in range(10):
    valor = int(input("Valor: "))
    v2.append(valor)

for i in range(10):
        if i % 2 == 0:
            intercalacao.append(v2[i])
        else:
            intercalacao.append(v1[i])

print(intercalacao)
