from sys import stdin, stdout

n, m = map(int, stdin.readline().rstrip().split())

board = []

for _ in range(n):
    board.append(stdin.readline().rstrip()) # 한 줄

# 8 * 8 규격으로 잘라야 됨.
# 즉, 0~7까지, 1~8 등 "끝" 인덱스가 "시작" 인덱스와 7의 차이가 나야 함

# 가로든 세로든 먼저 검사하고 해당 방향으로 움직여야 함.
# 이 경우 가로로 움직이고 세로로 한칸씩 움직이는게 편할 듯?
# 따라서 세로 반복문 안에 가로 반복문을 넣는 편이 낫다고 판단됨.

# 시작을 B로 하는 경우와 W로 하는 경우를 모두 따져봐야 함.
# 시작이 B라면 인덱스 0이 B이므로 짝수는 B이고, 홀수는 W임
# 반대로 시작이 W라면 짝수는 W고 홀수는 B임

min_paint = 64

for j in range(n - 7): # n이 세로 길이. 입력 값만큼 단순 반복
    for i in range(m - 7): # m이 가로 길이. 입력 값만큼 단순 반복

        paint1 = 0
        paint2 = 0

        for y in range(j, j + 8): # 이 경우 8*8에서 W 먼저 칠하는 경우임
            for x in range(i, i + 8):
                if y % 2 == 0: # y축으로 0, 2, 4, 6 일때
                    if x % 2 == 0: #x축으로 0, 2, 4, 6일때
                        if board[y][x] != 'W':
                            paint1 += 1
                    elif x % 2 == 1: #x축으로 1,3,5,7일때
                        if board[y][x] != 'B':
                            paint1 += 1

                else: # y축으로 1, 3, 5, 7일때
                    if x % 2 == 0: #x축으로 0, 2, 4, 6일때
                        if board[y][x] != 'B':
                            paint1 += 1
                    elif x % 2 == 1: #x축으로 1,3,5,7일때
                        if board[y][x] != 'W':
                            paint1 += 1

        for y in range(j, j + 8): # 이 경우 8*8에서 B 먼저 칠하는 경우임
            for x in range(i, i + 8):
                if y % 2 == 0: # y축으로 0, 2, 4, 6 일때
                    if x % 2 == 0: #x축으로 0, 2, 4, 6일때
                        if board[y][x] != 'B':
                            paint2 += 1
                    else: #x축으로 1,3,5,7일때
                        if board[y][x] != 'W':
                            paint2 += 1

                else: # y축으로 1, 3, 5, 7일때
                    if x % 2 == 0: #x축으로 0, 2, 4, 6일때
                        if board[y][x] != 'W':
                            paint2 += 1
                    else: #x축으로 1,3,5,7일때
                        if board[y][x] != 'B':
                            paint2 += 1

        min_paint = min(paint1, paint2, min_paint)

stdout.write(str(min_paint))