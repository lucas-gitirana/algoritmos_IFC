anoNasc = int(input("Ano de nascimento: "))

if 2022 - anoNasc >= 16:
    votar = "permitido"
    
    if 2022 - anoNasc >= 18:
        habilitacao = "permitido"
    else:
        habilitacao = "não permitido"
else:
    votar = "não permitido"
    habilitacao = "não permitido"

print("Idade para votar: ", votar)
print("Idade para dirigir: ", habilitacao)