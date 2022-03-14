n = int(input())
english_roll_num = set(input().split())

b = int(input())
french_roll_num = set(input().split())

print(len(english_roll_num.intersection(french_roll_num)))
