cube = lambda x: x**3

def fibonacci(n):
    l = [0, 1]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    return(l[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
