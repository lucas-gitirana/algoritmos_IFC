peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** (2))

if imc < 18.5:
    condicao = "Abaixo do peso" 

if imc >= 18.5 and imc <= 25:
    condicao = "Peso normal"

if imc > 25 and imc <= 30:
    condicao = "Acima do peso"

if imc > 30:
    condicao = "Obeso"


print("A condição é: ", condicao)