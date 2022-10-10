idade = int(input("Idade: "))
sexo = input("Sexo (M ou F): ")

if idade >= 0 and idade <= 12:
    if sexo == 'F':
        print("Menina")
    else:
        print("Menino")
elif idade <= 24:
    if sexo == 'F':
        print("Moça")
    else:
        print("Rapaz")
else:
    if sexo == 'F':
        print("Mulher")
    else:
        print("Homem")

    

