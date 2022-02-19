import cmath

num = complex(input())
z = complex(num)

for i in range(2):
    print(cmath.polar(z)[i])
