from itertools import *

s = input()
for i,j in groupby(map(int,list(s))):
    print(tuple([len(list(j)), i]), end = " ")
