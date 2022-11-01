""" .Faça uma sub-rotina que recebe duas listas A e B com dez 
elementos inteiros como parâmetro. A sub-rotina deverá determinar 
e mostrar o vetor C que contém os elementos que estão em A, mas 
que não estão em B. A lista C deverá ser mostrada no programa 
principal. """

def diferenca(a, b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    return c

print('OLÁ!')
print('----- Enunciado: -----')
print('.Faça uma sub-rotina que recebe duas listas A e B com dez elementos inteiros como parâmetro. \n A sub-rotina deverá determinar  e mostrar o vetor C que contém os elementos que estão em A, \nmas que não estão em B. A lista C deverá ser mostrada no programa principal. ')
print('----------------------------------------------------------------------------------')

""" lista_a = [0,1,2,3,4,5,6,7,8,9,]
lista_b = [0,2,4,6,8,10,12,14,16,18] """

lista_a = []
lista_b = []

tam = int(input('Tamanho das listas: '))

print('----- LISTA A -----')
for i in range(tam):
    lista_a.append(int(input(f'A[{i}]: ')))

print('----- LISTA B -----')
for i in range(tam):
    lista_b.append(int(input(f'B[{i}]: ')))


print('=========LISTAS ORIGINAIS==========')
print(f'A: {lista_a}')
print(f'B: {lista_b}')

print('===================')
print(f'Diferença entre A e B: {diferenca(lista_a, lista_b)}')
