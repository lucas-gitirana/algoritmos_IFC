""" Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO. A seguir ler
um vetor A de 10 elementos inteiros contendo uma aposta. A seguir imprima quantos
pontos fez o apostador. """

pontos = 0
resultado = []
aposta = []

for i in range(5):
    valor = int(input("Resultado: "))
    resultado.append(valor)

for i in range(10):
    valor = int(input("Valor: "))
    aposta.append(valor)

for i in range(len(resultado)):
    for j in range(len(aposta)):
        if aposta[j] == resultado[i]:
            pontos+=1
        
print("Você fez ", pontos, " ponto(s)!")