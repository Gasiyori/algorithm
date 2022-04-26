from sys import stdin, stdout
from math import ceil

a, b, v = map(int, stdin.readline().rstrip().split())

day = ceil((v - b) / (a - b))

stdout.write(str(day))