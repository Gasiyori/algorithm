from sys import stdin, stdout

n = int(stdin.readline().rstrip())

student = {}

for _ in range(n):
    x, y = stdin.readline().rstrip().split()
    y = int(y)
    
    student[x] = y

student = sorted(student, key=lambda x:x[1], reverse=True)

for x in student:
    stdout.write(x + ' ')

"""
# 튜플 방식으로도 가능

n = int(input())

array = []

for i in range(n):
    input_data = input().split()

    array.append((input_data[0], int(input)data[1]))

array = sorted(array, key=lambda student : student[1])

for student in array:
    print(student[0], end=' ')

"""