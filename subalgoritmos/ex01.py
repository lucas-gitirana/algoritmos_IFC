def maximo(x:int, y:int):
    if x > y:
        return x
    else:
        return y

x = int(input('Informe o primeiro valor: '))
y = int(input('Informe o segundo valor: '))

print(f'Maior valor {maximo(x,y)}')