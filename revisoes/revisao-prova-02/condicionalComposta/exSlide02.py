a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a > c:
    maior = a

    if b > c:
        media = b
        menor = c
    else:
        media = c
        menor = b
elif b > a and b > c:
    maior = b

    if a > c:
        media = a
        menor = c
    else:
        media = c
        menor = a

elif c > a and c > b:
    maior = c

    if a > b:
        media = a
        menor = b
    else:
        media = b
        menor = a

print(menor, media, maior)
