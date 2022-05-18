codigo = int(input("Código: "))

if codigo == 1:
    classificacao = "Aliemento não-perecível"
elif codigo > 1 and codigo <= 4:
    classificacao = "Alimento perecível"
elif codigo > 4 and codigo <= 6:
    classificacao = "Vestuário"
elif codigo == 7:
    classificacao = "Higiene pessoal"
elif codigo > 7 and codigo <= 15:
    classificacao = "Limpeza e utensílios domésticos"
else:
    classificacao = "Inválido"

print(classificacao)