
def decresce(num, cont):
    if cont < num:
        print(num - cont)
        cont += 1
        decresce(num, cont)

contador = 0
x = int(input('Informe um valor: '))

decresce(x,contador)

