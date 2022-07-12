nome = input("Nome: ")
novoNome = ""

for i in range(len(nome)-1, -1, -1):
    novoNome = novoNome + nome[i]

print(novoNome.upper())