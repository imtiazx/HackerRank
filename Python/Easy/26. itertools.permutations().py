from itertools import permutations

s, k = input().split()
words = sorted(list(permutations(s, int(k))), reverse = False)

for word in words:
    p = ''.join(word)
    print(p)
