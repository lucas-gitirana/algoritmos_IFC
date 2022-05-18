valorSal = float(input("Valor do salário: "))
valorConta1 = float(input("Valor conta 01: "))
valorConta2 = float(input("Valor conta 02: "))

restante = valorSal - (valorConta1 * 1.02) - (valorConta2 * 1.02)

print("Quanto restará de salário: ", restante)