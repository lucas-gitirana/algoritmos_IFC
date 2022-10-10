contOtimo = 0 
contBom = 0
contRegular = 0
contRuim = 0
somaIdadeRuim = 0 
contPessimo = 0
maiorIdadePessimo = 0
maiorIdadeOtimo = 0
maiorIdadeRuim = 0

for i in range(5):
    idade = int(input("Idade: "))
    opiniao = input("Opinião: ")

    if opiniao == 'A':
        contOtimo += 1

        if contOtimo == 1:
            maiorIdadeOtimo = idade
        elif contOtimo > 1:
            if idade > maiorIdadeOtimo:
                maiorIdadeOtimo = idade
        else:
            maiorIdadeOtimo = 0

    elif opiniao == 'B':
        contBom += 1
    elif opiniao == 'C':
        contRegular += 1
    elif opiniao == 'D':
        contRuim += 1
        somaIdadeRuim += idade

        if contRuim == 1:
            maiorIdadeRuim = idade
        elif contRuim > 1:
            if idade > maiorIdadeRuim:
                maiorIdadeRuim = idade
        else:
            maiorIdadeRuim = 0

    elif opiniao == 'E':
        contPessimo += 1

        if contPessimo == 1:
            maiorIdadePessimo = idade
        elif contPessimo > 1:
            if idade > maiorIdadePessimo:
                maiorIdadePessimo = idade
        else:
            maiorIdadePessimo = 0

percBom = (contBom / (i + 1)) * 100
percRegular = (contRegular / (i + 1)) * 100


print("Quantidade de respostas ÓTIMO: ", contOtimo)
print("Diferença perncentual entre BOM e REGULAR: ", percBom - percRegular)
print("Média de idade das pessoas que responderam ruim: ", somaIdadeRuim / contRuim)
print("Percentagem de repostas PÉSSIMO: ", (contPessimo / (i + 1)) * 100)
print("Maior idade que respondeu péssimo: ", maiorIdadePessimo)
print("Diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim: ", maiorIdadeOtimo - maiorIdadeRuim)
    