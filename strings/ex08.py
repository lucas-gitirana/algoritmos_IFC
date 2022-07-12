palavra = input("Digite uma palavra: ")

palavraParcial = ""

for i in palavra:

    if i not in palavraParcial:
        print(i, ": ", palavra.count(i), "x")

    palavraParcial = palavraParcial + i