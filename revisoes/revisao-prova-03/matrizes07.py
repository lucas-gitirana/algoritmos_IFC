m = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(int(input(f'Informe um valor para m{i}{j}: ')))
    m.append(linha)

for i in range(10): 
    print(m[i])


for i in range(10):    
    for j in range(10):
        
        if i == 2:
            aux = m[i][j]
            m[i][j] = m[8][j]
            m[8][j] = aux
        
        if i == 5:
            aux = m[i][j]
            m[i][j] = m[j][9]
            m[j][9] = aux

for i in range(10): 
    print(m[i])
