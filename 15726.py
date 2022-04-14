from sys import stdin, stdout

a, b, c = map(int, stdin.readline().rstrip().split())

stdout.write(str(int(max(a * b / c, a / b * c))))