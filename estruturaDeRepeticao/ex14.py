x = 1
contOtimos = 0
diferencaPercentual = 0
somaIdadeRuim = 0
percPessimo = 0
maiorIdadePessimo = 0
maiorIdadeRuim = 0
maiorIdadeOtimo = 0
diferencaIdadeOtimoERuim = 0
contBom = 0
contRegular = 0
contPessimo = 0

while x <= 3:
    
    idade = int(input("Idade: "))
    opiniao = input("Opinião (A,B,C,D,E): ")

    if opiniao == 'a' or opiniao == 'A':
        contOtimos += 1

        if x == 1:
            maiorIdadeOtimo = idade
        else:
            if idade > maiorIdadeOtimo:
                maiorIdadeOtimo = idade
    
    if opiniao == 'B' or opiniao == 'b':
        contBom += 1 

    if opiniao == 'C' or opiniao == 'c':
        contRegular += 1    

    if opiniao == 'D' or opiniao == 'd':
        somaIdadeRuim += idade

        if x == 1:
            maiorIdadeRuim = idade
        else:
            if idade > maiorIdadeRuim:
                maiorIdadeRuim = idade
    
    if opiniao == 'E' or opiniao == 'e':
        contPessimo += 1

        if x == 1:
            maiorIdadePessimo = idade
        else:
            if idade > maiorIdadePessimo:
                maiorIdadePessimo = idade
    

    
    x += 1

diferencaPercentual = ((contBom / (x - 1)) * 100) - ((contRegular / (x - 1)) * 100)
percPessimo = (contPessimo / (x - 1)) * 100
diferencaIdadeOtimoERuim = maiorIdadeOtimo - maiorIdadeRuim
mediaIdadeRuim = somaIdadeRuim / (x - 1)

print("Quantidade de respostas ÓTIMO: ", contOtimos)
print("Diferença percentual entre respostas BOM e REGULAR: ", diferencaPercentual)
print("Média de idade das pessoas que responderam RUIM: ", mediaIdadeRuim)
print("Percentagem de respostas PÉSSIMO: ", percPessimo)
print("Maior idade que utilizou PÉSSIMO: ", maiorIdadePessimo)
print("Diferença entre a maior idade que respondeu ÓTIMO e a maior idade que respondeu RUIM: ", diferencaIdadeOtimoERuim)
