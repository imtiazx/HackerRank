from collections import Counter

X = input()
S = Counter(map(int,input().split()))
n = input()
N = int(n) 
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings)
