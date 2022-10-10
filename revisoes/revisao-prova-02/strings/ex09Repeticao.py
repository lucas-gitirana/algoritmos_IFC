frase = input("Digite a frase: ").replace(" ", ",").split(",")

contPalavras = 0

for i in frase:
    if (i != ''):
        contPalavras += 1


print("Palavras: ", contPalavras)