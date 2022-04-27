from sys import stdin, stdout

k, d, a = map(int, stdin.readline().rstrip().split('/'))

if (k + a < d or d == 0):
    stdout.write("hasu")
else:
    stdout.write("gosu")