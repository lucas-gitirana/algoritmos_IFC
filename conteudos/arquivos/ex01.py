with open("ex01nome.txt", "w") as arquivo:
    arquivo.write(input('Informe seu nome: '))

    arquivo.close
    print('O seu nome foi inserido no arquivo!')