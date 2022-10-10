data = input("Data: ").split("/")

meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto'
, 'setembro', 'outubro', 'novembro', 'dezembro']

print("Você nasceu em ", data[0], "de ", meses[int(data[1]) - 1], "de ", data[2])