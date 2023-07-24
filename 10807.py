from sys import stdin, stdout

n = int(stdin.readline().rstrip()) # 1 <= n <= 100
num = list(map(int, stdin.readline().rstrip().split()))
v = int(stdin.readline().rstrip()) # -100 <= n <= 100

cnt = 0

for x in num:
    if x == v:
        cnt += 1

int(str(stdout.write(str(cnt))))