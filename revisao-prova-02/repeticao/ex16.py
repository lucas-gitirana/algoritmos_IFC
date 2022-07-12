n = int(input("Número de alunos: "))

x = 1
while x <= n:
    av1 = float(input("Avaliação 1: "))
    av2 = float(input("Avaliação 2: "))
    
    somaTrabalho = 0
    for i in range(1, 5):
        print("Trabalho ", i)
        trabalho = float(input("Trabalho : "))
        somaTrabalho += trabalho

    mt = somaTrabalho / 4

    mediaSemestral = 0.3 * av1 + 0.3 * av2 + 0.4 * mt

    if mediaSemestral >= 7:
        print("Aluno aprovado com média ", mediaSemestral)
    else:
        print("Aluno reprovado com média ", mediaSemestral)
    
    x+=1