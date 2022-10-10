matricula = int(input("Número de matrícula: "))
prova1 = float(input("Nota da prova 01: "))
prova2 = float(input("Nota da prova 02: "))
prova3 = float(input("Nota da prova 03: "))
notaExercicios = float(input("Nota de exercícios: "))

mediaPonderada = (prova1 + (prova2 * 2) + (prova3 * 2) + notaExercicios) / 6

if mediaPonderada >= 9:
    conceito = "A"
    situacao = "Aprovado"

if mediaPonderada >= 7.75 and mediaPonderada < 9:
    conceito = "B" 
    situacao = "Aprovado"

if mediaPonderada >= 6 and mediaPonderada < 7.75:
    conceito = "C"
    situacao = "Aprovado"

if mediaPonderada >= 4 and mediaPonderada < 6:
    conceito = "D"
    situacao = "Reprovado"

if mediaPonderada < 4:
    conceito = "E"
    situacao = "Reprovado"

print("O aluno com matrícula ", matricula, " obteve o conceito", conceito, "e está ", situacao)