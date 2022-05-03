from sys import stdin, stdout

a = []

n = int(stdin.readline().rstrip())

for _ in range(n):
    a.append(list(map(int, stdin.readline().rstrip().split())))

# 아래처럼 쓰면 x축, y축 순으로 정렬 가능
# 반대로 쓰려면 위치 바꾸면 됨
a.sort(key=lambda x: (x[1], x[0]))
 
for x in a:
    stdout.write(str(x[0]) + ' ' + str(x[1]) + '\n')