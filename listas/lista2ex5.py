""" Faça um programa que preencha dois vetores de dez elementos numéricos cada um e
mostre o vetor resultante da intercalação deles: 


se o indice é par, coloca vetor A
se o indice é impar, coloca vetor B

"""
import numpy as np

v1 = []
v2 = []
intercalacao = np.zeros(20)

#PREENCHENDO VETORES
print("VETOR 1")
for i in range(10):
    valor = int(input("Valor: "))
    v1.append(valor)

print("VETOR 2")
for i in range(10):
    valor = int(input("Valor: "))
    v2.append(valor)

#INTERCALANDO VALORES
for i in range(10):
    intercalacao[2 * i] = v1[i]
    intercalacao[(2 * i) + 1] = v2[i]

print("Intercalação: ", intercalacao)

