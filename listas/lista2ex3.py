""" Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros. Gere
um vetor X que possua os elementos comuns a R e a S. Considere que no
mesmo vetor não haverá números repetidos. """

r = []
s = []
x = []

print('LISTA R')
for i in range(5):
    valor = int(input("Informe o valor: "))
    r.append(valor)

print('LISTA S')
for i in range(10):
    valor = int(input("Informe o valor: ")) 
    s.append(valor)

for i in range(len(r)):
    for j in range(len(s)):
        if r[i] == s[j]:
            x.append(s[j])

# OPERAÇÃO COM CONJUNTOS
# resultado = set(r) & set(s)

print(x)


