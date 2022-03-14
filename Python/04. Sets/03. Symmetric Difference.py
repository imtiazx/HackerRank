M = int(input())
A = set(map(int, input().split()))

N = int(input())
B = set(map(int, input().split()))

C = A.difference(B)
D = B.difference(A)

for i in sorted(C.union(D)):
    print(i)
