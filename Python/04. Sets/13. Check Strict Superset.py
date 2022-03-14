A = set(input().split())
n_sets = int(input())
output = True

for i in range(n_sets):
    storage = set(input().split())
    if not storage.issubset(A):
        output = False
    if len(storage) >= len(A):
        output = False

print(output)
