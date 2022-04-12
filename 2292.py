from sys import stdin, stdout

n = int(stdin.readline().rstrip()) # 입력 값

# 한 번 사이클이 돌 때마다 최대 개수가 6씩 늘어난다.
"""
6개는 1
12개는 2
18개는 3
24개는 4
30개는 5
"""
num = 1  # 벌집의 개수
cnt = 1

while n > num :
    num += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문 카운트

stdout.write(str(cnt))