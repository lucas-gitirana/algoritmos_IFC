from re import A


a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a < c:
    medio = a
elif a < b and a > c:
    medio = a
elif b > a and b < c:
    medio = b
elif b > c and b < a:
    medio = b
elif c > a and c < b:
    medio = c
elif c < a and c > b:
    medio = c

print(medio)
