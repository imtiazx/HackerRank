xk  = list(map(int, input().split()))
x = xk[0]
k = xk[1]
polynomial = input()

print(eval(polynomial) == k)
