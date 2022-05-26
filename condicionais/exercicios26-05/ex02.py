a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a > c:
    maior = a
    if b > c:
        medio = b 
        menor = c
    else:
        medio = c
        menor = b
elif b > a and b > c:
    maior = b
    if a > c:
        medio = a
        menor = c
    else:
        medio = c
        menor = a
else:
    maior = c
    if a > b:
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print(menor, medio, maior)