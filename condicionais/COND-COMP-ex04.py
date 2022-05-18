pesoSaco = float(input("Peso do saco de ração (kg): "))
qtdRacao = float(input("Quantidade de ração para cada gato (g): "))

restante = (pesoSaco * 1000) - (qtdRacao * 2 * 5)


print("Após cinco dias de consumo a quantidade de ração restante será de ", restante, "gramas.")