from sys import stdin, stdout

# 소들의 수 n, 헛간 크기 w, h, 공간 크기 l

n, w, h, l = map(int, stdin.readline().rstrip().split())

count_w = w // l
count_h = h // l

stdout.write(str(min(count_w * count_h, n)))