# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x. Após completar toda a leitura da lista, 
# verificar se cada valor armazenado na lista é par ou ímpar. Se for par, 
# fazer com que o valor seja atualizado para o resultado da multiplicação do valor contido pelo índice. 
# Se for impar fazer com que a lista receba o valor do seu próprio índice.

x = []

for i in range(10):
    valor = int(input("Valor: "))
    x.append(valor)

for i in range(len(x)):
    
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i
    
print(x)