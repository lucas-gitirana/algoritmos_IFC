# EXERCÍCIO 02
import numpy as np

vetor = []

for i in range(9):
    vetor.append(int(input(f'Informe um valor para a posição {i}: ')))

""" for i in range(len(vetor)):
    divisores = 0
    for numIntervalo in range(1, vetor[i]):
        if vetor[i] % numIntervalo == 0:
            divisores += 1
    
    if divisores == 2: """
        

for numero in vetor:
    divisores = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores += 1
        
    if divisores == 2:
        print(f'O número {vetor[i]} é primo e sua posição é {i}')

