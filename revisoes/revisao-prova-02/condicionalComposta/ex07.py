codigo = int(input("Código do funcionário: "))
salario = float(input("Salário atual: "))

if codigo == 1:
    cargo = 'Escriturário'
    valorAumento = salario * 0.5
    novoSal = salario + valorAumento
elif codigo == 2:
    cargo = 'Secretário'
    valorAumento = salario * 0.35
    novoSal = salario + valorAumento
elif codigo == 3:
    cargo = 'Caixa'
    valorAumento = salario * 0.2
    novoSal = salario + valorAumento
elif codigo == 4:
    cargo = 'Gerente'
    valorAumento = salario * 0.1
    novoSal = salario + valorAumento
elif codigo == 5:
    cargo = 'Diretor'
    valorAumento = 0
    novoSal = salario
else:
    print("Código inválido")
    cargo = ''
    valorAumento = 0
    novoSal = 0

print(cargo)
print("Valor do aumento: ", valorAumento)
print("Novo salário: ", novoSal)