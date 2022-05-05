a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a > c:
    maior = a
    
    if b > c:
        menor = c
    if c > b:
        menor = b

if b > a and b > c:
    maior = b

    if a > c:
        menor = c
    if c > a:
        menor = a

if c > a and c > b:
    maior = c

    if a > b:
        menor = b
    if b > a:
        menor = a

print("O maior valor lido é: ", maior, "e o menor é: ", menor)