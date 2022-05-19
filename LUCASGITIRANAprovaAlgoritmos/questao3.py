# LUCAS EMANOEL GITIRANA

a = int(input("Primeiro valor inteiro: "))
b = int(input("Segundo valor inteiro: "))
c = int(input("Terceiro valor inteiro: "))

if a > b and a > c:
    if b > c:
        intermediario = b
    else: 
        intermediario = c
elif b > a and b > c:
    if a > c:
        intermediario = a
    else:
        intermediario = c
elif c > a and c > b:
    if a > b:
        intermediario = a
    else:
        intermediario = b


print("Valor intermediário: ", intermediario)