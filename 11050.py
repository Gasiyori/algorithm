from itertools import combinations
from sys import stdin, stdout

n, k = map(int, stdin.readline().rstrip().split())

stdout.write(str(len(list(combinations(range(n), k)))))