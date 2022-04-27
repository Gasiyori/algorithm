from sys import stdin, stdout

n, m = map(int, stdin.readline().rstrip().split())
# n은 기준값, m은 실제 입력값

if m < 3: #1 or 2학년
    stdout.write("NEWBIE!")
elif m <= n:
    stdout.write("OLDBIE!")
else:
    stdout.write("TLE!")