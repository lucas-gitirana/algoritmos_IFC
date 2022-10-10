def epar(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
x = int(input('Informe um valor: '))
print(epar(x))