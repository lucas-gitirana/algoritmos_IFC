with open('ex02nome.txt', 'w') as arquivo:
    arquivo.write(input('Escreva seu nome: '))
    arquivo.close
    print('Nome inserido!')

with open('ex02nome.txt', 'w') as arquivo:
    arquivo.write('Eu amo algoritmos!')