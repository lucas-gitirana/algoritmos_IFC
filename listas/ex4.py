# Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo inverso da segunda lista.

x = []
y = []
produto = []

print("LISTA X: ")
for i in range(5):
    x.append(int(input("Informe um valor: ")))

print("LISTA Y: ")
for i in range(5):
    y.append(int(input("Informe um valor: ")))

for i in range(5):
    produto.append(x[i] * y[4- i])

""" for i in range(len(x)):
    produto.append(x[i] * y[len(x)-1 - i]) """

print(produto)