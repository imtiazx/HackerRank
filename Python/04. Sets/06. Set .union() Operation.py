n = int(input())
english_roll_num = set(input().split())

b = int(input())
french_roll_num = set(input().split())

print(len(english_roll_num.union(french_roll_num)))
