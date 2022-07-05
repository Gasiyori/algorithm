from sys import stdin, stdout
from collections import deque

n = int(stdin.readline().rstrip())

array = deque()

# 입력 문자열 받고 쪼개기
for _ in range(n):
    temp = list(stdin.readline().rstrip().split())

    if temp[0] == 'push': # push 문자 뒤의 값 저장
        array.append(temp[1])
    if temp[0] == 'pop':
        if len(array) <= 0: # 스택이 비었으면
            stdout.write(str('-1\n')) # -1 출력
        else:
            stdout.write(str(array.pop()) + '\n') # 
    if temp[0] == 'size':
        stdout.write(str(len(array)) + '\n')
    if temp[0] == 'empty':
        if len(array) <= 0:
            stdout.write('1\n')
        else:
            stdout.write('0\n')
    if temp[0] == 'top':
        if len(array) <= 0: # 스택이 비었으면
            stdout.write(str('-1\n')) # -1 출력
        else:
            stdout.write(str(array[-1]) + '\n')