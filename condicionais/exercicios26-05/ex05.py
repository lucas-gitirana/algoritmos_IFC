litrosVendidos = float(input("Litros vendidos: "))
tipoCombustivel = input("Tipo de combustível (A ou G): ")

if tipoCombustivel == 'A':

    valorOriginal = litrosVendidos * 6.5

    if litrosVendidos <= 20:
        desconto = litrosVendidos * 3                
    else:
        desconto = litrosVendidos * 5

    precoFinal = valorOriginal - (valorOriginal * (desconto/100))        

else:

    valorOriginal = litrosVendidos * 7.2

    if litrosVendidos <= 20:
        desconto = litrosVendidos * 4
    else:
        desconto = litrosVendidos * 6
    
    precoFinal = valorOriginal - (valorOriginal * desconto/100)


print("Valor a ser pago: ", precoFinal)