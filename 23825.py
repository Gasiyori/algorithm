from sys import stdin, stdout

n, m = map(int, stdin.readline().rstrip().split())

stdout.write(str(min(n, m) // 2))