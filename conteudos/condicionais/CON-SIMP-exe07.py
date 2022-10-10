sexo = input("Informe o sexo (F e M): ")
altura = float(input("Informe a altura: "))

if sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7

if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58

print("O peso ideal é: ", pesoIdeal)