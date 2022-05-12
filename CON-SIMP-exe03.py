a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

#if a > b and a > c:
#    maior = a

#if b > a and b > c:
#    maior = b

#if c > a and c > b:
#    maior = c
    
maior = a

if b > maior:
    b = maior

if c > maior:
    c = maior  
    
# OU

if a > b and a >c:
    maior = a
elif b > a and b > c:
    maior = b
else    
    maior = c

print("O maior valor lido é: ", maior)
