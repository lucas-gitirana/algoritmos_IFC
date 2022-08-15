num = int(input("Valor: "))

penultimo = 0
ultimo = 1

atual = penultimo + ultimo
print (atual)


while num > atual:
    atual = penultimo + ultimo

    if atual <= num:
        print(atual)

    penultimo = ultimo
    ultimo = atual

