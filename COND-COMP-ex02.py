nasc = int(input("Ano de nascimento: "))

if 2022 - nasc >= 16:
    print("Você já tem idade para votar")
    if 2022 - nasc >= 18:
        print("Você já pode dirigir")
    else:
        print("Voê não pode dirigir.")    
else: 
    print("Você não tem idade para votar nem dirigir")    
