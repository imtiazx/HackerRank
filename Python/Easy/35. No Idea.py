n, m =  map(int, input().split())

e = list()
e = list(map(int, input().strip().split()))

H = set(map(int, input().strip().split()))
S = set(map(int, input().strip().split()))

count = 0
for i in e:
    if i in H:
        count = count+1
    if i in S:
        count = count-1
print(count)
