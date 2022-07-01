# 혼자 해결한 방법은 이런식인데, 조금 더 검증이 필요함
# 추후 유사 문제 나오면 해결하고, 교재 코드 추가해놓기

from sys import stdout, stdin

n, m = map(int, stdin.readline().rstrip().split()) # 맵 크기. 세로 n * 가로 m
x, y, d = map(int, stdin.readline().rstrip().split()) # 위치는 x, y, d는 방향(0이 북)

map_array = []
for i in range(n):
    map_array.append(list(map(int, input().split())))

# 북쪽 기준으로 0번부터 북, 서, 남, 동
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# r을 받아서 회전해서 반환
# 0~3 이므로 경우 4인 경우 0으로 초기화
def turn(r):
    result = (r + 1) % 4

    return result

proto_map = map_array.copy()
map_array[x][y] = 1 # 초기 캐릭터 위치
count = 1 # 방문한 칸 횟수 (초기 시작 포함해서 1)
rotate = 0 # 바라보는 방향
turn_count = 0

while True:
    if map_array[x + move[rotate][0]][y + move[rotate][1]] == 0 : # 바라보는 방향으로 갈 수 있으면
        x = x + move[rotate][0]
        y = y + move[rotate][1]
        map_array[x][y] = 1
        count += 1
        turn_count = 0
    else: # 바라보는 방향으로 갈 수 없으면
        rotate = turn(rotate)
        turn_count += 1

    if turn_count == 4: # 4방향을 모두 훑어봤음에도 갈 수 없으면
        if proto_map[x - move[rotate][0]][y - move[rotate][1]] == 0: # 뒤로 가되, 원본 맵을 참고해서 육지인 경우만
            x = x - move[rotate][0]
            y = y - move[rotate][1]
        else:
            break

stdout.write(str(count))