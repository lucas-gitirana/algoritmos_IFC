anoNasc = int(input("Ano de nascimento: "))

if 2022 - anoNasc >= 16 and 2022 - anoNasc >= 18:
    print("Você tem idade para votar e dirigir")
elif 2022 - anoNasc >= 16 and 2022 - anoNasc < 18:
    print("Você pode votar mas não pode dirigir")
else:
    print("Você não pode votar nem dirigir")