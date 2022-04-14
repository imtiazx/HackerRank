import numpy as np

n, m, p = map(int, input().split())
my_array1 = np.array([input().strip().split() for _ in range(n)], int)
my_array2 = np.array([input().strip().split() for _ in range(m)], int)

print(np.concatenate((my_array1, my_array2), axis = 0))
