import numpy as np

x = np.zeros(10)
y = np.zeros(10)
diferenca = []

contIguais = 0

print('LISTA X')
for i in range(len(x)):
    x[i] = int(input("Informe o valor: "))

print('LISTA Y')
for i in range(len(y)):
    y[i] = int(input("Informe o valor: "))

for i in range(len(x)):
    contIguais = 0

    """ ## PODERIA USAR
    if x[i] not in y[i]:
        diferenca.append(x[i]) """
        
    for j in range(len(y)):
        if x[i] == y[j]:
            contIguais += 1            
    if contIguais == 0:
        diferenca.append(x[i])

print("Diferença: ", diferenca)