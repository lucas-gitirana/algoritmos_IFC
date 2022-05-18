codigo = int(input("Código: "))

if codigo == 1:
    print("Alimento não-perecível")
elif codigo <= 4:
    print("Alimento perecível")     
elif codigo <= 6:
    print("Vestuário")    
elif codigo == 7:
    print("Higiene pessoal")    
elif codigo <= 15:
    print("Limpeza e utensílios domésticos")
else: 
    print("Inválido")    