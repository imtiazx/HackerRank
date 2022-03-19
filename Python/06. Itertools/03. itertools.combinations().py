from itertools import combinations

ip = input().split()
S = ip[0]
k = int(ip[1])

for i in range(1, k+1):
    for j in combinations(sorted(S), i):
        print("".join(j))
