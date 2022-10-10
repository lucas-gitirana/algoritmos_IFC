x = set()
y = set()

print('LISTA X')
for i in range(10):
    valor = int(input("Informe o valor: "))
    x.add(valor)

print('LISTA Y')
for i in range(10):
    valor = int(input("Informe o valor: "))
    y.add(valor)

diferenca = x - y


print("Diferença: ", diferenca)