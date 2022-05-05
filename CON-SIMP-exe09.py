etiqueta = float(input("Informe o preço da etiqueta: "))
codigo = int(input("Digite o código de condição de pagamento: "))

if codigo == 1:
    preco = etiqueta * 0.85

if codigo == 2:
    preco = etiqueta * 0.90

if codigo == 3:
    preco = etiqueta

if codigo == 4:
    preco = etiqueta * 1.10

print("Preço final: ", preco)