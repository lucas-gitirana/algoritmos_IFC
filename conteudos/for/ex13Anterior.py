maiorTurma = 0
menorTurma = 0
somaAlturaMulheres = 0
contMulheres = 0
somaAlturaTurma = 0

for fichas in range(1, 11):
    print("REPETIÇÃO ", fichas)
    altura = float(input("Altura: "))
    sexo = input("Sexo (M ou F): ")

    somaAlturaTurma += altura

    if fichas == 1:
        maiorTurma = altura
        menorTurma = altura
    else:
        if altura > maiorTurma:
            maiorTurma = altura
        elif altura < menorTurma:
            menorTurma = altura
    
    if sexo == 'F' or sexo == 'f':
        somaAlturaMulheres += altura
        contMulheres += 1


print("Maior altura da turma: ", maiorTurma)
print("Menor altura da turma: ", menorTurma)
print("Média de altura das mulheres: ", somaAlturaMulheres / contMulheres)
print("Média de altura da turma: ", somaAlturaTurma / fichas)

