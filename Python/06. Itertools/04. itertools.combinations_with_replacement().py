from itertools import combinations_with_replacement

s, k = input().split()
all_combinations = list(combinations_with_replacement(sorted(s), int(k)))

for c in all_combinations:
    p = ''.join(c)
    print(p)
