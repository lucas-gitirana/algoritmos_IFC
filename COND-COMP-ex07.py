codigo = int(input("Código: "))
sal = float(input("salário: "))

if codigo == 1:
    cargo = "Escriturário"
    aumento = sal * 0.5
    salNovo = sal + aumento
elif codigo == 2:
    cargo = "Secretária"
    aumento = sal * 0.35
    salNovo = sal + aumento
elif codigo == 3:
    cargo = "Caixa"
    aumento = sal * 0.2
    salNovo = sal + aumento
elif codigo == 4:
    cargo = "Gerente"
    aumento = sal * 0.1
    salNovo = sal + aumento
else:
    cargo = "Diretor"
    aumento = 0
    salNovo = sal + aumento

print("Seu cargo é: " + cargo)
print("O aumento foi de : R$ ", aumento)
print("Seu novo salário é: ", salNovo)
