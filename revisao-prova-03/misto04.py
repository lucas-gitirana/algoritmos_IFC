import numpy as np

a = np.array([3, 5, 4, 2, 2, 5, 3, 2, 5, 9])
b = np.array([7, 15, 20, 0, 18, 4, 55, 23, 8, 6])
c = np.zeros(20)

for i in range(len(a)):
    c[2 * i] = a[i]
    c[(2 * i) + 1] = b[i]

print(c)
