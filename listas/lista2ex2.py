""" Faça um programa que preencha um vetor com 9 números inteiros, calcule e
mostre os que são números primos e suas respectivas posições. """

import numpy as np

vetor = []
primos = []
contDivisores = 0

for i in range(9):
    valor = int(input("Valor: "))
    vetor.append(valor)

for i in range(9):
    contDivisores = 0
    for j in range(1, vetor[i] + 1):
        if (vetor[i] % j) == 0:
            contDivisores += 1
    
    if contDivisores == 2:
        print("O número ", vetor[i], "é primo. Ele está na posição ", i)

