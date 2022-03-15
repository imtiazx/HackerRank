import math
# In a right angled triangle: BM = 1/2(AC)
# BM = MC i.e. angle(MBC) = angle(MCB)
# angle(MCB) = tan^(-1)(AB/BC)

len_AB = int(input())
len_BC = int(input())

print(round(math.degrees(math.atan(len_AB/len_BC))), chr(176), sep = '')
