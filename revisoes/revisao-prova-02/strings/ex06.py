frase = input("Frase: ").upper().replace(" ", "")
palavraInvertida = ""

for i in range(len(frase) - 1, -1, -1):
    palavraInvertida += frase[i]

if palavraInvertida == frase:
    print("A frase é um palíndromo")



