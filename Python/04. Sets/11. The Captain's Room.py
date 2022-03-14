from collections import Counter

n = int(input())
x = Counter(list(map(int,input().split())))
for i in x:
    if x[i]==1:
        print(i)
