x = 1
maior = 0
menor = 0
soma_alt = 0
soma_fem = 0
cont_fem = 0

while x <= 10:
    altura = float(input("Altura: "))    
    sexo = float(input("Sexo (1 para masculino e 2 para feminino): "))

    if(x == 1):
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        elif altura < menor:
            menor = altura
    
    if sexo == 2:
        cont_fem += 1
        soma_fem += altura        
    
    soma_alt += altura

    x+=1

print("Menor altura: ", menor)
print("Maior altura: ", maior)
print("Média de altura das mulheres: ", (soma_fem / cont_fem))
print("Média de altura da turma: ", (soma_alt / 10))