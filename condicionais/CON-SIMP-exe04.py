a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a < b and a < c:
    menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

print("O menor valor lido é: ", menor)