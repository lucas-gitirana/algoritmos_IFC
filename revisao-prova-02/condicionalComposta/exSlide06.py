dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

diasParaSomar = int(input("Dias a serem somados: "))

jan = 31
fev = jan + 28
mar = fev + 31
abr = mar + 30
maio = abr + 31
jun = maio + 30
jul = jun + 31
ago = jul + 31
sete = ago + 30
out = sete + 31
nov = out + 30
dez = nov + 31

#ACHAR QUAL O DIA DO ANO DA DATA DIGITADA
if mes == 1:
    diaDoAno = dia
elif mes == 2:
    diaDoAno = dia + jan
elif mes == 3:
    diaDoAno = dia + fev
elif mes == 4:
    diaDoAno = dia + mar
elif mes == 5:
    diaDoAno = dia + abr
elif mes == 6:
    diaDoAno = dia + maio
elif mes == 7:
    diaDoAno = dia + jun
elif mes == 8:
    diaDoAno = dia + jul
elif mes == 9:
    diaDoAno = dia + ago
elif mes == 10:
    diaDoAno = dia + sete
elif mes == 11:
    diaDoAno = dia + out
elif mes == 12:
    diaDoAno = dia + nov

print("Dia do ano: ", diaDoAno)

soma = diasParaSomar + diaDoAno


if soma > 365:
    ano += soma // 365
    soma = soma % 365
    print("Resto da divisão: ", soma)
    print(ano)

if soma < jan:
    mes = 1
    dia = soma
elif soma < fev: 
    mes = 2
    dia = soma - jan
elif soma < mar:
    mes = 3
    dia = soma - fev
elif soma < abr:
    mes = 4
    dia = soma - mar
elif soma < maio:
    mes = 5
    dia = soma - abr
elif soma < jun:
    mes = 6
    dia = soma - maio
elif soma < jul:
    mes = 7
    dia = soma - jun
elif soma < ago:
    mes = 8
    dia = soma - jul
elif soma < sete:
    mes = 9
    dia = soma - ago
elif soma < out:
    mes = 10
    dia = soma - sete
elif soma < nov:
    mes = 11
    dia = soma - out
elif soma < dez:
    mes = 12
    dia = soma - nov



print(dia,"/",mes,"/", ano)

