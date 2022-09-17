gabarito = set([1, 2, 3, 4, 5])
aposta = set()

for i in range(10):
    valor = int(input("Aposte um número: "))
    aposta.add(valor)

resultado = gabarito & aposta
print("Você acertou os números", resultado, " e fez ", len(resultado), "ponto(s).")

# COMO FAZER COM TUPLAS: 

""" gabarito = (1, 2, 3, 4, 5)
aposta = []

cont = 0

for i in range(10):
    valor = int(input("Aposte um número: "))
    aposta.append(valor)

    if valor in gabarito:
        cont += 1

print("Resultado: ", cont, " pontos.") """
