from sys import stdin, stdout

n = int(stdin.readline().rstrip())

array = []

for _ in range(n):
    array.append(int(stdin.readline().rstrip()))

array.sort(reverse=True)

for x in array:
    stdout.write(str(x) + ' ')