#IMPORTANDO UM ARRAY
import numpy as np

#INICIALIZANDO UM ARRAY
N = 10
vetor = np.zeros(N)

# mostra o tipo da estrutura
print(type(vetor))

 # somatório
soma2 = vetor.sum()

# média
media = vetor.mean() 

# desvio padrão
desvio = vetor.std() 

# o maior valor
max = vetor.max() 

# o menor valor
min = vetor.min() 

# retorna a posição que contém o maior valor da estrutura
argmax = vetor.argmax() 

# retorna a posição que contém o menor valor da estrutura
argmin = vetor.argmin() 