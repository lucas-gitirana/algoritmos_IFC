a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
e = int(input("E: "))

maior = a

if b > maior:
    maior = b

if c > maior:
    maior = c

if d > maior:
    maior = d

if e > maior:
    maior = e


print("Maior: ", maior)