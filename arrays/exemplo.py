from tkinter import N
import numpy as np

N = 5

vetor = np.zeros(N)

#exemplo um
print(vetor)

#exemplo dois

for i in range(N):
    vetor[i] = float(input(f"Informe um valor para V[{i}]: "))

print(vetor)

