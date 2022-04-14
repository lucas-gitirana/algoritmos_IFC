deposito = float(input("Informe o valor do depósito: "))
taxa_juros = float(input("Informe o valor da taxa de juros anual: "))

rendimento = deposito * taxa_juros / 100
total = deposito + rendimento

print("O valor do rendimento é " ,rendimento, " e o valor total é ",total)
