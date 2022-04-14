# ENTRADA
sal_base = float(input("Informe o salário base: "))

# PROCESSAMENTO
gratificacao = sal_base * 0.05
imposto = sal_base * 0.07
sal_final = sal_base + gratificacao - imposto 

#SAÍDA
print("O salário final é: ", sal_final)