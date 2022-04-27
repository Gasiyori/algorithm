from sys import stdin, stdout

a = stdin.readline().rstrip()

if a == 'n' or a == 'N':
    stdout.write("Naver D2")
else:
    stdout.write("Naver Whale")