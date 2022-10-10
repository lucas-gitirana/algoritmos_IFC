a = []
b = []

for i in range(5):
    a.append(int(input("Valor A: ")))

for i in range(5):
    b.append(int(input("Valor B: ")))

resultado = []
resultado = a + b

print(a)
print(b)
    
for i in range(5):    
    a.append(b[i])

print("Lista concatenada: ", resultado)
print("Lisa unida com append: ", a)
