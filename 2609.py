from sys import stdin, stdout
from math import lcm, gcd

a, b = map(int, stdin.readline().rstrip().split())

stdout.write(str(gcd(a, b)) + '\n' + str(lcm(a, b)))