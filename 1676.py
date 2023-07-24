from sys import stdin, stdout
from math import factorial

n = str(factorial(int(stdin.readline().rstrip())))
cnt = 0

for x in n[::-1]:
    if x == "0":
        cnt += 1
    else:
        break

print(cnt)