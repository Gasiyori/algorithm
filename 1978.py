from math import sqrt
from sys import stdin, stdout

n = int(stdin.readline().rstrip())
array = list(map(int, stdin.readline().rstrip().split()))

def prime_check(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

count = 0

for i in array:
    if prime_check(i):
        count += 1

stdout.write(str(count))