import cmath

num = complex(input())
for i in range(2):
    print(cmath.polar(num)[i])
