codigo = int(input("Código: "))
salario = float(input("Salário: "))

if codigo == 1:
    cargo = "Escriturário"
    aumento = salario * 0.5
    novoSalario = salario + aumento
elif codigo == 2:
    cargo = "Secretário"
    aumento = salario * 0.35
    novoSalario = salario + aumento
elif codigo == 3:
    cargo = "Caixa"
    aumento = salario * 0.20
    novoSalario = salario + aumento
elif codigo == 4:
    cargo = "Gerente"
    aumento = salario * 0.10
    novoSalario = salario + aumento
elif codigo == 5:
    cargo = "Diretor"
    aumento = 0
    novoSalario = salario + aumento
else:
    print("Código inválido")

print("Cargo: ", cargo)
print("Aumento: ", aumento)
print("Novo salário: ", novoSalario)