from sys import stdin, stdout

n = int(stdin.readline().rstrip()) # 회수

a = set()

for i in range(n):
    a.add(int(stdin.readline().rstrip()))

a = sorted(a)

for i in range(n):
    stdout.write(str(a[i]) + '\n')