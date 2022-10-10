qtd_broas = int(input("Quantidade de broas: "))
qtd_paes = int(input("Quantidade de pães: "))

total = qtd_broas * 1.50 + qtd_paes * 0.50
pupanca = total * 0.1

print("O total arrecadado é: R$ ",total)
print("O valor a ser poupado é: R$ ",pupanca)