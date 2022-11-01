with open("pares.txt", "r") as pares:
    linhas_pares = pares.readlines()

with open("pares2.txt", "w") as pares:
    for i in range(len(linhas_pares)-1, -1, -1):
        pares.write(linhas_pares[i])