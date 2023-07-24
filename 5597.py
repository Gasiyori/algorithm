from sys import stdin, stdout

n = []
for _ in range(1, 29):
    n.append(int(stdin.readline().rstrip())) #출석번호

for x in range(1, 31):
    if n.count(x) == 0:
        print(x)
