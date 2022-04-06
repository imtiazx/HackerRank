N, X = map(int, input().split())
sheet = []

for _ in range(X):
    sheet.append(map(float, input().split())) 

for i in zip(*sheet): 
    print(sum(i)/len(i))
