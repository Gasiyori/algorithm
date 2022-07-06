from sys import stdin, stdout
from collections import deque

n = int(stdin.readline().rstrip())

array = deque()

# 입력 문자열 받고 쪼개기
for _ in range(n):
    temp = list(stdin.readline().rstrip().split())

    if temp[0] == 'push_front': # 덱 앞쪽에 저장
        array.appendleft(temp[1])
    if temp[0] == 'push_back': # 덱 뒤쪽에 저장
        array.append(temp[1])
    if temp[0] == 'pop_front':
        if len(array) <= 0: # 큐가 비었으면
            stdout.write(str('-1\n')) # -1 출력
        else: # 큐에 내용물이 있으면
            stdout.write(str(array.popleft()) + '\n') # 가장 앞의 내용물 출력
    if temp[0] == 'pop_back':
        if len(array) <= 0: # 큐가 비었으면
            stdout.write(str('-1\n')) # -1 출력
        else: # 큐에 내용물이 있으면
            stdout.write(str(array.pop()) + '\n') # 가장 앞의 내용물 출력
    if temp[0] == 'size':
        stdout.write(str(len(array)) + '\n')
    if temp[0] == 'empty':
        if len(array) <= 0: # 비어있으면
            stdout.write('1\n') # 1 출력
        else:
            stdout.write('0\n')
    if temp[0] == 'front':
        if len(array) <= 0: # 비어있으면
            stdout.write('-1\n') # -1 출력
        else:
            stdout.write(str(array[0]) + '\n')
    if temp[0] == 'back':
        if len(array) <= 0: # 비어있으면
            stdout.write('-1\n') # -1 출력
        else:
            stdout.write(str(array[-1]) + '\n')