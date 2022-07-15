from sys import stdin, stdout

n = int(stdin.readline().rstrip())

array = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

for x in array: # 5명
    rank = 1
    for y in array: # 자신 제외한 나머지들
        if x[0] < y[0] and x[1] < y[1]: # 자신이 나머지보다 덩치가 작을 때
            rank += 1

    stdout.write(str(rank) + ' ')