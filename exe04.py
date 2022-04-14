salario = float(input("Informe o salário: "))
valor_cheque01 = float(input("Informe o valor do primeiro cheque: "))
valor_cheque02 = float(input("Informe o valor do segundo cheque: "))

saldo_atual = salario - valor_cheque01 - (valor_cheque01 * 0.38 / 100) - valor_cheque02 - (valor_cheque02 * 0.38 / 100) 

print("O saldo atual é: ", saldo_atual)