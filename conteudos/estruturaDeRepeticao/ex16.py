n = int(input("Número de alunos: "))

x = 1

while x <= n:

    av1 = float(input("Avaliação 1: "))
    av2 = float(input("Avaliação 2: "))

    t1 = float(input("Trabalho 1: "))
    t2 = float(input("Trabalho 2: "))
    t3 = float(input("Trabalho 3: "))
    t4 = float(input("Trabalho 4: "))

    mt = (t1 + t2 + t3 + t4) / 4
    ms = 0.3 * av1 + 0.3 * av2 + 0.4 * mt

    if ms >= 7:
       print('Aprovado')
    else:
       print('Em recuperação final') 

    x += 1