etiqueta = float(input("Informe o preço da etiqueta: "))
codigo = int(input("Digite o código de condição de pagamento: "))

if codigo == 1:
    preco = etiqueta * 0.85
    condicao = "À vista em dinheiro, débito ou pix"
    parcelas = preco

if codigo == 2:
    preco = etiqueta * 0.90
    condicao = "À vista no cartão de crédito"
    parcelas = preco

if codigo == 3:
    preco = etiqueta
    condicao = "Em duas vezes"
    parcelas = preco / 2

if codigo == 4:
    preco = etiqueta * 1.10
    condicao = "Em três vezes"
    parcelas = preco / 3

print("O preço final é ", preco, " e a condição de pagamento é: ", condicao, ", com parcela(s) de R$ ", parcelas)