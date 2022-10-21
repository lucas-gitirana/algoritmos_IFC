def soma_impares(x):
    soma = 0
    for i in range(1, x+1):
        if i % 2 != 0:
            print(i)
    
    return(soma)


x = int(input('Informe um valor para x: '))
soma_impares(x)
#print(f'Soma dos ímpares no intervalo de 1 a {x}: {soma_impares(x)}')