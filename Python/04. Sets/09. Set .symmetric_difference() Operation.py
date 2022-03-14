n = int(input())
english_roll_num = set(input().split())

b = int(input())
french_roll_num = set(input().split())

only_english = english_roll_num.difference(french_roll_num)
only_french = french_roll_num.difference(english_roll_num)

print(len(only_english.union(only_french)))
