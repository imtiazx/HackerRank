import numpy as np

n, m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)

print(np.transpose(my_array))
print(my_array.flatten())
