pesoSaco = float(input("Peso do saco de ração (kg): "))
qtdRacao = float(input("Quantidade de ração de cada gato (g): "))

restante = (pesoSaco) - ((qtdRacao / 1000) * 2 * 5)

if restante > 0: 
    print("Quanto restará de ração no saco após 5 dias de consumo:", restante)
else:
    print("Não restará nada.")