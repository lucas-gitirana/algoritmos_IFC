nomes = []
espacos_ocupados = []

#Função para calcular espaço total utilizado
def espaco_total():
    total = 0
    for i in range(len(espacos_ocupados)):
        total += converter_mb(espacos_ocupados[i])
    return total

#Função para calcular espaço médio utilizado
def espaco_medio():
    qtd_contas = len(espacos_ocupados)
    return "{:.2f}".format(espaco_total() / qtd_contas)

# FUNÇÃO PARA CONVERTER BYTES PARA MEGABYTES
def converter_mb(num_bytes):
    return float("{:.2f}".format(float(num_bytes) / 1048576))

# FUNÇÃO PARA CALCULAR PERCENTUAL DE ESPAÇO OCUPADO
def percentual(espaco):    
    return float("{:.2f}".format((float(espaco) / espaco_total()) * 100))


# PEGANDO NOME E ESPAÇO OCUPADO POR CADA USUÁRIO
with open("usuarios.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for i in range(len(linhas)):
    #  usuario = linhas[i].split()
        nomes.append(linhas[i][0:14])
        espacos_ocupados.append(linhas[i][15:26])

    # MONTANDO O RELATORIO
    with open('relatorio.txt', 'w') as relatorio:
        #ADICIONANDO CABEÇALHO
        relatorio.write(f'ACME Inc. \t\t\t Uso do espaco em disco pelos usuarios \n')
        relatorio.write('----------------------------------------------------------\n')
        relatorio.write(f'ID \t Usuario \t\t\t Espaco e % de uso \n\n')

        # ADICIONANDO USUÁRIOS E ESPAÇOS    
        for i in range(len(linhas)):
            id = i + 1
            nome_usuario = nomes[i] 
            espaco_usuario = converter_mb(espacos_ocupados[i])
            percentual_uso = percentual(espaco_usuario)         
            
            relatorio.write(f'{id} \t {nome_usuario} \t {espaco_usuario} MB = {percentual_uso} % \n')

        # ADICIONANDO ESPAÇO TOTAL E MÉDIA DE ESPAÇO OCUPADO
        relatorio.write(f'\nEspaco total ocupado: {espaco_total()} MB')
        relatorio.write(f'\nEspaco medio ocupado: {espaco_medio()} MB')




for i in range(len(nomes)):
    print(nomes[i])
    print(espacos_ocupados[i])


