def area_figura(base, altura):
    if figura == 'Q':
        return base * altura
    else:
        return (base * altura) / 2

figura = input('Informe a sua figura (T ou Q): ')
base = float(input('Informe o valor da base: '))
altura = float(input('Informe o valor da altura: '))

print('Área: ', area_figura(base, altura))