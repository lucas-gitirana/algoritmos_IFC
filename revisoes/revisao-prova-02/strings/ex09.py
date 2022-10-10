frase = input("Frase: ").upper().replace(" ", ",").split(",")
contPalavras = 0
print(frase)

for i in range(len(frase)):
    if frase[i] != '':
        print(frase[i])
        contPalavras += 1

print("Número de palvras: ", contPalavras)


