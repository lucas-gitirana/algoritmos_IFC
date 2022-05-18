xA = float(input("Eixo x do primeiro ponto: "))
yA = float(input("Eixo y do primeiro ponto: "))

xB = float(input("Eixo x do segundo ponto: "))
yB = float(input("Eixo y do segundo ponto: "))

dAB = ((xB - xA)**2 + (yB - yA)**2)**(0.5)

print("A distância entre os dois pontos é de ",dAB)