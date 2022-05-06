from sys import stdin, stdout

n = int(stdin.readline().rstrip())

a = []

for _ in range(n):
    a.append(stdin.readline().rstrip())

a = list(set(a))

a.sort(key = lambda x : (len(x), x))

for x in a:
    stdout.write(str(x) + '\n')