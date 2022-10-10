def area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input('Informe o valor da base: '))
altura = float(input('Informe o valor da altura: '))
print(f'Área do triângulo: {area_triangulo(base, altura)}')
