from sys import stdin, stdout

t = int(stdin.readline().rstrip())

for _ in range(t):
    stdout.write(str(sum(list(map(int, stdin.readline().rstrip().split())))) + "\n")