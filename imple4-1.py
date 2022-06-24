# 도착 좌표 찾기

from sys import stdin, stdout

n = int(stdin.readline().rstrip())
plans = stdin.readline().rstrip().split()

x, y = 1, 1

for i in plans:
    print(x, y)
    if i == 'U':
        if y > 1:
            y -= 1
    elif i == 'D':
        if y < n:
            y += 1
    elif i == 'L':
        if x > 1:
            x -= 1
    elif i == 'R':
        if x < n:
            x += 1

stdout.write(str(y) + " " + str(x))


"""

n = input(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in plans:
    for i in range(len(move_type)): # move_type이 뭔지 체크
        if plan == move_type[i]: # move_type의 인덱스에 맞게 이동
            nx = x + dx[i] # x축만
            ny = y + dy[i] # y축만
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간 벗어나면 무시
        continue
    x, y = nx, ny # 이동 수행

print(x, y)

# """