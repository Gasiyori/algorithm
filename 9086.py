from sys import stdin, stdout

tc_num = int(stdin.readline().rstrip())

for _ in range(tc_num):
    word = stdin.readline().rstrip()
    stdout.write(word[0] + word[-1] + "\n")