from sys import stdin, stdout

s, k, h = map(int, stdin.readline().rstrip().split())

if s + k + h < 100: # 미만일 때
    if min(s, k, h) == s:
        stdout.write("Soongsil")
    elif min(s, k, h) == k:
        stdout.write("Korea")
    else:
        stdout.write("Hanyang")
else:
    stdout.write("OK")