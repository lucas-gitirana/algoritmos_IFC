data = input("Informe a data no formato dd/mm/aaaa: ")

dataLista = list(data)
dia = dataLista[0]+dataLista[1] 
ano = dataLista[6]+dataLista[7]+dataLista[8]+dataLista[9]

if "/01/" in data:
    print("Você nasceu em", dia, " de janeiro de", ano)

elif "/02/" in data:
    print("Você nasceu em", dia, " de fevereiro de", ano)

elif "/03/" in data:
    print("Você nasceu em", dia, " de março de", ano)

elif "/04/" in data:
    print("Você nasceu em", dia, " de abril de", ano)

elif "/05/" in data:
    print("Você nasceu em", dia, " de maio de", ano)

elif "/06/" in data:
    print("Você nasceu em", dia, " de junho de", ano)

elif "/07/" in data:
    print("Você nasceu em", dia, " de julho de", ano)

elif "/08/" in data:
    print("Você nasceu em", dia, " de agosto de", ano)

elif "/09/" in data:
    print("Você nasceu em", dia, " de setembro de", ano)

elif "/10/" in data:
    print("Você nasceu em", dia, " de outubro de", ano)

elif "/11/" in data:
    print("Você nasceu em", dia, " de novembro de", ano)

elif "/12/" in data:
    print("Você nasceu em", dia, " de desembro de", ano)
