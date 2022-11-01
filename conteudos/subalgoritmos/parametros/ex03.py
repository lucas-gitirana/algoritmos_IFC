""" Crie uma sub-rotina que receba como parâmetro um vetor V[25] de 
números inteiros e substitua todos os valores negativos de A por 0. O 
vetor deverá ser mostrado no programa principal """

def negativos(v):
    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0

vetor = []
tam = int(input('Tamanho do vetor: '))

for i in range(tam):
    vetor.append(int(input(f'Valor para a posição {i}: ')))

print('=====VETOR ORIGINAL:=====')
print(vetor)
print('=====VETOR MODIFICADO:=====')
negativos(vetor)
print(vetor)


