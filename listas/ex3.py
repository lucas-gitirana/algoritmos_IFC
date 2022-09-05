# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.

x = []
y = []
soma = []

print("LISTA X")
for i in range(5): 
    x.append(int(input("Informe o valor: ")))
    

print("LISTA Y")
for i in range(5): 
    y.append(int(input("Informe o valor: ")))    

for i in range(5):
    soma.append(x[i] + y[i])

print("Soma das listas: ", soma)
print("Concatenação das listas: ", x + y)