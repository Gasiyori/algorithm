from sys import stdin, stdout

n = int(stdin.readline().rstrip())

d = []

for x in range(n):
    # 2차원 리스트
    a, b = stdin.readline().rstrip().split()
    
    a = int(a)
    
    d.append([a, b])

# 2차원 리스트에서 2번째 리스트 기준으로 정렬
d.sort(key = lambda x: (x[0]))

for x in range(n):
    stdout.write(str(d[x][0]) + ' ' + str(d[x][1]) + '\n')