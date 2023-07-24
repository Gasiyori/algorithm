from sys import stdin, stdout

word = stdin.readline().rstrip()
n = int(stdin.readline().rstrip())-1

stdout.write(str(word[n]))