from sys import stdin, stdout

n = int(stdin.readline().rstrip())

a = [0 for _ in range(0, 10001)]

for x in range(n):
    a[int(stdin.readline().rstrip())] += 1

for x in range(10001):
    if a[x] != 0:
        for y in range(a[x]):
            stdout.write(str(x) + '\n')