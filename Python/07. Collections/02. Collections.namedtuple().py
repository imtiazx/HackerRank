import collections 

N = int(input())
scol = ','.join(input().split())
Student = collections.namedtuple('Student', scol)

sum  = 0
for i in range(N):
    row =  input().split()
    student = Student(*row)
    sum += int(student.MARKS)
    
print(sum/N)
