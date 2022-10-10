# LUCAS EMANOEL GITIRANA

salario = float(input("Salário: "))

if salario > 1100:
    aumento = 0.1 * salario
else:
    aumento = 0.15 * salario

print("Valor do aumento: ", aumento)
print("Salário final: ", salario + aumento)