dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

diasSoma = int(input("Dias a serem somados: "))

if diasSoma >= 365:
    somaAnos = diasSoma // 365


if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10):
    if (dia + diasSoma) <= 31:
        print((dia + diasSoma), mes, ano)
    else:
        diferenca = (dia + diasSoma) - 31        
        print((diferenca), mes + 1, ano)

elif (mes == 2):
    if (dia + diasSoma) <= 28:
        print((dia + diasSoma), mes, ano)
    else:
        diferenca = (dia + diasSoma) - 28
        print((diferenca), mes + 1, ano)

elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    if (dia + diasSoma) <= 30:
        print((dia + diasSoma), mes, ano)
    else:
        diferenca = (dia + diasSoma) - 30
        print((diferenca), mes + 1, ano)

elif (mes == 12):
    if (dia + diasSoma) <= 31:
        print((dia + diasSoma), mes, ano)
    else:
        diferenca = (dia + diasSoma) - 31

        if diferenca <= 31:
            print(diferenca, (mes + 1) - mes, ano + 1)      
        else:
            print(diferenca, (diferenca // 31), ano + 1)



