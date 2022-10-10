somaAlturaMulheres = 0
contMulheres = 0
somaAlturaTurma = 0 

for i in range(4):
    codigo = int(input("Código (1 - M; 2 - F): "))
    altura = float(input("Altura: "))

    somaAlturaTurma += altura

    if i == 0:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        elif altura < menor:
            menor = altura
    
    if codigo == 2:
        contMulheres += 1
        somaAlturaMulheres += altura

print("Maior altura: ", maior)
print("Menor altura: ", menor)
print("Média de altura das mulheres: ", somaAlturaMulheres / contMulheres)
print("Média de altura da turma: ", somaAlturaTurma / (i + 1))