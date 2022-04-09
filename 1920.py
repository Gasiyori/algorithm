from sys import stdin

m = int(stdin.readline().rstrip())
a = set(stdin.readline().rstrip().split())

n = int(stdin.readline().rstrip())
b = list(stdin.readline().rstrip().split())

for x in range(len(b)): # b만큼 반복
    if b[x] in a:
        print(1)
    else:
        print(0)