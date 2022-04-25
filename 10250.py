from sys import stdin, stdout

# 테스트 케이스
t = int(stdin.readline().rstrip())


for _ in range(t): # 사실상 main

    # 호텔 층 수, 방 수, 몇 번째 손님
    h, w, m = map(int, stdin.readline().rstrip().split())

    # 층 수를 우선으로 쌓고,
    # 층 수가 넘어가면 방 수를 넘김
    # 6, 12, 10 >> 402
    # 30, 50, 72 >> 1203

    if m % h == 0:
        room = (h * 100) + m // h
    else:
        room = 1 + (m % h) * 100 + (m // h)
    stdout.write(str(room) + '\n')