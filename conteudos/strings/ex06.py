entrada = input("Escreva o termo: ")

termo = entrada.replace(" ", "")
testePalindromo = ""

for i in range(len(termo) - 1, -1, -1):
   testePalindromo = testePalindromo + termo[i]

if testePalindromo == termo:
    print("O termo é um palíndromo")
else:
    print("O termo não é um palíndromo")
