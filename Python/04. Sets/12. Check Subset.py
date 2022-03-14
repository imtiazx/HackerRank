n_cases = int(input())
for i in range(n_cases):
    n_A = int(input())
    A = set(input().split())
    n_B = int(input())
    B = set(input().split())
    print(A.issubset(B))
