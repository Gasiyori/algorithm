from sys import stdin, stdout

word = stdin.readline().rstrip()

for x in word:
    if x.isupper(): #대문자인 경우
        stdout.write(x.lower())
    else: #소문자인 경우
        stdout.write(x.upper())
