# CRIANDO ARQUIVOS PARES E IMPARES
with open("pares.txt", "w") as pares, open("impares.txt", "w") as impares:
    for i in range(0,1000):
        if i % 2 == 0:
            pares.write(f'{i}\n')
        else:
            impares.write(f'{i}\n')

# CRIANDO ARQUIVO COM A UNIÃO DOS DOIS ARQUIVOS ACIMA
with open("pares.txt", "r") as pares, open("impares.txt", "r") as impares:
    linhas_pares = pares.readlines()
    linhas_impares = impares.readlines()

    with open("paresimpares.txt", "w") as paresimpares:
        for i in range(len(linhas_pares)):
            paresimpares.write(f'{linhas_pares[i]}')
            paresimpares.write(f'{linhas_impares[i]}')
