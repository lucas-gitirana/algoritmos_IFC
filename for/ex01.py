numero = int(input("Número: "))

if numero >= 0 and numero <= 10:
        
    for i in range(1, 11):
        multiplicacao = i * numero
        print(numero, 'X', i, '=', multiplicacao)
else:
    print("Valor inválido")
    
    
