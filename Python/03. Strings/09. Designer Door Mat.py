# Code for mat size n X m
n, m = map(int, input().split())

if n*3 != m:
    print("Invalid size")
else:
    for i in range(1, n, 2):
        print(str('.|.'*i).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n-2, -1, -2):
        print(str('.|.'*i).center(m, '-'))
    
