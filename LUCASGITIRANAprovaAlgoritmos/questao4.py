# LUCAS EMANOEL GITIRANA

capacidade = float(input("Capacidade do elevador em quilos: "))
p1 = float(input("Peso da pessoa 01: "))
p2 = float(input("Peso da pessoa 02: "))
p3 = float(input("Peso da pessoa 03: "))
p4 = float(input("Peso da pessoa 04: "))
p5 = float(input("Peso da pessoa 05: "))

if (p1 + p2 + p3 + p4 + p5) <= capacidade:
    status = "Liberado para subir"
else:
    status = "Capacidade máxima excedida"

print("Condição do elevador: ", status)