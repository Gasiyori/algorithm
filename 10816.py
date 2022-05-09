from collections import Counter
from sys import stdin, stdout

_ = int(stdin.readline().rstrip())
card = list(map(int, stdin.readline().rstrip().split()))

_ = int(stdin.readline().rstrip())
count = list(map(int, stdin.readline().rstrip().split()))

c = Counter(card)

for x in count:
    if c[x] != 0:
        stdout.write(str(c[x]) + ' ')
    else:
        stdout.write("0 ")