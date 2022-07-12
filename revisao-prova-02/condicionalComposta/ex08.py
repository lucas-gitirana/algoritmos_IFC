codigo = int(input("Código do produto: "))

if codigo == 1:
    classificacao = 'Alimento não-perecível'
elif codigo > 1 and codigo <= 4:
    classificacao = 'Alimento perecível'
elif codigo == 5 or codigo == 6:
    classificacao = 'Vestuário'
elif codigo == 7:
    classificacao = 'Higiene pessoal'
else:
    classificacao = 'Código inválido'


print(classificacao)