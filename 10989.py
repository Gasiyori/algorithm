from sys import stdin, stdout

n = int(stdin.readline().rstrip())

a = [0 for _ in range(0, 10000)]

for x in range(n):
    a[x] = int(stdin.readline().rstrip())

a.sort()

for x in range(n):
    if a[x] != 0:
        stdout.write(str(a[x]) + '\n')